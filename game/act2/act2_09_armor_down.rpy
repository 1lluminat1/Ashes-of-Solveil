# =======================================================
# ACT 2 - Scene 9: Armor Down
# File: act2_09_armor_down.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_09_armor_down"
$ scene_mark(_current_scene_id, "entered")

label act2_09_armor_down:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Intimate 50mm+; shallow depth of field. Slow movements, no quick cuts. Hold on faces during vulnerable moments. Two-shots that emphasize closeness.
    # LIGHTING: Low amber from a single safehouse bulb. Cold blue from the barred window—moonlight or distant neon. Skin tones warm against cool shadows.
    # SFX: Loop — muted Unders hum (softer than usual), their breathing. One-shots — fabric shift, skin contact, the pendant chain.
    # FX/COMP: Dust motes in the amber light. Lyra's eyes catch the light when she looks at him. Her Band visible, dormant.
    # BLOCKING/PROPS: Safehouse interior, single bedroll (or two pushed together), Lyra's pendant, minimal props—focus on the characters.
    # FACE: Lyra oscillates between vulnerability and need. Aeron uncertain but present. Both learning how to be unarmored.

    # ========== SCENE GATE CHECK ==========
    # This scene has two major branches:
    # 1. INTIMATE PATH: If intimacy_seed_planted (EMP choice in A2_07) - full intimate scene
    # 2. GUARDED PATH: If not - emotional closeness but physical boundary respected

    if not scene_has("act2_07_quiet_night", "intimacy_seed_planted"):
        jump act2_09_guarded_path

    # ========== INTIMATE PATH — SAFEHOUSE, NIGHT ==========

    athought "Night falls different in the Unders. No sunset—just the lights dimming in waves as the upper tiers cycle down."

    athought "Zira left hours ago. Something about checking a node in Sector 7, making sure the seventy-two hour window doesn't close early."

    athought "Just the two of us now. The safehouse feels smaller."

    # VISUAL: Lyra sitting on her bedroll, back against the wall. She's holding the pendant again.
    athought "Lyra's been quiet since the analyst's call."
    athought "Not the cold quiet from before. Something else. Thinking quiet."

    "The pendant rests in her palm."

    l "She knew about your father."

    a "Everyone knows about Marcus."

    l "Not that. The way she talked about him. 'Behavioral patterns.' 'Not proportional to a simple defection.'"
    l "She knows him like data. But you know him like..."

    "She trails off. Doesn't finish."

    a "Like a son."

    l "(quiet) Like a wound."

    if empathy_band() == "obedience":
        athought "She's not wrong. Marcus isn't just a tactical problem. He's the shape of every failure I've ever felt."
    else:
        athought "She sees it. The part I try to keep buried."
        athought "She's not flinching from it."

    "He moves closer. Sits beside her, like last night. Shoulder to shoulder."

    "For a moment, neither of them speaks."

    "She's holding the pendant again."

    athought "She's not thinking about the analyst or the seventy-two hours. I can tell by the way she's holding it."

    l "I keep waiting for something to make sense."
    l "The Purge. The running. Us."

    a "Does it need to make sense?"

    l "It used to. The Order taught me everything had a pattern. A purpose."
    l "Now I'm not sure anything does."

    "She reaches out. Her hand finds his."

    l "Except maybe this."

    a "Lyra—"

    l "I signed a false report to preserve a lie. I watched them seal my mentor's memory in glass and called it sanctified."
    l "If that's not broken, nothing is."
    l "But you sat with me anyway. You didn't try to fix me or explain me away."
    l "You just... stayed."

    "Her eyes find his. The light catches the amber in them—warm against the cold blue from the window."

    l "I've never had anyone stay before."

    athought "She's opening a door. The question is whether I walk through."

    # --- PLAYER CHOICE: How does Aeron respond to her vulnerability? ---
    menu:
        "She's offering something fragile. How does he receive it?"

        "Close the distance—let this become what it's becoming.":
            $ record_choice_once(
                _current_scene_id, "_close_distance",
                note="Aeron chooses to pursue intimacy with Lyra. Consent affirmed."
            )
            $ scene_mark(_current_scene_id, "intimacy_chosen")

            athought "I don't think about it. Just act."

            "My hand comes up to her face. Gentle."

            athought "The way you touch something you're afraid might disappear."

            a "I'm not going anywhere."

            l "(barely a whisper) Promise?"

            a "No. Promises are cheap."
            a "I'm just telling you."

            "She laughs."

            athought "Her laugh is small and broken, but somehow beautiful because of it."

            l "You remembered."

            a "I remember everything you say."

            athought "The distance between us closes. Inches becoming nothing."

            athought "I can feel her breath. The faint tremor in her fingers where they grip my hand."

            l "Aeron."

            a "Yeah?"

            l "I don't know how to do this. Any of it."
            l "The Order taught me stillness. Echelon taught me duty."
            l "No one ever taught me how to want something for myself."

            a "Then we figure it out together."

            "She nods."

            athought "She looks small and scared, but there's certainty in her eyes that wasn't there before."

            "And then her lips find his."

            jump act2_09_intimate_scene

        "Hold back—this isn't the right time.":
            $ record_choice_once(
                _current_scene_id, "_hold_back",
                note="Aeron chooses to hold back from intimacy despite the opening."
            )
            $ scene_mark(_current_scene_id, "intimacy_delayed")

            athought "I want to close the distance. Every part of me is screaming to move."
            athought "But something stops me."

            a "Lyra..."

            l "(reading his hesitation) It's okay. You don't have to."

            a "It's not that I don't want to. It's that I want it to mean something."
            a "We're running on seventy-two hours and adrenaline. I don't want this to be something we do because we might die tomorrow."

            "She's quiet for a moment."

            athought "Processing."

            l "That's... actually thoughtful."

            a "Don't sound so surprised."

            l "(small smile) I'm not. I just... didn't expect you to be the one to slow down."

            "She squeezes my hand."

            l "Okay. We wait."
            l "But Aeron?"

            a "Yeah?"

            l "Don't wait too long. We might not get another chance."

            "She leans into me. Head on my shoulder."

            athought "We stay like that until sleep comes."

            jump act2_09_scene_close


