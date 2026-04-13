# =======================================================
# ACT 1 - Scene 21: Rooftop Reflection → The Purge
# File: a1_s28_purge.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a1_s28_purge"
$ scene_mark(_current_scene_id, "entered")


label a1_s28_purge:
    $ show_timeline("48th of Forge, 383 A.C.", "19:00", "Aeries — Rooftop")

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Wide static establishing → slow dolly-in → shockwave coverage → slow pull-back on aftermath.
    # LIGHTING: Warm amber → deep blue → BLINDING WHITE → fire glow.
    # SFX LOOP: High rooftop wind @ -12 dB; distant transit; antenna creak.
    # SFX ONE-SHOTS: Door latch; orbital strikes; shockwave; explosions; collapse.
    # BLOCKING: Same rooftop as Kael's jump. Aeron at rail, then with Lyra. Then on knees.
    # FX/COMP: Orbital lances, sector-scale blooms, rolling shockwave, ember fields, smoke columns.

    #scene bg_rooftop_evening with fade

    # ========= SETUP =========

    $ sv = int(player_state.get("civilians_saved", 0))
    $ kv = int(player_state.get("civilians_killed", 0))
    $ em = int(player_state.get("evidence_of_mercy", 0))

    $ saved_vendor = scene_has("a1_s23_the_sweep", "vendor_spared")
    $ saved_child = scene_has("a1_s23_the_sweep", "child_spared")
    $ saved_shelter = scene_has("a1_s23_the_sweep", "shelter_scattered")

    # ========= OPENING — THE ROOFTOP =========
    # VISUAL: Rooftop. Evening light—golden hour fading to dusk. Sectors 8–10 visible on horizon.

    "The rooftop. Same rail. Same wind."

    "Kael's place."

    # BLOCKING: Aeron at rail, not at edge; hands braced. Shoulders tight.

    athought "Two nights ago I came here to disappear."

    athought "Yesterday I killed [kv] people. Saved [sv]."

    athought "Last night Zira put a choice in my hand."

    if sv >= 1:
        athought "This morning I learned the ones I saved were moving others out."
        $ choice_and_dev(_current_scene_id, "purge_recalls_mercy_ripples", "EMP", factor=1,
                        note="Recalls survivors spreading warnings; empathy affirmed.")
    else:
        athought "This morning I stared at reports that said 'zero survivors.'"
        athought "I still don't believe them."

    # CAMERA: Slow dolly-in toward Aeron's back; city field-of-lights deepens.

    "The city wakes below. Lights like stars igniting. Millions of lives humming."

    "Sectors 8, 9, 10 stretch in the distance—dark patches among the glow."

    athought "Something's happening there tonight."

    athought "Marcus wants me to watch."

    athought "I came here first."

    # INSERT: Hands close-up; knuckles blanch; tiny tremor.

    "The rail bites into my palms. Knuckles whitening. A tremor I can't stop."

    athought "These hands killed [kv] people. Saved [sv]."

    athought "I still don't know what that makes me."

    # SFX: Far laughter; a scooter horn; life on some other level.

    "The wind carries city sounds. Distant laughter. Music. Life continuing."

    "For a moment, the world feels almost... okay."

    athought "I don't know what happens next."

    if sv >= 1:
        athought "But I'm not alone. Lyra sees me. The [sv] survived."
    else:
        athought "But I'm not alone. Lyra sees me. Someone may have survived."

    # ========= LYRA ARRIVES =========
    # SFX: Roof door latch clicks; soft footfalls.

    "Footsteps approaching from the rooftop door."

    athought "I don't turn. I know that rhythm."

    a "(quiet) Lyra."

    l "How did you know?"

    a "I always know when you're near."

    # BLOCKING: Lyra stops beside him, close but not touching; both watch horizon.

    l "I came looking for you. You weren't at your apartment."

    a "Needed air. Needed to think."

    l "And?"

    a "(small smile) Still thinking."

    # VISUAL: They stand in comfortable silence. Watching the city together.

    "Silence settles. Not awkward. Just two people existing together."

    l "How are you feeling? After yesterday?"

    a "(honest) Empty. But not the weapon kind."

    l "Good."

    # VISUAL: She looks at him. Studies his profile. Concern and something warmer.

    l "You look different."

    a "Different how?"

    l "Less like a weapon. More like you."

    a "(turns to look at her) Is that a good thing?"

    l "(soft smile) It's the best thing."

    # VISUAL: Their eyes meet. Hold. Connection visible.

    "Something passes between us."

    a "I checked the networks this morning. The resistance chatter."

    if sv >= 1:
        a "The people I saved—they're spreading word. Warning others. Evacuating families."
    else:
        a "Official channels say 'zero survivors.'"
        a "I don't believe it."

    l "It mattered."

    if sv >= 1:
        a "[sv] people alive because something in me cracked."
    else:
        a "And still I can't make the number come out clean."

    l "[kv] dead because I obeyed."

    a "(quiet) I know. The math doesn't work out."

    l "There is no math that works. There's just choices."

    l "You chose something he didn't order."

    # VISUAL: She moves closer. Shoulder almost touching his. Warmth between them.

    a "You came here yesterday too. After the gala. Before everything."

    l "I was worried. I knew something was wrong."

    a "You're always worried about me."

    l "Someone has to be."

    # VISUAL: Small, real smile. First genuine lightness in days.

    a "What would I do without you?"

    l "Let's not find out."

    # VISUAL: Comfortable silence. Both watching the city. Peaceful moment.

    "We stand together. The city hums."

    a "Lyra?"

    l "Yes?"

    a "Thank you. For yesterday. For holding me together when I shattered."

    l "You don't have to thank me."

    a "I do. You saw me at my worst. And you didn't leave."

    l "(turns to face him) I told you. Windows recognize windows."

    l "But we're not windows anymore."

    # BLOCKING: She takes his hand; frame pushes to medium two-shot.

    "Her hand finds mine. Fingers intertwine. Warm. Real. Alive."

    athought "Not a weapon. Not an asset. Just this."

    l "What time is Marcus expecting you?"

    a "2000 hours. Command deck. Observation duty."

    l "That's unusual. He never assigns you observation."

    a "I know. He said to witness 'Project Renewal.' Whatever that is."

    l "(frowns) I don't like the sound of that."

    a "Neither do I. But I don't know what it means."

    # VISUAL: She looks out at Sectors 8-10. Something crosses her face. Unease.

    l "Those sectors have been acting strange. Energy readings. Troop movements."

    a "You noticed too?"

    l "Hard not to. It feels like... preparation."

    a "For what?"

    l "I don't know. But something big."

    # VISUAL: Dread creeping back in. But they push it away. Not yet. Not now.

    a "Let's not think about it. Not right now."

    a "Right now, I just want to stand here. With you. And breathe."

    l "(squeezes his hand) Then that's what we'll do."

    # VISUAL: They turn back to the city. Hands still joined. Watching together.

    "The city glows below us. Unaware."

    a "Do you think we can fix this? Any of it?"

    l "Fix what?"

    a "The system. The city. Us."

    l "(pause) I don't know if we can fix the system."

    l "But us? Maybe. If we try."

    a "Together?"

    l "Together."

    # VISUAL: Small smile on both faces. Tentative. Fragile. Real.

    "Hope, fragile enough to bruise."

    # VISUAL: The sky. Still peaceful. City lights twinkling. Stars beginning to show.

    "The stars appear—faint against city glow, but there."

    l "(quiet) It's beautiful up here."

    a "It is."

    l "Thank you for letting me find you."

    a "Thank you for looking."

    # VISUAL: Time stretches. Peaceful. Connected.

    "Minutes pass. Maybe hours. Time loses meaning."

    "Just two people. One rooftop. One city. One moment."

    # ==========================================
    # THE PURGE BEGINS
    # ==========================================

    # UI: Subtle on-screen clock tick to 19:58

    "19:58. Two minutes until Marcus expects me on command deck."

    a "I should go. Marcus will be waiting."

    l "Do you have to?"

    a "(sighs) He's still my father. Still my commander."

    l "You're not his weapon anymore. You don't have to obey."

    a "I know. But..."

    a "He said to witness history. Part of me needs to see what that means."

    l "Then I'm coming with you."

    a "Lyra—"

    l "I'm not letting you face whatever this is alone."

    a "(quiet) Okay. Together."

    "We turn. Hands still joined. Ready to face whatever comes."

    "20:00. Exactly."

    "A hum builds—low, deep, vibrating through the air."

    l "(stops) What is that?"

    a "I don't—"

    # SFX/CAMERA: Flash; screen whiteout 0.2s; hpunch+vpunch stacked

    "The sky EXPLODES."

    "LIGHT. BLINDING. IMPOSSIBLE."

    "THE SKY TEARS OPEN."

    "SECTORS 8, 9, 10 IGNITE."

    l "(screaming over noise) WHAT IS THAT?!"

    a "(horror dawning) Oh god—"

    "STRIKE. STRIKE. STRIKE."

    "ORBITAL WEAPONS. SURGICAL. DEVASTATING."

    "ENTIRE SECTORS ERASED IN SECONDS."

    "SHOCKWAVE. THE ROOFTOP SHUDDERS."

    "WIND SCREAMS. WE GRAB THE RAIL OR FALL."

    a "(shouting) NO—NO NO NO—"

    l "(horror) THE SECTORS—THE PEOPLE—"

    "BUILDINGS COLLAPSE. ONE. TEN. HUNDREDS."

    "FIRES BLOOM. SMOKE RISES. THE CITY BURNS."

    a "(realization crushing) The energy maintenance—"

    a "The shield generators offline—"

    a "Troop evacuations—"

    a "Civilians locked down—"

    a "(voice breaking) PROJECT RENEWAL—"

    a "IT WAS ALWAYS—"

    a "THEY PLANNED THIS—"

    "MORE STRIKES. THE LIGHT NEVER STOPS."

    "SECTOR AFTER SECTOR. SYSTEMATIC. EFFICIENT. COMPLETE."

    l "(sobbing) HOW MANY—"

    a "(horror) HUNDREDS OF THOUSANDS—"

    l "(screaming) WHY?! WHY WOULD THEY—"

    # ========= SELF-BLAME BRANCHES =========

    if em >= 1:
        athought "[sv] people. I saved [sv]."
        athought "They warned others."
        athought "Marcus heard."
        athought "It should have been later. Not tonight."
        $ canon["aeron_believes_he_accelerated_purge"] = True

        a "(barely audible) I did this."

        l "(can't hear him over noise) WHAT?!"

        a "(louder, breaking) I DID THIS. MY MERCY CAUSED THIS."
    else:
        athought "This was always coming. He wanted me to watch."
        athought "He moved the timeline because he could. Because no one could stop him."

        a "(broken) I couldn't stop it. I couldn't stop anything."

        $ canon["aeron_believes_it_was_inevitable"] = True

    "Knees crack against stone. Hands clawing at my face. Body convulsing."

    if em >= 1:
        a "(screaming) I DID THIS."
        a "TRYING TO SAVE THEM."
        a "AND I DID THIS."
    else:
        a "(screaming) I FAILED THEM. I FAILED THEM ALL."
        a "OBEYING. WATCHING. DOING NOTHING."
        a "AND HUNDREDS OF THOUSANDS DIED."

    l "(crying) IT'S NOT YOUR FAULT—"

    if em >= 1:
        a "YES IT IS. I SHOULD'VE OBEYED. I SHOULD'VE KILLED THEM ALL."
        a "NO SURVIVORS. NO WARNING. NO MERCY."
        a "THEN MARCUS WOULDN'T HAVE KNOWN. WOULDN'T HAVE MOVED THE TIMELINE."
        a "THEY'D HAVE HAD A WEEK. THEY COULD'VE RUN."
    else:
        a "YES IT IS. I LET THIS HAPPEN. I STOOD HERE AND LET IT HAPPEN."

    "THE STRIKES CONTINUE. SECTOR BY SECTOR. BLOCK BY BLOCK."

    "SYSTEMATIC EXTERMINATION. EFFICIENT. PERFECT. COMPLETE."

    if saved_vendor or saved_child or saved_shelter:
        athought "The vendor. The child. The shelter families."
        athought "I dragged them one day further."
    else:
        athought "Faces from yesterday. The market. The doors. The shelter."
        athought "They're dying tonight."

    l "(sobbing) WE HAVE TO DO SOMETHING—"

    a "(hollow) THERE'S NOTHING. IT'S ALREADY DONE."

    a "HUNDREDS OF THOUSANDS. GONE. IN MINUTES."

    # ========= AFTERMATH =========
    # CAMERA: Very slow pull back; the city a wide field of fire.

    "The light fades. The strikes slow. Then stop."

    "Fire remains. Smoke rises. The city burns."

    # Codex — the Purge entry unlocks here, post-cinematic (Notion
    # spec doc 45: "After the cinematic, the entry unlocks; a
    # content warning is displayed.")
    $ codex_mention("purge_8_10", source="a1_s28_purge")

    "{a=codex:purge_8_10}Sectors 8, 9, 10{/a}. Gone. Erased. Cleansed."

    "Silence. Not peace. Just absence."

    "Two people on a rooftop. Holding each other. Broken beyond words."

    a "(whisper) My hands."

    l "Aeron—"

    a "My hands. I can see them. All of them."

    a "[kv] yesterday. [sv] I saved. Hundreds of thousands tonight."

    a "All on my hands."

    l "It's not your fault. Marcus did this. The system did this."

    a "(hollow laugh) The system? I AM the system."

    a "Father's weapon."

    a "(voice breaking) I cracked. And this is what followed."

    "Silence stretches. The city burns. The world has ended."

    "And we sit in the ruins. Together. Shattered. Human."

    athought "Father wanted me to witness this."

    athought "To learn what cracking costs."

    # ========= THE PIVOT =========

    l "(urgent) Aeron. Look at me."

    l "(grabs his face, forces eye contact) LOOK AT ME."

    a "(empty) What?"

    l "Don't let him win. Don't let this break you."

    a "(hollow laugh) I'm already broken."

    l "Then we're broken together. But we don't surrender."

    a "What else is there?"

    l "(fierce) REVENGE. RESISTANCE. DESTROYING THE SYSTEM THAT DID THIS."

    a "(quiet) Revenge."

    l "Yes. They did this. Marcus. The Directorate. Echelon."

    l "They ordered this. They pushed the button. They killed hundreds of thousands."

    l "(fierce) NOT YOU. THEM."

    a "...They did this."

    l "Yes."

    a "Father did this."

    l "Yes."

    a "And he wanted me to watch. To learn. To obey."

    l "Yes."

    a "(cold) Then I'll learn. But not what he wanted."

    "He rises anyway."

    a "I followed orders. I showed mercy. I failed."

    a "So no more kneeling to any of it."

    a "(looks at burning sectors) Just ash. And those who made it."

    l "What do we do?"

    a "We burn them back."

    a "Not today. Not tomorrow. But soon."

    a "We learn. We prepare. We find every crack in the system."

    a "And we shatter it from within."

    "Two silhouettes against the burning sky."

    athought "Operation 391. My last mission as what I was."

    athought "Everything after is something new."

    # ========= KAEL'S PHOTO — THE LAST CHOICE IN THE AERIES =========
    # VISUAL: They're leaving. The apartment is one corridor away. Two seconds. One thing.

    "On the way down, they pass his door. It's still open. The terminal still glowing."

    "Kael's photo on the desk. The tactical kit on the bed."

    menu:
        athought "One thing. I can take one thing."

        "Take the photo.":
            $ record_choice_once(_current_scene_id, "_took_photo",
                note="Carried Kael with him. EMP-coded.")
            $ flag("kael_photo_taken", True)
            $ scene_mark(_current_scene_id, "took_photo")

            "His fingers close around the frame before he thinks about it."

            athought "Kael's face under cracked glass."

        "Take the tactical kit.":
            $ record_choice_once(_current_scene_id, "_took_kit",
                note="Survival gear. OB-coded.")
            $ flag("tactical_kit_taken", True)
            $ scene_mark(_current_scene_id, "took_kit")

            "The kit is heavy and practical and might keep them alive."

        "Take nothing.":
            $ record_choice_once(_current_scene_id, "_took_nothing",
                note="Left everything behind. TP seed.")
            $ tp_seed("a1.purge.leave_everything")
            $ scene_mark(_current_scene_id, "took_nothing")

            athought "Kael isn't in the photo. He's in what I do next."

    "The door closes behind them. The Aeries swallows the room like it was never his."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a1_s28_purge
