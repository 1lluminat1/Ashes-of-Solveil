# =======================================================
# ACT 4 - Scene 20a: Command and the Door (Empathy Path)
# File: a4_s20a_command_and_the_door_emp.rpy
# Type: POLY BEAT — SELENE + ZIRA + AERON
# Placement: after s20 (Tessa erotic deepening), before s21
# (Marcus second cut). Late night. The civilian network move
# is being planned. Selene commands strategy. Zira runs
# routes. They have always worked in parallel — never
# overlapped intimately. This is the first time the two of
# them are together with Aeron outside of a tactical setting.
# The emotional core: two women who respect each other's
# professional edges and know they are shaping the same
# person from different directions. Their intimacy is about
# shared WEIGHT, not shared desire.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s20a_command_and_the_door_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s20a_command_and_the_door_emp:


    # Gallery — unlock this scene in the character replay grid.
    $ gallery_unlock("a4_s20a_command_and_the_door_emp")
    $ show_timeline("36th of Forge, 390 A.C.", "01:00", "Phoenix Secondary Base — Cipher Alcove")
    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Five movements.
    #         (1) The cipher alcove from outside. 50mm, locked. The alcove
    #             is the narrow room off the command wing where Selene
    #             keeps the operational ciphers — a room that is hers by
    #             function and temperament, the way the workshop is Zira's
    #             and the mapping station is shared. The door is open. Not
    #             the six-inch gap of the mapping station — fully open,
    #             the way Selene leaves doors when she is working at
    #             command pace and the door is not a variable she has time
    #             to manage. Two voices inside. The camera finds the voices
    #             from the corridor, the same grammar as s14a, but the
    #             corridor is the command wing and the voices are different.
    #         (2) Inside: 35mm, slow pan. Selene is at the cipher desk —
    #             the narrow metal desk bolted to the wall, the desk that
    #             is too small for two people and has two people at it
    #             tonight. The cipher — the brass cylindrical mechanism
    #             she carries as a grounding object — is on the desk
    #             surface between two stacks of operational documents. Zira
    #             is standing at the wall map — the large tactical map of
    #             the civilian network routes that Selene had moved from
    #             the war room to the cipher alcove three days ago because
    #             the war room had too many eyes for the kind of planning
    #             she needed to do. Zira's charcoal marks are on the map.
    #             Selene's red-pencil annotations are beside them. Two
    #             handwritings on the same surface — the third iteration
    #             of the two-handwriting motif (cf. s14a relay map, s16a
    #             datapads).
    #         (3) The doorway — Aeron. 35mm, locked from inside. He
    #             appears in the open door the way he appeared in the
    #             mapping station in s14a. But the two-look here is
    #             different. These two faces have a different relationship
    #             to his face. Selene has been his co-commander for three
    #             years. Zira has been building him doors for three months.
    #             The two-look is the look of two women who have shaped
    #             the same man from different angles and have never been
    #             in a room together with the man and the shaping at the
    #             same time.
    #         (4) The table — three-shot. Wide, low. The cipher desk is
    #             the central object. It is too small for three. Selene at
    #             the desk chair. Zira at the wall map. Aeron at the door
    #             end of the desk, leaning against the wall beside the
    #             frame. Three bodies in a room built for one.
    #         (5) The close — aftercare. Different camera vocabulary. The
    #             cipher on the desk, birdseye. Two hands reaching for it
    #             at the same moment — Selene's and Zira's. The hands
    #             meeting on the brass. The hands releasing. Hold. Fade.
    # LIGHTING: Cipher alcove at late-night. One practical — the desk
    #           lamp that Selene keeps bolted to the left edge of the
    #           cipher desk. It is the same model as the desk lamp in her
    #           quarters but this one has never been adjusted for warmth.
    #           It is the working lamp. The light is cooler than the
    #           two-lamp arrangement in the mapping station. The wall map
    #           is half in the lamp's pool and half in shadow. Zira is
    #           working at the edge of the light. Selene is in the center
    #           of it. When Aeron arrives the corridor light spills in
    #           through the open door but does not change the room because
    #           the door was already open. No overhead. No second lamp.
    #           If the poly gate opens: Selene reaches over and clicks the
    #           desk lamp to its lower setting — a half-step down that
    #           changes the color temperature from working-cool to
    #           something warmer without leaving the operational register.
    #           The lamp adjustment is the scene's visual consent.
    # SFX: Command wing at late-night. Different acoustic from the
    #      mapping station — the corridor outside is shorter, the walls
    #      are thinner, the distant sound is not the generator but the
    #      cipher room's ventilation unit which runs at a higher pitch.
    #      Selene's particular sound: the red pencil on paper, a slightly
    #      harder scratch than Zira's charcoal. Zira's particular sound:
    #      the charcoal on the wall map, softer, the sound of a woman
    #      whose marks are designed to be erased and redrawn. The cipher
    #      on the desk makes no sound. It does not need to make a sound.
    #      Its weight on the metal desk surface is the sound — the faint
    #      vibration of brass on steel when someone walks past or leans
    #      on the desk edge. No music bed until the poly gate. At the
    #      poly gate, if it opens: a held note lower than the cello from
    #      Zira's scenes, steadier than the prayer-note from Lyra's —
    #      the note of a woman who has been carrying command weight for
    #      nineteen years and is setting it down on a surface that has
    #      two other people near it.
    # FX/COMP: THE CIPHER. Brass cylinder on the desk. Selene's grounding
    #          object — the object she reaches for when the command
    #          register needs a physical anchor. It is the object from
    #          s10 (delegate the question) and s12a and s17. Tonight it
    #          is on the desk between the operational documents, not in
    #          her hand. The not-in-her-hand is the scene's first signal
    #          that she is working at a different pitch tonight.
    #          THE WALL MAP. The civilian network routes. Selene's red
    #          pencil and Zira's charcoal on the same surface. The two
    #          handwritings are the visual thesis — command strategy and
    #          route intelligence on the same map, aimed at the same
    #          civilians, drawn by two women who have been shaping the
    #          same operational picture from different rooms.
    # BLOCKING: Selene seated at the cipher desk. Zira standing at the
    #           wall map. Aeron enters and leans against the wall by the
    #           door. He does not approach the desk because the desk is
    #           Selene's and the approach is not his to make tonight. He
    #           does not approach the wall map because the wall map is
    #           where Zira is working and the approach would interrupt
    #           her line. He stays at the door end of the room. Later —
    #           if the poly gate opens — the blocking shifts from the
    #           three-point scatter to a close configuration at the desk.
    #           Selene stays in the chair. Zira comes to the desk edge.
    #           Aeron comes to the other desk edge. The three of them
    #           around the cipher desk that was built for one.
    # FACE: Selene — the stripped register from s17. The letter has been
    #       turned face-down. The teaching frame has been retired. What
    #       is in her face tonight is the face of a woman who commands
    #       by reflex and has been commanding the civilian network move
    #       for forty-eight hours and is reaching the limit of what
    #       command without witness looks like. The exhaustion is not
    #       physical. The exhaustion is structural. She has been the
    #       single load-bearing wall in the command architecture for
    #       nineteen years and the wall has a crack tonight and the
    #       crack is visible if you know where to look.
    #       Zira — the Ashmarket operational from s15 and s16a. She is
    #       in route-planning mode at the wall map. Her charcoal is on
    #       the map surface. She is working at the intersection of her
    #       network and Selene's command structure and the intersection
    #       is the civilian move. She has been in this room with Selene
    #       for two hours and the two hours have produced a working
    #       respect that both women recognize as the ground floor of
    #       something neither has named.
    #       Aeron — the face of a man who has walked into a room
    #       expecting to find Selene alone and has found Selene and
    #       Zira together at a planning surface and the together is not
    #       tactical. The together has a temperature he has not felt in
    #       a command wing room before.

    # ========= VOICE BASELINE =========
    # EMP cadence. Three-voice scene. Selene speaks in the stripped
    # command register from s17 — no teaching, no doctrine, the voice
    # of a woman who is tired of being the architecture. Zira speaks
    # in the Ashmarket precision from s15 and s16a — aimed at Selene
    # tonight rather than at Aeron, and the aiming-at-Selene is new
    # territory for both of them. Aeron is sparse. He speaks least in
    # the first three phases. His thoughts carry the interior. The
    # scene's diction rule: Selene and Zira talk TO each other about
    # Aeron. They do not route through him. The routing-past-him is
    # the scene's structural grammar and the grammar is load-bearing.

    # scene bg_cipher_alcove_night_late_emp with dissolve
    # play ambient "sfx/ambient/command_wing_night_late.ogg" fadein 2.5

    # ========== PHASE 1 — TWO VOICES ==========

    "Oh-one-forty. The base is in its deepest register. The overnight crew has been at their stations for two hours and forty minutes. The war room is running on the skeleton watch Selene set before she left it."

    "She left the war room at twenty-three hundred."

    "She has been in the cipher alcove since."

    "The cipher alcove is the narrow room off the command wing where the operational ciphers are stored in a locked cabinet that only Selene and Aeron can open. It is a room that was designed for one person, one desk, one chair. It was not designed for planning. It was designed for encoding. Selene has been using it for planning since the civilian network move became the kind of plan that could not be planned in a room with more than two eyes on it."

    "Tonight it has four eyes."

    "Aeron is walking the command wing at oh-one-forty because the ops table ran out of things it could give him an hour ago and walking is the alternative to lying in quarters and staring at the inventory of decisions he has not made."

    "He hears two voices."

    "The first voice is Selene's."

    sel "The western column cannot move until the relay at junction nine is confirmed. I am not sending sixty civilians into a corridor that has a gap in the intelligence chain."

    "The second voice is Zira's."

    z "The relay at junction nine is my relay. I confirmed it at eighteen hundred. The runner is in position. The gap you are seeing on the map is a documentation gap, not an operational gap."

    sel "Then close the documentation gap. If it is not on the map it does not exist in the command layer."

    z "I am closing it now."

    "The small sound of charcoal on paper. Zira marking the wall map."

    z "The mark is on the map. Junction nine. Confirmed eighteen hundred. Runner Voss. Do you need the secondary confirmation or is the mark sufficient."

    sel "The mark is sufficient if it is your mark."

    z "It is my mark."

    sel "Then it is sufficient."

    "A beat."

    athought "They are working the civilian move."

    athought "Selene and Zira. In the cipher alcove. At oh-one-forty. They are working the same problem I was working at the ops table an hour ago, and they are working it in a room I did not know Zira had access to, at a time I did not know Selene was still awake."

    athought "I am standing in the command wing corridor listening to a woman who commands strategy talk to a woman who runs routes, and the talking has no space in it that is shaped like me."

    athought "The space that is not shaped like me is the first thing I have heard tonight that does not cost me anything."

    "He listens."

    sel "The eastern column is the problem. The timing model from Noelle gives us a fourteen-minute window. The fourteen-minute window assumes the relay at the market junction holds for the full duration. Zira — what is the failure rate on a relay under sustained load for fourteen minutes."

    z "Under sustained load at this volume of civilian traffic. With the current runner rotation. At this time of night."

    sel "Yes."

    z "Seven percent. But the seven percent is front-loaded. If the relay holds for the first four minutes it will hold for fourteen."

    sel "Then the first four minutes are the four minutes I need to plan for."

    z "Yes."

    sel "I am planning for them now."

    "The scratch of Selene's red pencil on operational paper. A harder sound than Zira's charcoal. The two sounds in the same room — one softer, one harder — are the acoustic version of two handwritings on the same surface."

    athought "They have been here for a while. The working rhythm between them is not a first-hour rhythm. The rhythm has settled. Selene is asking questions in the command register and Zira is answering them in the operational register and neither of them is translating for the other. They are speaking at the same altitude."

    athought "I have been sharing a command table with Selene for three years and I have never heard her speak to another woman at this altitude. She speaks to Tessa at the altitude of trust. She speaks to Noelle at the altitude of data. She speaks to Lyra at the altitude of respect. She is speaking to Zira at the altitude of equals."

    athought "I am going to walk in now."

    # ========== PHASE 2 — THE DOORWAY ==========

    "He steps into the open doorway."

    "The cipher alcove is smaller than the mapping station. The desk is against the far wall. The wall map is on the left. The cipher — brass, cylindrical, the size of a fist — is on the desk between two stacks of operational documents. Selene is in the desk chair. Zira is at the wall map with a charcoal stick in her right hand."

    "Two faces look up."

    "Selene looks up from the desk. Her face is the stripped register from s17 — no mask, no teaching posture, the face of a woman who has been in command mode for nineteen years and is in command mode now and the command mode tonight has a crack in it that was not there six months ago. Her red pencil is in her hand. The cipher is on the desk within reach but she is not holding it."

    "Zira looks up from the wall map. Her face is the Ashmarket operational — sharp, precise, her charcoal-stained fingers on the map surface. But she is not looking at Aeron the way she looked at him in the mapping station doorway. She is looking at him from inside a working rhythm she has built with Selene over the last two hours, and the looking has the quality of a woman who is inside a room that has its own grammar and the man in the doorway is being assessed for whether he can speak it."

    "The two-look."

    "It is the third two-look. The third time two women have looked up at Aeron from inside a collaboration he did not build. The mapping station with Lyra and Zira. The workspace with Noelle and Zira. The cipher alcove with Selene and Zira."

    "Zira is the common variable."

    athought "She is in all three rooms."

    athought "Zira is in all three rooms. She is the woman who has been building doors, running routes, drawing maps, and she has put herself into every room in this building where two people are doing the work that keeps the civilians alive. The three two-looks are three rooms and Zira is in all of them and I am the man who walks in after the room has already formed."

    "Selene does not stand."

    sel "I expected you an hour ago."

    a "I was at the ops table."

    sel "I know you were at the ops table. I expected you to leave the ops table an hour before you did. You are getting slower at knowing when the table has given you everything it has."

    "It is a Selene sentence. The kind of sentence that sounds like correction and is actually diagnosis. He has been hearing these sentences for three years. He can read the grammar."

    a "You are right."

    sel "I am usually right about when you have stayed too long at a table."

    "Zira does not say anything. She is watching the exchange the way she watches a relay confirm — reading the signal, not the words."

    zthought "She talks to him like a woman who has been reading him for a decade. She talks to him the way I talk to a route I have walked a hundred times — she knows where the turns are. She knows where the dead spots are. She knows when he has been at the table too long because she has been counting his table-hours for three years."

    zthought "I have been counting his table-hours for three months."

    zthought "The difference in the count is the least interesting thing about us."

    "She thinks Lyra's line from s14a — the least interesting thing about us — and does not know she is echoing it. The echo is the scene's interior callback."

    a "How long have you been here."

    sel "Since twenty-three hundred. Zira arrived at twenty-three thirty."

    z "She did not invite me. I came because the relay updates needed to be on the wall map before the morning briefing and the wall map is in this room."

    sel "She came because the relay updates needed to be here and because she is the only person in this building who walks into a room I am working in without asking whether she is allowed to be in the room."

    "Zira looks at Selene."

    z "I did not ask because the door was open."

    sel "The door was open because I was working."

    z "The door was open because you were waiting for someone to walk through it without knocking."

    "A beat. Selene's red pencil stops on the operational document."

    "The beat is two women recognizing that Zira has just read a room that Selene did not know she was broadcasting."

    sthought "She read the door. She read the open door as a signal I did not know I was sending. I left the door open because I was working at command pace and the door was not a variable I was managing. But she is right. She is right and I did not know she was right until she said it."

    sthought "Zira reads doors."

    sthought "I command rooms. She reads doors. Those are not the same skill. Those are complementary skills. I have been in this room with her for two hours and fourteen minutes and I have not had a complementary skill in a room with me since Kael died."

    sel "You are reading me."

    z "I am reading the room. You are in the room. The distinction is slim."

    "A beat."

    sel "All right."

    sel "You can stay."

    z "I was not going to leave."

    "Aeron is in the doorway watching two women who have already negotiated a working arrangement he was not part of, and the arrangement is operational and personal at the same time, and the operational-and-personal is a register he has only heard Selene use with one other person, and that person was Kael, and Kael is dead."

    athought "She is letting Zira read her."

    athought "Selene does not let people read her. Selene is the reader. Selene is the one who sits in the chair and reads the room and reads the face and reads the operation. I have seen Selene be read exactly twice — once by Tessa in a medical exam that Selene did not know was a reading, and once by Kael in a meeting I was not supposed to be in."

    athought "Zira is reading her. And Selene is letting her."

    "He comes in. He leans against the wall beside the door frame. He does not approach the desk."

    a "What do you need from me."

    sel "Nothing operational. The plan is where it needs to be for tonight. Zira's relays are confirmed. The timing model is set. The morning briefing is prepared."

    a "Then why am I here."

    sel "Because you are always here when I am in a room at oh-one-forty and you know it."

    # ========== PHASE 3 — THE RECOGNITION ==========

    "They work."

    "For the next fifteen minutes they work the final details of the civilian network move in the three-body configuration the cipher alcove allows — Selene at the desk on command structure, Zira at the wall map on route intelligence, Aeron at the door end on operational bridge. The room is too small for three people to work without awareness of each other's bodies. Selene's chair is two feet from Zira when Zira turns from the wall map. Aeron's shoulder is against the frame and his voice carries the five feet to the desk without raising."

    "During the work, Aeron notices things."

    "He notices that Selene defers to Zira on route security without the command register — no 'confirmed' or 'noted,' just a nod and a red-pencil mark that absorbs Zira's intelligence into the command layer. He notices that Zira defers to Selene on strategic timing without the Ashmarket flat — the deference has an edge of genuine respect that Zira does not give to structures she has not tested."

    "He notices that Selene has not picked up the cipher."

    "He notices that Zira notices that Selene has not picked up the cipher."

    athought "The cipher is on the desk. Selene is not holding it. Selene holds the cipher when the command register needs grounding. The cipher is brass and it is the weight she reaches for when the architecture is shaking. She is not reaching for it tonight."

    athought "Either the architecture is not shaking, or it is shaking in a way the cipher cannot ground."

    "The work reaches a natural pause. The final relay confirmations are marked. The timing gaps are closed. The morning briefing is complete on paper."

    "Selene sets the red pencil down on the desk. She leans back in the chair."

    "Zira sets the charcoal stick on the map ledge. She turns from the wall map."

    "Aeron stays at the door end."

    "The cipher alcove is quiet."

    "Selene looks at Zira."

    "The look is not a command look. It is not a briefing look. It is the look of a woman who has been working at operational altitude with another woman for two hours and fifteen minutes and the altitude has burned through the professional register and left something underneath, and the something is about to be named."

    sel "You have been building him an exit plan."

    "She says it at the desk. She says it in the stripped register — not the command register, the register from s17, the register she used when she told Aeron she did not know how to be held by a student. She is using that register on Zira now."

    sel "I have been teaching him to stay."

    sel "Those are not the same thing."

    "A beat."

    "Zira does not look away from Selene."

    z "They are not the same thing."

    z "But they are the same man."

    "The sentence lands in the cipher alcove the way a sentence lands in a room where two people have been circling the same subject from different corridors and have just met at the junction."

    $ nudge_poly("selene_zira_recognized", delta=1)

    "Selene's hand comes to the desk surface — not to the cipher, to the desk surface beside the cipher, her palm flat on the metal."

    sthought "She said they are the same man."

    sthought "I have been teaching him to stay for three years. The staying has been my curriculum. The staying has been the doctrine I wrote with his body in the room — the doctrine of the chair, the doctrine of the table, the doctrine that says: you are here, and here is where the command lives, and the command needs your body in it."

    sthought "Zira has been building him an exit plan for three months. The exit plan is not a contradiction of the staying. The exit plan is the other side of it. The exit plan says: you can leave, and the leaving is real, and the door works, and a woman who builds doors has built one for you."

    sthought "A woman who teaches staying and a woman who builds doors. We have been shaping the same man from two directions and the man is in the room and the two directions are in the room and I am about to say a thing I have not said in nineteen years of command."

    sel "I knew about the exit plan."

    z "I know you knew."

    sel "I did not stop it."

    z "I know you did not stop it."

    sel "I did not stop it because the exit plan was the thing I could not build for him. A teacher cannot build her student a door to leave through. The teacher can only make the room worth staying in. You built the door. I built the room. Neither of us consulted the other."

    z "Neither of us needed to."

    sel "No."

    "A long beat."

    sel "And now we are in the same room."

    z "We have been in the same room for two hours and seventeen minutes."

    sel "I am not talking about the cipher alcove."

    z "I know you are not talking about the cipher alcove."

    "Zira crosses from the wall map to the desk. She does not sit — there is only one chair. She stands at the edge of the desk the way she stood at the edge of Noelle's desk in s16a — the position of a woman who does not need a chair to be in a room."

    "The two of them are close now. Selene in the chair, Zira at the desk edge. The cipher is between them on the desk surface."

    z "I have been in three rooms in this building with two women and one man. The mapping station with Lyra. The workspace with Noelle. This room with you."

    z "The three rooms are three different rooms. The three rooms are also the same room."

    sel "What is the same room."

    z "The room where two women discover that the thing they share is not the man. The thing they share is the weight of what the man costs."

    "Selene closes her eyes for a single second. Not a flinch. The closing of a woman who has just heard a sentence she has been carrying without a word for."

    "She opens her eyes."

    sel "Nineteen years."

    z "Three months."

    sel "Nineteen years of carrying the weight of what he costs. And three months of carrying the weight of what he costs. And the nineteen and the three are in the same room tonight."

    z "The time difference is the least interesting thing about us."

    "She says it the same way she said it to Lyra in s14a. The sentence is Zira's. The sentence is hers to repeat because it is hers and it is true every time."

    "Selene looks at Aeron."

    "Aeron has not spoken since 'then why am I here.' He has been at the door end of the cipher alcove listening to two women name the thing he has been carrying as a geometry without a name."

    sel "You have been quiet."

    a "I have been listening to two women say the thing I did not know how to say."

    sel "What is the thing."

    a "The thing is that I have been shaped by both of you and the shaping was not coordinated and it did not need to be. You taught me to stay. She built me a door. I have a room and I have a door and the room and the door are both real."

    a "I do not know what to call that except honest."

    "A beat."

    $ nudge_poly("selene_zira_weight_shared", delta=1)

    # ========== PHASE 4 — POLY GATE ==========

    if metric("poly_pressure") >= 3:

        "The quiet in the cipher alcove is different from the quiet of the mapping station or the workspace. The mapping station quiet was the quiet of logistics completed. The workspace quiet was the quiet of a failure rebuilt. This quiet is the quiet of command."

        "Selene's hand on the desk surface moves. Not toward the cipher. Away from it. Toward the edge of the desk where Zira is standing."

        "She does not touch Zira. The hand stops at the edge of the desk. The stopping is the grammar — the grammar of a woman who has been in command for nineteen years and knows that the difference between reaching and stopping is the difference between giving an order and making a request."

        sthought "I am going to say something I have not said in front of another person since Kael."

        sthought "I am going to say it because Zira read the door. I am going to say it because the door was open and she walked through it and she has been in the room for two hours and seventeen minutes and the room has changed. The room was a command room when she walked in. The room is still a command room. But the command has cracked, and the crack is the place where Zira's charcoal meets my red pencil, and the crack is not a failure. The crack is a door."

        sthought "A door in the command. I did not build it. She did."

        sel "I am not doing this as a commander tonight."

        "She says it at the desk. She says it in the register that is below the stripped register — the register that exists under nineteen years of architecture. The register of a woman."

        "Zira looks at her."

        z "Then who are you doing it as."

        sel "A woman who has nineteen years of this and is tired of carrying it alone."

        "The sentence fills the cipher alcove the way a cipher fills when the last tumbler falls — a small mechanical sound of a thing that was locked and is now not locked."

        "Zira's hand comes to the edge of the desk where Selene's hand stopped. The two hands are close. Not touching. The distance is the width of the cipher."

        z "I have been carrying weight for three months. You have been carrying weight for nineteen years. I cannot carry nineteen years. I can carry tonight."

        sel "Tonight is a start."

        "Selene looks at Aeron. Her face is the s17 face — the face of a woman who cried against the top of his head and did not hide it. The face is older than the command and younger than the grief and the age is the age of a person, not a rank."

        sel "Aeron."

        a "Yes."

        sel "Come to the desk."

        "He pushes off the wall. He crosses the five feet of the cipher alcove. He stands at the desk edge opposite Zira — the two of them at either end of the desk, Selene in the chair between them."

        "The cipher is on the desk. Three people around it. The brass is catching the desk lamp."

        # ========== CONSENT GATE ==========

        "Selene reaches for the desk lamp. She clicks it to the lower setting. The light shifts — from working-cool to something warmer. The wall map goes softer. The cipher glows."

        "She looks at Aeron. She looks at Zira. The two-look from the other side — a commander looking at two people and deciding that the command register is not the register for the next hour."

        sel "I am going to say three things. All three of them are true. You pick which one."

        sel "All three of them end with the three of us in this room. That is not the question. The question is how far from the desk we go."

        menu:
            "Stay. Both of you.":
                jump a4_s20a_command_door_full

            "Stay. But slowly -- I need to remember how this works when I am not leading.":
                jump a4_s20a_command_door_slow

            "I can't turn it off tonight. Just sit with me.":
                jump a4_s20a_command_door_sit

        # ========== VARIANT A — FULL ==========