# ========== INTIMATE SCENE ==========
label act2_09_intimate_scene:

    # NOTE: This scene is written to be sensual and meaningful without being gratuitous.
    # Focus on emotional truth, vulnerability, and connection.
    # Physical details serve character development, not titillation.

    athought "The kiss starts tentative. Two people who've forgotten how to be soft, trying to remember."

    "Her hand comes up to my chest."

    athought "Not pushing, not pulling. Just feeling. The heartbeat underneath."

    l "(breaking the kiss, breathless) Your heart's racing."

    a "So is yours."

    l "I didn't think I could still feel this."

    "She pulls back just enough to look at me. The pendant hangs between us, catching the amber light."

    l "This cracked piece of glass is the only thing I brought from the Order."
    l "It's supposed to remind me of faith. Of what I owe."
    l "But right now, looking at you, I can't remember why I was carrying it."

    "She lifts the chain over her head. Sets the pendant aside."

    l "Tonight, I don't want to be the person who signed that report."
    l "I just want to be here. With you."

    athought "She's taking off her armor. Not just the pendant—everything she's been carrying."
    athought "I can do the same. I can try."

    a "I've never been good at this. Being... present."
    a "Glass doesn't feel things. Glass observes. Processes. Reports."

    l "Then stop being Glass."

    a "I don't know if I know how."

    "She kisses him again. Slower this time. Deliberate."

    l "(against his lips) Then let me show you."

    # --- FADE TO INTIMATE CONTENT ---
    # VISUAL: Transition from kiss to implied intimacy. Tasteful, emotional, focused on connection.
    # LIGHTING: Amber glow, bodies in silhouette, focus on faces and hands.
    # SOUND: Breathing, fabric, soft whispers.

    athought "What follows is clumsy and careful in equal measure."

    athought "Hands that have only known weapons learning gentleness."
    athought "Lips that have only spoken orders finding new words."

    "Her hand finds his wrist and pulls gently. The bedroll is thin beneath them."

    athought "Not falling—following."

    "There's a moment where they both pause. Eyes meeting in the low light."

    l "Are you okay?"

    a "I should be asking you that."

    l "I asked first."

    a "(honest) I don't know what I am right now. But I know I want to be here."

    l "That's enough."

    athought "And it is. Somehow, impossibly, it is."

    # --- IMPLIED INTIMACY ---
    # Focus on emotional beats, not explicit physical description.

    athought "She moves with the precision the Order taught her, but there's something else now—spontaneity, need, life."
    athought "I let go of the control I've always clung to. Let her lead. Let myself follow."

    "At some point, the pendant falls from the crate where she left it."

    athought "The Unders hums its wrong song outside. Inside, we find a rhythm that's just for us."

    "When it's over, they lie tangled together, breathing hard, the sweat cooling on their skin."

    # --- POST-INTIMACY ---
    "Lyra's head rests on his chest. Her finger traces the scar tissue from the Brand—the mark that didn't take."

    l "(quiet) Does it still hurt?"

    a "Sometimes. When I forget it's there."

    l "I don't think I'll ever forget."

    a "The scar?"

    l "You. This."
    l "Whatever happens tomorrow, I want to remember that we had this."

    "He pulls her closer. A gesture that would have felt impossible a week ago."

    a "I used to think intimacy was weakness. An exploitable vulnerability."

    l "And now?"

    a "Now I think maybe I had it backwards."
    a "Maybe being vulnerable is the only thing that proves you're still human."

    "She tilts her head up and kisses the underside of his jaw, soft and almost reverent."

    l "Elisse would have liked you."

    a "You said that before."

    l "I know. But now I mean it differently."
    l "Before, it was because you don't sound like a prayer."
    l "Now, it's because you feel like one."

    "He doesn't know what to say to that. So he just holds her."

    "Outside, the Unders keeps turning. Echelon keeps hunting. Marcus keeps waiting."

    "But here, in this small concrete room, none of that matters."

    "There's only this: two broken people, finding something whole in each other."

    $ flag_on("Lyra", "first_intimacy_complete")
    $ rel_bump("Lyra", trust=2, affection=2)
    $ npc_remember("Lyra", "shared_first_intimacy", tone="tender")

    jump act2_09_scene_close


