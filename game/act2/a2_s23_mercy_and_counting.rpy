# =======================================================
# ACT 2 - Scene 23: Mercy and Counting
# File: a2_s23_mercy_and_counting.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_s23_mercy_and_counting"
$ scene_mark(_current_scene_id, "entered")

define torin = Character("Torin")

label a2_s23_mercy_and_counting:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked. Tighter than usual — this scene is claustrophobic by design.
    #         Two-shots of Tessa and Torin. Aeron framed in the doorway, then at the bedside.
    #         NEVER shoot the injection. The camera looks at Tessa's face when it happens.
    # LIGHTING: Surgical overhead on the cot — harsh, too bright. Rest of the medbay in deep shadow.
    #           One amber practical at Tessa's workstation. The board is visible in the background.
    # SFX: Loop — labored breathing (rattling, wet, wrong). IV drip. Generator hum.
    #       One-shots — tray clatter, bandage tear, the breathing stopping (the loudest silence in the game).
    # BLOCKING/PROPS: Medbay at night. One occupied cot under the surgical light. Tessa's board on the wall —
    #                 347 names on the left (her saves), 23 on the right (Aeron's). The "Dead" section doesn't exist yet.
    # FACE: Tessa composed at first — the professional mask. It cracks in stages.
    #        Torin lucid, suffering, certain. Not dramatic. Just done.
    #        Aeron in the doorway: recognition. He's made impossible choices. He knows the shape of this one.

    # ========== NIGHT — MEDBAY, DAY 11 OF 14 ==========

    "The medbay at night is a different place."

    "During the day it hums with triage — minor injuries, training sprains, the constant low-grade damage of 587 people living in a space built for eighty. Routine. Manageable."

    "At night, the failures stay."

    # VISUAL: Single cot under surgical light. Tessa at the bedside. She's been here for hours.
    "Torin Vell. Twenty-two. Joined two weeks ago during the recruitment wave. Enthusiastic. Trainable. Good hands."

    "Sparring accident three days ago. Strike landed wrong. Internal bleeding. Infection despite everything Tessa tried. Sepsis spreading through systems that were already compromised."

    "He's been dying for three days. Tessa's been fighting it for three."

    "Her hands are steady. They're always steady during."

    # ========== THE REQUEST ==========

    torin "(weak) Tessa."

    t "I'm here."

    torin "How long?"

    "She doesn't hesitate. He deserves the truth."

    t "Hours. Maybe until morning. The infection is past what we can treat."

    torin "Hours."

    "He processes that the way soldiers process things — not with denial, but with logistics."

    torin "That's hours of this."

    t "I can manage the pain. Keep you—"

    torin "You've been managing the pain. It's not working."

    "Silence. The IV drips."

    torin "Can you make it faster?"

    "Tessa's hands stop."

    torin "I don't want hours of this. I don't want to feel my body shutting down piece by piece. I want to choose how this ends."

    "Her hands. Still steady. Perfectly still. The stillness of someone holding something so tightly the tremor can't get through."

    torin "Please."

    # ========== AERON ==========

    "Aeron is in the doorway."

    "He didn't come for this. Couldn't sleep — eleven days left on Noelle's countdown, and sleep has become a negotiation he keeps losing. He came for bandage wrap for a training bruise."

    "He heard the silence between Tessa's words and Torin's breathing, and he stopped."

    athought "I know this shape."
    athought "The request. The impossible arithmetic. End suffering, add to the count. Refuse, watch someone die by inches."

    "Tessa sees him."

    "She doesn't tell him to leave."

    t "(barely audible) He's asking me to—"

    a "I heard."

    "Aeron comes to the bedside. Looks at Torin. Not at the sepsis, the sweat, the gray in his skin — at his eyes. Which are clear."

    a "Torin. You're choosing this? Clearly?"

    torin "Clearly. I'm not delirious. I'm not panicking. I'm dying and I'm tired of it taking so long."

    if empathy_band() == "obedience":
        athought "Clear-headed. Consensual. Lucid request for mercy. This isn't ambiguous."
    elif empathy_band() == "empathy":
        athought "He's twenty-two. He joined because he wanted to matter. And this is how it ends."
    else:
        athought "There's no good choice here. Just the one that costs less suffering."

    # ========== THE CRISIS ==========

    t "I count the living."

    "She says it like a diagnosis. Like she's reading her own chart."

    t "That's what I do. I save people. I make the number go up. If I do this — the number goes down. My hand makes it go down."

    torin "Keeping me alive for hours of agony isn't counting the living. It's counting the suffering."

    "The sentence lands in Tessa's chest like a physical thing."

    "Her hands. The same hands that held the clamp in The Patient's medbay. That didn't shake when a runner's life hung on twelve percent."

    "They're shaking now."

    a "Tessa."

    "She looks at him."

    a "This isn't failing to save. This is honoring a choice."

    t "You don't know that. You can't know—"

    a "I know what it looks like when someone has decided. I've seen it in 391 faces."

    "The number stops her."

    a "He's not asking you to give up. He's asking you to let go. There's a difference."

    # ========== THE MERCY ==========

    "Tessa stands for a long time."

    "Then she moves."

    "The morphine is in the lockbox. She's the only one with the code. Her fingers find it without looking — muscle memory from a thousand legitimate doses."

    "This dose isn't legitimate. This dose is mercy."

    t "Torin. This will be fast. You'll feel warm, then sleepy, then nothing."

    torin "(small smile) Thank you. For trying. For three days of trying."

    t "I'm sorry I couldn't—"

    torin "You couldn't. That's not failure. That's just the math."

    "She administers the injection."

    # VISUAL: Camera on Tessa's face. Not on the needle. Not on Torin.
    # On her face as the breathing beside her changes, slows, and stops.

    "The breathing changes."

    "Slows."

    "Stops."

    pause 1.5

    "The silence is the loudest thing in the building."

    # ========== THE BREAK ==========

    "Her hands start shaking."

    "Not the way they shook after The Patient — that was exhaustion, adrenaline bleeding off, the tremor of something held too tight for too long."

    "This is different."

    "This is her hands realizing what they just did."

    # VISUAL: Tessa on the floor. Not falling — folding. Like something structural gave way.
    "She sits on the floor beside the cot. Not dramatically — she just stops being able to stand."

    t "(quiet, broken) I killed him."

    t "I'm a healer and I killed him."

    "Aeron sits beside her. On the floor. Not touching — just present."

    "Minutes pass."

    t "My board has 370 names on it. Living. Saved. Counted."
    t "Now I need a new section."

    a "For what?"

    t "The dead. The ones I couldn't save. The ones who asked me to stop trying."

    "She looks at her hands."

    t "Torin goes there. First name."

    if empathy_band() == "obedience":
        a "When the raid comes, that section gets longer. You need to be ready for that."
        t "I know."
        a "Can you be?"
        t "I don't know. But I'll be here. That's all I can promise."
    elif empathy_band() == "empathy":
        a "He's counted. Living or dead — he's counted. That's what matters."
        t "Is it enough?"
        a "It has to be. Because the alternative is not counting at all."
    else:
        a "First name on that side of the board. Not the last."
        t "No. Not the last."
        a "You'll carry them all?"
        t "I'll carry them all."

    # ========== THE BOARD ==========

    "She stands. Slowly. The hands still shaking."

    "She walks to the board."

    "347 names on the left. Hers. 23 on the right. Aeron's. 370 total. The living."

    "She takes a marker. Draws a line beneath them."

    "Below the line, in smaller writing:"

    "THE DEAD"

    "And beneath that, the first name."

    "Torin Vell. 22. Mercy."

    "She puts the marker down."

    "Looks at the board."

    "370 living. 1 dead."

    t "(to herself) Both sides count."

    # ========== SCENE CLOSE ==========

    "Aeron stays until Tessa tells him to go."

    "She doesn't tell him to go."

    "Eventually, dawn leaks in through the ventilation slats, and the medbay becomes a daytime place again — routine, manageable, full of minor injuries and training sprains."

    "Tessa is at her station when the first patient arrives. Hands steady."

    "The board behind her has a new section."

    "Nobody asks about it."

    "Nobody needs to."

    # ========== STATE UPDATES ==========

    $ npc_remember("Tessa", "mercy_death_torin", tone="broken_but_standing")
    $ npc_remember("Aeron", "witnessed_mercy_death", tone="heavy")
    $ rel_bump("Tessa", trust=2)
    $ flag("mercy_death_delivered", True)
    $ canon_set("tessa_board_has_dead", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a2_s23_mercy_and_counting
# cann.chapter: Act II, Chapter IV — The Cost
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Day 11 of 14-day countdown. Night. Three days after massive recruitment.
# cann.what_happened:
#   - Torin Vell (22, recruited during wave) dying of sepsis from training accident. Three days of Tessa fighting it.
#   - Torin requests mercy death — lucid, consensual, clear. "I want to choose how this ends."
#   - Aeron arrives, witnesses. Supports Tessa: "This isn't failing to save. This is honoring a choice."
#   - Tessa administers lethal morphine dose. Torin dies peacefully.
#   - Tessa breaks: "I'm a healer and I killed him."
#   - Board updated: new section — THE DEAD. Torin Vell first name. "Both sides count."
#   - Dawn arrives. Hands steady again. Nobody asks about the new section.
# cann.aeron_state:
#   - Witness and support, not decision-maker. This is Tessa's scene.
#   - "I know what it looks like when someone has decided. I've seen it in 391 faces."
#   - EMP: "He's counted. Living or dead — he's counted."
#   - OB: "When the raid comes, that section gets longer. You need to be ready."
# cann.path_tracking:
#   - No player choice — this is a witnessed event, not a decision scene.
#   - trust +2 for Tessa (shared impossible moment).
#   - flag("mercy_death_delivered") for future gating.
#   - canon_set("tessa_board_has_dead") for board state tracking.
# cann.thematic_flags:
#   - "Count the Living" evolves to "Both sides count." Philosophy tested and expanded.
#   - Torin's line: "Keeping me alive for hours of agony isn't counting the living. It's counting the suffering."
#   - Tessa's hands callback from The Patient: steady during crisis, shaking after.
#     Here the shaking means something different — not exhaustion but recognition of what they did.
#   - The board gaining its dead section is the scene's physical transformation moment.
#   - "Nobody asks about it. Nobody needs to." — the community absorbs grief without being told to.
#   - Camera never shows the injection. Shows Tessa's face. The mercy is in the person, not the act.
# cann.character_moments:
#   - Tessa: Breaks completely, then stands back up. "Broken but standing" — the tone of everything she is.
#     Professional mask returns by dawn. Hands steady again. But the board has a new section.
#   - Torin: Lucid, certain, gracious. "You couldn't. That's not failure. That's just the math."
#     Small smile before the injection. Dignity in choosing.
#   - Aeron: Stays until Tessa tells him to go. She doesn't tell him to go.
#     "391 faces" — his past as credential for recognizing when someone has decided.
# cann.block_status:
#   - ANCHOR (both paths). Tessa's philosophy-defining scene.
# cann.requires_followup:
#   - Tessa's board now has two sections — referenced in all future medbay scenes.
#   - "Both sides count" becomes her operational philosophy for the raid and beyond.
#   - The raid (a2_s25) will add many names to the dead section. Torin was first. Not last.
#   - flag("mercy_death_delivered") gates Tessa's willingness to make battlefield mercy calls in Act 3.
#   - Hands shaking → hands steady by dawn. The cycle of composure recurs under greater pressure.