label a4_s20a_command_door_full:

        a "Stay. Both of you."

        "He says it at the desk. He says it the way he said stay in Zira's workshop doorway — short, flat, true. The word is the same. The room has two more people in it."

        "Selene's hand on the desk surface closes into a loose fist — not tension, release. The fist of a woman who has been holding the desk edge for two hours and is letting the holding go."

        sel "Good."

        "She looks at Zira."

        sel "I delegate the question to both of you tonight."

        "The sentence. The s10 sentence. Delegate the question. But the register is not doctrinal. The register is personal. The delegate is not about command or curriculum. The delegate is about a woman who has been carrying nineteen years of questions alone and is handing the weight to two people who are in the room."

        z "I did not expect that."

        sel "Neither did I. That is exactly why it needed to happen."

        "Zira's hand finds Selene's fist on the desk. She does not open the fist. She holds the fist — the closed shape of nineteen years of command — in her open hand. The open hand and the closed fist on the desk surface."

        "Aeron's hand finds the desk surface between them. Not on either woman's hand. On the desk. The bridge position. His hand between two hands the way his body has been between two forms of attention for three months."

        "The three of them at the desk. The cipher between them. The desk lamp at its lower setting."

        # ---------- [ THE INTIMATE BLOCK — PLAYER-AUTHORED ] ----------
        # [INTIMATE CONTENT HERE]
        # Full variant. Three-body intimacy in the cipher alcove. The
        # desk lamp is at its lower setting. The cipher stays on the
        # desk. Selene drives the register — she is the one who
        # delegated the question, and the delegation is her version of
        # Zira's door. She is not commanding. She is receiving. The
        # receiving is the thing she has not done in nineteen years
        # and the nineteen years are in the room. Zira brings the
        # precision from the workshop — the same hands that build
        # clocks and draw routes, now on a different surface. Aeron
        # is the bridge between the woman who taught him to stay and
        # the woman who built him a door. The cipher alcove is too
        # small for this. The too-small is the point. They do not
        # move to a larger room. The desk chair gets pushed back. The
        # wall is involved. The map is behind them. The desk lamp
        # stays on at its lower setting. Nothing goes dark.
        # ---------- [ END INTIMATE BLOCK ] ----------

        jump a4_s20a_command_door_aftercare

        # ========== VARIANT B — SLOW ==========