# ========== GUARDED PATH — FOR PLAYERS WHO DIDN'T PLANT THE SEED ==========
label act2_09_guarded_path:

    "Night falls different in the Unders. No sunset—just the lights dimming in waves as the upper tiers cycle down."

    "Zira left hours ago. Something about checking a node in Sector 7."

    "Just the two of them now. The silence from last night still hangs between them."

    # VISUAL: Lyra on her bedroll, turned away. Aeron on his, watching the ceiling.
    "Lyra's on her side, facing the wall. Not asleep—he can tell by her breathing—but not talking either."

    athought "The distance between us feels like more than meters."

    athought "I said the wrong thing last night. Tried to make her guilt useful instead of just... holding it."
    athought "Now there's a wall where there used to be a door."

    athought "I think about saying something. Apologizing. Explaining."

    athought "But what would I say? 'Sorry I treat everything like a tactical problem'?"

    athought "It's true, but it's not helpful."

    l "(without turning) The analyst called you an anomaly."

    a "She did."

    l "Do you feel like one?"

    a "I feel like someone who's made a lot of mistakes."

    "Silence. Then she rolls over. Faces him across the gap."

    l "Last night, when you said guilt is a resource..."

    a "I shouldn't have said it that way."

    l "No. You shouldn't have."
    l "But I've been thinking about it all day, and... you're not entirely wrong."

    "That wasn't what he expected."

    a "What do you mean?"

    l "I signed that report because I was afraid. Of the Order. Of losing my place."
    l "But now, knowing what I know—about Marcus, about the Purge, about what we were really doing..."
    l "Maybe the guilt isn't just weight. Maybe it's fuel."

    if empathy_band() == "obedience":
        athought "She took what I said and found her own meaning in it."
        athought "That's more than I gave her credit for."
    else:
        athought "She's trying to meet me halfway. Even after I hurt her."
        athought "That's more than I deserve."

    a "I'm sorry. For last night."
    a "I'm not good at... being there without solving something."

    l "I know."
    l "But you're trying. That's something."

    "She doesn't cross the gap. Neither does he."

    athought "But the wall feels thinner than before."

    l "Get some sleep, Aeron. Seventy-two hours, remember?"

    a "You too."

    "She rolls back over. This time, her breathing really does even out."

    "He lies awake a while longer, thinking about walls and doors and the space between."

    athought "Maybe next time. If there is a next time."
    athought "Maybe I can learn to just be present."
    athought "Maybe she'll give me another chance."

    $ flag_on("Lyra", "intimacy_delayed_wall_present")
    $ rel_bump("Lyra", trust=1)
    $ npc_remember("Lyra", "aeron_apologized_morning_after", tone="softening")

    jump act2_09_scene_close