# cann.when_in_timeline: Evening into 20:00; rooftop reflection immediately before and during orbital strikes.
# cann.what_happened:
#   - Aeron + Lyra share a quiet rooftop reconnection; hope beat just before catastrophe.
#   - 20:00 → Orbital batteries execute purge of Sectors 8–10.
#   - Aeron witnesses mass extermination; self-blame branch depends on prior mercy evidence.
#   - Post-event pivot: declares Operation 391 his last; vows retribution with Lyra.
# cann.aeron_state: Pre-purge: fragile hope → During: shock/helplessness → Post: numb guilt → cold resolve.
# cann.path_tracking:
#   - One conditional nudge: purge_recalls_mercy_ripples (EMP+1 if sv >= 1).
#   - Scene empathy delta: 0 to +1.
#   - Flags: completed.
#   - Canon flags: aeron_believes_he_accelerated_purge | aeron_believes_it_was_inevitable.
# cann.thematic_flags: Hope-before-catastrophe; witness-as-indoctrination; mercy vs consequence; birth of vengeance.
# cann.block_status: KEY SETPIECE (Act I climax) / ANCHOR to Act II motivation.
# cann.visual_plate_economy:
#   - REUSE: Rooftop master (golden hour → dusk → night); skyline plate with Sectors 8–10.
#   - VFX: Orbital lances, sector-scale blooms, rolling shockwave, ember fields, smoke columns.
# cann.requires_followup:
#   - Next: command-deck debrief/confrontation with Marcus OR silent aftermath.
#   - Seed Zira comm follow-up and survivor ambiguity hooks for Act II.