label a4_s20a_command_door_slow:

        a "Stay. But slowly."

        a "I need to remember how this works when I am not leading."

        "He says it at the desk. The second sentence is for Selene. The second sentence is a man telling a woman who taught him command that he needs to find the register that exists under the command, and he needs the finding to be slow enough that the register does not break when he reaches it."

        "Selene's mouth does the corner thing — the acknowledgment from s17 that is not a smile and is not not-a-smile."

        sel "Slowly is a register I have not used in eight years."

        "She says it the way she said I have not said that sentence in eight years in s17. The eight years is Kael. The eight years is the last time she was slow about anything with another person."

        z "Slowly is a register I know."

        "She says it to Selene. Not to Aeron. She is telling Selene about the workshop the way she told Lyra about the workshop in s14a — one woman giving another woman the information that makes the room possible."

        sel "Then you set the pace."

        "The command is not a command. The command is Selene handing the pace to a woman she has known for three months because the pace of nineteen years is the pace that does not work tonight."

        "Zira nods."

        "Selene's hand opens on the desk. Zira's hand takes it. Aeron's hand finds Selene's other hand — the red-pencil hand, the command hand. He holds it the way he held her at the collarbone in s17 — with the pressure of a man who is not performing arrival."

        "Three people at the cipher desk. The cipher between them. The desk lamp at its lower setting."

        # ---------- [ THE INTIMATE BLOCK — PLAYER-AUTHORED ] ----------
        # [INTIMATE CONTENT HERE]
        # Slow variant. Zira sets the pace — she is the one Selene
        # asked to set it, and the asking is the scene's inversion.
        # Selene is not commanding. Selene is being paced by a woman
        # who builds clocks and knows what slow means. Aeron is
        # present in the register from s17 — the register of a man
        # who arrived as something other than a student. The cipher
        # alcove. The desk lamp at its lower setting. The cipher on
        # the desk catching the warm light. Zira's charcoal-stained
        # fingers on Selene's command hands. The pace is Zira's and
        # the pace is deliberate and the deliberation is the gift.
        # The wall map behind them with both their handwritings on it.
        # ---------- [ END INTIMATE BLOCK ] ----------

        jump a4_s20a_command_door_aftercare

        # ========== VARIANT C — SIT ==========

