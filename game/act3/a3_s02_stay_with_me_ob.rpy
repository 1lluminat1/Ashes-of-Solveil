# =======================================================
# ACT 3 - Scene 02: Stay With Me (Obedience Path)
# File: a3_s02_stay_with_me_ob.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s02_stay_with_me_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s02_stay_with_me_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm lens (OB detachment), locked tripod with minimal drift.
    #         Wide shots emphasize distance between them. Close-ups catch micro-expressions.
    #         When/if intimacy occurs, camera stays clinical - observing, not participating.
    # LIGHTING: Aeron's quarters: cold 5000K overhead, single amber practical (desk lamp).
    #           Shadows are hard-edged, not soft. Blue-grey wash from window (city glow).
    #           If intimacy: no warmth bloom. Same cold palette. Bodies as shapes, not heat.
    # SFX: Loop - ventilation hum, distant base machinery, wind against reinforced glass.
    #      One-shots - door hiss, fabric shift, breath catch, mattress compress.
    # FX/COMP: Window reflection shows city lights. Dust motes in lamp beam. Cold breath visible.
    # BLOCKING: Aeron at desk, back to door. Lyra enters. Distance closes reluctantly.
    #           Physical contact is initiated by HER, not him. He permits. He doesn't reach.
    # CANON: This is OB Lyra's first Act 3 intimacy attempt. She needs proof he's still human.
    #        He may not be able to give it. The scene should feel like reaching for someone drowning.
    # CONSENT: 3-gate framework. But the consent here is tinged with desperation, not joy.
    # FACE: Both visible. Her searching. His... present but not there.

    # ========= VOICE BASELINE =========
    # OB Aeron: Formal, clinical, minimal contractions. Short declarative sentences.
    #           He's detached but not cruel. He permits contact. He doesn't initiate.
    # OB Lyra: Faith cracking. She's numb from the funeral but desperate for warmth.
    #          Her usual composure is fractured. She asks questions she already knows the answers to.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - AERON'S QUARTERS - NIGHT]
    # Sparse. Functional. A cot, a desk, tactical displays dark. The room of someone who
    # doesn't expect to stay. Cold light from the window. The base is quiet - night watch only.
    # Hours after the funeral. Hours after he sat in Selene's chair.

    #scene bg_aeron_quarters_ob_night with dissolve
    #play ambient "sfx/ambient/quarters_cold_hum.ogg" fadein 2.0

    # --- OPENING: AERON ALONE ---

    # VISUAL: Aeron at his desk, reviewing something on a tablet. His posture is rigid.
    # The lamp casts hard shadows. He hasn't changed from the funeral.

    athought "The reports blur together. Supply lines. Patrol rotations. Names I should memorize."

    athought "I've read the same paragraph four times. The words don't stay."

    athought "Selene's chair is in the war room. I sat in it. The metal was cold."

    athought "I should feel something about that."

    athought "I don't."

    # VISUAL: The door hisses. He doesn't turn.

    #play sound "sfx/door_hiss_soft.ogg"

    athought "I know who it's before she speaks. The cadence of her footsteps. The way she breathes when she's trying not to cry."

    # --- LYRA ENTERS ---

    # VISUAL: Lyra in the doorway. Still in her funeral clothes. Her composure is cracked.
    # She doesn't ask permission to enter. She simply does.

    #show lyra quarters_doorway_ob with dissolve

    "She stands in the doorway for three seconds before stepping inside. The door closes behind her."

    athought "Three seconds. She was deciding whether to run."

    l "You didn't come to dinner."

    a "I wasn't hungry."

    l "You haven't eaten since yesterday."

    a "That isn't accurate. I'd field rations at 0600."

    "She flinches. Not at the words. At the voice. The flat, clipped cadence that sounds like someone else."

    athought "She hears it. The way I speak now. The rhythm that sounds like my father."

    athought "She isn't wrong to flinch."

    # VISUAL: Lyra moves into the room. Stops at the edge of the lamp's light.

    #show lyra quarters_standing_ob with dissolve

    l "Aeron."

    a "Yes."

    l "Look at me."

    athought "I should. It would be the correct response. The human response."

    athought "I turn."

    # VISUAL: He turns. Their eyes meet. She's searching for something. He isn't sure it exists.

    "He turns. The lamp catches his face - hollow, composed, still."

    "She studies him the way she used to study scripture. Looking for meaning that might not be there."

    l "I told you I chose this. I chose you."

    a "I remember."

    l "I said I needed to understand why."

    a "Yes."

    l "I still don't understand."

    athought "Neither do I."

    a "That makes two of us."

    # --- THE CRACK ---

    # VISUAL: Something breaks in her expression. Not tears - something worse. Hope, dying.

    "Her jaw tightens. Her hands ball into fists at her sides."

    l "Say something real."

    a "I don't know what that means."

    l "Something that isn't a report. Something that isn't... this."

    "She gestures at him. At the room. At the cold light and the hard shadows."

    l "You spoke at her funeral like you were reading from a script. Because you were. Because we wrote it together."

    l "But that voice - the one you used - that wasn't acting. That was you."

    athought "She's correct."

    a "Yes."

    l "Is that all that's left?"

    athought "I don't know how to answer that."

    athought "The honest answer is: I don't know."

    athought "The kind answer is: no, there's more."

    athought "I don't know which one is true."

    # --- CHOICE: RESPONSE ---

    menu:
        "She's waiting. Her faith is a thread stretched to breaking."

        "I don't know what's left.":
            $ choice_and_dev(
                _current_scene_id, "_honest_doubt", "OB", factor=1,
                next_scene_label=None,
                note="Honest uncertainty. OB vulnerability. Lyra responds to the crack."
            )
            jump .honest_doubt

        "There's more. I'm still here.":
            $ choice_and_dev(
                _current_scene_id, "_reassurance", "OB", factor=0,
                next_scene_label=None,
                note="Attempted reassurance. May or may not be true. Lyra tests it."
            )
            jump .reassurance

    # --- BRANCH: HONEST DOUBT ---
    label .honest_doubt:

        a "I don't know what's left."

        "The words hang in the air. He didn't plan to say them."

        athought "That wasn't tactical. That wasn't controlled."

        athought "That was honest."

        l "..."

        "She stares at him. For a moment, something flickers in her expression. Recognition."

        l "That. That was real."

        a "It wasn't useful."

        l "I don't need useful. I need you."

        athought "She crosses the distance. I don't step back."

        # VISUAL: Lyra closes the gap. Her hand reaches for his face. Stops inches away.

        #show lyra quarters_close_ob with dissolve

        l "Can I...?"

        athought "She's asking permission. Even now. Even after everything."

        a "Yes."

        "Her palm touches his jaw. Her fingers are cold. She's shaking."

        l "You're still in there. I can feel it."

        athought "I don't know if she's right."

        athought "I want her to be."

        $ rel_bump("Lyra", trust=1)
        $ flag("lyra_ob_honest_doubt", True)

        jump .intimacy_gate

    # --- BRANCH: REASSURANCE ---
    label .reassurance:

        a "There's more. I'm still here."

        "The words come out flat. Rehearsed. Even he can hear it."

        l "Are you?"

        a "Yes."

        l "Then show me."

        athought "She's testing the claim. She should."

        athought "I don't know if I can pass."

        # VISUAL: Lyra steps closer. Her eyes are searching, skeptical.

        #show lyra quarters_close_ob with dissolve

        l "Touch me. Not because I asked. Because you want to."

        athought "I should want to. I remember wanting to."

        athought "I reach for her face."

        "His hand rises. Stops. Hovers near her cheek without making contact."

        l "You can't, can you."

        a "I'm trying."

        l "Trying isn't the same."

        "She closes her eyes. When she opens them, the hope is quieter. Harder."

        l "Then let me try for both of us."

        "She takes his hand. Places it against her cheek. Holds it there."

        l "Feel that. I'm real. This is real."

        athought "Her skin is warm. Her pulse flutters against my palm."

        athought "I feel it. I don't know what to do with it."

        $ rel_bump("Lyra", affection=1)

        jump .intimacy_gate

    # --- INTIMACY GATE ---
    label .intimacy_gate:

        # Gate check: OB Lyra intimacy requires trust >= 2 OR (trust >= 1 AND witnessed_murder complicity)
        if not (trust("Lyra") >= 2 or (trust("Lyra") >= 1 and flag("lis_witnessed_execution"))):
            jump .comfort_variant

        # --- CONSENT GATE A: Verbal Cue ---

        l "I need something tonight. I need to know you're still capable of..."

        "She trails off. Her hand is still pressed against his."

        a "Of what."

        l "Feeling. Wanting. Being human."

        athought "She's asking for proof I may not be able to provide."

        athought "But she's asking. And I owe her an answer."

        a "What do you need."

        l "Stay with me. Tonight. Not as a commander. Not as whatever you're becoming."

        l "Just... stay."

        # --- CONSENT GATE B: Reciprocal Action ---

        menu:
            "Her breath is shallow. Her hand trembles against his jaw."

            "Stay.":
                $ choice_and_dev(
                    _current_scene_id, "_stay", "OB", factor=1,
                    next_scene_label=None,
                    note="Accepts intimacy. OB version: permits rather than initiates."
                )
                jump .intimacy_path

            "I don't think I can give you what you need.":
                $ choice_and_dev(
                    _current_scene_id, "_cannot", "OB", factor=0,
                    next_scene_label=None,
                    note="Honest refusal. Routes to comfort variant."
                )
                jump .comfort_variant

    # --- INTIMACY PATH ---
    label .intimacy_path:

        a "Stay."

        athought "The word comes out quieter than I intended."

        "Something shifts in her expression. Relief. Desperation. Both."

        l "You mean it."

        a "I don't say things I don't mean."

        l "You used to say things you felt. That's different."

        athought "She's right. It's different."

        athought "I don't correct her."

        # --- CONSENT GATE C: Explicit Exit ---

        "She steps closer. Her forehead touches his. Her breath is warm against his lips."

        l "If you want to stop - at any point - tell me."

        a "The same applies to you."

        l "I know what I want, Aeron. I've known since the funeral."

        l "I want proof that you're still in there. That I didn't choose a ghost."

        athought "She kisses me."

        athought "I let her."

        # VISUAL: The kiss. Desperate. Searching. She's the one reaching; he's permitting.
        # CAMERA: Stays wide. Clinical. Observing.

        #show lyra_aeron kiss_ob with dissolve

        # --- INTIMACY SEQUENCE (OB Tone: Desperate, Not Joyful) ---

        "The kiss isn't gentle. It isn't tender. It's a question asked with lips and teeth."

        "Are you still there? Are you still mine? Did I lose you when I watched you pull the trigger?"

        athought "I don't have answers. I have hands. I have breath. I have the mechanics of presence."

        athought "I give her what I can."

        "Her hands pull at his collar. His hands find her waist - not grasping, just... there."

        "She makes a sound against his mouth. Grief or relief. He can't tell the difference."

        l "Say my name."

        a "Lyra."

        l "Like you mean it."

        athought "I try."

        a "Lyra."

        "Her breath catches. It was enough. Barely."

        # --- FADE TO BLACK (OB: Clinical, Not Warm) ---

        "What follows isn't passion. It isn't love, not in the way she remembers."

        "It's two people trying to prove something to each other in the dark."

        "She proves she's still willing to reach for him."

        "He proves he's still capable of being reached."

        "Whether either proof is enough remains to be seen."

        #scene black with fade
        #pause 1.5

        # --- AFTERMATH ---

        #scene bg_aeron_quarters_ob_night_after with dissolve

        # VISUAL: Later. The lamp is off. City light through the window. Two shapes in the dark.
        # She's curled against him. His arm is around her, but the gesture looks learned, not felt.

        athought "She's asleep. Or pretending to be."

        athought "Her head rests on my chest. I can feel her heartbeat against my ribs."

        athought "It's faster than it should be for sleep."

        "Her voice comes in the dark. Small. Fragile."

        l "Did you feel anything?"

        athought "The honest answer would wound her."

        athought "The kind answer might be a lie."

        athought "Somewhere under the numbness, something flickers. Just for a moment. Her warmth, her breath, the way she said my name like it still meant something."

        athought "Then it's gone. Buried under the static."

        athought "I choose precision."

        a "I felt you."

        "Silence. Then her grip on his shirt tightens."

        l "That isn't an answer."

        a "It's the only one I have."

        "She doesn't respond. After a long moment, her breathing evens out. Real sleep this time."

        athought "I felt you."

        athought "I don't know if that's the same as feeling."

        athought "I don't know if there's a difference anymore."

        # --- SCENE CLOSE ---

        athought "Outside, the base hums. The city bleeds. The rebellion moves forward without Selene."

        athought "In this room, a woman who watched me commit murder is sleeping against my chest."

        athought "She chose this. She chose me."

        athought "I don't know if I'm capable of deserving that choice."

        athought "I don't know if I'm capable of anything but the next mission."

        athought "But she's warm. And she stayed."

        athought "That will have to be enough."

        $ metric("lyra_intimacy_level", set_to=max(metric("lyra_intimacy_level"), 1))
        $ rel_bump("Lyra", affection=1)
        $ rel_bump("Lyra", trust=1)
        $ flag("lyra_ob_first_intimate", True)
        $ flag("lyra_ob_aftercare", True)

        jump .scene_end

    # --- COMFORT VARIANT ---
    label .comfort_variant:

        # Either gate failed or player chose "I can't give you what you need"

        athought "I should want to. I remember wanting to."

        athought "The memory is there. The feeling isn't."

        a "I don't think I can give you what you need. Not tonight."

        "Her face crumbles. Not surprise - she expected this. That makes it worse."

        l "Then what can you give me?"

        athought "An honest answer. That's all I have left."

        a "Presence. I can stay. I can be here."

        l "But not... with me."

        a "I don't know how to be with anyone right now. I'm barely here at all."

        "She closes her eyes. When she opens them, the tears she has been holding back finally fall."

        l "I watched you kill her, Aeron."

        l "I watched, and I stayed, and I told myself it was because I believed in you."

        l "But you're disappearing. And I don't know how to reach what's left."

        athought "She isn't wrong."

        athought "I don't know how to tell her that the thing she's reaching for might already be gone."

        a "Then stay anyway. Even if you can't reach me."

        a "Stay because the alternative is leaving, and neither of us can afford that."

        "She stares at him. Something hardens in her expression. Not anger - determination."

        l "I'll not give up on you."

        l "Even if you've given up on yourself."

        athought "She turns. Walks to the door. Pauses."

        l "When you find whatever is left of you... come find me."

        l "I'll be waiting. I have nothing else to do with my faith."

        "The door hisses shut behind her."

        athought "I stand in the cold light for a long time."

        athought "She'll wait. I believe that."

        athought "I don't know if there will be anything left to find."

        $ rel_bump("Lyra", trust=1)
        $ flag("lyra_ob_comfort_scene", True)

        jump .scene_end

    # --- SCENE END ---
    label .scene_end:

        #stop ambient fadeout 2.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ scene_mark(_current_scene_id, "completed")

        return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s02_stay_with_me_ob
