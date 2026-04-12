# =======================================================
# ACT 4 - Scene 22: The Convoy (Empathy Path)
# File: a4_s22_act_four_close_emp.rpy
# Type: ACT CLOSE — the relay, the handoff, the title card to Act V
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s22_act_four_close_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s22_act_four_close_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Three movements.
    #         (1) Open wide. Aeron at the edge of the secondary base. Behind him
    #             the base wall. In front of him the access road and, beyond it,
    #             the convoy — fourteen civilians walking in a loose column
    #             behind three Phoenix runners, moving toward the Sector 6
    #             staging point. The camera is at Aeron's height, one step back
    #             and to his right. It does not move for the whole of the relay.
    #         (2) The relay. Each LI enters and exits the frame from Aeron's
    #             left (the base side). They come one at a time. The camera
    #             does not cut between them — it holds on Aeron's position and
    #             lets each LI come into the shot, do the beat, and leave. The
    #             edit is a series of long takes marked by the coming and going
    #             of each LI. Zira first — she is moving, running, a pack on
    #             her back. Noelle second — walking, a tablet in her hand.
    #             Lyra third — walking, her hands empty. Tessa fourth — walking,
    #             her medic jacket on again but the front closures are not all
    #             done. Selene fifth — walking, stopping beside him, not
    #             speaking for the length of a full breath before her line.
    #         (3) Aeron alone at the end. The camera pulls back one small step
    #             — one step only — and holds on the wide. The convoy in the
    #             mid-ground. Aeron in the foreground. The sun choice is the
    #             cinema choice: either rising (hope register) or setting
    #             (cost register). The scene directs the rise version as
    #             default because Phase III has earned a rise, but the setting
    #             variant is available and this file flags it.
    # LIGHTING: The cinema choice. Default: sun rising over the east ridge, the
    #           light cold and honest, the same kind of light as s01 but twelve
    #           days later and with a lot more weight on it. Variant: sun
    #           setting over the west ridge, the light warm and going. Either
    #           way the convoy is in the light and Aeron is at the edge of the
    #           light and his face is half in and half out.
    # SFX: The base behind him — quieter than it has been in the act, because
    #      most of the base is in motion with the move. The convoy — footsteps
    #      on the access road, the small sound of a child asking a question
    #      and a father answering the question, a runner's pack creaking, the
    #      crunch of gravel under fourteen pairs of feet. No score until the
    #      end. One long low string at the last beat. Rising and falling across
    #      the final line.
    # FACE: Aeron — the act's accumulated weight, held. Not crushed. Not light.
    #        The face of a man who has carried a question for twelve hours and
    #        has not answered it and is not going to answer it tonight and is
    #        okay inside the not-answering. Each LI: the face they bring to
    #        the relay is different and they are not performing for each other
    #        because they are not in the same frame with each other. The scene
    #        is a series of two-shots that are really one-shots with a second
    #        person entering and leaving.
    # BLOCKING: The edge of the base. The access road running east. The convoy
    #           in the road. Aeron standing at the edge of the wall where the
    #           wall meets the road. Each LI comes from the base side, does
    #           the beat, leaves toward the convoy or back into the base or —
    #           in Selene's case — stays.

    # ========= VOICE BASELINE =========
    # EMP cadence. The scene is very quiet. Five LI beats, one sentence each
    # (or one gesture plus a word). Aeron has almost no spoken lines. The load
    # is on the internal voice and on the final line, which is Aeron's
    # internal and is the act's last line.

    # scene bg_secondary_base_edge_morning_rise with fade
    # play ambient "sfx/ambient/convoy_road_morning.ogg" fadein 4.0

    # ========== PHASE 1 — THE EDGE ==========

    "Aeron walks to the edge of the base."

    "He has not been at the edge of the base in twelve days. The edge of the base is the place where the secondary base's wall meets the access road, and the access road runs east toward the ridge, and the ridge is the ridge Lyra called in the Sector 7 interdiction, and the ridge is where the Sector 6 staging point waits at the bottom of the far side of it."

    "He stops at the edge."

    "He does not cross."

    "He has no reason to cross. His place tonight is here. The crossing is for the runners and the civilians and the medics and the blessings. The staying is for the man who decided, twelve hours ago, in a room with no head, that the move was the shape of mercy the room could afford."

    "The convoy is on the access road."

    "Fourteen civilians walking in a loose column behind three Phoenix runners. The runners are at the front — two of them are Zira's runners, one is from Lyra's chapel cell. The civilians are: nine adults and five children, the same fourteen from the Sector 11 safehouse. Paela Venn is at the back of the column because Paela is holding the rear, because Paela is nineteen and competent and Zira put her there."

    "Oris Telm is in the middle of the column. He is walking. He is not being carried. That is his one thing — he asked Zira, before the convoy started, to let him walk, because walking was the correction he could make to the walking he did yesterday toward the east checkpoint. Zira said yes. He is walking."

    "Aeron watches the column."

    athought "Fourteen. Fourteen is the headcount that left the safehouse. Fourteen is the headcount that is supposed to arrive at the Sector 6 staging point. Tessa is going to confirm the fourteen at arrival. Tessa does not confirm numbers she has not seen herself."

    athought "If one of the fourteen does not arrive, the board gets a new name. That is the math the morning has."

    athought "I am at the edge of the base and I am watching them walk and I am not walking with them because my walking would slow them down and it would be a performance and the performance is not the thing that saves them. The staying is the thing."

    athought "This is the last beat of the act. I can feel the shape of it. The act is about to hand forward."

    # ========== PHASE 2 — ZIRA ==========

    "Footsteps behind him from the base side. Fast. Runner-fast."

    "Zira runs up to the edge. She is in her runner's pack and she has two comm pieces clipped to her collar and she has the list from the safehouse inside her jacket against her ribs where the fold is safe. She is not stopping at the edge — she is going to the convoy. This is a pass-through for her. The whole length of her being in the frame is five seconds."

    "She does not stop."

    "She touches his sleeve as she goes past. Not a grab — a touch. Her fingers on the outside of his right forearm for less than a second. Her face does not turn to him. Her voice is low and fast."

    z "Door."

    "Then she is past him."

    "She does not look back. She catches up to the convoy at the rear of the column — she is at Paela's shoulder within ninety seconds — and she is on the access road with her runners and she is moving."

    "Aeron does not turn to watch her go."

    athought "Door."

    athought "One word."

    athought "She said door."

    athought "That is Zira's word. It is a runner's word. It is the word she used in the Sector 9 alley in Act III when she talked about trust as the thing that is either there or it is not, the shape of a threshold you either cross or you do not. Door is her vocabulary. Door is what she says when she means we are through. We are on the other side of the thing. The thing is behind us."

    athought "She is telling me we are through the decision and into the move. She is telling me in the only kind of sentence a runner has time for."

    athought "I heard her."

    # ========== PHASE 3 — NOELLE ==========

    "A minute. Maybe two."

    "Noelle walks up to the edge. Not fast. Noelle does not run unless the math requires running and Noelle has spent the last ninety minutes doing the math. Her framework is the thing she is bringing, and Noelle is always unhurried about the delivery of a framework because the framework is the thing the scene is for, not the delivery speed."

    "She stops beside Aeron at the edge. She has a tablet in her hand. The tablet is on."

    "She does not speak immediately."

    "She is looking at the convoy on the access road. Her framework is drafted and her eyes are on the convoy and her face is — this is the Noelle beat — her face is the face of a woman who has been making analysis her whole life and who has just watched her analysis walk out into the open with fourteen people depending on it."

    "Then she offers him the tablet."

    n "Version two."

    "He takes the tablet. He does not read it yet. He looks at Noelle and Noelle is already turning — she is going back into the base to run the comms bridge from Noelle's workspace, because the move has a comms layer and the comms layer is hers."

    "She takes two steps back toward the base, then stops."

    n "I wrote the framework three times this morning. The first version was the one I would have written if I thought frameworks could answer the question. The second version is the one I am giving you. It is the version I wrote after I stopped believing frameworks can answer the question and started writing a framework that was about how we carry the question while we move people."

    n "Do not read the first version. I deleted it. I am telling you the first version existed because I want you to know I noticed I was writing the wrong framework and I stopped."

    "She does not wait for his answer."

    "She goes back into the base."

    "Aeron looks down at the tablet. Version two is on the screen. The header of the framework reads: FRAMEWORK FOR THE MOVE — VERSION TWO — NOT AN ANSWER, A CARRYING."

    athought "She wrote that header."

    athought "Noelle, who has never in her life written a framework whose first line is a disclaimer, wrote a framework whose first line is a disclaimer."

    athought "Noelle's Act IV arc just moved one click forward. She is not going to go back to writing frameworks that pretend to have answers. That is the whole of her learning this act and it is in the header of a framework she is handing me at the edge of a base while fourteen civilians walk east."

    athought "I am going to read version two later. Right now the beat is not the reading. The beat is the receiving."

    "He sets the tablet down on the top of the wall beside him. He will read it in ten minutes."

    # ========== PHASE 4 — LYRA ==========

    "Lyra walks up to the edge."

    "She is not in a hurry. Lyra is never in a hurry at the edge of a base. Her hands are empty. Her face is the blessing face — the face she uses when she is naming something and the naming is the blessing."

    "She stops beside Aeron. She does not look at the convoy. She looks at Aeron."

    "She says one word."

    l "Seren."

    "She does not wait for a response."

    "She turns and walks back toward the chapel."

    athought "Seren."

    athought "That is Anayet's word. That is the word from a3_s19 when Lyra was at the altar with three candles and the word was on her tongue and she did not say it into the room because saying it would have been a performance."

    athought "Seren is the word that means {i}the one who is still becoming.{/i} It is the word the Anayet tradition uses for a soul that has not finished the shape of what it is going to be. It is not a word for the dead. It is a word for the living. It is a word for the living who are in the middle of being changed by something they are walking through."

    athought "She is giving me Seren."

    athought "She is giving me Seren because Seren is the word she has for the thing I am becoming in this act, and she is giving it to me at the edge of the base while fourteen civilians walk east and she is telling me the becoming is not finished and is not expected to be finished and is expected instead to be walked through."

    athought "She said it and she did not wait for a response and the not-waiting is the shape of the word. Seren does not require a reply. Seren is a naming. You do not reply to a naming. You carry it."

    athought "I am carrying it."

    # ========== PHASE 5 — TESSA ==========

    "Tessa walks up to the edge."

    "She is in her medic jacket. The jacket is back on. The top two closures are done and the bottom closure is not — there was no time. She has her clinic datapad under her arm and her supply bag over her shoulder. She is going to the Sector 6 staging point because she is going to run the field clinic at the first arrival point and she is going to run it herself for the first six hours until her relief comes in."

    "She stops at the edge."

    "She sets the datapad down on top of the wall beside Noelle's tablet. She does not speak."

    "Her right hand comes up to Aeron's chest. Flat palm, fingers spread. Her palm goes on the place her palm went in s12 — the sternum. The bone. The center line."

    "The touch is exactly as long as it needs to be and not a second longer."

    t "You are held."

    "She takes her hand off his chest. She picks up her datapad. She walks past him toward the access road. She is not going in the convoy — she is taking the runner shortcut to the Sector 6 staging point, which is thirty minutes by foot along a different path. She will arrive before the convoy."

    "At the edge of the wall she stops and turns back for a half-second."

    t "The board is on my back. It is where I am taking it. It will be in the staging point by the time the first name comes in."

    "Then she is gone."

    athought "She took the board."

    athought "She took the board from the main medical area and she is carrying it to the Sector 6 staging point on her back. The board is rolled up and strapped to a frame and the frame is on her back and the ghost text and the living column and the dead column and LIORA RYLAN on both sides and KESA MARIN and JOREN HALE and DAVEL OSTRA — all of it — is on Tessa's back right now going east along the runner shortcut."

    athought "That is the answer to the question I did not ask her last night. The question I did not ask was: is the board going to stay in the medbay while you go to the field. The answer is: the board is going with her. The board is the shape her counting takes and her counting is going where her work is going and the two are not separable."

    athought "She carried the board across the displacement in Act II. She is carrying it across sectors in Act IV. The board is going to be in whichever room Tessa is counting in. That is the rule. I did not know it was the rule until she said it at the edge of the wall and then I knew it had always been the rule."

    athought "You are held."

    athought "She said that too."

    athought "I am held."

    # ========== PHASE 6 — SELENE ==========

    "Selene walks up to the edge."

    "Selene does not walk fast. Selene walks at the pace of a woman who has been commanding since she was twenty-three years old and who has learned, over that long accumulation of years, that commanders who walk fast are commanders who are being watched, and that there is a pace which tells a base that command is not in a hurry and the not-in-a-hurry is the reassurance the base needs at the edge of a difficult day."

    "She stops beside Aeron at the edge."

    "She does not speak."

    "Not right away. She stands beside him for the length of a full breath. Then another. The silence is load-bearing in a way Aeron has learned to recognize as Selene — the silence is not her withholding a line, it is her being in the room with him in a way that the line is going to arrive out of."

    "Then she speaks."

    sel "Chapter four."

    "A beat."

    sel "We did not break."

    "That is the whole of her turn."

    "She does not leave. Selene is the only one of the five who does not leave after the beat. She stays at the edge of the wall beside him. She is going to stay at the edge of the wall until the convoy is out of sight. That is the shape of her presence tonight."

    athought "We did not break."

    athought "She said {i}we.{/i}"

    athought "Selene does not use {i}we{/i} lightly. Selene uses {i}we{/i} when she is saying the word on the record and she is at the edge of a base and the record is the convoy on the access road and she is at my side and the {i}we{/i} is all six of us — her and me and Noelle and Lyra and Tessa and Zira — and possibly the fourteen civilians and the three runners and the dead on the board and the living on the board and possibly every person who chose Phoenix and every person who was chosen by Phoenix and every person whose name has passed through the broadcast and every person whose name has not yet passed through anything."

    athought "She said we."

    athought "We did not break."

    athought "That is not the same as {i}we won.{/i} That is not the same as {i}we were right.{/i} That is not the same as {i}mercy was the correct answer.{/i} That is the sentence that means {i}we held the shape of the thing we were trying to be, even under the pressure that Phase III put us under, and we are still the thing at the end of Phase III that we were at the start of Phase I, which is not the same thing as having succeeded.{/i}"

    athought "That is what she is giving me. That is the line the act ends on from her side."

    athought "I am going to carry it."

    # ========== PHASE 7 — AERON ALONE WITH SELENE ==========

    "The camera pulls back one small step."

    "Aeron and Selene at the edge of the base. The convoy in the mid-ground, walking east, fourteen civilians and three runners and one runner at the rear. The ridge beyond the convoy. The sun over the east ridge — the cinema choice is the rising sun and the rising sun is the default version and the rising sun is on his face. The light is cold and honest the way s01's light was cold and honest, but twelve days of weight has moved across it and the light is different for the weight."

    "Selene is beside him."

    "He is not alone but he is alone in the way the scene needs him to be alone. The relay has run. Zira has run past. Noelle has given him the tablet. Lyra has given him the word. Tessa has given him the hand on the sternum and the board on her back. Selene is the last one and Selene is going to stay and the staying is her relay gift."

    "Aeron does not speak."

    "He watches the convoy."

    "The convoy is small in the mid-ground now. Fourteen civilians — he can count them from here because the column is loose enough to count. Three runners. The smallest of the children is being held by her mother. The oldest of the adults is walking in the middle of the column, carefully, with one of the runners a half-step behind her in case her weight fails. Oris Telm is in the middle. Paela Venn is at the rear. The column is moving."

    "It is going to keep moving for forty-eight hours."

    "It is going to move through three sectors and two checkpoints and three handoffs. Tessa is going to meet it at Sector 6. Lyra is going to bless it at Sector 4. Zira is going to walk every foot of it. Noelle is going to run the comms layer from her workspace. Selene is going to be at the cipher plate when something goes wrong, because something is going to go wrong, because forty-eight hours of moving fourteen civilians in Echelon's city always produces something going wrong."

    "The convoy is going to arrive with fourteen, or it is going to arrive with fewer than fourteen, and Aeron is not going to know which until Tessa confirms it herself at the last staging point, because Tessa does not confirm numbers she has not seen."

    "The question is going to be at the head of the table the entire time."

    "The question is: what does mercy look like when the enemy has your family's names."

    "Aeron does not have an answer."

    "He is not going to have an answer by the end of Act V either. The question is not a question that gets answered. The question is the shape of the thing they are doing while they walk east. The walking is the shape of the answer and the walking is not the answer itself."

    "He watches the convoy."

    "The sun moves up a quarter-finger-width on the ridge."

    # ========== PHASE 8 — THE LAST LINE ==========

    "Aeron's internal voice takes the last beat of the act."

    "He does not speak it aloud. Selene is beside him and the saying is for him alone, which is how the act is ending — not with a declaration but with a sentence he says to himself at the edge of a wall while a convoy walks east."

    athought "Mercy is a decision made today against a future we do not get to pick."

    "The line is the line Lyra said to him in a3_s11 when she was at her altar and the candles were burning and the word was on her tongue. Lyra said it to him then and he heard it but he did not yet understand it."

    "He understands it now."

    athought "Lyra said that sentence to me in Act III."

    athought "I did not know what she meant. I thought I did. I was wrong."

    athought "I know what she meant now. She meant that mercy is not a reward for the future being what you hoped it would be. Mercy is a decision you make today, inside the shape of a today you are inside, against a future you cannot see and are not going to be given the chance to negotiate with. The future does not promise you it is going to be the kind of future where mercy was the right call. The future is going to be whatever the future is. Mercy is the thing you do anyway, not because it works, but because the doing of it is the shape of the person you are choosing to be inside the today."

    athought "I chose mercy today."

    athought "Yesterday I chose mercy."

    athought "The day before yesterday I chose mercy."

    athought "Every day this act I chose mercy and the choosing cost me things I do not know the full shape of yet and the cost is going to keep arriving for the rest of Act V and for the rest of my life."

    # Callback: Zira's backward clock (a4_s15); Tier Hall age 12 (a1_s01/a1_s09)
    athought "Zira has a clock on her bench that gives back one second per minute. She has been building it for eleven months and she does not know why. I know why. The clock is the shape of the thing we are all doing. We are giving back the time the Aeries took from us, one second at a time, and the giving back is slower than the taking was."

    athought "I am going to keep choosing it."

    athought "Not because it works. Because the shape of the person I am choosing to be is the shape of a person who chooses it."

    athought "Chapter four."

    athought "We did not break."

    # ========== PHASE 9 — THE HOLD ==========

    "The camera holds on the wide for a long beat."

    "Aeron and Selene at the edge of the base. The convoy walking east. The sun on the ridge. The cold and honest morning. Noelle's tablet on top of the wall beside Aeron's elbow. Tessa's field clinic gear already halfway to the Sector 6 staging point on Tessa's back. Lyra walking back to the chapel. Zira running with the convoy. Paela Venn at the rear of the column. Oris Telm in the middle. The five children. The nine adults. The three runners."

    "The question at the head of the table in the council room behind them."

    "The empty chair behind the question."

    "The board rolling east on Tessa's back with LIORA RYLAN on both sides and DAVEL OSTRA at the bottom of the dead column and an undetermined number of spaces waiting beneath him."

    "The sun rising."

    "The wall."

    "The convoy."

    "Silence."

    "Selene does not move."

    "Aeron does not move."

    "The camera holds."

    "Then:"

    # scene black with slowfade
    # play music "music/score/act4_close_long_low_string.ogg" fadein 6.0

    pause 2.5

    centered "{size=+20}END OF ACT IV{/size}"
    pause 1.8
    centered "{size=+12}Chapter I — Shared Authority{/size}"
    pause 2.0
    centered "{size=+10}{i}to be continued in Act V{/i}{/size}"
    pause 2.5

    # scene black with fade
    # stop music fadeout 5.0

    # ========= STATE UPDATES =========
    $ rel_bump("Zira", trust=1)
    $ rel_bump("Noelle", trust=1)
    $ rel_bump("Lyra", trust=1)
    $ rel_bump("Tessa", trust=1)
    $ rel_bump("Selene", trust=1)
    $ canon_set("act4.emp.close", "delivered")
    $ canon_set("phoenix.civilian_move", "underway")
    $ canon_set("tessa.board_traveling_with_her", True)
    $ canon_set("lyra.gave_aeron_seren", True)
    $ canon_set("aeron.carries_lyra_mercy_line", True)
    $ flag("act4_emp_complete", True)
    $ flag("a4_relay_delivered", True)
    $ npc_remember("Zira", "touched_sleeve_and_said_door", tone="runner_vocabulary")
    $ npc_remember("Noelle", "framework_version_two_disclaimer", tone="analysis_as_carrying")
    $ npc_remember("Lyra", "gave_seren_at_the_wall", tone="naming_without_reply")
    $ npc_remember("Tessa", "board_on_her_back_to_sector_six", tone="counting_goes_where_work_goes")
    $ npc_remember("Selene", "we_did_not_break", tone="chapter_four_named_on_record")
    $ tp_seed("a4.emp.handoff")
    $ metric("act4_emp_scenes_delivered", add=1)
    $ metric("aeron_mercy_choices_cumulative", add=1)
    $ scene_mark(_current_scene_id, "exited")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s22_act_four_close_emp