label a4_s20a_command_door_sit:

        a "I can't turn it off tonight."

        a "Just sit with me."

        "He says it at the desk. He says it in the register of a man who knows that the command architecture is the architecture he lives inside, and the architecture does not have an off switch, and the not-having-an-off-switch is not a failure. The not-having-an-off-switch is the truth of a man who has been commanded and who has been teaching himself to command and who needs the two women in the room to sit with him inside the architecture rather than asking him to leave it."

        "Selene nods."

        sel "Sitting is a room I have always been in."

        "She does not click the desk lamp to its lower setting. The lamp stays at working temperature. The working temperature is the right light for sitting — the light of a cipher alcove that is still a cipher alcove, where three people are not pretending the alcove is something else."

        "Zira nods."

        z "Sitting is enough."

        "Aeron sits on the floor."

        "He sits on the floor because there is one chair and the chair is Selene's and the desk edge is Zira's and the floor is the only surface left. He sits the way he sat on the floor of Noelle's workspace — the way a man sits among the work when the work is the thing he is inside of."

        "Zira sits on the floor beside him. She sits the way she sat on the workshop floor in s15 — with her back against the desk leg, her knees drawn up, her hands on her knees."

        "Selene looks at the two of them on the floor."

        "She does not sit on the floor."

        "She turns the desk chair toward them. She sits in the chair with her feet on the floor near Aeron's knee. She is above them. The above is not authority. The above is a woman who has been in the chair for nineteen years and the chair is where she sits, and she is going to sit in it near two people on the floor and the near is going to be enough."

        "Selene's hand comes off the desk. It finds Aeron's shoulder — not a grip, a rest. Her palm on the top of his shoulder the way she placed her palm on his sternum in s17."

        "Her other hand finds Zira's shoulder. The same rest. Two hands, two shoulders, from the chair."

        "Zira's hand comes up and covers Selene's hand on her shoulder. The cover is light — the jeweler's hold from s15, applied to a different woman's hand."

        "Aeron's hand covers Selene's other hand on his shoulder. The same hold."

        "Three people in the cipher alcove. One in the chair. Two on the floor. The cipher on the desk above them. The desk lamp at working temperature. The wall map behind them with both their handwritings on it."

        "Nobody speaks for a long time."

        # ---------- [ NO INTIMATE BLOCK IN THIS VARIANT ] ----------
        # Sit variant: the scene proceeds directly to aftercare with
        # the intimate block replaced by a non-erotic hold in the
        # cipher alcove. The desk lamp stays at working temperature.
        # The cipher is on the desk. The wall map is behind them.
        # Three people in the room — Selene in the chair, Aeron and
        # Zira on the floor. Selene's hands on their shoulders. Their
        # hands on her hands. The hold is the physical realization of
        # "delegate the question" in the register where the delegation
        # is not about command but about weight, and the weight is
        # lighter when three people are under it.
        # ---------- [ END NON-EROTIC HOLD ] ----------

        jump a4_s20a_command_door_aftercare

