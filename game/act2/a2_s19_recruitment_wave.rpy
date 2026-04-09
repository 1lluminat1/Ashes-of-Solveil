# =======================================================
# ACT 2 - Scene 19: Recruitment Wave
# File: a2_s19_recruitment_wave.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_s19_recruitment_wave"
$ scene_mark(_current_scene_id, "entered")

define daven = Character("Daven")
define elara = Character("Elara")
define senna = Character("Senna")
define maren = Character("Maren")

label a2_s19_recruitment_wave:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35mm, starts wide on ops room energy then tightens for interviews. Two-shot for Elara.
    #         Push-in on Aeron when he sees Maren. Hold on his face. Let the recognition land.
    # LIGHTING: Morning wash through base — practical overheads mixed with warm amber from the corridor.
    #           Interview space: single overhead, slightly clinical. Faces half-lit.
    # SFX: Loop — base hum (more people than before, background voices, movement, life).
    #       One-shots — chair scrape, table tap, door open/close between interviews.
    # BLOCKING/PROPS: Ops room busier than previous scenes. More bodies, more gear on racks.
    #                 Interview corner: table, two chairs, minimal. Professional but not cold.
    #                 Daven's detail: a bruised pear, carried in his coat pocket. From nowhere.
    # FACE: Selene satisfied but watchful. Aeron carrying weight from the base-building weeks.
    #        Recruits: nervous, hopeful, desperate in varying proportions.
    #        Maren: calm. Too calm. The calm of someone who rebuilt themselves from rubble.

    # ========== GROWTH — MORNING, OPS ROOM ==========

    "The ops room sounds different this morning."

    "Not louder — fuller. More voices layered into the ambient hum. More boots on metal. More breath in the air."

    athought "When did we get this many people?"

    # VISUAL: Selene at the command table. Map marked with new positions. She looks almost pleased.
    sel "Aeron. Good. We need to talk numbers."

    a "I can see numbers. When did the ops room get crowded?"

    sel "Word is spreading. Purge survivors, sector refugees, a few Echelon deserters. We're averaging five new arrivals per day."

    a "Five per day?"

    sel "Fifty-five total now. Up from twenty last week."

    # VISUAL: Noelle at her station, data crystal projecting growth curves.
    n "5.2 per day, to be precise. Retention rate after screening: 89%. Projected strength by end of week: 85. End of month: 140."

    z "(from the doorway) Feeding eighty-five people is a different problem than feeding twenty. Just so we're clear."

    sel "We're clear. That's why we're expanding. Secondary locations, decentralized structure. Harder to kill all at once."

    "Selene turns to Aeron."

    sel "But first — screening. Five arrived this morning. I need you and Lyra on interviews."

    l "What's the process?"

    sel "Triple verification. Noelle's algorithm cross-references Echelon databases — 87% accuracy. Zira's contacts verify stories on the ground. Tessa evaluates psychological conditioning patterns."

    t "(arriving with a tray of something warm) Echelon training leaves marks. Movement patterns, response times, eye behavior under stress. I can spot it."

    sel "Anyone who passes all three gets in. Anyone who fails any one gets watched or rejected."

    if empathy_band() == "obedience":
        athought "Triple verification. Redundant layers. Good operational security."
    elif empathy_band() == "empathy":
        athought "People coming to us because they have nowhere else to go. And we're screening them like suspects."
        athought "We have to. I know that. It still costs something."
    else:
        athought "Five per day. That's growth. That's also exposure."

    # ========== THE INTERVIEWS ==========

    # VISUAL: Interview corner. Simple. Table, two chairs. Aeron and Lyra across from an empty seat.
    "They set up in a corner of the ops room. Table. Two chairs. Room for honesty."

    # --- DAVEN (Purge survivor, medical connection) ---

    "First in: a young man, early twenties. Burns visible on his forearms — old but deep. Thermal scarring."

    "He sits down and puts something on the table between them."

    "A pear. Bruised, slightly soft, carried too long in a coat pocket."

    daven "Daven. Sector 9. Before the Purge."

    "He rolls up his sleeve without being asked. The skin is mottled, tight, wrong."

    daven "Thermal bloom from the orbital strike. Tessa treated me. That's how I heard about you."

    a "Skills?"

    daven "I was a market vendor. Sold fruit."

    "He glances at the pear."

    daven "That's from a stall three sectors over. Woman who runs it knew my mother. She gives me one every time I pass through. Habit, I think. From when I used to deliver."

    "He doesn't explain further. He doesn't need to. The stall is a ghost of the market that burned. The pear is proof that something survived."

    daven "Never held a weapon. But I can learn. I'm here because 100,000 people died and I'm still standing. That should mean something."

    a "We'll verify with Tessa. If it checks out, you're in."

    "He leaves. The pear stays on the table."

    # --- ELARA (Sweep victim's family — the emotional weight) ---

    "Second: a woman in her forties. Textile worker's hands — rough, capable, worn down to the patience underneath."

    elara "Elara. Forty-three. Textile factory, Sector 6, twenty years."

    "She pauses. Not for drama — for control."

    elara "I lost my husband and my daughter in the Sweep. Four years ago. Operation 391."

    "The number lands like a fist."

    elara "My husband was designation 247. My daughter was 248. They died in their apartment. Never knew why."

    "She's looking at Aeron. Directly. Unblinking."

    elara "I know who you are. Everyone knows."

    athought "247. 248."

    elara "You killed 390 people that night. Maybe you killed my family. Maybe you didn't."

    "A breath."

    elara "But you stopped. You gave mercy. You chose different."
    elara "That's more than Marcus ever did."

    if empathy_band() == "obedience":
        athought "She's here despite what I was. Pragmatism over grief. Useful quality."
        athought "The number still sits in my chest."
    elif empathy_band() == "empathy":
        athought "247. 248. I don't remember their faces. Too many. Too fast."
        athought "She remembers. She carries them. And she's here anyway."
    else:
        athought "I can't give her what she lost. I can give her what she's asking for."

    a "I'm sorry. For your loss. For my part in it."

    elara "Words are cheap. Action matters."
    elara "Help me make Echelon pay. That's the only redemption worth anything."

    a "...Welcome to the resistance."

    "She stands. Reaches across the table."

    "Not a handshake. Her hand just — open. Waiting."

    "Aeron takes it."

    elara "My daughter's name was Naia."

    "She holds his hand for exactly one second. Then lets go."

    elara "Don't forget it."

    "She's gone before he can answer."

    athought "Naia."
    athought "I won't."

    $ npc_remember("Aeron", "elara_confrontation", tone="heavy")
    $ npc_remember("Aeron", "liora_name", tone="burden")
    $ scene_mark(_current_scene_id, "elara_accepted")

    # --- SENNA (rage, flagged unstable) ---

    "Third: a girl. Eighteen, maybe. Eyes that haven't stopped burning since they started."

    senna "Senna. Eighteen. Echelon killed my parents. Then my brother. Then my uncle. I'm the last one."

    senna "I want to fight. I want to hurt them. I want them to know what it costs."

    # VISUAL: Lyra leaning forward. She sees something in this girl. Recognition. Concern.
    l "Revenge burns you out. Leaves nothing."

    senna "Then I'll be ash. But I'll be ash that burned Echelon on the way down."

    athought "She reminds me of—"

    "Lyra glances at Aeron. She's thinking the same thing."

    menu:
        athought "She's a weapon looking for a target. That's useful. That's also dangerous."

        "Let her train while Tessa evaluates.":
            $ choice_and_dev(
                _current_scene_id, "_senna_train_during", "EMP", factor=1,
                note="Trust during observation. Lets Senna train while being evaluated — belief that purpose shapes rage."
            )
            $ scene_mark(_current_scene_id, "senna_trust_during")

            a "You start training tomorrow. But you also work with Tessa. Evaluation runs parallel."

            senna "Parallel? Meaning I train AND talk?"

            a "Meaning we trust you enough to put a weapon in your hands while we figure out if you're ready to use it."

            l "(quiet, to Aeron) That's a risk."

            a "(quiet, back) She's burning either way. At least here we can see the fire."

        "Evaluation first. Then training.":
            $ choice_and_dev(
                _current_scene_id, "_senna_eval_first", "OB", factor=1,
                note="Observation before trust. Tessa clears her before field access — structure prevents collapse."
            )
            $ scene_mark(_current_scene_id, "senna_eval_first")

            a "You talk to Tessa first. She clears you, then you train."

            senna "(frustrated) How long?"

            a "As long as it takes to know the difference between fighting and burning."

            senna "I know the difference."

            a "Tessa will confirm that. Not you."

            "She leaves. The anger trailing behind her like heat off asphalt."

    # --- MAREN (the one Aeron recognizes) ---

    "Fourth."

    "Aeron looks up from the table."

    "And stops."

    # VISUAL: PUSH-IN on Aeron's face. Something shifts. Not shock — recognition. The slow, sick kind.
    # CAMERA: Hold. Let the silence fill the frame.

    "A woman, mid-thirties. Dark hair pulled back. Scar along her left jawline — surgical, not combat. She sits down with the careful posture of someone who's had to relearn how to hold herself upright."

    athought "I know her."

    "She doesn't recognize him. Why would she? He was wearing a visor. She was designation 312."

    athought "Sector 7. Op 390. The apartment complex on Viaduct Row."
    athought "She was flagged as a Ghostline affiliate. We breached at 04:00."
    athought "She was holding a child."

    maren "My name is Maren. I'm from Sector 7. I heard you're building something worth fighting for."

    athought "The child wasn't hers. Neighbor's kid. She was watching him overnight. Wrong place, wrong night."

    athought "I cleared the apartment. Filed the report. Designation 312: detained, processed, released after 72 hours."

    athought "Released. Like that word covers what happens in seventy-two hours of Echelon processing."

    maren "I have organizational experience. Community coordination. I ran a mutual aid network in Sector 7 before Echelon dismantled it."

    "She speaks evenly. No tremor. No rage. The scar on her jaw catches the overhead light."

    athought "I did that. Not the scar — the processing that led to it. The breach that put her in the system. The system that left marks."

    maren "I'm not a fighter. But I can organize. Schedule. Coordinate supply distribution. Keep people fed and accounted for. That's what I'm good at."

    "Lyra is watching Aeron. She can tell something's wrong."

    l "(low) You okay?"

    menu:
        athought "She's sitting three feet away from the man who put her in the system. And she doesn't know."

        "Tell her.":
            $ choice_and_dev(
                _current_scene_id, "_told_maren", "EMP", factor=2,
                note="Aeron tells Maren he was the one who breached her apartment. Radical honesty. Risk of losing her."
            )
            $ scene_mark(_current_scene_id, "told_maren")
            $ npc_remember("Aeron", "told_maren_truth", tone="exposed")

            a "Before we continue — I need to tell you something."

            "Maren looks at him. Patient. Waiting."

            a "Sector 7. Viaduct Row. Op 390. The apartment complex."

            "The patience drains from her face. Not all at once — in stages, like water finding cracks."

            a "I was the team lead. I breached your apartment at 04:00. You were holding a child."

            "Silence."

            maren "...The boy. Tomas. He was my neighbor's son."

            a "I know."

            maren "You filed me as a Ghostline affiliate. I wasn't."

            a "I know that too. Now."

            "She stares at him. The scar on her jaw seems louder in the silence."

            maren "Seventy-two hours. They processed me for seventy-two hours."

            a "I'm sorry. It's not enough. But it's true."

            "A long moment. Lyra's hand is near her sidearm — not reaching, just ready. Habit."

            maren "(quietly) You could have said nothing."

            a "I could have."

            maren "Why didn't you?"

            if empathy_band() == "obedience":
                a "Because if you find out later — and you would — you'd have reason to doubt everything we built. Better now than after you're inside."
            elif empathy_band() == "empathy":
                a "Because you deserved to know who was sitting across from you. Before you chose."
            else:
                a "Because carrying it silently felt worse than whatever happens next."

            "Maren looks at her hands. Then at him. Then at the door."

            "She doesn't leave."

            maren "The boy was fine. Scared, but fine. His mother got him back."
            maren "I wasn't fine. But I rebuilt."

            "She touches the scar. Brief. Automatic."

            maren "You're telling me because you think it matters. That means it matters to you."
            maren "I'll work with you. Not because I forgive you. Because you told me when you didn't have to."

            athought "Not forgiveness. Something harder to name."

        "Say nothing. Carry it.":
            $ choice_and_dev(
                _current_scene_id, "_silent_about_maren", "OB", factor=2,
                note="Aeron recognizes Maren but says nothing. Operational pragmatism — or cowardice. The weight stays."
            )
            $ scene_mark(_current_scene_id, "silent_about_maren")
            $ npc_remember("Aeron", "recognized_maren_silent", tone="guilt_carried")

            athought "She doesn't need to know. It doesn't help her. It doesn't help the resistance."
            athought "It would only help me. And I don't deserve that relief."

            a "Organizational skills are exactly what we need. You're in."

            maren "Thank you. I'll make myself useful."

            "She stands. Extends her hand. Professional. Clean."

            "Aeron shakes it."

            athought "Designation 312. Maren. She shook the hand that signed her intake form."
            athought "She doesn't know. She might never know."
            athought "And I'll carry that every time I see her face in the ops room."

            "Lyra waits until Maren is gone."

            l "(quiet) What was that?"

            a "Nothing."

            l "That wasn't nothing."

            a "It was nothing she needs to know."

            "Lyra doesn't push. But she files it. She always files it."

    # ========== AFTERMATH — OPS ROOM ==========

    # VISUAL: Back at the command table. Interviews done. Selene waiting for assessment.
    sel "Assessment?"

    a "Daven's clean — Tessa connection, verifiable burns. Trainable."

    if scene_has(_current_scene_id, "told_maren"):
        a "Maren — organizational coordinator. I told her about my involvement in her processing. She stayed."
        sel "(pause) You told a recruit you were responsible for her detention?"
        a "She deserved to know."
        sel "...That's either the most honest or most reckless thing you've done since you got here."
    else:
        a "Maren — organizational coordinator from Sector 7. Clean background. Useful skill set."

    a "Elara is... complicated. Sweep victim's family. She knows who I am. She's here anyway."

    sel "And the young one?"

    if scene_has(_current_scene_id, "senna_trust_during"):
        a "Senna trains while Tessa evaluates. Parallel track. She's burning — better to channel it than bottle it."
    else:
        a "Senna goes through Tessa first. She's motivated but she's burning, not fighting."

    sel "Fair calls. Thirty more waiting, by the way."

    a "Thirty?"

    sel "Word's spreading faster than we can process."

    n "At current intake velocity, we'll exceed base capacity within nine days."

    z "And Echelon will notice the population shift within fourteen. Bodies move. Supply chains change. They'll see it."

    sel "Which is why we're decentralizing. Four secondary locations. Distributed command. If they hit one, the others survive."
    sel "Aeron — you're taking point on the screening process going forward. Your instincts are good. Lyra assists."

    if empathy_band() == "obedience":
        athought "Recruiter. Screener. That's a command function."
        athought "Maren's face. I'll see it in the ops room every morning."
    elif empathy_band() == "empathy":
        athought "Elara gave me her daughter's name. Naia."
        athought "Maren shook my hand."
        athought "The weight of what I did becoming the foundation of what we're building."
    else:
        athought "Twenty became fifty-five. By month's end, 140."
        athought "Every one of them carrying a story that connects back to something Echelon broke."

    "The ops room hums around them. More voices than last week. More purpose."

    "Daven's pear is still on the table. Nobody moved it."

    "It sounds like growing."

    # ========== STATE UPDATES ==========

    $ stat_inc("resistance_strength", 35)
    $ canon_set("recruitment_working", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a2_s19_recruitment_wave
# cann.chapter: Act II, Chapter III — Proving Ground
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Approximately Day 15-16. Two weeks after base selection. Growth milestone.
# cann.what_happened:
#   - Resistance has grown from 20 to 55 fighters in one week. Rate: 5.2/day.
#   - Triple screening process established: Noelle's algorithm (87%), Zira's contacts, Tessa's evaluation.
#   - Four key recruits interviewed:
#       - Daven: Sector 9 Purge survivor, burns, market vendor. Carries a pear from a stall that survived.
#       - Elara: Sweep victim's family. Designation 247 and 248. Knows Aeron is Glass. Chooses to fight beside him.
#         Gives Aeron her daughter's name: Naia. "Don't forget it."
#       - Senna: 18, orphaned by Echelon, rage-driven. Player choice: train during evaluation or evaluate first.
#       - Maren: Sector 7, Op 390. Designation 312. Aeron RECOGNIZES her — he breached her apartment.
#         Player choice (factor=2): tell her the truth or carry it silently.
#   - Thirty more recruits waiting. Growth exceeding capacity.
#   - Selene assigns Aeron to lead screening. Command role evolution continues.
#   - Decentralization strategy: four secondary bases planned.
# cann.aeron_state:
#   - Role shifting from soldier to leader/recruiter/screener.
#   - Elara gives him a name to carry: Naia. His victims are becoming people retroactively.
#   - Maren is the transformation moment: the subject of his mission sitting across from him.
#     EMP tells her. OB carries it. Both cost something.
# cann.path_tracking:
#   - Two choice_and_dev decisions:
#       - Senna (factor=1): _senna_train_during (EMP) vs _senna_eval_first (OB)
#         Trust during observation vs observation before trust.
#       - Maren (factor=2): _told_maren (EMP) vs _silent_about_maren (OB)
#         Radical honesty vs operational pragmatism. The scene's major moral choice.
#   - stat_inc("resistance_strength", 35) — resistance grows to 55.
#   - canon_set("recruitment_working") for future gating.
# cann.thematic_flags:
#   - Elara: "My daughter's name was Naia." — giving him a name makes the numbers human. Retroactive personhood.
#   - Maren: The reversal — Aeron's subject becomes his recruit. He recognizes her; she doesn't recognize him.
#     Telling/not telling is about whether honesty serves the person or the self.
#   - Daven's pear: a piece of fruit from a market that burned. Proof that something survived.
#     "Nobody moved it." — small objects carrying enormous weight.
#   - Senna as mirror for early Aeron: a weapon looking for a target, burning instead of fighting.
#   - "It sounds like growing." — closing line as thesis.
# cann.character_moments:
#   - Elara: The scene's emotional anchor. Confronts Aeron, chooses forward, gives him Naia's name.
#     Hand extended — not a handshake, just open. One second of contact. "Don't forget it."
#   - Maren: The scene's transformation. Calm, competent, rebuilt from rubble. The scar on her jaw.
#     If told: "You're telling me because you think it matters. That means it matters to you."
#     If silent: Lyra notices. "That wasn't nothing." She files it.
#   - Daven: The pear. A vendor who survived the Purge carrying fruit from a ghost market. Small, human, sticky.
#   - Senna: Lyra sees herself. "She reminds me of—" Mirror of rage that could be shaped or could destroy.
#   - Selene: Strategic mind. Decentralization, distributed command. Already planning for the hit.
#   - Noelle: 5.2/day, 89% retention. She'd give you the percentage.
#   - Zira: "Feeding eighty-five people is a different problem." Logistics of hope.
#   - Tessa: "Training leaves marks. I can see them."
# cann.block_status:
#   - ANCHOR (both paths). Growth milestone scene. Two significant choices (Senna factor=1, Maren factor=2).
# cann.requires_followup:
#   - Elara should appear again. Her presence = reminder of what Aeron did and what Naia's name means.
#   - Maren's arc diverges:
#       If told: she works alongside Aeron with full knowledge. Complex trust. Possible future ally/confidante.
#       If silent: Aeron sees her in the ops room daily. The weight compounds. Possible later revelation.
#   - Senna depends on player choice: if training, she appears in ops. If deferred, she returns after clearing Tessa.
#   - Daven should appear in the Echelon Raid Defense as a combatant (first real test).
#   - Daven's pear: can recur as a motif. "He still carries fruit" or "the pear rotted but he kept the stem."
#   - Noelle's growth projections become the basis for the discovery timeline in a2_s22.
