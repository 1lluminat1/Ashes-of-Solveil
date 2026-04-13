# =======================================================
# ACT 3 - Scene 24: Liora (Obedience Path)
# File: a3_s24_liora_ob.rpy
# Type: ACT 3 FINALE (OB)
# THIS IS THE MOST IMPORTANT SCENE IN OB ACT 3.
# THE MIRROR IS WORSE THAN DEATH.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s24_liora_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s24_liora_ob:


    # Codex — stage bumps for characters the player learns more about here.
    $ codex_reveal("liora_rylan", to_stage=2, source="a3_s24_liora_ob")
    $ show_timeline("DAY 42", "10:00", "Sector 5 — Outlander Safe House")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: This scene uses three visual grammars:
    #         (1) THE APPROACH: 50mm, locked. OB precision. Aeron walking toward the meeting.
    #             The camera is behind him. We see what he sees. The corridor. The door.
    #             The guards. The room beyond.
    #         (2) THE MIRROR: 85mm telephoto, handheld (subtle drift). The compression of distance.
    #             Liora's face: close. The depth of field is shallow. Only her face is sharp.
    #             Everything else -- the room, the guards, Aeron -- is soft. The world dissolves
    #             around the act of being seen.
    #             Then: reverse angle. 85mm on Aeron. Seen the way she sees him.
    #             The two-shot never appears. They are never in the same sharp focus.
    #             That's the grammar: two people who can't occupy the same clarity.
    #         (3) AFTERMATH: 40mm, handheld (3% drift). Each LI in their own frame.
    #             The camera visits. Doesn't stay. The brevity is the respect.
    #             Aeron alone: 50mm returns. Locked. The mask. The thought beneath.
    #         CRITICAL: The slap (if it happens) is a single frame wider -- 35mm. The physicality
    #         needs the wider frame. Then back to 85mm. The telephoto returns. The distance returns.
    # LIGHTING: The meeting room: neutral ground. An Outlander safe house.
    #           Overhead strip -- functional, cold. The light is fair. Equally unflattering.
    #           No shadows for either of them to hide in.
    #           Aftermath: base interior. The war room. Overheads at full. Same as the bookend.
    # SFX: The approach: footsteps on concrete. Guards shifting. A door mechanism.
    #      The mirror: near-silence. Breathing. The room itself. No music.
    #      The slap: if it happens -- the sound is sharp. Not theatrical. Real.
    #      Her exit: footsteps. Receding. A door closing. Not slamming. Closing.
    #      Aftermath: base ambient. The silence of a room full of people not speaking.
    # FX/COMP: The safe house: Outlander territory. Neutral architecture. A room designed
    #          for meetings between people who don't trust each other.
    #          Table between them. Guards visible but distant. The geography of negotiation.
    #          Liora: older than the letter. The years visible. But the posture -- the refusal
    #          to be hurried, the pace, the uncorrected hair -- unchanged.
    # BLOCKING: Aeron enters. Liora is already there. Seated. Not standing for him.
    #           The table between them. Outlander guards at the walls.
    #           She doesn't rise. Doesn't reach. Looks.
    #           The conversation happens across the table. The distance is non-negotiable.
    #           After: he walks back to base. The team receives him. Each in their own space.
    # CANON: ACT 3 FINALE. The scene that mirrors (not matches) the EMP execution.
    #        EMP lost Liora to death. OB loses her to judgment.
    #        She looks at him and sees Marcus. She says it. He hears it.
    #        She doesn't die. She refuses to be his absolution. She walks away.
    #        The mirror is worse than any execution.
    # FACE: Liora -- the face of a woman watching her son become the thing she ran from.
    #        Not rage. Not grief. Recognition. The devastation of seeing what you always feared.
    #        Aeron -- the mask. Breaking. For the first time since Selene's funeral, breaking.
    #        The mask doesn't shatter. It cracks. And she can see through the cracks.

    # ========= VOICE BASELINE =========
    # Liora: Calm. Not cold -- calm. The calm of someone who has spent nineteen years
    # making peace with what she left and what she couldn't change.
    # Her words are precise. She doesn't waste them. She doesn't perform grief.
    # Aeron: OB cadence fractures. Short sentences become fragments. The clinical voice
    # can't hold. For the first time in the OB path, the internal monologue bleeds.
    # The spoken dialogue is sparse. Most of this scene lives in silences and looks.

    # --- VISUAL SETUP ---
    # [INT. OUTLANDER SAFE HOUSE - MEETING ROOM - DAY]

    #scene bg_outlander_safe_house with dissolve
    #play ambient "sfx/ambient/safe_house_neutral.ogg" fadein 2.0

    # ========== PHASE 1 -- THE APPROACH ==========

    "The Outlander safe house sits in the contested strip between Sector 5 and the outer ring. Neutral territory. The architecture is deliberate -- no faction markers, no territorial signals. A room designed for people who need to talk and can't afford to trust."

    "Zira arranged it through three intermediary contacts. The Outlander channels move slowly. Aeron waited nine days."

    athought "Operations. Briefings. Patrol rotations. Normal. The machine ran."

    # Callback: a3_s19a_the_letter_ob — Aeron has been carrying the letter
    athought "The letter is still in my jacket. I have not re-read it since the drop box. I don't need to. The sentence in the middle has been playing in my skull for nine days."

    athought "And underneath the machine, the sentence I can't stop turning over."

    athought "'She kept the names of strangers. She didn't keep mine.'"

    "The corridor narrows. Two Outlander guards at the door. They don't salute. They don't challenge. They step aside."

    athought "She's in there."

    athought "My mother is in that room."

    athought "I don't know what I expect. Explanation. Maybe anger. Maybe even forgiveness, though I wouldn't--"

    athought "I wouldn't admit to wanting it."

    "He straightens his jacket. The letter is inside. Still there. Close to the chest."

    "He enters."

    # ========== PHASE 2 -- THE MIRROR ==========

    "She's already seated."

    "Not standing. Not at attention. Not performing. Seated at the far side of the table with her hands flat on the surface and her back straight and her hair uncorrected."

    "She's older than the letter. The years are in her face -- the lines, the weathering, the particular aging of someone who spent two decades in the Outlands. But the posture. The refusal to be rearranged by circumstance."

    "That hasn't changed."

    athought "I know her."

    athought "The same way I knew the handwriting. Not from memory. From the mirror."

    "She looks at him."

    "Not at his rank. Not at his uniform. Not at the tactical posture or the command bearing or the controlled expression."

    "At him."

    athought "She's looking at me the way--"

    athought "No."

    athought "She's looking at me the way she looked at him."

    "The recognition hits before the thought finishes forming. He's seen that look. Not directed at him -- directed at Marcus, in the fragments of memory that survived the Glass. The look of a woman watching a wound she can't stitch."

    "She doesn't stand. Doesn't reach for him. Doesn't speak."

    "The look is enough."

    "The look is everything."

    "He sits. The table between them. The distance non-negotiable."

    a "Liora."

    "Her name in his mouth. He hasn't said it in years. It feels like speaking a language he forgot he knew."

    "She doesn't correct him. Doesn't say 'mother.' Doesn't offer the word. He has to earn it or do without."

    "Silence. The safe house breathes around them. The guards at the walls. The light, fair and cold."

    "She speaks first."

    "Her voice is calm. Not cold. The voice of a woman who spent nineteen years making peace with what she couldn't change."

    li "You have his discipline."

    athought "His. Not 'your father's.' Not 'Marcus's.' His. As if there's only one man she could mean."

    a "I have what I needed to survive."

    li "Yes. He said that too."

    "The sentence lands without emphasis. A fact. An observation. The way Noelle delivers data."

    "Silence."

    li "I left so my hands wouldn't be covered in this."

    "She looks at his hands. On the table. Still. Controlled."

    li "You found a way to cover yours and call it duty."

    athought "Duty."

    athought "She's reading me. Nineteen years apart and she's reading me like a debrief."

    a "I did what was necessary--"

    li "So did your father. Word for word."

    "He stops. The sentence dies in his mouth."

    athought "Word for word."

    athought "She heard me say 'necessary' and she heard Marcus."

    athought "Zira said the same thing. In the corridor. 'That's what your father said. Word for word.'"

    athought "Everyone hears him when I speak."

    athought "Am I the only one who doesn't?"

    "Liora's hands haven't moved from the table. Flat. Open. Not reaching."

    li "The courier network tells me things. The Ghostline carries more than intelligence."

    li "I know about the operation. The seven phantom positions. The supply depot."

    li "I know about the civilians."

    athought "The civilians."

    athought "Five to eleven. The rounding error."

    li "Marcus used to call it 'operational efficiency.' He had charts. Projections. He could make any number of dead people look reasonable on a display."

    li "You learned that from him. Or you learned it from whoever taught you after I left."

    li "Either way, I can see his charts in the way you sit."

    "She stands."

    "The movement is slow. Not dramatic. The standing of a woman who has spent years moving through hostile territory at her own pace."

    "She walks around the table. Not toward him. Past him. To the side of the room where the light is even and the distance is her choice."

    "She looks at him."

    "Not the command mask. Not the OB posture. Through it."

    "She lifts her hand."

    "The slap is not theatrical. Not rage. Not violence."

    "It's a mother's hand on her son's face and the sound is sharp and real and it echoes in the safe house and the Outlander guards don't move because they've seen grief before."

    athought "She hit me."

    athought "My mother is standing in front of me and she hit me and I didn't move."

    athought "I didn't move because the Glass trained me not to flinch."

    athought "I didn't move because some part of me knew I deserved it."

    "Her hand drops to her side."

    li "Aeron Rylan."

    "His full name. Not 'Aeron.' Not 'son.' His full name, spoken the way a judge delivers a verdict. The way the record speaks."

    li "I left because I couldn't watch your father finish becoming the thing he was becoming."

    li "I can't watch you finish either."

    athought "She's leaving."

    athought "She's going to leave again."

    a "You left me with him."

    "The words escape the operational voice. Raw. The voice of a child, not a commander."

    a "You saw what he was. You wrote about it. You put it in a letter and you left. And you left me there."

    li "Yes."

    "One word. No defense. No justification."

    li "I left you with him because I believed you had something he didn't. The pause. The hesitation. The part of him that stopped before signing."

    li "I believed that part would survive."

    "She looks at him. Through him."

    li "Did it?"

    "He doesn't answer."

    "The silence is the answer."

    li "I kept six thousand names. Every person Echelon erased. Every family. Every child."

    li "I didn't keep yours because I thought you didn't need keeping."

    li "I was wrong about that too."

    "She turns away."

    "She walks toward the door. Her pace is her own. The same pace she walked to the dead drop. The same pace she walked through the Outlands for nineteen years. No one adjusts her rhythm."

    "She doesn't look back."

    "The door opens. The corridor beyond. The Outlander guards."

    "She walks through."

    "The door closes."

    athought "She left."

    athought "Again."

    athought "She looked at me and she saw him. She saw Marcus. She saw the charts and the projections and the civilians reduced to rounding errors and the discipline that I called survival."

    athought "She slapped me. Once. Not because she was angry."

    athought "Because she recognized me."

    athought "And recognition was worse."

    # ========== PHASE 3 -- THE AFTERMATH ==========

    #stop ambient fadeout 2.0
    #scene bg_war_room_ob with dissolve
    #play ambient "sfx/ambient/war_room_quiet.ogg" fadein 2.0

    "He returns to base. The war room. The team is waiting. They know where he went."

    "The room is quiet. The kind of quiet that happens when people don't know what to say and are afraid of what they'll say if they try."

    # --- NYRA ---

    ny "She chose weakness. She always did."

    "Nyra says it the way she says everything: with certainty. With the clean conviction of someone who has never been uncertain about anything in her life."

    ny "A woman who abandons her family to keep lists of the dead is a woman who chose sentiment over structure. That's weakness."

    ny "Her weakness is not our concern."

    athought "Weakness."

    athought "Nyra didn't hear what Liora said. She heard 'mother left' and she filed it under 'irrelevant.'"

    athought "That should comfort me."

    athought "It doesn't."

    # --- ZIRA ---

    "Zira says nothing."

    "She's at her station. Hands on the Ghostline terminal. Working. The same hands. The same station."

    "She doesn't look at Aeron."

    "She doesn't look at Aeron and that says everything."

    athought "Zira is quiet."

    athought "Zira who told me I was becoming hollow. Zira who said 'that's what your father said, word for word.' Zira who didn't slam the door."

    athought "She's not looking at me."

    athought "She's looking at the Ghostline and the Ghostline runs through the same courier infrastructure my mother built."

    athought "Zira knows whose roads she built on."

    athought "She can't look at me right now."

    # --- TESSA (conditional) ---

    if flag("tessa_stayed_s10"):

        "Tessa is by the board. Her board. The names. Living and dead."

        "She looks at Aeron. Direct. The look of a healer assessing damage she can see but can't treat."

        t "She's right, you know."

        "Three words. Four. Quiet. Not a challenge. Not confrontation."

        "A diagnosis."

        athought "Tessa said it out loud."

        athought "Nobody else will. Nyra dismissed it. Zira can't speak. Noelle is cataloging."

        athought "Tessa looked at me and said: she's right."

        athought "She's right."

    # --- NOELLE ---

    "Noelle sits at her terminal. Her stylus moves. It hasn't stopped."

    "She's logging the interaction. Recording the behavioral data. The meeting with the subject's biological mother. The emotional volatility indices."

    "Her stylus shakes."

    "Not the hand. The stylus. As if the instrument itself is refusing the data."

    athought "Noelle's stylus is shaking."

    athought "She's recording this and the stylus is shaking and she hasn't noticed because she notices everything except the things that aren't data."

    athought "This isn't data."

    athought "This is a woman who looked at her son and saw his father and walked away."

    athought "There's no metric for that."

    # --- LYRA ---

    "Lyra is in the corner. Her hands are folded. Her lips move."

    "She's praying."

    "The prayer is silent. But the shape of it -- the way her shoulders curve, the way her head bows -- the shape is different from her usual prayers."

    "This one sounds like grieving."

    athought "Lyra is praying."

    athought "Lyra is praying the way people pray when they've seen something they can't unsee."

    athought "She doesn't need to. She can see it in my face."

    athought "She's praying for my mother."

    athought "She's praying for me."

    athought "I need it more."

    # ========== PHASE 4 -- ALONE ==========

    "The room empties. One by one. Nyra to her soldiers. Zira to the Ghostline. Noelle to her data. Lyra to her prayers."

    if flag("tessa_stayed_s10"):
        "Tessa leaves last. She pauses at the door. Doesn't turn. Leaves."

    "Aeron is alone in the war room."

    "The tactical displays cycle. The lights are at full brightness. The maps show patrol routes and supply lines and casualty projections."

    "He reaches into his jacket. The letter. Still there. Still warm from his body heat."

    "He takes it out. Holds it."

    "The handwriting. The curling 'a.' The high 't.' His handwriting."

    athought "She looked at me the way she looked at him."

    athought "I am my father's son."

    athought "I don't know if that's the worst thing I've ever thought, or the most honest."

    "He puts the letter back. Inside the jacket. Close to the chest."

    "The oldest place to keep something that matters."

    "The same gesture. EMP or OB. The letter goes back in the same place."

    "The meaning is different."

    "He stands. The war room hums."

    athought "She refused."

    athought "She refused to forgive me. She refused to explain. She refused to stay."

    athought "She refused to be my absolution."

    athought "EMP Aeron lost his mother to Echelon's cruelty."

    athought "I lost mine to her judgment."

    athought "I don't know which is worse."

    athought "I know which one I deserve."

    "He turns off the tactical display. The room goes dim."

    "He stands in the dark."

    "The letter against his chest. The slap still warm on his face."

    "The door closes behind him."

    #stop ambient fadeout 4.0
    #scene black with fade

    # ========== ACT TRANSITION ==========

    pause 1.5

    centered "{size=+20}END OF ACT III{/size}"
    pause 1.0
    centered "{size=+10}The Iron Accord{/size}"
    pause 2.0
    scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("liora_rejected_aeron", True)
    $ flag("liora_confrontation_ob", True)
    $ npc_remember("Nyra", "dismissed_liora_as_weakness", tone="absolute_certainty")
    $ npc_remember("Zira", "silent_after_liora_confrontation", tone="devastated_recognition")
    $ npc_remember("Noelle", "logged_liora_interaction_stylus_shaking", tone="instrument_failing")
    $ npc_remember("Lyra", "prayed_grief_for_aeron_and_liora", tone="witnessing_damage")
    if flag("tessa_stayed_s10"):
        $ npc_remember("Tessa", "shes_right_you_know", tone="quiet_diagnosis")
    $ flag("act3_complete", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s24_liora_ob
# cann.chapter: Act III, Phase III -- Revelation & Cost (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - ACT 3 FINALE. After the bookend (s23). The mirror scene.
#   - Nine days after courier contact confirmed. Outlander safe house. Neutral ground.
# cann.what_happened:
#   - Phase 1: Aeron approaches the meeting. Nine days of waiting. The letter in his jacket.
#   - Phase 2 (THE MIRROR): Liora is seated. Doesn't stand for him. Doesn't reach.
#     She looks at him the way she looked at Marcus. The recognition hits.
#     "I left so my hands wouldn't be covered in this. You found a way to cover yours and call it duty."
#     "I did what was necessary--" "So did your father. Word for word."
#     She knows about the Hunt. The civilians. "I can see his charts in the way you sit."
#     The slap: one. Not rage. Recognition. The sound echoes.
#     "Aeron Rylan." Full name. Verdict.
#     "Did it [survive]?" He doesn't answer. The silence IS the answer.
#     "I didn't keep yours because I thought you didn't need keeping. I was wrong about that too."
#     She turns away. Walks out. Doesn't look back.
#   - Phase 3 (AFTERMATH): Each LI responds.
#     Nyra: "She chose weakness. She always did."
#     Zira: says nothing. Doesn't look at Aeron.
#     Tessa (if present): "She's right, you know."
#     Noelle: logs the interaction. Her stylus shakes.
#     Lyra: prays. The prayer sounds like grieving.
#   - Phase 4 (ALONE): The letter. The handwriting. "I am my father's son."
#     "I don't know if that's the worst thing I've ever thought, or the most honest."
#     She refused to be his absolution. EMP lost her to death. OB lost her to judgment.
#   - Act transition: END OF ACT III -- "The Iron Accord"
# cann.aeron_state:
#   - The OB mask cracks. For the first time since Selene's funeral.
#   - "You left me with him" -- the child's voice escaping the commander.
#   - "I am my father's son." The thesis of the OB path stated by its subject.
#   - She refused absolution. He knows he deserved the refusal.
# cann.path_tracking:
#   - canon_set("liora_rejected_aeron"). flag("liora_confrontation_ob").
#   - npc_remember for all LIs. flag("act3_complete").
#   - Conditional Tessa beat on flag("tessa_stayed_s10").
#   - No player choice. No branching. The mirror is the scene.
# cann.thematic_flags:
#   - THE MIRROR: She looks at him the way she looked at Marcus. The recognition.
#     EMP's execution is external loss. OB's rejection is internal recognition.
#     "The mirror is worse than any execution." -- design thesis.
#   - "Word for word": Liora hears Marcus in Aeron's mouth. Same phrase Zira used.
#     The parallel is now confirmed by the person who knew Marcus best.
#   - The slap: not rage. Not violence. A mother's hand on her son's face.
#     The sound is real. The Glass trained him not to flinch. Something in him knew he deserved it.
#   - "Aeron Rylan": full name as verdict. Not maternal. Legal. Final.
#   - The pause: "Did it survive?" He doesn't answer. The OB path's answer to
#     "I fell in love with the pause" is silence. The pause didn't survive.
#   - "I didn't keep yours because I thought you didn't need keeping." The cruelest kindness.
#   - Nyra's "weakness" vs Liora's "judgment": the two philosophies in direct opposition.
#   - Noelle's stylus shaking: the instrument failing. Data can't hold this.
#   - Lyra's prayer as grieving: faith responding to damage it can witness but not repair.
# cann.character_moments:
#   - Liora: Calm. Not cold. Precise. She doesn't perform. She diagnoses.
#     "I left so my hands wouldn't be covered in this." The thesis.
#     "So did your father. Word for word." The mirror.
#     "Did it survive?" The question with no answer.
#     Walks out. Doesn't look back. The exit is not dramatic. It's final.
#   - Nyra: "She chose weakness." Dismissal. Complete. The wrong reading.
#   - Zira: Silence. Can't look at him. Built on Liora's roads. Knows it.
#   - Tessa: "She's right, you know." The quiet diagnosis nobody else will say.
#   - Noelle: Stylus shaking. The instrument failing. Not-data.
#   - Lyra: Praying. Grief. She can see the damage without hearing the words.
# cann.callbacks:
#   - a3_s19a: The letter. "I fell in love with the pause." The pause is dead.
#   - a3_s20: Zira's confrontation. "That's what your father said, word for word." Liora says it too.
#   - a3_s22: The Hunt. "Five to eleven." Liora knows about the civilians.
#   - a3_s23: The bookend. "The base functions. That's not the same as living."
#     Liora is naming the same thing from the outside.
#   - a3_s02a: Noelle comparing Aeron to Marcus. The comparison confirmed by his mother.
#   - a3_s01: "I feel efficiency." The efficiency that Liora can see in how he sits.
#   - EMP s22: Liora's execution. The parallel finale. Death vs judgment.
#     EMP lost her to cruelty. OB lost her to recognition. Both are true.
# cann.block_status:
#   - ACT 3 FINALE. No branching. No choice. The mirror is the cost.
# cann.requires_followup:
#   - Act 4: Aeron after the mirror. Does recognition change anything?
#   - The letter: still in his jacket. Heavier now.
#   - Liora's archive: intelligence value. Does he weaponize her work?
#   - "I am my father's son": the sentence he'll carry into Act 4.
#   - Nyra's dismissal vs the LIs' responses: the schism deepens.
#   - Zira's silence: the loudest response. Where does she go from here?
#   - The pause: dead or dormant? Can it be recovered?
