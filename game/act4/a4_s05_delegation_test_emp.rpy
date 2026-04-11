# =======================================================
# ACT 4 - Scene 05: Delegation (Empathy Path)
# File: a4_s05_delegation_test_emp.rpy
# Type: OPERATION SCENE — commanded NOT to lead
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s05_delegation_test_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s05_delegation_test_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Three distinct visual registers across the scene.
    #         (1) Briefing/assignment: 35mm, council framing, the war table between
    #             Aeron and Selene. Static. Eye-level. No angles — authority is being
    #             negotiated, not staged.
    #         (2) Operation (command center): locked mids on Aeron at the relay console.
    #             Noelle's crystal hazing the frame in blue-green. Selene in overwatch —
    #             background, out of focus, but present in every shot. The tactical
    #             overlay is visible over Aeron's shoulder. When calls come in from Lyra
    #             on-site, the camera does NOT cut to her — she exists only as voice.
    #         (3) Post-op: Aeron alone at the cipher table. Noelle's models as floating
    #             overlays around him. Two plans side-by-side: the one that was and the
    #             one that would have been. The delta in red. Selene's entrance is from
    #             the side; she does not sit down.
    # LIGHTING: War room tactical amber and green. Command center colder — Noelle's
    #           crystal light, the relay displays. The post-op cipher table is nearly
    #           dark; one work lamp and the projection.
    # SFX: Briefing — war room hum. Command center — active: relay chatter, tactical
    #      alerts, the particular heartbeat of an operation in progress. Post-op —
    #      silence. The hum of a room that has just finished doing something.
    # FX/COMP: Noelle's side-by-side projection at the close. Aeron's hypothetical
    #          operation in one color. Lyra's actual operation in another. The delta
    #          in red: two Phoenix KIA that would not have died under Aeron's plan,
    #          three Phoenix alive who would have died, one civilian extracted.
    # BLOCKING: Three locations. Briefing in the war room. Operation in the command
    #           center (Noelle at comms, Selene standing overwatch, Aeron at the relay
    #           console). Post-op in the cipher alcove — Aeron seated, Selene entering.
    # FACE: Aeron moves from tactical resistance to reluctant acceptance to operational
    #        discipline to grief. The grief arrives only at the cipher table and it does
    #        not leave for the rest of the scene.

    # ========= VOICE BASELINE =========
    # EMP cadence. Selene is the command voice in the briefing and again at the close.
    # Lyra is voice-only during the operation — comms-clean, tactical, the version of
    # her voice that does not belong to the quarters scene. Noelle speaks in data.
    # Aeron has fewer lines than he normally would. The scene is happening to him,
    # and the discipline of not intervening is the lesson.

    # scene bg_war_room_emp with dissolve
    # play ambient "sfx/ambient/war_room_planning.ogg" fadein 2.0

    # ========== PHASE 1 — THE ASSIGNMENT ==========

    "The war table. Morning briefing. The Sector 7 interdiction brief is pinned to the tactical display — an Echelon supply convoy running through a choke point Phoenix has been tracking for a week."

    "Noelle has the patterning. Selene has the authority. Aeron has the muscle memory of seventy-odd operations in his father's voice and the beginnings of operations in his own."

    "He is already reading the approach vectors when Selene speaks."

    sel "Lyra is leading on-site."

    "He looks up."

    a "Say that again."

    sel "Lyra. Leading on-site. You are coordinating from base command. Noelle is at comms. I am in overwatch."

    "He does not speak for two seconds. He also does not sit down."

    athought "The first thing I want to do is argue. The second thing I want to do is argue. The third thing I want to do is point at the Echelon patrol pattern Noelle pulled yesterday and explain exactly why the approach should be run the way I have been running approaches for five years."

    athought "All three of those impulses are the problem."

    a "Selene."

    sel "Don't."

    a "I know this corridor."

    sel "I know."

    a "I have run seven operations in Sector 7 since we moved to the secondary base. I know the patrol cycles, I know where the old freight relay cuts through the ravine, I know which of the Echelon junior officers is going to buckle first under pressure because I have seen him panic twice."

    sel "I know that too."

    a "Then why—"

    sel "Because you are not going to be the only person in this building anyone trusts to run a corridor."

    "The war room is quiet."

    sel "That is how command dies, Aeron. It dies when the people under it look up at one chair and wait for one face to make the one call. You and I agreed to share authority at the start of this chapter. Sharing authority is not saying 'we co-command' and then handing you the board every time the board is complicated."

    sel "You get to share by not running this one."

    "Noelle is at the far end of the table. Her hands are folded on the edge of her crystal. She has said nothing. She is watching Aeron the way she watches a variable she is waiting to see resolve."

    n "I modeled both versions."

    "Her voice is low. She does not interrupt Selene — she waits for the gap and steps into it clean."

    n "I modeled the operation with you leading on-site and the operation with Lyra leading on-site. The outcome distributions are different. Neither is strictly dominant. The variance is lower in your version. The variance is lower because your version is structured around a narrower tolerance for contingency. That is a precise way of saying: you are better at executing the plan you made. Lyra will make a different plan."

    a "Different how?"

    n "I do not predict other people's plans, Aeron. I predict outcomes across plan-spaces. Lyra's plan will be inside the plan-space. That is the only commitment I am willing to make."

    athought "She is being careful. Noelle is always careful. She is being more careful than usual because she knows this is a moment I could use her numbers to break."

    athought "I am not going to use her numbers to break."

    # ========== PHASE 2 — THE BRIEF ==========

    "Lyra is in the room by the time he makes the decision. She has been standing near the door. She does not speak until he turns toward her."

    a "Lyra."

    l "Commander."

    athought "She calls me Commander in operational contexts. She stopped calling me Aeron in the field eight weeks ago. It is not distance; it is discipline."

    athought "I appreciate the discipline right now in a way I would not have appreciated it six months ago."

    a "Brief yourself on the Sector 7 corridor. Noelle will give you the patrol analysis. I will give you — I will give you my tactical notes from the seven operations I ran through there. You do not have to use them."

    l "I will read them."

    a "I am not asking you to use them. I am asking you to read them."

    l "Yes."

    a "And then I am asking you to run your operation."

    "She nods. Once. Precise."

    l "Understood."

    "She leaves with the datapad. Noelle follows. Selene does not."

    sel "That was well done."

    a "That was the minimum."

    sel "The minimum is well done in Act IV. That is the whole difference."

    athought "I am going to let that sit without answering it."

    # ========== PHASE 3 — THE TACTICAL NOTES ==========

    "An hour in the briefing room with Lyra. The datapad between them. The Sector 7 map pulled up in half a dozen resolutions."

    "He walks her through the seven operations. Which cycles he used. Which cycles burned. Which junior officer panics. Which freight relay cuts through the ravine and which one looks like it cuts through the ravine and actually dead-ends into a drone blind."

    "Lyra listens the way she does everything — completely, without interrupting, her thumb resting in her lap instead of on the Band."

    athought "Eleven years of Academy listening is an unbeatable tool if you know how to use it. She is using it."

    "When he is done, she looks at the map for a long moment."

    l "I would take the slower approach route. The one you marked as sub-optimal."

    a "It costs twelve minutes."

    l "Yes."

    a "The twelve minutes put you inside the second patrol sweep."

    l "I know."

    a "Lyra—"

    l "I know, Aeron. I have read your notes. I have reviewed Noelle's patterning. I am choosing the slower route because the faster route requires four Phoenix fighters to be in three places in under a minute, and I am not confident in my ability to run that kind of compression with fighters who do not know my voice yet."

    "She looks up from the map."

    l "You could run it. I cannot. The correct plan for me is not the correct plan for you. I am not going to pretend it is."

    athought "That is the honest answer. And it is also the right answer for the person actually going into the corridor."

    athought "I am going to let her take the slow route."

    a "Run your plan."

    l "Thank you."

    a "You do not need to thank me for it."

    l "I know. I am thanking you anyway."

    # ========== PHASE 4 — THE OPERATION ==========

    # scene bg_command_center_emp with dissolve

    "The command center. Relay console. Noelle at comms. Selene standing at the back wall, arms crossed, not speaking. The tactical display shows the Sector 7 corridor in wire-frame overlay — Lyra's team of eight moving through it in real time."

    "The first call."

    l "Team One in position. Slow approach — matching the patrol gap. Fighter Three is flanking high on the ravine ridge."

    athought "She put a fighter on the ridge. I would not have done that. The ridge is a longer sightline than the corridor wants. It costs her a shooter from her assault pair."

    athought "She is covering a blind angle I would have left open. I left it open in four of the seven operations and it was never exploited. That is not the same as saying it was never exploitable."

    "He does not speak into the comms. Noelle is the comms voice from base. Aeron is the silent overhead."

    "The second call."

    l "Convoy in range. Fighter Three reports patrol movement on the northeast ridge. Secondary patrol — not on the original pattern. Three hostiles, light equipment, moving parallel to our approach."

    "Aeron's hand moves toward the relay before he stops it."

    athought "Hit the secondary patrol first. That is the call. Hit them before they see you, because if they see you, they will be on your extract route by the time you have the convoy."

    athought "That is the call I would have made at this point in the operation. I have made it four times. It worked every time."

    "Lyra's voice comes back."

    l "Holding on the secondary patrol. Fighter Three confirms they are not converging on us. We are engaging primary target first. Breaking in three, two—"

    "The assault starts."

    "The tactical display lights up."

    athought "She is holding."

    athought "She is holding on the secondary patrol."

    athought "I am sitting in this chair and my hands are on the relay console and if I move them three inches I can override her and tell the team to take the ridge patrol out first and—"

    athought "I am not going to move my hands."

    "He does not move his hands."

    "Thirty seconds of assault. The convoy disables. Two Echelon drivers down — non-lethal, per Phoenix protocol. Supplies secured."

    "The third call."

    l "Convoy secured. Fighter Six reports a civilian in the rear cargo compartment. Not manifested. Repeat — civilian, not on the manifest, non-combatant, unrestrained."

    "Silence on the command center floor for a full second."

    sel "Noelle."

    n "Running facial against the civilian database. — Confirmed: non-combatant. Sector 7 displaced. The civilian is a relocation case Echelon was moving without documentation. Extraction parameters permit."

    l "Extracting the civilian. We are taking three additional seconds at the convoy."

    athought "A civilian I would not have looked for."

    athought "I would have cleared the convoy. I would not have checked the rear compartment for an unmanifested passenger because there was no reason to check — Echelon does not transport civilians in interdiction-grade cargo. Except apparently tonight they were."

    athought "She knew to look. Or she is just thorough in a way I have not been."

    "The fourth call."

    "The secondary patrol appears on the tactical display. They have rounded the ridge. They are on the extract route. Not converging — parallel. But close."

    "Aeron's hand is already moving toward the relay."

    l "Engaging secondary patrol now. Fighter Three and Fighter Five — suppressive. Fighter Six — cover the civilian. Breaking."

    "The assault."

    "The tactical display lights up again."

    "Twenty seconds."

    "The display registers two Phoenix indicators dimming."

    "Two."

    "Aeron is out of his chair before he has decided to stand up."

    athought "Two down."

    athought "Two."

    "Noelle's voice is very level."

    n "Confirming casualties. Fighter Three and Fighter Five. Both non-responsive."

    "The tactical display finishes the resolution. The convoy is secured. The civilian is extracted. The secondary patrol is eliminated. The extract route is clear."

    "Six Phoenix on the extract route. Three alive who would not have been if the extract route had been hit by a patrol still on its feet. One civilian in the extract vehicle who would not have been extracted at all."

    "And two indicators, dimmed, where they used to be lit."

    sel "Get Lyra's team home."

    "Noelle moves to comms. Aeron sits back down because his legs are not quite doing what he wants them to do."

    # ========== PHASE 5 — THE NAMES ==========

    "The command center empties over the next forty minutes. The team comes home. Lyra comes in the door ahead of the wounded — one shoulder wound, one grazed thigh, three uninjured. She has the civilian under her left arm because the civilian is shaking and no one else is free to hold her."

    "Lyra hands the civilian off to medbay. She stands at the center of the command center and does not sit."

    l "Fighter Three — Kesa Marin. The woman who joined from the broadcast wave. She had a brother who watched Liora's execution. That is why she came in."

    l "Fighter Five — Joren Hale. He came in the week after. He said his grandmother used to say your mother's name the way people say a prayer. He was quiet about it. He told me once."

    "She is not crying. Her voice is the calm voice from the comms."

    l "I am going to the medbay to write the condolence notes to their families before I go anywhere else. I wanted you to have their names first."

    a "Lyra."

    l "I am not asking for a debrief."

    a "That is not—"

    l "I know. But I am not asking for a debrief right now. I am going to the medbay. I will come find you in the cipher alcove in an hour."

    "She leaves."

    athought "Kesa Marin. Joren Hale."

    athought "I did not know their names this morning. I knew their faces — Kesa was the one who asked for extra rations for a week because she was recovering from a field injury. Joren was the one who stood too close to the board the day after his first operation because the dead column was the only thing in the room not moving."

    athought "I knew their faces. I know their names now."

    athought "I have to know their names."

    # ========== PHASE 6 — THE CIPHER TABLE ==========

    # scene bg_cipher_alcove_emp with dissolve

    "The cipher alcove. One work lamp. Noelle has left her projection running — two versions of the operation, side-by-side, the delta in red."

    "Aeron is alone with it."

    "Plan A: his hypothetical. The faster route. The ridge patrol eliminated first. Extract clean, no civilian retrieval because the civilian is not checked for. Projected casualties: zero Phoenix. Projected extractions: none beyond the primary objective."

    "Plan B: what actually happened. The slower route. The ridge flank covered. The ridge patrol held on. The civilian extracted. The secondary patrol engaged after the primary objective. Actual casualties: two Phoenix KIA. Actual extractions: one civilian, three Phoenix fighters who would have died on the clean extract route in Plan A when the ridge patrol — which Plan A did not account for because Plan A ran too fast to see it — would have caught them from behind."

    "The delta, in red, on the projection:"

    "— 2 Phoenix dead who lived in Plan A."
    "— 3 Phoenix alive who died in Plan A."
    "— 1 civilian extracted who was never retrieved in Plan A."

    "Net: plus two lives."

    "Net: minus two names."

    athought "The math is not the question."

    athought "The math is plus two. I know the math is plus two. I can look at the projection and see the math and I can say the math out loud — plus two, plus two, plus two — and it does not make the names smaller."

    athought "Kesa Marin. Joren Hale."

    athought "I would not have called for the ridge flank. That is the whole thing. I would not have called for the ridge flank because in four out of seven operations the ridge was not a threat and my pattern recognition said the ridge was not a threat. Lyra called for the ridge flank because she did not have my pattern recognition. She had her own. She had the kind of pattern recognition that puts a fighter on a blind sightline because the sightline is blind."

    athought "She saved three. And the three are not abstract. The three are Joran Tev — the one who is going to recover from the shoulder wound tonight and be at breakfast in the morning — and Sana and Reis, who came in from the Southside wave, who I have been planning to promote to assault lead next month, both of whom I would have buried in Plan A."

    athought "The three have names too."

    athought "The three have names too and the three are alive and two have names and two are dead and the math is plus two and I cannot hold the math and the names in the same thought at the same time."

    athought "Selene said the counting is the lesson."

    athought "I am counting."

    # ========== PHASE 7 — SELENE ==========

    "Footsteps at the alcove entrance. He does not look up."

    "Selene stops at the edge of the projection. She does not sit down. She does not put a hand on his shoulder — Selene does not do that, ever, and it is one of the reasons her authority is what it is."

    sel "Kesa Marin."

    "She says the name flatly. The way Tessa says names when she is adding them to the board."

    sel "Joren Hale."

    a "Selene."

    sel "I am saying their names first because if I do not say them, the scene collapses into the math. And I know you know the math. Noelle walked me through the projection before I came in here."

    sel "I am not here to give you comfort. You know that."

    a "I know."

    sel "I am here because I have been on the other side of this once."

    "She is looking at the projection. Not at Aeron."

    sel "When I was twenty-four, Marcus made me watch one of his lieutenants run an operation I would have run differently. I had run a version of the operation the month before. The lieutenant lost three people. I would not have lost the three people. Marcus watched me sit at a console and count the three names and he did not say a word about it until the operation was over and we were alone."

    sel "And then he said: 'This is what command costs when you do not run it. Now you know what it costs. I could have given you the math. The math would not have taught you. Only the names teach you.'"

    sel "I hated him for a month. Then I understood him."

    sel "This is that scene. I am the Marcus in it tonight. I am aware of the irony."

    a "Selene—"

    sel "Let me finish."

    "She finally looks at him."

    sel "You will run operations again. You will run them better than I will. You will run them better than Lyra will. You are the best field commander in this building and we both know it and nothing I say tonight is going to pretend otherwise."

    sel "But you cannot be the only chair at the table. If you are the only chair, the table dies with you. And you are at an elevated probability of dying, Aeron. I am being clinical about it because I do not have another register available at this hour. You are the highest-priority target in the Echelon theater. You are also the commander the secondary base cannot function without. Those two facts are a time bomb. The way I defuse the bomb is by making sure Phoenix has a command culture that can survive you being removed from the board for any reason."

    sel "Tonight's two names are the cost of that defusing."

    sel "I am not going to tell you the cost was worth it. The cost does not work that way. I am going to tell you the cost was necessary."

    sel "There is a difference."

    "He does not answer for a long time."

    athought "Necessary is not worth it."

    athought "Necessary is the word for things you do because the alternative is worse and you are still going to have to live with both of them."

    athought "Kesa Marin. Joren Hale."

    athought "I have to say their names more than Selene did. I have to say them until the saying has somewhere to put them."

    athought "That is Tessa's rule, and I am borrowing it without telling her."

    a "Kesa Marin."

    a "Joren Hale."

    a "Kesa Marin."

    a "Joren Hale."

    a "Kesa Marin. Joren Hale."

    "Selene does not speak during it. She lets the names fall."

    sel "That is the lesson."

    sel "I will leave you with the projection. Lyra will be here in an hour. She is writing to the families first, the way she should be, and the way I would have asked her to if she had not already chosen it."

    sel "I am going back to the command center."

    "She pauses at the edge of the alcove."

    sel "For what it is worth — I would not have called the ridge flank either. Not with seven operations of precedent. Lyra called it because she has not run a Sector 7 operation before and her base model did not know to discount the ridge."

    sel "Ignorance caught a sightline experience would have missed."

    sel "I have been doing this for a long time, Aeron. That sentence is almost never true."

    sel "Tonight it was true. You have to carry both things. You were right about the ridge in seven operations. You were wrong about it tonight. Both are facts. Neither cancels the other."

    "She leaves."

    # ========== PHASE 8 — THE CLOSE ==========

    "The projection is still running. Two plans. The delta in red. The names are not on the projection — the projection does not know how to display names."

    "He pulls up the command directory. Finds their personnel files. Kesa Marin's intake interview. Joren Hale's intake interview."

    "He does not read them."

    "He just looks at the names on the screen next to the tactical delta and lets both be in the frame at the same time."

    athought "I am going to learn how to read a board that has the names on one side and the math on the other."

    athought "I do not know how to read it yet."

    athought "I am going to learn by morning. Tessa would say that. Tessa would say she always does."

    athought "I am going to borrow that too."

    "He stays at the cipher table with the projection and the directory open until Lyra comes in an hour later."

    "The scene ends before she does."

    # stop ambient fadeout 3.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("aeron_first_delegation", True)
    $ flag("sector_7_interdiction_complete", True)
    $ canon_set("phoenix_kia.kesa_marin", True)
    $ canon_set("phoenix_kia.joren_hale", True)
    $ canon_set("civilian_extracted.sector_7_unmanifested", True)
    $ npc_remember("Aeron", "first_delegation_cost", tone="grief")
    $ npc_remember("Aeron", "kesa_marin_name", tone="kept")
    $ npc_remember("Aeron", "joren_hale_name", tone="kept")
    $ npc_remember("Selene", "gave_necessary_not_worth_it", tone="inherited_marcus_lesson")
    $ rel_bump("Selene", trust=1)
    $ rel_bump("Lyra", trust=1)
    $ metric("aeron_delegation_cost", set_to=2)
    $ tp_seed("a4.shared_command_cost")
    $ nudge_poly("authority", "shared")
    $ scene_mark(_current_scene_id, "completed")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s05_delegation_test_emp
