# =======================================================
# ACT 3 - Scene 10: Tessa Friction (Obedience Path)
# File: a3_s10_tessa_friction_ob.rpy
# Path: OB
# Type: TESSA VS DOCTRINE
# Character Focus: Tessa, Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s10_tessa_friction_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s10_tessa_friction_ob:

    $ show_timeline("DAY 28", "09:00", "Phoenix Base — Medbay")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, handheld with subtle drift. Two-shot throughout -- Tessa and Aeron
    #         across the medbay table. Close-ups alternate. Her face open, his guarded.
    #         When she says "discipline isn't healing" -- hold on Aeron's hands. The tremor.
    #         The choice moment: camera at his eye level. She is below frame. He looks down.
    # LIGHTING: Medbay warm lighting -- the only warm space on the OB path.
    #           Tessa's domain. Practicals: desk lamp, instrument lights, the amber glow
    #           of sterilization units. The warmth makes the conversation harder.
    # SFX: Loop -- medbay hum, sterilization unit cycle, distant base activity.
    #      One-shots -- chair creak, medical instruments clinking, Tessa setting down a cup.
    # FX/COMP: Medical supplies organized on shelves. Tessa's handwritten patient notes
    #          visible on the desk. A half-eaten protein bar beside her coffee.
    # BLOCKING: Aeron enters the medbay. Tessa at her desk, finishing notes. She expected him.
    #           They talk across the desk -- the professional distance is deliberate.
    #           She doesn't stand. He doesn't sit. The geometry says everything.
    # CANON: After the Sector 4 operation. Tessa has completed her morale assessments.
    #        She uses the findings as the door, but the real conversation is about Aeron.
    # FACE: Tessa: open, direct, compassionate but unflinching. Aeron: mask cracking.

    # ========= VOICE BASELINE =========
    # Tessa: Direct. No softening. She is the one person who will not pretend.
    #        Compassion as confrontation. She cares too much to be polite about it.
    # OB Aeron: Controlled, but Tessa gets under the armor. The cracks show in
    #           shorter sentences, longer pauses, the tremor in his hand.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - MEDBAY - EVENING]
    # Tessa's domain. The warmest room in the base. Amber light.
    # Medical supplies in careful order. Patient charts on the desk.
    # Two days after the Sector 4 strike.

    #scene bg_medbay_ob with dissolve
    #play ambient "sfx/ambient/medbay_hum.ogg" fadein 2.0

    # --- OPENING ---

    "The medbay smells like antiseptic and coffee. Tessa's two constants."

    "She sits at her desk, a patient chart open beneath her pen. She doesn't look up when the door hisses."

    #show tessa medbay_desk with dissolve

    t "Your morale assessment results are in."

    athought "That is not a greeting. She is already in it."

    a "And?"

    t "Sit down."

    a "I'm fine standing."

    t "That wasn't a suggestion."

    "A beat. He sits."

    athought "She is the only person in this base who can do that."

    athought "Make me sit with two words."

    # --- THE FINDINGS ---

    "She slides a chart across the desk. Handwritten. Tessa doesn't trust digital records for this kind of thing."

    t "Thirty-one fighters assessed. Nineteen show elevated stress markers. Seven report sleep disruption. Four have stopped eating regular meals."

    a "We are in a war. Stress is expected."

    t "Stress is expected. What isn't expected is eleven fighters reporting that they're afraid of the morning drill rotations."

    "She lets that settle."

    t "Not afraid of Echelon. Not afraid of the next operation. Afraid of the drills. Of being seen making a mistake in front of Nyra's soldiers."

    athought "Afraid of the drills."

    athought "Not the enemy. The training."

    t "Three fighters asked to be reassigned to supply runs rather than continue integrated patrols. Two of them are veterans. They've been with Phoenix since before Selene."

    t "They didn't leave when Selene died. They're asking to leave because the rebellion doesn't feel like the rebellion anymore."

    a "Feelings do not determine operational effectiveness."

    t "No. But they determine whether people stay."

    "She closes the chart. Folds her hands over it."

    t "You asked me to assess morale. I assessed it. The morale is damaged. Not by the enemy. By the restructuring."

    # --- THE REAL CONVERSATION ---

    "Tessa takes off her glasses. Sets them on the desk. When she does that, the professional distance collapses."

    t "That's the report. Now I'm going to tell you what isn't in it."

    athought "Here it comes."

    t "You're different."

    a "People keep saying that."

    t "Because it's true. And because you keep not hearing it."

    "She leans forward. Her voice drops."

    t "The Sector Four operation. Fourteen dead in seventy-one seconds. Zero Phoenix casualties. The whole base is talking about it like it was a miracle."

    t "It wasn't a miracle. It was a machine. And you built it with her."

    a "The operation succeeded. Our people came home."

    t "Our people came home to a base that doesn't feel like home anymore."

    "She stands. Walks to the supply shelf. Picks up a roll of gauze, puts it back. Nervous energy. Tessa is never nervous."

    t "Aeron. I'm not Zira. I'm not going to call Nyra a spy or an infiltrator. I don't have evidence of that and I don't think that's what she is."

    t "What I think she is... is a mirror. She reflects back the version of you that you're most afraid of becoming. And she tells you it's beautiful."

    athought "A mirror."

    athought "She reflects back the version of you that you are most afraid of becoming."

    athought "And she tells you it is beautiful."

    t "Discipline isn't healing. Control isn't safety. And the fact that no one died on that operation doesn't mean nothing was lost."

    a "What was lost?"

    t "I don't know yet. That's what scares me."

    "She turns back to face him. Her eyes are steady. No tears. No softness. Just the hard clarity of someone who has decided to say the difficult thing."

    t "I need to know. Are you still in there?"

    athought "Are you still in there."

    athought "She is asking if Aeron exists underneath the commander."

    athought "She is asking if the man who carried a wounded fighter three kilometers on his back still lives inside the one who counted fourteen bodies and called it optimal."

    athought "I do not know."

    # --- CHOICE ---

    menu:
        "She waits. The medbay hums. The sterilization unit cycles."

        "You're right. I'll watch myself.":
            $ choice_and_dev(
                _current_scene_id, "_apologize", "EMP", factor=1,
                next_scene_label=None,
                note="Crack in the OB armor. Tessa stays close. Her thread remains open."
            )
            jump .apologize

        "Your concern is noted. We have operations to plan.":
            $ choice_and_dev(
                _current_scene_id, "_dismiss", "OB", factor=1,
                next_scene_label=None,
                note="Full OB dismissal. Tessa retreats to professional distance. Relationship freezes."
            )
            jump .dismiss

    # --- BRANCH: APOLOGIZE ---
    label .apologize:

        "The words come out before the armor can stop them."

        a "You're right."

        "Tessa blinks. She didn't expect that."

        a "I'll watch myself."

        "The room is quiet. The sterilization unit hums."

        a "I don't... I am not certain what is happening to me. The operation felt right. The structure feels right. The control feels..."

        "He stops. His hand is on the desk. The tremor is visible."

        athought "She can see it. The tremor. The thing I have been hiding."

        t "Necessary?"

        a "Yes."

        t "It always does. That's how it works."

        "She comes around the desk. Sits in the chair beside him instead of across from him. The professional distance dissolved."

        t "I'm not asking you to stop being the commander. Someone has to be. I'm asking you to let someone check the foundation while you build."

        a "And you're volunteering."

        t "I've been volunteering since the day you walked into my medbay with a dislocated shoulder and refused anesthetic."

        athought "She remembers that."

        athought "I barely remember it."

        athought "She remembers everything."

        t "Let me do my job. Not just the bones and the blood. The rest of it. The parts you won't look at."

        a "And if what you find is bad?"

        t "Then we deal with it. Together. Like we did before all of this."

        "Her hand is near his on the desk. Not touching. Available."

        athought "She is not Nyra. She does not validate. She does not worship."

        athought "She sees the fracture and she wants to set the bone."

        athought "That might be the braver kind of loyalty."

        a "Okay."

        t "Okay."

        "The simplest word. The hardest one."

        $ rel_bump("Tessa", trust=1)
        $ scene_mark("apologized_to_tessa")
        $ npc_remember("Tessa", "friction_scene", tone="crack_in_armor")
        $ flag("tessa_thread_open", True)

        jump .scene_close

    # --- BRANCH: DISMISS ---
    label .dismiss:

        "The armor holds."

        a "Your concern is noted."

        "He stands. The chair scrapes against the floor."

        a "We have operations to plan. The morale data is useful -- I'll factor it into the rotation adjustments."

        "Tessa doesn't move. Her hands stay folded on the desk."

        t "That's it?"

        a "That is the report and that is my response. Adjustments will be made."

        t "I'm not talking about the report."

        a "I know."

        "The word hangs. He knows. He heard her. He understood."

        "And he is choosing not to engage."

        t "Okay."

        "Her voice is flat. Not angry. Something worse than angry."

        "She puts her glasses back on. Opens the next patient chart. Her pen moves."

        t "Send me the updated rotation schedule when it's ready. I'll need to adjust clinic hours."

        athought "She retreated. Pulled back behind the professional wall."

        athought "I put her there."

        athought "It is easier this way."

        athought "The operation was clean. The structure is sound. The rotation schedules are tight."

        athought "And the warmest room in the base just got colder."

        "He walks to the door."

        t "Aeron."

        "He stops. Doesn't turn."

        t "The offer doesn't expire. When you want to hear it."

        "He leaves."

        $ rel_bump("Tessa", trust=-1)
        $ scene_mark("dismissed_tessa")
        $ npc_remember("Tessa", "friction_scene", tone="professional_retreat")
        $ flag("tessa_thread_frozen", True)

        jump .scene_close

    # --- SCENE CLOSE ---
    label .scene_close:

        "The corridor outside the medbay is cold. The base hum fills the silence."

        athought "Discipline is not healing."

        athought "She said that. Days ago. And again just now."

        athought "I keep hearing it."

        athought "I keep not changing."

        "He walks toward the operations room. Nyra's patrol grids are cycling on the displays. Blue light through the window. Clean lines."

        "His hand trembles. He presses it flat against his thigh."

        athought "Are you still in there."

        # --- END ---

        #stop ambient fadeout 2.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ scene_mark(_current_scene_id, "completed")

        call li_lore_check("Tessa") from _a3_s10_lore

        return

# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s10_tessa_friction_ob
# cann.chapter: Act III, Phase I -- Consolidation
# cann.chapter_start: False
# cann.when_in_timeline: Two days after Sector 4 strike. After morale assessments complete.
# cann.what_happened:
#   - Tessa presents morale assessment: 19/31 fighters show elevated stress. 11 afraid of drills.
#     3 requesting reassignment. Veterans asking to leave.
#   - Tessa confronts Aeron directly: "Discipline isn't healing."
#   - She calls Nyra "a mirror" that reflects Aeron's worst self and calls it beautiful.
#   - "Are you still in there?"
#   - Player choice: Apologize (crack in the OB armor, Tessa thread open)
#     or Dismiss (professional retreat, Tessa thread frozen).
# cann.aeron_state:
#   - OB under pressure. The hand tremor visible. Tessa gets under the armor.
#   - Apologize: acknowledges the fracture. "Okay." The simplest, hardest word.
#   - Dismiss: maintains control. "Your concern is noted." Loses the warmest room.
# cann.path_tracking:
#   - Apologize: choice_and_dev EMP factor=1, rel_bump("Tessa", trust=1),
#     scene_mark("apologized_to_tessa"), flag("tessa_thread_open")
#   - Dismiss: choice_and_dev OB factor=1, rel_bump("Tessa", trust=-1),
#     scene_mark("dismissed_tessa"), flag("tessa_thread_frozen")
# cann.thematic_flags:
#   - "Discipline isn't healing." -- Tessa's thesis. Repeated from Terms of Order.
#   - Nyra as mirror: "She reflects back the version of you that you're most afraid of
#     becoming. And she tells you it's beautiful."
#   - The medbay as the warmest room -- and the choice to make it colder.
#   - The hand tremor: visible, physical evidence of the cost Aeron won't name.
#   - "Are you still in there?" -- the question the OB path keeps circling.
#   - Apologize path: "She sees the fracture and she wants to set the bone."
#     Tessa as the anti-Nyra. Compassion as confrontation.
#   - Dismiss path: "The warmest room in the base just got colder."
#     The cost of control measured in warmth lost.
# cann.character_moments:
#   - Tessa: "I'm not Zira." Differentiates herself. Not suspicious -- worried.
#     "A mirror." Her read on Nyra is psychological, not tactical.
#     "The offer doesn't expire." -- even dismissed, she leaves the door open.
#   - Aeron: The tremor. The armor. The crack (if player chooses).
#     "I keep hearing it. I keep not changing."
# cann.block_status:
#   - ANCHOR (always plays). Choice determines Tessa thread for remainder of OB path.
#   - Apologize gates: Tessa erotic scene availability in Phase II.
#   - Dismiss gates: Tessa becomes professional-only. Cold. The relationship freezes.
# cann.requires_followup:
#   - If apologized: Tessa becomes Aeron's conscience. Private check-ins continue.
#   - If dismissed: Tessa withdraws. Her insight is lost. The cost compounds.
#   - Counter-strike scene -- Tessa's reaction depends on this choice.
#   - The hand tremor thread -- escalates. Tessa noticed; others will too.