label a4_s20a_command_and_the_door_emp_below_threshold:

    # ========== BELOW THRESHOLD — TENDER NON-ESCALATION ==========

    "The cipher alcove holds the three sentences — Selene's naming, Zira's answer, Aeron's honest — and the three sentences are enough for the night."

    "Nobody moves toward the desk edge."

    "Instead, they settle. Selene picks up the red pencil. Zira turns back to the wall map. Aeron stays at the door end."

    "They work for another ten minutes."

    "The ten minutes are different from the first fifteen. The difference is: the room has been named. The room knows what it is now. The planning continues but the planning is happening inside a room that has acknowledged itself, and the acknowledgment changes the temperature of the work without changing the content."

    "Selene marks a timing adjustment on the operational document and her pencil pauses near the edge of the desk where Zira's charcoal marks begin on the wall map, and the pause is the pause of a woman whose red line is about to meet a charcoal line and the meeting is not about pencils."

    "Zira updates a relay confirmation on the wall map and her hand passes close to Selene's stack of operational documents, and neither of them adjusts the distance."

    "Aeron reads the wall map from across the room — Selene's red pencil and Zira's charcoal on the same surface, the same civilians, the same forty-eight hours — and the two handwritings are a sentence he is going to carry out of this room."

    athought "This is not how command is supposed to feel."

    "He does not say it aloud. He does not need to. The sentence is in the room."

    "At oh-two-hundred Selene sets the red pencil down. She straightens the operational documents into a single stack. Zira caps the charcoal stick and places it on the map ledge."

    "They stand in the cipher alcove in the desk lamp light."

    sel "This is not how command is supposed to feel."

    "She says it at the desk. She says it in the stripped register. She is not performing the observation. She is making it."

    z "Nothing about this is how anything is supposed to feel."

    "A beat."

    "Selene reaches for the cipher."

    "At the same moment, Zira reaches for the cipher."

    "Their hands meet on the brass."

    "Selene's fingers on the left side of the cylinder. Zira's fingers on the right. The cipher between them — the grounding object, the command weight, the brass that Selene has been carrying alone for nineteen years."

    "They both look at their hands on the cipher."

    "They both let go."

    "The cipher stays on the desk. Neither woman picks it up. The letting-go is the beat. The letting-go says: the weight is on the desk tonight and neither of us is going to carry it alone out of this room."

    "Aeron watches."

    athought "They reached for the same object at the same time. They reached for the cipher — Selene's cipher, the thing she holds when the architecture needs grounding — and they reached for it together and they both let go."

    athought "The letting-go is not surrender. The letting-go is the acknowledgment that the weight has a second hand available to it now, and the second hand is Zira's, and the cipher does not need to be carried out of the room tonight."

    "Selene looks at Aeron."

    "Aeron is quiet."

    "He has been quiet for the entire recognition. He has been the man in the room while two women who have been shaping him from different directions discovered that the shaping is the thing they share."

    "Selene picks up the operational documents. She does not pick up the cipher."

    sel "Leave the cipher on the desk tonight."

    a "All right."

    sel "We will pick it up together in the morning."

    "She does not say who 'we' is. The 'we' is in the room."

    z "Tomorrow night. Same time. I will bring the updated western relays."

    sel "Bring them here. Not to the war room. Here."

    z "Here."

    "Zira says it back. The echo is a confirmation — the same grammar as Lyra's 'three cups' in s14a."

    "Aeron says nothing. The cipher is on the desk. The two handwritings are on the wall map. The door is open. The three of them leave the cipher alcove at oh-two-hundred with the cipher on the desk and the weight on the desk and the desk in the room that all three of them are going to come back to."

    $ nudge_poly("selene_zira_cipher_shared", delta=1)

    jump a4_s20a_command_door_state_updates

    # ========== PHASE 5 — AFTERCARE ==========