# cann.chapter: Act IV, Chapter I — Shared Authority
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Early Act IV. After the Lyra unbuckled scene (a4_s04). Sector 7 supply
#     interdiction. The first operation Aeron has not led since the Phoenix
#     rebellion was formalized.
# cann.what_happened:
#   - Briefing: Selene assigns Lyra to lead on-site. Aeron pushes back twice, is
#     refused twice, accepts. Selene delivers the thesis line: "If you lead every
#     operation, you become the only person anyone trusts. That is how command dies."
#   - Aeron briefs Lyra on seven prior Sector 7 operations. She listens completely,
#     then tells him she will take the slower route because the faster route
#     requires compression she cannot run with a team that does not know her voice.
#     He accepts her plan.
#   - Operation from the command center. Aeron is at the relay console but does
#     not transmit. Noelle runs comms. Selene stands overwatch. Lyra's calls:
#       (1) Slower approach route — costs 12 minutes.
#       (2) Fighter Three to the ridge flank — covers a blind sightline Aeron
#           would have left uncovered (and did leave uncovered in 4 of 7 prior ops).
#       (3) Holds on the secondary patrol — engages convoy first instead of
#           eliminating the patrol pre-emptively as Aeron would have.
#       (4) Extracts an unmanifested civilian from the rear cargo compartment.
#           Aeron would not have checked for the civilian.
#       (5) Engages secondary patrol post-objective. Loses two Phoenix fighters.
#   - Aeron does not touch the relay. The discipline of not intervening is the
#     entire tactical beat. His hand moves; he stops it.
#   - Casualty report: two Phoenix KIA (Kesa Marin, Joren Hale). Three Phoenix
#     alive on the extract route who would have died under Plan A when an
#     unmodeled patrol caught them from behind. One civilian extracted.
#   - Lyra delivers the names herself — she comes into the command center with
#     the civilian under her arm and states the names before going to write
#     condolence letters. She explicitly does not ask for a debrief.
#   - Post-op cipher alcove: Aeron alone with Noelle's side-by-side projection.
#     Plan A (his hypothetical) vs Plan B (what happened). The delta in red.
#     The math is plus two lives. The names are not on the projection.
#   - Selene enters. She says the two names flatly first. Then she tells the
#     story of her own version of this scene under Marcus at twenty-four. She
#     names the irony of being the Marcus in this scene tonight. She gives the
#     lesson in two forms: "Necessary is not worth it" and "You were right about
#     the ridge in seven operations. You were wrong about it tonight. Both are
#     facts. Neither cancels the other."
#   - Aeron repeats the two names out loud three times — Tessa's rule, borrowed
#     silently. Scene closes with Aeron at the cipher table waiting for Lyra.
# cann.aeron_state:
#   - Tactical resistance in briefing. Reluctant acceptance. Operational discipline
#     during the op — the hand that does not touch the relay is the scene's core
#     physical beat. Grief at the cipher table. The grief stays.
#   - He begins to integrate a command vocabulary that is not singular. He does
#     not accept the math as sufficient. He keeps the names. Both.
# cann.lyra_state:
#   - Voice-only during the operation by design. She exists to Aeron in this scene
#     primarily as a set of calls he is not making. When she enters the command
#     center physically, it is to deliver the names, not the after-action. Her
#     discipline is load-bearing: she went to the families first.
#   - The ridge flank call is the scene's tactical pivot. It is explicitly framed
#     as a call ignorance made that experience would have missed. This is the
#     first operational beat where Lyra's not-Aeron-ness is the advantage.
# cann.selene_state:
#   - Selene is the Marcus of the scene and she knows it. She explicitly names the
#     irony. Her Marcus reference establishes her own relationship to delegation
#     as inherited pain, not imposed ideology. She refuses comfort and offers
#     "necessary is not worth it" as the precise register.
# cann.path_tracking:
#   - EMP path. Linear. No branching choice — the scene is a consequence scene.
#   - canon_set phoenix_kia.kesa_marin and phoenix_kia.joren_hale — both names are
#     now permanent board entries. canon_set civilian_extracted.sector_7_unmanifested.
#   - metric aeron_delegation_cost set to 2 (the KIA count under shared command).
#   - tp_seed a4.shared_command_cost. nudge_poly authority toward shared.
#   - rel_bump Selene +1 trust (she held the line and he let her). rel_bump Lyra
#     +1 trust (she ran an operation he could not run and delivered the names).
# cann.thematic_flags:
#   - Shared authority is harder, not easier — the Act IV lie laid bare.
#   - "The counting is the lesson" — Selene's line, Marcus's inheritance, the
#     grief discipline of leadership that shares.
#   - Plan A vs Plan B as a projection the math cannot name — the names are the
#     untranslatable part.
#   - The hand that does not touch the relay: discipline as the physical form of
#     delegation. The scene's one camera-holdable gesture.
#   - Borrowing Tessa's rule of three — Aeron does it silently, alone. This is the
#     first time an LI's grief practice has been adopted by Aeron in Act IV.
# cann.character_moments:
#   - Aeron: moves his hand toward the relay and stops it. Says the two names
#     three times. Pulls up the intake interviews but does not read them. These
#     three specific physical and textual gestures are the character moment
#     trifecta.
#   - Lyra: delivers the names carrying the civilian under her arm. Goes to
#     write the family letters before the after-action. Operational composure
#     with grief underneath.
#   - Selene: the Marcus confession. The explicit naming of the irony. "I hated
#     him for a month. Then I understood him." Her self-awareness is load-bearing
#     for the Act IV arc of distributed authority.
#   - Noelle: minimal dialogue, maximum presence. She models both plans and
#     refuses to call either one strictly dominant. Her projection is the scene's
#     continuous visual object. Her restraint is the character note.
# cann.callbacks:
#   - a3_s07_echelon_strikes_back_emp: "I know this handwriting." Aeron's
#     tactical precision — the thing that is being asked to sit still tonight.
#   - a3_s04a_the_silence_emp: the refusal of borrowed voices. Here, Aeron is
#     refusing his own voice. Inverse register.
#   - a2_int_tessa_torins_name: the rule of three. Aeron borrows it silently.
#   - a3_int_tessa_the_board_emp: the board that holds names. Aeron is
#     pre-echoing the board from the cipher table.
#   - Marcus as Selene's teacher: backfills Selene's own leadership inheritance.
#     Establishes that Selene learned delegation through grief the same way.
# cann.block_status:
#   - MAJOR SCENE. Linear. EMP path only. Consequence scene, no branching.
# cann.requires_followup:
#   - Kesa Marin and Joren Hale are now permanent canonical Phoenix KIA. They
#     appear on Tessa's board in a4_s06 (the silent addition scene).
#   - Lyra's condolence letters are a potential hook scene — not written here.
#   - The three Phoenix saved (Joran Tev, Sana, Reis) are referenced in Aeron's
#     internal monologue. They are not canon_set here — they are load-bearing
#     names Aeron is carrying, not official scene entries. Future scenes may
#     promote them to canon or leave them as Aeron's private ledger.
#   - Selene's Marcus anecdote is now part of her backstory canon. Any later
#     Selene scene that touches her twenty-fourth year must be consistent with
#     the version given here.
#   - The "hand that did not touch the relay" is a body-memory motif for Aeron
#     delegating. Future delegation scenes should reference or evolve it.