# ========== SCENE CLOSE ==========
label act2_09_scene_close:

    # Final beat before scene wraps

    if scene_has(_current_scene_id, "intimacy_chosen"):
        "Morning finds them still tangled together. The first real sleep either of them has had in days."

        "Somewhere outside, the seventy-two hour clock keeps ticking."

        "But for one night, they were just two people in a room."

        "That has to count for something."

    elif scene_has(_current_scene_id, "intimacy_delayed"):
        "Morning comes cold and gray through the barred window."

        "She's still against his shoulder, the warmth between them real even if they didn't cross the line."

        "There will be time. He has to believe there will be time."

    else:
        "Morning comes cold and gray."

        "The gap between their bedrolls feels smaller than it did last night. Not gone. But smaller."

        "Progress. Maybe."

    # --- SCENE WRAP ---
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_09_armor_down
# cann.chapter: Act II, Chapter II — Constellation
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Night of Day 4, after Noelle call (A2_08). Zira is out checking nodes.
# cann.what_happened:
#   - INTIMATE PATH (if intimacy_seed_planted from A2_07):
#       • Lyra and Aeron sit together, processing the weight of recent events.
#       • She's searching for meaning—"I keep waiting for something to make sense."
#       • She redirects to what matters: "Except maybe this."
#       • She opens up about not knowing how to want things for herself.
#       • Player choice: close distance or hold back.
#       • If close distance: First intimate scene. Emotional, focused on vulnerability and connection.
#       • The pendant comes off—symbolic removal of her Order armor.
#       • Post-intimacy: She traces his Brand scar. "You feel like a prayer."
#   - GUARDED PATH (if no seed planted):
#       • Distance from A2_07 still present. Lyra initially won't talk.
#       • She eventually engages—reframes his "guilt as resource" comment.
#       • Aeron apologizes for last night. Wall thins but doesn't break.
#       • No physical intimacy, but emotional progress made.
# cann.aeron_state:
#   - INTIMATE PATH: Learning to be vulnerable, to let go of Glass.
#   - GUARDED PATH: Recognizing his failure to be present, trying to repair.
# cann.path_tracking:
#   - Gate: scene_has("act2_07_quiet_night", "intimacy_seed_planted")
#   - INTIMATE PATH flags:
#       • `first_intimacy_complete` (Lyra flag)
#       • `intimacy_chosen` or `intimacy_delayed` (scene flags)
#       • trust +2, affection +2 if intimacy_chosen
#   - GUARDED PATH flags:
#       • `intimacy_delayed_wall_present` (Lyra flag)
#       • trust +1 (from apology)
#   - NPC memories stored via `npc_remember()`.
#   - Running empathy range at scene end: -13 to +3 (no empathy choices, just consequence)
# cann.thematic_flags:
#   - Motifs: Armor as protection/prison, the pendant as faith removed, Brand scar as failed control.
#   - "You feel like a prayer" — Lyra finding divinity in connection, not machines.
#   - "Maybe being vulnerable is the only thing that proves you're still human."
#   - The intimate scene advances character truth: armor off, wounds revealed, choice to be present.
# cann.character_moments:
#   - Lyra: Takes off the pendant for the first time. Admits she doesn't know how to want things.
#   - The "stop being Glass" line is her direct challenge to his persona.
#   - Post-intimacy tenderness: tracing the Brand, reverent kiss on jaw.
#   - GUARDED PATH: She reframes his words rather than staying angry—shows her growth.
# cann.intimacy_notes:
#   - Scene is sensual but not explicit. Focus on emotional beats over physical description.
#   - Consent is explicit: "Are you okay?" / "I asked first."
#   - Physical vulnerability paralleled with emotional vulnerability.
#   - The pendant being set aside = symbolic armor removal.
# cann.block_status:
#   - First Lyra lewd complete (INTIMATE PATH) or deferred (GUARDED/DELAYED PATH).
#   - Regardless of path, relationship has progressed.
# cann.requires_followup:
#   - INTIMATE PATH: Lyra's warmth should be notably different in subsequent scenes.
#   - GUARDED PATH: Lyra is softening but still guarded—potential for later intimacy.
#   - The pendant should reappear in later scenes—does she put it back on?
#   - Brand scar mentioned again in Lyra's deep dive or Verdant revelations.
#   - "You feel like a prayer" can echo in Act III faith resolution.