# cann.chapter: Act IV — Shared Authority
# cann.chapter_start: False
# cann.chapter_end: True
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - Approximately oh-nine-thirty on the morning of the civilian move,
#     twelve hours after the Phase III night of erotic beats and
#     approximately ninety minutes after the council in s21. The
#     forty-eight-hour move is underway. Aeron is at the edge of the
#     secondary base watching the Sector 11 convoy walk east along the
#     access road toward the Sector 6 staging point.
# cann.what_happened:
#   - Aeron stands at the edge of the base watching the convoy of
#     fourteen civilians walk east. Each of the five LIs comes to him
#     sequentially at the edge of the wall, does one beat, and leaves.
#     The relay is the scene.
#     - Zira: runs past on her way to the convoy, touches his sleeve,
#       says one word: "Door." (Runner vocabulary for a threshold
#       crossed — we are through the decision and into the move.)
#     - Noelle: brings him a tablet with version two of the move
#       framework. Header: "Framework for the Move — Version Two —
#       Not an Answer, a Carrying." She tells him the first version
#       existed and she deleted it because she caught herself writing
#       a framework that pretended to have answers.
#     - Lyra: walks up, says one word — "Seren" — and walks back
#       toward the chapel without waiting for a reply. Seren is the
#       Anayet word for "the one who is still becoming."
#     - Tessa: puts her hand on his sternum (the s12 gesture) and
#       says "You are held." Takes her hand off. Then tells him the
#       board is on her back going to the Sector 6 staging point.
#       The board is traveling with her because her counting goes
#       where her work goes.
#     - Selene: walks up, stands beside him for a full breath, and
#       says: "Chapter four. We did not break." She does not leave
#       after the beat. She stays at the edge of the wall with him
#       until the convoy is out of sight.
#   - Aeron alone with Selene for the final beat. Internal monologue
#     closes the act. He understands Lyra's a3_s11 line for the
#     first time — the line he is now going to speak to himself as
#     the act's last sentence:
#     "Mercy is a decision made today against a future we do not get
#     to pick."
#   - ACT IV END TITLE CARD. "End of Act IV — Chapter I — Shared
#     Authority — to be continued in Act V."
# cann.aeron_state:
#   - The thesis has held. The act has cost him things whose full
#     shape he does not know yet, and he is at peace with the
#     non-knowing. He has moved from delegating the question (s21)
#     to carrying the question (s22). The carrying is the answer
#     he has. It is not a solution — it is the shape the doing
#     takes.
#   - First time he says Lyra's a3_s11 mercy line to himself. The
#     internalization is the act's last character beat. The line
#     has moved from being a sentence Lyra said at her altar to
#     being a sentence Aeron says to himself at the edge of a wall.
#     This is a canonical inheritance.
# cann.path_tracking_mechanics:
#   - EMP. Linear. No player choice.
#   - rel_bump +1 trust for all five LIs. The relay is the closing
#     gift each LI gives and Aeron gives back.
#   - canon_set act4.emp.close "delivered" — Act IV EMP path is now
#     canonically complete. Act V entry can check this state.
#   - canon_set phoenix.civilian_move "underway" — the move is in
#     motion across the Act IV/V boundary. Act V will open with it
#     still in motion. No completion until mid-Act V.
#   - canon_set tessa.board_traveling_with_her True — the board is
#     now a traveling object, not a fixed object. Any Act V scene
#     that references the board must account for where Tessa is.
#   - canon_set lyra.gave_aeron_seren True — load-bearing Lyra
#     state. The word is now Aeron's to carry. Act V Lyra beats
#     may return to Seren.
#   - canon_set aeron.carries_lyra_mercy_line True — the
#     internalization of the a3_s11 mercy line. The line is now
#     available as Aeron's internal vocabulary in Act V.
#   - flag act4_emp_complete True — Act IV EMP gate. Required for
#     Act V EMP entry.
#   - flag a4_relay_delivered True — the relay closing pattern.
#   - tp_seed a4.emp.handoff — True Path seed. The relay itself
#     (five LIs arriving and departing without coordinating) is
#     a True-Path-legible shape. The whole act has been building
#     toward this handoff.
#   - metric aeron_mercy_choices_cumulative +1 — accruing metric
#     for Act V and beyond. Counts the number of days/scenes Aeron
#     has actively chosen mercy against the weaponization pressure.
#   - metric act4_emp_scenes_delivered +1 — bookkeeping metric.
# cann.thematic_flags:
#   - The answer to the act's question is provisional, expensive,
#     and correct. "Can I lead without turning leadership into a
#     weapon?" — Yes, and it is expensive. The expense is the
#     forty-eight-hour move and the injuries Tessa has named and
#     the list Rhea still has and the question at the head of the
#     council room table.
#   - Relay, not choir. The act's thesis in closing form. The five
#     LIs each give one beat, each distinct, each essential, none
#     coordinated. The shared authority is the shape the relay
#     takes, not the coordination of it.
#   - Mercy as a decision against a future we do not get to pick.
#     Lyra's a3_s11 line now internalized by Aeron. The
#     inheritance is the act's last character beat.
#   - The question at the head of the table. The empty chair from
#     s21 carried forward into s22 as an internal image Aeron is
#     carrying with him. The question is at the head and Aeron is
#     at the edge of a wall.
#   - No over-closure. The act does not resolve. It hands forward.
#     The convoy is still moving. The list is still in Zira's
#     jacket. Rhea still has her copy. Marcus is still in his grey
#     room cataloguing. The sun is either rising or setting and the
#     choice is cinema, not thematic — the act has earned the rise
#     but the fall is available and the file flags it.
# cann.character_moments:
#   - Aeron: the edge of the wall. The receiving of each LI's beat
#     without response. The internal understanding of Lyra's a3_s11
#     line. The refusal to cross the access road. The carrying of
#     the question.
#   - Zira: "Door." One word, in motion. Runner vocabulary at full
#     compression.
#   - Noelle: "Version two." The disclaimer header. The naming of
#     the deleted first version. Noelle learning, out loud, to
#     write frameworks that do not pretend to have answers.
#   - Lyra: "Seren." The word without a reply. The walking back
#     to the chapel. The naming as the blessing.
#   - Tessa: "You are held." The board on her back. The field
#     clinic going east. Her counting going where her work goes.
#   - Selene: "Chapter four. We did not break." The staying after
#     the beat. The only LI who does not leave. The we.
# cann.callbacks:
#   - a3_s11 (Lyra): the mercy line. The scene's load-bearing
#     inheritance. "Mercy is a decision made today against a
#     future we do not get to pick."
#   - a3_s19 (Lyra Anayet / Seren): the word Lyra did not say
#     into the room at her altar. In s22 she says it into the
#     room at the edge of the wall.
#   - a3_s13 (Tessa scar and steady): the sternum gesture from
#     s12 carried forward one more time. The hand on the
#     sternum is now the shape of Tessa's "you are held" —
#     her three-scene Act IV arc condensed into one gesture.
#   - a4_s01 (morning after broadcast): the cold and honest
#     light. S22's light is the same light twelve days later
#     with twelve days of weight on it.
#   - a4_s05 (Selene delegation): the lesson Selene has been
#     teaching Aeron all act. The "we did not break" is her
#     naming, on the record, that the lesson has taken.
#   - a4_s06 (Tessa silent board): the board as a traveling
#     object. S06's board was a fixed object with a clip lamp.
#     S22's board is a traveling object on Tessa's back. The
#     evolution is the act's closing Tessa beat.
#   - a4_s14 (side chair, parallel batch): the refusal of the
#     head of the table carried forward.
#   - a4_s20 (Tessa erotic deepening): the jacket back on, the
#     closures not all done. The hour that ended is now behind
#     them and the work is back in front of them. The act is
#     honest about the return.
#   - a4_s21 (Marcus second cut / council): the framework
#     decided in s21 is the framework being executed in s22.
#     The empty head chair is the internal image Aeron carries
#     with him to the wall.
#   - Parallel batches (s15 Zira, s17 Selene, s18 Noelle, s19
#     Lyra): the erotic deepening beats from Phase III are
#     honored in the relay. Each LI comes to Aeron with the
#     vocabulary the parallel scene gave them. The act is
#     keeping its canon.
# cann.requires_followup:
#   - Act V opens with the civilian move still underway. The
#     canon_set phoenix.civilian_move "underway" state is the
#     first state Act V must read against.
#   - Tessa's board is in the Sector 6 staging point as of the
#     act's close. Any Act V Tessa scene must account for where
#     the board is.
#   - Rhea still has her copy of the list. Marcus is still
#     operational. The surgical-on-humans threat is deferred,
#     not removed.
#   - The Seren word is now Aeron's to carry. Act V Lyra beats
#     may return to it.
#   - The a3_s11 mercy line is now canonical Aeron internal
#     vocabulary. Any Act V internal monologue may reference it.
#   - Paela Venn, Oris Telm, and the fourteen civilians are a
#     canonical headcount. Act V must deliver or account for
#     each of them.
#   - Act IV EMP path is formally closed by this scene. Act V
#     EMP path entry point is gated on flag act4_emp_complete.