# cann.chapter: Act III, Chapter I - Complicity (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Night after Selene's funeral. Same day as Ashes in Formation.
# cann.what_happened:
#   - Lyra comes to Aeron's quarters seeking proof he's still human.
#   - Player choice: honest doubt ("I don't know what's left") or reassurance ("I'm still here").
#   - Honest doubt route: trust+1, Lyra recognizes the crack.
#   - Reassurance route: affection+1, Lyra tests the claim.
#   - If thresholds met: intimacy gate opens. She asks him to stay.
#   - Intimate path: desperate, searching sex. She reaches; he permits. Not joyful - proof-seeking.
#   - Aftermath: "Did you feel anything?" / "I felt you." - ambiguous, painful.
#   - Comfort variant: he admits he can't give her what she needs. She vows to wait.
# cann.aeron_state:
#   - OB detachment at its peak. He permits contact but doesn't initiate.
#   - His internal voice questions whether he can feel anything anymore.
#   - "I felt you" is the most he can offer - and it may not be enough.
# cann.path_tracking:
#   - OB baseline. Honest doubt adds trust+1, reassurance adds affection+1.
#   - Intimate path adds intimacy_level, affection+1, trust+1.
#   - Comfort variant adds trust+1.
# cann.thematic_flags:
#   - Motifs: Cold light, hard shadows, "I felt you" (ambiguous proof).
#   - Lyra's faith as thread: "I'll not give up on you. Even if you've given up on yourself."
#   - The complicity bond: "A woman who watched me commit murder is sleeping against my chest."
#   - His self-question: "I don't know if I'm capable of anything but the next mission."
# cann.character_moments:
#   - Lyra: Faith cracking. Needs proof he's still human. Reaches desperately.
#   - Post-intimacy: uncertain if she found what she was looking for.
#   - Comfort variant: determined to wait, even if there's nothing left to find.
# cann.block_status:
#   - VARIANT (intimacy optional); requires followup scene load.
# cann.requires_followup:
#   - This scene sets up A3_10 "Kneel With Me" (Lyra forces emotional confession).
#   - "I felt you" should echo later - either as comfort or as wound.
#   - Comfort variant's "come find me" is a thread for late OB Lyra reconciliation.