label a4_s20a_command_door_aftercare:

    "Later."

    "The desk lamp is at its lower setting. The cipher is on the desk. The wall map is behind them with both handwritings on it — Selene's red pencil, Zira's charcoal. The operational documents are in a stack at the far edge of the desk."

    "The three of them are in the cipher alcove."

    "Selene is in the chair. She has not left the chair. Even now — even after — she is in the chair, because the chair is where Selene is, and the chair is the sentence she has been living inside for nineteen years, and the chair is not a cage tonight. The chair is a place."

    "Zira is on the floor beside the desk, her back against the wall, the position from the workshop. Her hands are in her lap. The charcoal is still on her fingertips."

    "Aeron is on the floor on the other side, his shoulder against the desk leg. His hands are on his knees."

    "Selene is above them. They are below her. The geometry is not hierarchy. The geometry is a woman in a chair and two people on her floor."

    "Nobody has spoken for a while."

    "Selene speaks first."

    "She speaks to Zira. Not to Aeron."

    sel "I delegate the question to both of you tonight."

    "She says it again. She said it before — in the moment before the consent gate, in the register of command-becoming-personal. She says it now in the register of after. The repetition is not a repetition. The first time was an offering. This time is a record."

    "Zira looks up at Selene from the floor."

    z "I did not expect that."

    sel "Neither did I. That is exactly why it needed to happen."

    "The exchange repeats. The same words, different register. The first time was the door opening. This time is the door being noted as open. Two women confirming that the thing that happened is a thing that happened."

    "A beat."

    z "You have been carrying the command weight alone for nineteen years."

    sel "Yes."

    z "You do not have to carry it alone tomorrow."

    sel "I am going to carry it alone tomorrow. That is what command is. What I do not have to carry alone is this."

    "She means the room. She means the three of them in the cipher alcove at — whatever hour this is now, the hour past the hour when the work stopped being work. She means the weight of what the man costs, carried by two women who have been shaping him from different directions."

    z "Then I will carry this."

    sel "Good."

    "A beat."

    "Selene's hand comes off the chair arm. She reaches down — not far, the chair is low and Zira is on the floor beside the desk — and she finds Zira's hand in Zira's lap. She takes it."

    "The grip is not the command grip. The grip is the grip of a woman who has been holding a brass cylinder for nineteen years and is now holding a charcoal-stained hand and the hand is warm and the hand is not brass and the not-brass is the point."

    zthought "She is holding my hand."

    zthought "Selene is holding my hand. The same hand that drew the relay routes on the wall map. The same hand that built the clock. The same hand that held Lyra's liturgical hand in the mapping station. Selene is holding my hand and the holding is not command. The holding is the holding of a woman who has been alone in the chair for too long."

    zthought "I am going to hold it back."

    "Zira's hand closes on Selene's."

    "Selene's other hand — the red-pencil hand — finds Aeron's shoulder. The same rest from the chair. Her palm on his shoulder."

    "Aeron does not reach up. He does not need to reach up. Selene's hand on his shoulder is the version of holding that the chair allows, and the chair is where she is, and the holding from the chair is enough."

    "The cipher is on the desk above all three of them."

    "The cipher catches the desk lamp at its lower setting. The brass glows."

    "Nobody picks it up."

    athought "The cipher is on the desk."

    athought "Selene's cipher. The grounding object. The command weight. It is on the desk and nobody is picking it up and nobody needs to pick it up because the grounding tonight is not brass. The grounding tonight is two hands — Zira's charcoal hand and Selene's command hand — and the grounding is enough."

    athought "I am on the floor of the cipher alcove with a woman who taught me to stay in the chair above me and a woman who built me a door on the floor beside me, and neither of them is asking me to choose, and neither of them is asking the other to leave, and the cipher is on the desk, and the cipher does not need to be carried tonight."

    "The scene holds on the three of them in the cipher alcove."

    "Selene in the chair. Zira on the floor. Aeron on the floor. The cipher on the desk. The wall map behind them."

    "Fade."

    $ nudge_poly("selene_zira_aeron_triad", delta=1)

    jump a4_s20a_command_door_state_updates


    # ========== STATE UPDATES (CONVERGENCE) ==========

