# =======================================================
# ACT 2 - Scene 7: Quiet Night
# File: act2_07_quiet_night.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_07_quiet_night"
$ scene_mark(_current_scene_id, "entered")

label act2_07_quiet_night:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35–50mm intimate; slow drifts, minimal cuts. Two-shots and close singles. Hold on Lyra's face during vulnerable beats. Push-in when she talks about Elisse.
    # LIGHTING: Low amber safehouse bulb. Cold blue-gray from the barred window. Lyra's pendant catches light when she holds it. Her face half-lit during confession.
    # SFX: Loop — distant Unders hum (wrong pitch for her), occasional pipe groan, muffled voices far away. One-shots — pendant chain, fabric shift, her breath catching.
    # FX/COMP: Faint dust motes in the amber light. Window shows distant neon bleed, not stars.
    # BLOCKING/PROPS: Safehouse interior, two bedrolls, crate-table with supplies, Lyra's pendant (cracked Core shard), her Band visible under pushed-up sleeve.
    # FACE: Lyra oscillates between composed stillness and micro-cracks—jaw tight, eyes wet, breath controlled. Aeron attentive, uncertain how to help.

    # ========== SAFEHOUSE - LATE NIGHT ==========

    "Later that night."

    athought "I return from the Ghostline node to find the safehouse unchanged—the same concrete, the same trapped air, the same thin light."

    athought "But Lyra isn't asleep anymore."

    # VISUAL: Lyra sitting against the wall, knees drawn up, staring at nothing. Her hand rests on her pendant.
    "She's sitting against the wall, knees pulled to her chest."

    athought "Fingers wrapped around something at her throat. Her pendant. The cracked Core shard she's worn since the Order."

    if empathy_band() == "obedience":
        athought "She's awake. Posture says she's been awake for a while."
        athought "The pendant means she's thinking about the Order. That's never good."
    elif empathy_band() == "empathy":
        athought "She's holding the pendant. She only does that when something's breaking inside her."
    else:
        athought "She's awake. And holding the pendant. That combination usually means trouble."

    "I close the door quietly. She doesn't look up."

    a "Hey."

    l "(flat) Hey."

    "I move to sit against the opposite wall, giving her space."

    athought "The silence stretches."

    l "Did Zira need something?"

    a "She showed me the Ghostline. The network. All of it."

    l "(still not looking at him) She trusts you."

    a "She's taking a risk on me. I'm not sure that's the same thing."

    l "It's more than most people get."

    athought "The Unders hums around us—pipes, distant machinery."

    if empathy_band() == "obedience":
        athought "She's not sleeping. In the Aeries, she needed the hum of power conduits to rest."
        athought "The Unders has a different frequency. Wrong pitch. Wrong rhythm."
    else:
        athought "She can't sleep here. The silence is wrong—not the clean hum she grew up with."
        athought "The Unders sounds like chaos to someone who was raised in the Cathedral."

    a "You couldn't sleep."

    l "The sound is wrong."

    a "The Unders?"

    l "Everything."

    "She finally looks at me."

    athought "Her eyes are red-rimmed but dry. Whatever crying happened, it happened before I got back."

    l "I keep thinking about the clinic."

    a "Tessa?"

    l "The way she worked. Hands steady. No hesitation."
    l "She looked at that man's leg—a mess of bone and blood—and she just... fixed it."
    l "Like it was the most natural thing in the world."

    if empathy_band() == "obedience":
        a "She's trained. Repetition creates competence."
        l "(bitter laugh) Is that what you think it is? Repetition?"
    else:
        a "She's had practice. Too much of it, probably."
        l "That's not what I mean."

    # VISUAL: Lyra's grip tightens on the pendant.
    l "I was trained too, Aeron. By the best the Order had."
    l "But my training was about resonance. Purity. Making the Cores hum in harmony."
    l "I never learned how to put someone back together."

    athought "Her voice cracks on the last word. She swallows, forces the calm back."

    l "I only ever learned how to take them apart."

    athought "She's not talking about the Order anymore. She's talking about Echelon."
    athought "About what we did. What she did under Marcus's command."

    a "Lyra—"

    l "Don't."
    l "Don't tell me it wasn't my fault. Don't tell me I was following orders."
    l "I know the speech. I've given the speech."

    "She pulls the pendant out from under her shirt. Holds it in front of her."

    athought "The amber light catches the crack that runs through the Core shard."

    l "Do you know what this is?"

    a "Your relic. From the Cathedral."

    l "It's a piece of a Harmony Core. Cracked during the collapse of Wing Seven."
    l "When my mentor died."

    $ npc_remember("Lyra", "told_aeron_about_pendant", tone="vulnerable")

    "She turns it over in her fingers."

    athought "The light shifts across the fracture."

    l "Her name was Elisse. High Cantor. She taught me everything about resonance, about stillness, about listening for the divine."
    l "When the containment field ruptured, she used her body to shield me."

    if empathy_band() == "obedience":
        athought "Sacrifice and protection. I understand that part."
        athought "What I don't understand is why she's telling me this now."
    else:
        athought "She watched her mentor die protecting her. And then—"

    l "The Order blamed her. Called her a heretic. Said she 'succumbed to emotion during calibration.'"
    l "They needed someone to blame, and the dead can't defend themselves."

    "Her voice is steady now. Too steady."

    athought "The kind of calm that comes from rehearsing something a thousand times."

    l "I signed the report, Aeron."
    l "I knew it was a lie. I knew she died saving me. And I signed my name to a document that called her impure."

    $ npc_remember("Lyra", "admitted_signing_false_report", tone="shame")
    $ scene_mark(_current_scene_id, "elisse_confession")

    "The pendant swings gently in her grip. The crack catches the light like a fault line."

    l "That was the first time I chose obedience over truth."
    l "It wasn't the last."

    if empathy_band() == "obedience":
        athought "She's confessing. Waiting for judgment."
        athought "I've seen this in interrogations. The relief of finally saying it out loud."
        athought "But she's not a suspect. She's Lyra."
    elif empathy_band() == "empathy":
        athought "She's been carrying this for years. The weight of one signature."
        athought "I know what that feels like. Different document, same betrayal."
    else:
        athought "She signed a lie to survive. I've done worse."
        athought "But that doesn't make it hurt less."

    # ========== THE CLINIC CONNECTION ==========

    l "When I watched Tessa today, I kept thinking about Elisse."
    l "What she would say if she saw what I became."
    l "A soldier for the man who 'saved' me from the Order. A weapon in dress uniform."
    l "Signing reports. Following orders. Calling it duty."

    "She looks at him now. Really looks."

    athought "Searching for something."

    l "I was the one who did things like that to people, Aeron."
    l "Not just watched. Did."
    l "I've seen bodies on tables that looked like Jace. I've signed off on operations that put them there."
    l "And then I went home and prayed to machines for forgiveness."

    if pass_tier("OB2", "OB3"):
        athought "She's describing my life. Our life. The one we chose."
        athought "The one we're trying to escape."
    elif pass_tier("EMP2", "EMP3"):
        athought "She's breaking. Not the loud kind—the quiet kind."
        athought "The kind where everything you believed falls away and there's nothing underneath."
    else:
        athought "She's seeing herself clearly. Maybe for the first time."
        athought "It's not a pretty picture. But it's honest."

    l "Tessa heals people. We hurt them."
    l "What's the point of running if we're still the same underneath?"

    athought "The question hangs in the air. She's not asking rhetorically—she wants an answer."

    # --- PLAYER CHOICE: How does Aeron respond to her vulnerability? ---
    menu:
        "She's asking if they can change. If running means anything at all."

        "Hold space for her—let her feel it without fixing it.":
            $ choice_and_dev(
                _current_scene_id, "_hold_space", "EMP", factor=1,
                note="Aeron sits with Lyra's pain instead of trying to solve it. Emotional presence over solutions."
            )
            $ npc_remember("Lyra", "aeron_held_space_for_pain", tone="grateful")
            $ scene_mark(_current_scene_id, "held_space")
            $ rel_bump("Lyra", trust=2, affection=1)

            athought "I don't answer immediately. Just let the question exist."

            "He moves beside her, sits against the same wall, close enough that their shoulders almost touch."

            a "I don't know if we can change what we are."
            a "But we're not what we were yesterday. That has to count for something."

            l "(quiet) Does it?"

            a "You watched Tessa work and felt something break. That's not nothing."
            a "Glass wouldn't have felt that. Neither would the person you were six months ago."

            "She's quiet for a long moment. Then, slowly, she leans into him. Shoulder to shoulder."

            l "I keep waiting for the hum to come back."
            l "The Order taught us that the divine speaks through resonance. That if you're still enough, pure enough, you can hear it."
            l "I haven't heard it in years."

            a "Maybe the divine doesn't sound like machines."

            l "(almost a laugh) Heresy."

            a "I've been accused of worse."

            "She turns the pendant over again. The crack catches the light."

            l "Elisse would have liked you."
            l "She always said the truest prayers were the ones that didn't sound like prayers at all."

            if pass_tier("OB1", "OB2", "OB3"):
                athought "She's leaning on me. Literally. I should pull away—maintain distance."
                athought "I don't."
            else:
                athought "She's leaning on me. It feels like trust. It feels like something I don't want to name."

            a "I didn't know her. But I know you."
            a "And you're not the person who signed that report. Not anymore."

            l "How do you know?"

            a "Because the person who signed it wouldn't be here. Hiding in the Unders with a traitor."
            a "She would have stayed. Kept signing. Kept praying."
            a "You left."

            "Lyra is silent. Then her hand finds his in the dark."

            l "Thank you."

            a "For what?"

            l "For not telling me it's okay. For not pretending I didn't do terrible things."
            l "For just... sitting here."

            athought "We stay like that. Shoulder to shoulder. Hand touching hand. The Unders humming its wrong song around us."

        "Offer perspective—reframe the guilt as something useful.":
            $ choice_and_dev(
                _current_scene_id, "_reframe_guilt", "OB", factor=1,
                note="Aeron tries to make the guilt productive rather than sitting with the emotion."
            )
            $ npc_remember("Lyra", "aeron_reframed_guilt", tone="mixed")
            $ scene_mark(_current_scene_id, "reframed_guilt")
            $ rel_bump("Lyra", trust=1)

            a "Guilt is a resource."

            l "(sharp) What?"

            a "I'm not saying it doesn't matter. I'm saying it can be used."
            a "The person who signed that report knows exactly how the system works. How it justifies itself."
            a "That knowledge is valuable now."

            "She stares at him."

            athought "Something flickering behind her eyes. Hurt, maybe. Or disappointment."

            l "You sound like Marcus."

            athought "The words hit harder than she probably intended. I feel myself stiffen."

            a "I'm trying to help."

            l "By turning my dead mentor into a tactical asset?"

            if pass_tier("EMP1", "EMP2", "EMP3"):
                athought "She's right. That was wrong."
                athought "But I don't know how to do this. How to just... be here without fixing something."
            else:
                athought "She asked a question. I answered it. What does she want from me?"

            a "...That's not what I meant."

            l "(exhaling) I know."
            l "I know you're trying."

            "She pulls her knees tighter."

            athought "Creates distance even while sitting still."

            l "Maybe I just needed someone to listen. Not solve."

            a "I'm not good at that."

            l "I noticed."

            athought "The silence returns. Heavier than before."

            l "(after a long pause) Elisse used to say that the hardest prayers are the ones you don't know how to finish."
            l "Maybe this is one of those."

            a "I don't know how to pray."

            l "Neither do I. Not anymore."

            "She looks at the pendant again. Then tucks it back under her shirt."

            l "Get some sleep, Aeron. Tomorrow will be worse."

            "She lies down, turns toward the wall."

            athought "Conversation over."

            athought "I said the wrong thing. Or said the right thing the wrong way."
            athought "Either way, something closed that was starting to open."

    # ========== CLOSING — THE WEIGHT BETWEEN THEM ==========

    if scene_has(_current_scene_id, "held_space"):
        # --- EMP BRANCH CLOSING ---

        "Her breathing evens out."

        athought "Not sleep—just exhaustion finding a resting place."

        athought "I don't move. Don't want to break whatever fragile thing we've built in the dark."

        # VISUAL: Lyra's hand still touching his. Her pendant resting against her chest. The barred window showing nothing but distant neon.
        l "(half-asleep) Aeron."

        a "Yeah?"

        l "The sound is still wrong."
        l "But it's better when you're here."

        "She's asleep before he can respond. Or pretending to be."

        athought "I'm not sure which."

        athought "Better when I'm here."
        athought "That's not nothing. That might be everything."

        athought "I stay awake a while longer, feeling the weight of her shoulder against mine."

        "The Unders hums its wrong song. Somewhere out there, Zira is watching through cameras he can now see."

        "Somewhere above, Marcus is planning their deaths."

        athought "But here, in this concrete box, something small and impossible is growing."

        athought "Elisse died protecting her, and maybe that's what this is—not romance, not yet, just protection."
        athought "Being the wall between her and the things that want to break her."
        athought "I can do that. I think I want to."

        $ scene_mark(_current_scene_id, "intimacy_seed_planted")

    else:
        # --- OB BRANCH CLOSING ---

        athought "I lie on my bedroll, staring at the ceiling. Lyra's back is to me. Wall of silence between us."

        athought "I tried to help. It came out wrong."
        athought "Story of my life, apparently."

        "The Unders hums. Lyra doesn't move."

        athought "Not sure if she's asleep or just done talking."

        athought "She wanted something I don't know how to give."
        athought "Presence without purpose. Feeling without function."
        athought "I was trained to solve problems. She's not a problem to solve."
        athought "But I don't know what else to be."

        athought "Sleep comes eventually. Thin and restless."

        athought "Tomorrow will be worse. She was right about that."

        athought "Maybe I can try again. Do better."
        athought "Or maybe the moment's gone and there's nothing to do but keep moving."
        athought "Either way, the pendant stays around her neck. The crack stays in the Core."
        athought "And somewhere underneath all the doctrine, Lyra is still waiting for a hum that will never come."

    # --- SCENE WRAP ---
    $ flag_on("Lyra", "elisse_confession_heard")
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_07_quiet_night
# cann.chapter: Act II, Chapter II — Constellation
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Late night of Day 3, after Aeron returns from Ghostline node (A2_06).
# cann.what_happened:
#   - Aeron returns to find Lyra awake, holding her pendant (cracked Core shard from the Order).
#   - She can't sleep—the Unders has the wrong sound. She's used to the hum of power conduits.
#   - She processes the clinic: watching Tessa heal made her realize she only learned to hurt.
#   - Major confession: Lyra tells Aeron about Elisse, her dead mentor, and signing the false report.
#   - She asks if running means anything—if they can change what they are.
#   - Core choice: Aeron either holds space for her pain (EMP) or tries to reframe guilt as useful (OB).
#   - EMP branch: Physical closeness, emotional connection, "better when you're here."
#   - OB branch: She compares him to Marcus, conversation shuts down, distance remains.
# cann.aeron_state:
#   - Processing his new Ghostline access while Lyra is processing her faith collapse.
#   - EMP branch: Learns to be present without solving; earns trust/affection.
#   - OB branch: Falls into "fix it" mode; misses the emotional beat; Lyra withdraws.
# cann.path_tracking:
#   - One `choice_and_dev` decision:
#       • `_hold_space` → EMP +1 weight, trust +2, affection +1 with Lyra.
#       • `_reframe_guilt` → OB +1 weight, trust +1 with Lyra.
#   - Scene flags: `held_space` vs `reframed_guilt` for intimacy gating.
#   - `intimacy_seed_planted` flag set only on EMP branch—required for first lewd.
#   - NPC memories for Lyra stored via `npc_remember()`.
#   - Running empathy range at scene end: -12 to +2.
# cann.thematic_flags:
#   - Motifs: Wrong sound/wrong hum, the crack in the Core, prayers that don't finish.
#   - Lyra's arc: Faith collapsing, seeking something to believe in, finding it in Aeron (or not).
#   - Elisse as parallel to Aeron's role: protector, shield, someone who died for her.
#   - The pendant as symbol: cracked faith, carried guilt, something beautiful that broke.
#   - "Better when you're here" — key intimacy seed line.
# cann.alignment_flavor_points:
#   - Opening: OB reads tactical, EMP reads emotional
#   - "Wrong sound": connects to her addiction to silence/hum
#   - Elisse confession: different internal reactions by band
#   - Response to "what's the point of running": hold space vs reframe
#   - Post-choice: physical closeness vs distance/wall
#   - Closing internal: protection vs failed problem-solving
# cann.character_moments:
#   - Lyra: Most vulnerable we've seen her. Confesses Elisse, the false report, her complicity.
#   - The "you sound like Marcus" line on OB path is a significant wound.
#   - EMP path: "Better when you're here" is the seed for later intimacy.
#   - The pendant as physical anchor throughout—she holds it when breaking.
# cann.block_status:
#   - Lyra intimacy setup scene. Single alignment choice, significant relationship divergence.
# cann.requires_followup:
#   - `intimacy_seed_planted` flag gates A2_09 (first Lyra lewd).
#   - `held_space` vs `reframed_guilt` affects Lyra's warmth in subsequent scenes.
#   - Elisse can be referenced again in Lyra's deep dive or Act III.
#   - "Better when you're here" can echo in later intimate moments.
#   - OB branch should show Lyra more guarded in next interactions.
