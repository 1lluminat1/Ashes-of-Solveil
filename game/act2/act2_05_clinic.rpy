# =======================================================
# ACT 2 - Scene 5: The Clinic
# File: act2_05_clinic.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_05_clinic"
$ scene_mark(_current_scene_id, "entered")

define jace = Character("Jace")

label act2_05_clinic:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 28–35mm, handheld but steadier than yard; push-ins on Tessa during philosophy beats and when she's reading Aeron.
    # LIGHTING: Sickly overhead strips mixed with warm amber/green practicals around Tessa's workspace. Shadows in corners. Cots lit unevenly.
    # SFX: Loop — low murmurs, occasional groans, soft beeps from hacked monitors, clink of metal trays. One-shots — door hiss, basin water, bandage tear.
    # FX/COMP: Faint steam/humidity from boiled water. Dust motes in the amber light pools.
    # BLOCKING/PROPS: Narrow approach corridor, metal door with painted symbol, cots along walls, cloth curtain dividers, IV bags on pipes, scavenged metal braces, basin with bloody water, threadbare towels, lockbox for supplies.
    # FACE: Tessa reads calm but watchful; fatigue around her eyes but hands always steady. Aeron carrying weight from the yard. Lyra uncertain but attentive.

    # ========== CHAPTER TITLE CARD ==========
    scene black with fade
    centered "{size=+20}ACT II{/size}"
    pause 0.5
    centered "{size=+10}Chapter II — Constellation{/size}"
    pause 2.0
    scene black with fade

    # ========== APPROACH TO THE CLINIC ==========

    athought "Evening settles over the Unders like a held breath."

    "The market noise fades behind them as Zira leads them down a corridor narrower than the rest."

    # VISUAL: Tight corridor, metal walls stained with oil and time. Cables bundled overhead.
    "Pipes sweat condensation. The walls are close enough to touch on both sides."

    if empathy_band() == "obedience":
        athought "Chokepoint. No room to maneuver. Bad place for an ambush, worse for escaping one."
    elif empathy_band() == "empathy":
        athought "People live in spaces like this. Raise kids. Try to build something in the cracks."
    else:
        athought "Tight and claustrophobic. The Unders keep shrinking the further in we go."

    "Zira moves without hesitation."

    athought "Her path automatic. She's walked this route a thousand times."

    z "Underground clinic. Don't call it that where anyone can hear you."
    z "Down here it's just 'Tessa's.' Everyone knows what that means."

    # VISUAL: Metal door with hand-painted symbol — faded green cross inside an amber circle.
    "A metal door ahead, marked with a faded symbol—a green cross inside a hand-painted amber circle."

    "The paint is old. Chipped at the edges."

    athought "But someone keeps touching it up."

    if scene_has("act2_04_first_day_out", "helped_injured_worker"):
        athought "The crate, the scream, the weight in my hands as we lifted."
        if empathy_band() == "obedience":
            athought "I moved on instinct. Still not sure if that was tactical or something else."
        else:
            athought "It comes back faster than I want it to. The sound he made when we got it off him."
    else:
        athought "The scream from the line. I never saw how it ended."
        if empathy_band() == "obedience":
            athought "The belt kept moving. So did I. That's how you survive."
        else:
            athought "Just kept my hands on the belt and let someone else handle it. The math made sense. It still doesn't sit right."

    l "(low) Are we patients or problems?"

    z "Today? Neither."
    z "Today you're the rare idiots who walked into Tessa's on purpose."
    z "That already makes you interesting."

    "Zira knocks twice, then pushes the door open without waiting for an answer."

    # ========== INTERIOR — FIRST LOOK ==========

    # VISUAL: Clinic interior. Low ceiling, cots along walls, cloth curtains making half-hearted rooms. Amber light over central workspace.
    athought "The air hits different—boiled water, cheap antiseptic, sweat, and something metallic underneath."

    "Cots line the walls, some occupied, others stained."

    athought "Stained with the memory of whoever bled on them last."

    if empathy_band() == "obedience":
        athought "Triage setup. Limited resources, maximum efficiency. She's running this like a field hospital."
    elif empathy_band() == "empathy":
        athought "Every cot is a person. Every stain is someone who bled here and maybe walked out, maybe didn't."
    else:
        athought "It's not much. But it's more than nothing, and down here that counts."

    "Murmurs of pain and whispered conversation fill the space."

    athought "Less a hospital than a place where the city's wreckage washes up."

    # VISUAL: Tessa, back to camera, working on a leg immobilized in a scavenged metal brace. Amber work light clipped to a pipe above her.
    "At the center of the room, a woman works over a cot, her back to the door."

    "Amber light catches her hair and the white of fresh bandages as she tightens a metal brace around a man's leg."

    jace "(hissing) That's—that's tight."

    t "Tight means the bone stays where it belongs."
    t "Stop falling under machinery and we won't have to do this again."

    # VISUAL: Tessa wipes her hands on a threadbare cloth, turns to face them. Reads the room in one sweep.
    "The cloth in her hands might have been white once. She turns, and her eyes sweep the room in a single motion."

    athought "Her eyes move across Zira first—familiar—then to Aeron and Lyra, reading posture, clothes, the way we hold ourselves."

    $ encounter_inc("Tessa")

    # Tessa's read of Aeron varies by his current state
    if pass_tier("OB2", "OB3"):
        athought "Her gaze lingers on me a moment longer. Something in my posture, maybe. The way I scanned the room before I looked at her."
    elif pass_tier("EMP2", "EMP3"):
        athought "Her gaze lingers on me a moment longer. I'm looking at the cots, not the exits. She notices."
    else:
        athought "Her gaze lingers on me a moment longer. Whatever she's reading, she keeps it to herself."

    t "Friends of yours?"

    z "Depends who's asking."

    t "The person who just spent an hour making sure your yard friend keeps his leg."

    "Her eyes settle on Aeron and Lyra. The silence stretches."

    t "So. Are you trouble, or are you useful?"

    # ========== YARD CHOICE PAYOFF ==========

    if scene_has("act2_04_first_day_out", "helped_injured_worker"):
        # --- BRANCH A: Aeron helped the worker ---

        # VISUAL: Jace squints through pain, recognizes Aeron.
        "The man on the cot shifts, squinting through whatever pain and sedation Tessa's given him."

        jace "(hoarse) Hey... I know you."
        jace "You're the one from the line. Pulled the crate off me."

        if empathy_band() == "obedience":
            a "You weren't getting out alone. Someone had to move."
        elif empathy_band() == "empathy":
            a "I couldn't just watch. You weren't getting out alone."
        else:
            a "You weren't getting out alone."

        jace "(to Tessa) He's the reason you had a leg to work with at all."

        t "(to Aeron) That true?"

        if empathy_band() == "obedience":
            a "There were others. I assessed the situation and acted."
        else:
            a "There were others. I didn't do it alone."

        t "Most people don't even start."
        t "Good to know you're not 'most people.'"

        $ npc_remember("Tessa", "heard_aeron_helped_jace", tone="cautious_respect")
        $ npc_remember("jace", "saved_by_aeron", tone="grateful")

    else:
        # --- BRANCH B: Aeron stayed on the line ---

        # VISUAL: Jace is half-conscious, not tracking them.
        "The man on the cot doesn't look up. His eyes are glassy, unfocused."

        athought "Wherever his mind is, it's not in this room."

        t "(to Zira) These two from the yard?"

        z "Line B and parts run. First shift."

        t "(to Aeron) You were on the belt when this happened?"

        if empathy_band() == "obedience":
            a "I was. The line needed to keep moving."
        else:
            a "Yeah. I was."

        t "Foreman Rusk says the line never backed up at your station."
        t "So either you have excellent reflexes, or you're very good at looking straight ahead."

        if empathy_band() == "obedience":
            athought "She's probing. Testing. I've done the same thing in interrogations."
            athought "Her calm is more effective than the foreman's bark. She knows it, too."
        elif empathy_band() == "empathy":
            athought "It hurts more than any shouting would."
            athought "Because she's not angry. She's just disappointed, and she doesn't even know me yet."
        else:
            athought "She's not accusing. She's just... seeing."
            athought "Somehow that's worse."

        $ npc_remember("Tessa", "knows_aeron_stayed_on_line", tone="assessing")

    # ========== NAMES & IDENTITY ==========

    t "Names?"

    z "Kade Voss and Mira Chen. Sector 6 yard."

    t "I asked them."

    "She's looking at Aeron. Not Zira."

    if empathy_band() == "obedience":
        # He delivers the cover name cleanly, like a soldier giving a report
        a "Kade. Kade Voss."

        athought "The name comes out flat and professional—a tool, not an identity."
    elif empathy_band() == "empathy":
        # There's hesitation, the weight of the lie
        a "...Kade. Kade Voss."

        athought "The name feels strange in my mouth. Like wearing someone else's skin."
    else:
        a "...Kade. Kade Voss."

    l "Mira. Mira Chen."

    "Tessa holds my gaze."

    athought "A beat, then two."

    if pass_tier("OB2", "OB3"):
        athought "Neither of us looks away. Not a challenge. Just two people who know how to hold a stare."
    elif pass_tier("EMP2", "EMP3"):
        athought "I don't look away. But something in me wants to. She's not buying the name entirely, and we both know it."
    else:
        athought "I hold it. Barely."

    athought "Then something in her shoulders eases, just slightly."

    t "Alright, Kade. Mira."
    t "Zira says you're going to be around for a while. If that's true, you need to understand something."

    # VISUAL: Tessa gestures around the clinic — the cots, the makeshift equipment, the bodies in various states of damage.
    "Her hand sweeps the room—cots along the walls, bodies in various states of damage, salvaged equipment humming to keep them alive."

    t "This is where the Unders come when the city chews them up."
    t "Falls. Fights. Patrols. Collapses. Everything ends up here eventually."
    t "I don't care who started it or who won. I care who's bleeding."

    l "You do all this alone?"

    t "Mostly. I've got a couple runners. A guy who can handle an IV if he's sober."
    t "Which is about half the time, so I don't plan around it."

    if scene_has("act2_04_first_day_out", "helped_injured_worker"):
        t "(glances at Jace) He says you didn't hesitate. That's not nothing."

        if empathy_band() == "obedience":
            athought "Didn't hesitate. She makes it sound like a character trait. It was just faster than thinking."
        else:
            athought "Didn't hesitate. I'm not sure that's true. It just happened before hesitation could catch up."

    else:
        t "(glances at Jace) He won't remember much. Just that the belt didn't stop."
        t "Sometimes that's survival. Sometimes it's just fear wearing a practical mask."

        if empathy_band() == "obedience":
            athought "Fear. She's wrong about that. It was calculation. Clean. Practical."
            athought "So why does it feel like she's right?"
        else:
            athought "Fear wearing a practical mask—she just described half my life in seven words."

    z "They're looking for ways to be less hated."

    t "Down here, the people on these cots remember everything."
    t "Who pulled them out. Who walked past. Who paid scrip or time so a stranger got another day."
    t "That's the only currency that actually matters. Everything else is just noise."

    # ========== THE CORE CHOICE ==========

    # VISUAL: Tessa watches Aeron, waiting. Reading.
    "The weight of her attention settles over me."

    athought "Patient. Waiting to see what kind of man walks out of the answer."

    if pass_tier("OB2", "OB3"):
        athought "She's good at this. Reading people. I've done the same thing from the other side of the table."
        athought "The question is what answer she wants to hear—and whether that's the answer I should give."
    elif pass_tier("EMP2", "EMP3"):
        athought "She's not judging. Not yet. Just... listening."
        athought "When was the last time someone actually listened?"
    else:
        athought "She's waiting. The silence stretches, and I have to fill it with something."

    menu:
        athought "She's asking without asking. Why are you really here?"

        "Be honest about the guilt.":
            $ choice_and_dev(
                _current_scene_id, "_tessa_clinic_own_guilt", "EMP", factor=1,
                note="Aeron admits past harm and offers genuine help rather than reputation management."
            )
            $ npc_remember("Tessa", "aeron_admitted_guilt", tone="cautious_respect")
            $ scene_mark(_current_scene_id, "first_impression_soft")

            a "I've spent years being the reason places like this stay full."

            athought "The words come out before I can stop them. Heavier than I expected."

            if scene_has("act2_04_first_day_out", "helped_injured_worker"):
                a "Today I watched a man almost get crushed, and I moved. It still didn't feel like enough."
            else:
                a "Today I watched a man get crushed and kept my hands on the belt."
                a "That felt worse than any firefight I've been in."

            a "I don't want that to be the whole story."

            "Tessa studies me."

            athought "Something around her eyes shifts. Not softening exactly. But listening."

            if pass_tier("OB1", "OB2", "OB3"):
                # Even on OB lean, this choice shows cracking
                athought "That was more than I meant to say. The mask slipped."
                athought "Strange that it doesn't feel like a mistake."
            else:
                athought "It's not absolution. I'm not asking for that."
                athought "I'm just... tired of pretending the weight isn't there."

            t "Honest answer."
            t "Doesn't fix anybody's fractures. But it's a start."

            # VISUAL: Tessa moves, grabs a basin and cloths, puts them in Aeron's hands.
            "A basin lands in his hands—cold water, a handful of worn cloths that smell like chemical disinfectant."

            t "Wash those trays. Disinfect them properly. Don't cut corners."

            "To Lyra:"

            t "You help me rewrap the corner beds."
            t "If you're going to carry guilt, you might as well carry gauze too."

        "Frame it as pragmatic survival.":
            $ choice_and_dev(
                _current_scene_id, "_tessa_clinic_stay_masked", "OB", factor=1,
                note="Aeron frames helping as tactical reputation investment rather than moral repair."
            )
            $ npc_remember("Tessa", "aeron_framed_pragmatic", tone="wary")
            $ scene_mark(_current_scene_id, "first_impression_hard")

            a "Zira says clinics remember faces."

            athought "I keep my voice level. Practical."

            a "The Unders already hate us. We can't survive that forever."
            a "If helping here buys us less hatred, that's a trade worth making."

            if pass_tier("EMP1", "EMP2", "EMP3"):
                # Even on EMP lean, this choice shows retreat into armor
                athought "It's not the whole truth. But it's easier than the alternative."
                athought "Easier than admitting I don't know what I'm doing anymore."
            else:
                athought "Clean and transactional. She'll respect the honesty even if she doesn't like it."
                athought "People understand self-interest. It's predictable."

            "Tessa's jaw tightens. Just slightly."

            t "So this is an investment."
            t "You pay in effort, collect interest in goodwill."
            t "Not the worst math I've heard."

            if empathy_band() == "obedience":
                t "Just remember these aren't numbers you're moving around a board."
                t "They're people who bleed when the line doesn't stop."

                athought "She's warning me. Or testing me. Maybe both."
            else:
                t "Numbers are easy to shuffle. These aren't numbers."

                athought "She knows there's more. She's giving me the chance to keep it buried."

            # VISUAL: She moves, grabs basin and cloths, puts them in his hands anyway.
            "The basin is cold in his hands—water, cloths, the sharp smell of disinfectant."

            t "Wash those trays. Disinfect them properly."
            t "Even mercenaries can learn how to fold bandages."

            "To Lyra:"

            t "You help me with the corner beds. Watch how I wrap. Copy it."

    # ========== WORK MONTAGE ==========

    # VISUAL: Time compression. Aeron scrubbing trays. Lyra folding bandages beside Tessa. The clinic's rhythm.
    athought "The work is simple. Repetitive. Real."

    "Aeron scrubs dried blood and antiseptic from metal trays until the water in the basin turns rust-colored."

    if empathy_band() == "obedience":
        athought "Focus on the task. Don't think about whose blood this is. It's just material to remove."
    elif empathy_band() == "empathy":
        athought "Someone bled on this tray. Someone Tessa kept alive, or tried to."
        athought "Every scrub feels like it means something."
    else:
        athought "Blood and rust. The Unders runs on both."

    "Across the room, Lyra moves along the cots beside Tessa, copying the way she folds and ties bandages."

    "Her motions are slow at first, careful, then faster as she gets the rhythm."

    # VISUAL: Tessa checking their work.
    "Tessa comes back to check his trays."

    t "Not bad."
    t "Most first-timers either under-scrub or try to polish until the metal wears through."

    if empathy_band() == "obedience":
        a "Efficiency matters when resources are limited."
        t "(a hint of dry humor) You sound like a quartermaster. But you're not wrong."
    else:
        a "Easier to focus when someone might die from laziness."
        t "Good. Keep that."

    "Her attention shifts to Lyra, fingers testing a wrapped wrist."

    t "Your wraps will hold through the night."
    t "That's more than I can say for some people who claim to be professionals."

    "Lyra allows herself a small, exhausted smile."

    athought "The first one I've seen from her since the Purge."

    "The clinic's sound bed softens. The worst cries settle into exhausted silence. The murmur remains."

    # ========== TESSA'S PHILOSOPHY & THE MEDKIT ==========

    # VISUAL: Tessa leaning against the counter, studying them. Tired but still sharp.
    "Tessa leans against the counter, taking a breath."

    t "Zira says you're complicated."
    t "That you've done things that can't be undone."
    t "Down here, that describes almost everyone."

    l "Almost?"

    t "Some kids are still clean. For now."
    t "I'd like to keep it that way."

    if empathy_band() == "obedience":
        athought "Clean and innocent. I'm not sure I remember what that looks like."
    else:
        athought "I was clean once, probably. Before the training, before Glass."
        athought "It feels like another person's memory."

    if scene_has("act2_04_first_day_out", "helped_injured_worker"):
        t "(glances toward Jace's cot) He'll walk again, if infection doesn't take him."
        t "He wanted to say thank you. Fell asleep before you came in."
        t "I don't pass along gratitude lightly. Don't make me regret it."

        $ rel_bump("Tessa", trust=1)

        if empathy_band() == "obedience":
            athought "Gratitude. An asset, if used correctly."
            athought "That thought feels wrong the moment I have it."
        else:
            athought "Thank you. Two words I didn't earn yet."
            athought "But maybe I can."

    else:
        t "(glances toward Jace's cot) His leg's a mess, but he'll live if the bones knit clean."
        t "If you were on his line, you'll see him again."
        t "Decide now what you want him to see when he looks at you."

        if empathy_band() == "obedience":
            athought "She's giving me an assignment. A test with a delayed result."
            athought "I've passed harder tests. This one just feels different."
        else:
            athought "What do I want him to see?"
            athought "I don't know yet. But I don't want him to see Glass."

    # VISUAL: Tessa goes to a small lockbox, pulls out a compact field medkit.
    "A small lockbox on the wall, opened with a key from around her neck."

    athought "Inside: limited supplies. Organized chaos. Every item accounted for."

    "A compact kit slides across the counter—palm-sized, faded olive fabric, worn at the edges."

    t "Basic field kit. Antiseptic, coagulant patches, bandages."
    t "Enough to keep a bad cut from becoming a funeral if you move fast."

    $ add_item_counter("medkits", 1)
    $ scene_mark(_current_scene_id, "received_medkit")

    l "We'll make it count."

    t "I don't have the stock to hand these out for free."
    t "But Zira's vouching, and you washed the trays without complaining."
    t "That puts you ahead of most."

    t "I expect it to come back empty because you used it. Not because you lost it."

    if empathy_band() == "obedience":
        athought "Medical supplies. Leverage. Bargaining power if things go wrong."
        athought "No. That's not what this is."
        athought "That's not what she meant it to be."
    else:
        athought "A kit to help someone. Given freely."
        athought "I can't remember the last time someone handed me something without expecting blood in return."

    # ========== EXIT & WRAP ==========

    # VISUAL: Zira reappears at the door frame.
    "Zira appears at the doorway."

    z "So? Do they pass triage?"

    t "They pass 'didn't make anything worse.'"
    t "For day one, I'll take it."

    z "That's practically a glowing review."

    t "Don't let it go to their heads."

    # VISUAL: Tessa turns back toward the cots, but throws final words over her shoulder.
    "A groan rises from one of the corner cots. Tessa's already moving toward it."

    t "(over her shoulder) You need help and you're not bleeding out? You wait your turn or you help."
    t "You are bleeding out? Come here and don't lie to me about what caused it."
    t "I can work with ugly. I can't work with lies."

    "She's gone behind a curtain before she finishes the last word."

    # VISUAL: Zira nudges them toward the door.
    z "Time to go before she drafts you as permanent volunteers."

    "The door hisses shut behind them. The clinic noise muffles to nothing."

    # VISUAL: Corridor outside. Quieter. Aeron holding the medkit.
    l "She's... intense."

    if empathy_band() == "obedience":
        a "She's efficient. Runs this place with almost nothing and keeps people alive."
        a "That's worth respecting."
        l "(quiet) That's not a word I expected from you."
        a "What?"
        l "Respecting. Usually you say 'useful' or 'competent.'"
    else:
        a "She's keeping people alive with less than I used to spend on a single operation."
        l "(quiet) We used to spend."
        a "Yeah. We."

    z "That's Tessa."
    z "Gentle until you give her a reason not to be."
    z "If she decides you're worth the space you take up, you'll know."

    "The field kit sits in his hand, smaller and lighter than he expected."

    athought "But somehow heavier than it should be."

    # VISUAL: Walking back toward safehouse. Unders corridor. Neon bleed from distant markets.
    "The maze of corridors and service passages swallows them again—neon bleeding from distant markets, the familiar press of damp walls."

    athought "First the yard. Now the clinic."
    athought "The Unders keep showing me where the machine leaves its scars."

    if empathy_band() == "obedience":
        athought "I used to stand above it and call it necessary. Efficient. The cost of order."
        athought "Down here, 'necessary' has faces and names. It's harder to file them away."
    elif empathy_band() == "empathy":
        athought "I used to call it collateral. Acceptable losses."
        athought "Now it looks a lot more like consequence. And I'm standing in the middle of it."
    else:
        athought "I used to think I understood the shape of things. The math."
        athought "Down here, the math bleeds."

    # VISUAL: Safehouse door. Same concrete box. Different weight walking back into it.
    "The safehouse door closes behind them."

    "The same concrete walls, the same thin light, the same trapped air."

    "But the medkit on the crate beside them is new."

    athought "Proof that something in this city gave instead of took."

    if empathy_band() == "obedience":
        athought "A resource. A connection. The start of something that might keep us alive."
        athought "It's not enough. But it's a start."
    elif empathy_band() == "empathy":
        athought "It's not redemption. I'm not foolish enough to think that."
        athought "But it's something. A hand reaching back."
    else:
        athought "It's not much. It's not redemption."
        athought "But it's something."

    # --- SCENE WRAP ---
    $ flag_on("Tessa", "met_in_clinic")
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_05_clinic
# cann.when_in_timeline:
#   - Same day as act2_04_first_day_out (machine yard); evening after the shift ends.
# cann.what_happened:
#   - Zira brings Aeron and Lyra to Tessa's underground clinic, hidden in the Unders.
#   - Tessa is introduced in her element: treating Jace, the worker injured in the yard accident.
#   - Yard choice payoff:
#       • If Aeron helped: Jace recognizes him, expresses gratitude; Tessa notes he "didn't hesitate."
#       • If Aeron stayed: Jace is sedated, no recognition; Tessa pointedly notes "the line never backed up."
#   - Aeron and Lyra give their cover names (Kade/Mira) but Tessa insists on hearing it from them directly.
#   - Core choice: Aeron either admits guilt and offers genuine help (EMP) or frames it as pragmatic reputation investment (OB).
#   - Work montage: Aeron scrubs medical trays, Lyra learns to wrap bandages under Tessa's supervision.
#   - Tessa gives them a field medkit — concrete reward and future prop.
#   - Tessa's philosophy established: she remembers faces, doesn't care who started fights, only who's bleeding.
# cann.aeron_state:
#   - Continuing to process the yard and his new "nobody" status.
#   - Internal monologue varies significantly by empathy band throughout:
#       • OB: tactical framing, efficiency focus, but cracks showing ("that thought feels wrong")
#       • EMP: emotional weight, connection to people, guilt processed openly
#       • Conflicted: caught between, uncertainty as theme
#   - EMP branch: Aeron is honest about his past and guilt; Tessa responds with cautious respect.
#   - OB branch: Aeron frames helping as tactical investment; Tessa accepts the work but remains wary.
# cann.path_tracking:
#   - One `choice_and_dev` decision:
#       • `_tessa_clinic_own_guilt` → EMP +1 weight.
#       • `_tessa_clinic_stay_masked` → OB +1 weight.
#   - Scene flags: `first_impression_soft` vs `first_impression_hard` for Tessa's initial read.
#   - NPC memories stored via `npc_remember()` for future Tessa scenes.
#   - If Aeron helped Jace: `rel_bump("Tessa", trust=1)` as small early trust seed.
#   - Running empathy range at scene end: -10 to 0 (prior range ±1 from this choice).
# cann.thematic_flags:
#   - Motifs: Care as resistance, the body as record of systemic violence, "the machine leaves scars."
#   - Tessa as moral center: pragmatic compassion, not naive idealism.
#   - Work as proof: Tessa puts them to work immediately, judges by action not words.
#   - Callback structure: Jace's presence ties directly to yard choice, creating immediate consequence.
# cann.alignment_flavor_points:
#   - Approach corridor: OB notices chokepoints, EMP notices people live here
#   - Clinic interior: OB sees triage efficiency, EMP sees individuals
#   - Yard memory: internal framing differs by band
#   - Cover name delivery: OB is flat/professional, EMP feels the weight of the lie
#   - Tessa's read: she notices different things about OB vs EMP Aeron
#   - Work montage: OB focuses on task efficiency, EMP connects to meaning
#   - Medkit receipt: OB initially frames as leverage (then corrects), EMP sees gift
#   - Exit dialogue with Lyra: different word choices reveal state
#   - Final internal: three distinct closings by band
# cann.character_moments:
#   - Tessa: Sharp, tired, compassionate underneath the armor. Reads people instantly. Puts you to work.
#   - Lyra: Uncertain but capable; learns the bandage work quickly. First smile since the Purge.
#   - Zira: Knows when to disappear and reappear; clearly has history with Tessa.
# cann.inventory:
#   - +1 medkit added via `add_item_counter("medkits", 1)`.
# cann.block_status:
#   - ANCHOR scene; single alignment choice, yard payoff integrated organically.
# cann.requires_followup:
#   - Tessa can reference `first_impression_soft`/`first_impression_hard` in future scenes.
#   - Jace can reappear later; his reaction depends on `helped_injured_worker` flag.
#   - Medkit becomes a prop in future injury/field scenes.
#   - `npc_remember` entries allow Tessa to reference these events naturally later.