label a4_s20a_command_door_state_updates:

    # stop ambient fadeout 3.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Selene", trust=1, attraction=1)
    $ rel_bump("Zira", trust=1, attraction=1)
    $ flag("selene_zira_poly_recognized", True)
    $ flag("command_and_the_door_scene_complete", True)
    $ flag("selene_delegated_question_personal", True)
    $ canon_set("selene_zira.working_rhythm", "command_strategy_plus_route_intelligence")
    $ canon_set("selene.delegation_register", "personal_not_doctrinal")
    $ npc_remember("Selene", "said_i_am_not_doing_this_as_commander_tonight", weight=3)
    $ npc_remember("Selene", "said_delegate_the_question_to_both_of_you", weight=3)
    $ npc_remember("Zira", "said_they_are_the_same_man", weight=3)
    $ npc_remember("Zira", "said_the_thing_they_share_is_the_weight", weight=3)
    $ npc_remember("Selene", "said_this_is_not_how_command_is_supposed_to_feel", weight=2)
    $ npc_remember("Zira", "said_nothing_about_this_is_how_anything_is_supposed_to_feel", weight=2)
    $ npc_remember("Selene", "cipher_left_on_desk_not_carried", weight=3)
    $ tp_seed("a4.selene_zira.command_and_the_door")
    $ tp_seed("a4.poly.weight_shared_not_desire")
    $ scene_mark(_current_scene_id, "exited")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s20a_command_and_the_door_emp
# cann.chapter: IV — Shared Authority
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - Oh-one-forty the night before the civilian network move.
#     Selene has been in the cipher alcove since twenty-three
#     hundred. Zira arrived at twenty-three thirty. Aeron
#     arrives at oh-one-forty after leaving the ops table.
# cann.what_happened:
#   - Selene and Zira have been working the civilian network
#     move in the cipher alcove — Selene on command structure,
#     Zira on route intelligence. Their handwritings are on the
#     same wall map (red pencil and charcoal). Aeron arrives
#     in the doorway. Two faces look up. The third two-look.
#   - Recognition beat: Selene names the shaping. "You have
#     been building him an exit plan. I have been teaching him
#     to stay. Those are not the same thing." Zira: "They are
#     not the same thing. But they are the same man." Selene
#     acknowledges she knew about the exit plan and did not
#     stop it because a teacher cannot build a door.
#   - Poly gate: if metric("poly_pressure") >= 3, Selene
#     initiates: "I am not doing this as a commander tonight."
#     Zira: "Then who are you doing it as." Selene: "A woman
#     who has nineteen years of this and is tired of carrying
#     it alone." Consent gate: three choices (full / slow / sit).
#     All three end with three people in the cipher alcove. Two
#     lead to [INTIMATE CONTENT HERE] blocks, one to a non-erotic
#     hold with Selene in the chair and the others on the floor.
#   - If poly_pressure below threshold: the room is named but
#     not escalated. Selene: "This is not how command is supposed
#     to feel." Zira: "Nothing about this is how anything is
#     supposed to feel." The cipher beat: both women reach for
#     the cipher at the same moment. Their hands meet on the
#     brass. They both let go. The letting-go is the below-
#     threshold version of shared weight.
#   - Aftercare (escalated variants): Selene repeats the
#     delegation line: "I delegate the question to both of you
#     tonight." The repetition is not doctrinal — it is personal.
#     Zira: "I did not expect that." Selene: "Neither did I.
#     That is exactly why it needed to happen." Selene holds
#     Zira's hand from the chair. The cipher stays on the desk.
#     Nobody picks it up.
# cann.aeron_state:
#   - Third time in Act IV walking into a room where two women
#     are already collaborating. Zira is the common variable in
#     all three rooms. He speaks least in this scene. His honest
#     sentence: "I have a room and I have a door and the room
#     and the door are both real."
#   - The floor of the cipher alcove is his position — below
#     Selene in the chair, beside Zira on the floor. The
#     geometry is not hierarchy. The geometry is a man being
#     held by two women from different altitudes.
# cann.selene_state:
#   - Post-s17. The letter has been turned face-down. The
#     teaching frame is retired. What remains is the stripped
#     register — the woman under the commander. Nineteen years
#     of carrying the command weight alone. Tonight the weight
#     has two other people near it.
#   - "I delegate the question to both of you tonight" is the
#     s10 thesis sentence ("delegate the question") in personal
#     register. The repetition in aftercare is the confirmation.
#     Do not give this phrasing to another scene in this register.
#   - The cipher left on the desk = the command weight set down.
#     Cross-reference with the cipher in s10, s12a, s17. The
#     cipher has been in Selene's hand in every prior scene.
#     Tonight it is on the desk and stays on the desk.
# cann.zira_state:
#   - Post-s15 and post-s14a and post-s16a. She is the common
#     variable in all three poly rooms. The Ashmarket precision
#     is aimed at Selene tonight. "They are not the same thing.
#     But they are the same man" is her Act 4 poly thesis for
#     this scene.
#   - "The time difference is the least interesting thing about
#     us" recurs from s14a — the sentence is hers and it is true
#     every time she says it. The repetition is the confirmation
#     that Zira's poly grammar is consistent across all three
#     rooms.
#   - She reads Selene's open door the way she reads relay
#     networks — by the grammar of the opening. Cross-reference
#     with Noelle's open door in s16a.
# cann.thematic_flags:
#   - Act 4 EMP arm: the third poly beat completes the trio.
#     s14a = Lyra+Zira+Aeron (care as parallel shapes).
#     s16a = Noelle+Zira+Aeron (intelligence as intimacy).
#     s20a = Selene+Zira+Aeron (command as shared weight).
#   - Zira as common variable: she is in all three poly rooms.
#     The three rooms are three different rooms and three rooms
#     that are the same room. The same room is: two women who
#     discover that what they share is not the man but the weight
#     of what the man costs.
#   - The cipher on the desk = the command weight set down. Two
#     women reaching for it at the same time and both letting go
#     = the below-threshold visual thesis. The cipher not being
#     picked up in the aftercare = the above-threshold version.
#   - "Delegate the question" in personal register inverts the
#     s10 doctrinal usage. The doctrine becomes the body. The
#     body becomes the doctrine. The inversion completes the
#     Act 4 EMP arc of command-as-intimacy.
