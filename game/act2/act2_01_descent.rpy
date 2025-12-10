# =======================================================
# ACT 2 - Scene 1: Descent
# File: act2_01_descent.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_01_descent"
$ scene_mark(_current_scene_id, "entered")

define vendor = Character("Vendor")
define man = Character("Local")

label act2_01_descent:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 28–40mm; handheld sway on rooftop; steadier as they commit to moving; tighter CUs in crowd crush.
    # LIGHTING: Dawn over burning sectors; orange fire wash vs cold upper-tier skylight; deep smoke plumes.
    # SFX: Loop — distant sirens, low fire roar, city hum; one-shots — elevator chimes, crowd reactions, feedback shriek, sparking neon.
    # FX/COMP: Heat shimmer over Purge zones, drifting ash; light smoke layer on rooftop; neon + steam in Lower Spans.
    # BLOCKING/PROPS: Rooftop ledge, Aeron's apartment interior, Zira's device, maintenance stairwell, Sector 6 market, Ghostline relay boxes.
    # FACE: Aeron's expression stays controlled but strained; Lyra visibly worn; Zira relaxed, eyes sharp, amused.

    # ========== CHAPTER TITLE CARD ==========
    scene black with fade
    centered "{size=+20}ACT II{/size}"
    pause 0.5
    centered "{size=+10}Chapter I — From Glass to Nobody{/size}"
    pause 2.0
    scene black with fade

    # VISUAL: Rooftop where they watched the Purge; fires still burn below.
    athought "Hours pass. Or maybe it's minutes. Time doesn't mean much when the city's still burning."

    "Sectors 8, 9, and 10 glow orange below, heat still rising in visible waves."

    athought "Like an open wound."

    if empathy_band() == "obedience":
        athought "I catalog the fire lines by sector and grid, turning the slaughter into data because that's the only way it fits."
    else:
        athought "I can't stop seeing people in the fire—not numbers, not targets, just lives I helped erase."

    a "We can't stay here."

    l "(quiet) Where would we even go?"
    if empathy_band() == "obedience":
        a "Anywhere with cover and three exits."
    else:
        a "Anywhere that isn't watching this."

    # VISUAL: Lyra studies him; both shattered and exhausted.
    l "Echelon will be looking for us."
    a "Yeah."
    l "They'll check your command terminal. Your apartment. Your schedule."
    a "I know."
    l "Marcus will realize you weren't on the deck when the order went through."

    if empathy_band() == "obedience":
        a "(cuts in) I know."

        athought "The words come out clipped. Control over comfort."
    else:
        a "(soft) I know."

        athought "The admission tastes like rust."

    "Dawn light grows, staining the smoke in gold and red."

    l "How long do we have?"
    a "Not long. He'll start at my quarters. We should already be gone."

    l "Then let's move."
    a "You don't have to come. This was my break, not yours."
    l "Don't start that. We jumped together, so we burn together."

    if empathy_band() == "obedience":
        athought "Together or not, we're already off the map."
    else:
        athought "Together. That's the only part that still feels solid."

    # ========== APARTMENT ==========

    scene bg_aeron_apartment with fade

    "The apartment looks the same as it did yesterday—neat and ordered, a life built around missions and reports."

    athought "Now it just feels like a stage set after the show ends."

    # VISUAL: Aeron moves efficiently, grabbing essentials.
    athought "Weapons, credits, clothes—anything else is weight."

    # VISUAL: Kael's photo on the desk.
    "Kael's photo still sits on the desk."

    athought "Smiling at a world that doesn't exist anymore."

    if pass_emp():
        athought "I left you once. I'm not doing it again."

        "The photo is lighter than it should be—just paper and polymer, nothing that should weigh this much."
    else:
        athought "If I leave it, someone will bag it and tag it."

        "The photo feels clinical in his fingers—just another item to secure."

        athought "Not sentiment—evidence of a life they'll try to erase."

    # VISUAL: Lyra grabs a small pack; she moves with trained economy, but her hands shake.
    l "How much can we carry?"
    a "Not much. We'll need to move fast and quiet."
    l "Where?"
    a "Down. Lower Spans first. Maybe the Unders if we make it that far."
    l "(grim) The Unders will tear us apart."
    a "Echelon will shoot us on sight. I'll take uncertainty over certainty."

    l "Some of the people you pulled out during the Sweep were from down there."
    a "If they survived the Purge."
    l "They might remember that you saved them."
    a "They'll remember who gave the order too."

    # VISUAL: Aeron at the terminal.
    "The terminal hums, cold light washing over his hands as lines of text scroll up the screen."

    athought "Mission logs, patrol routes, access patterns—everything I used to prove I was loyal."

    if empathy_band() == "obedience":
        athought "I strip the system clean with the same focus I used to plan operations."
        athought "It feels like just another task, even if I know it isn't."
    else:
        "His fingers tremble on the keys."

        athought "Every file I delete feels like a small, precise funeral."

    "The cursor reaches the last entry—nothing left to erase."

    # VISUAL: Zira's device on the desk.
    "The encrypted relay Zira gave him sits in the corner of the desk."

    athought "She said to use it when I needed her."
    athought "If I ping her, I expose us. If I don't… we're alone."

    # --- PLAYER CHOICE: contact Zira or not ---
    menu:
        "The relay blinks once."
        "Activate the device — reach out to Zira.":
            $ choice_and_dev(
                _current_scene_id, "_a2_01_contact_zira", "EMP", factor=2,
                next_scene_label="act2_02_reality_check",
                note="Chooses to trust Zira and ask for help instead of staying fully independent."
            )
            $ flag_on("Zira", "contacted_in_scene1")

            "The relay is warm in his palm, heavier than it looks. The interface blossoms with encrypted prompts he barely understands."

            athought "I don't bother with codes or explanations."

            "One word on the screen: {i}Help.{/i}"

            "The relay pulses, then returns to a steady light."

            athought "If she got it, she knows we've jumped."
            athought "If she didn't… we walk alone."

        "Pocket it — too risky to send a signal.":
            $ choice_and_dev(
                _current_scene_id, "_a2_01_ignore_device", "OB", factor=2,
                next_scene_label="act2_02_reality_check",
                note="Keeps control by refusing to broadcast position, even to a potential ally."
            )

            "The relay's light is insistent, almost accusatory. He stares at it until the glow annoys him more than the risk."

            "The device goes dark with a soft click. Cold weight against his thigh."

            athought "No signals, no trails, no favors owed."
            athought "If we live, I can change my mind later."

    # VISUAL: Lyra re-enters frame with her pack.
    l "I'm set. Are you?"
    a "(gives the room one last scan) Yeah. I'm done here."

    athought "The apartment feels smaller on the way out. Like it knows I won't be coming back."

    # ========== DESCENT THROUGH TIERS ==========

    "The corridor outside is spotless—too bright, sterile. Propaganda screens pivot in real time."

    # VISUAL: Screens updating.
    # TEXT: "TERRORIST ATTACK CONTAINED"
    # TEXT: "ECHELON PROTECTS. ECHELON PROVIDES."

    athought "Terrorist attack, contained—a hundred thousand dead, rebranded as 'security'."

    athought "Stopping to argue with a screen won't save anyone."

    # VISUAL: Maintenance stairwell door.
    "The maintenance stairwell door is heavy, the metal cold under his palm—rarely used, by the look of the dust."

    "It opens with a groan."

    athought "Too loud."

    l "How far down?"
    a "As far as we can. Lower Spans first. We'll see from there."
    l "Fifty levels."
    a "Then we take fifty."

    # VISUAL: Descending; light quality shifts each landing.
    "The stairwell echoes with their footsteps, each landing a little darker than the last."

    athought "The air changes with every landing—from filtered to stale, from quiet to layered with distant machinery and voices."

    if empathy_band() == "obedience":
        athought "I count the floors and keep a mental map running, forcing the chaos into structure."
    else:
        "Voices bleed through thin doors—arguments, lullabies, someone trying not to cry."

        athought "The city feels more alive the lower we go."

    # VISUAL: Passing Mid Levels.
    athought "Mid Levels—workers, families, people who don't know the ground just shifted under them."
    athought "Or maybe they do and pretend they don't. I've done the same."

    "A few residents glance at their clothes and look away quickly."

    athought "Nobody wants to be caught staring at uniforms when uniforms are hunting."

    l "We stand out."
    a "We'll fix it when we can. For now, keep moving."
    l "We need different clothes before the Unders. These scream Echelon."
    a "One problem at a time."

    # VISUAL: Lower Spans threshold — neon, rust, steam, crowded walkways.
    "By the time they reach the Lower Spans, the stairwell walls sweat rust."

    "Neon bleeds in through the door frame, mixed with steam and the smell of too many people packed into too little space."

    athought "I know this grid."
    athought "We swept near here. We called it a containment zone."

    # VISUAL: Step out into Sector 6 market street.
    "The market hits like a wall—noise, heat, the press of bodies and the smell of frying oil and recycled air."

    "Vendors shout over each other while kids dart between adults and hawkers push cheap tech and fake meds. Everyone is scanning everyone else."

    "The noise drops half a step the moment they appear."

    athought "The crowd feels it."

    l "(under her breath) Eyes on us."
    a "Keep walking. Don't reach for anything you don't have."

    # VISUAL: An older vendor steps out, blocking their path.
    vendor "You're Echelon."

    a "...We were."

    vendor "You swept Sector 10 three days ago."

    a "(carefully) I was part of the operation."

    vendor "My nephew worked there. He's ash now."
    vendor "Did you kill him?"

    if pass_emp():
        a "...I don't know. Maybe."

        athought "I hold her gaze. I don't look away."
    else:
        a "...I followed orders. That's the only honest answer I have."

        athought "No excuses—just the ugly truth I was built on."

    "She studies him for a long, quiet second, then spits at his feet."

    vendor "Get out of my sight before someone decides you're worth more dead than angry."

    "She turns away, but the rest of the market doesn't."

    athought "The air tightens."

    # VISUAL: Young man pushes forward, improvised weapon in hand.
    man "You. Glass."

    athought "The word hits me like a physical thing."

    man "Sector 10. You killed my sister."

    if pass_emp():
        a "I'm sorry."
    else:
        a "(low) I know what I did."

    man "She was nine. You don't get to be sorry."

    "More faces close in—someone else has a pipe, another a broken bottle. Fury builds faster than they can back away."

    l "(barely audible) Aeron..."
    a "(quiet) Don't reach for a weapon you don't have."

    l "Then what?"
    a "We move when there's a gap. If there's a gap."

    # ========== ZIRA INTERVENES (TECH, NOT GUNSHOT) ==========

    # SFX: A rising electronic whine from every battered speaker on the street.
    "Every battered speaker bolted to the walls starts to hum at once."

    "The hum spikes into a piercing feedback shriek that punches straight through bone."

    "A neon sign over the nearest stall flares white-hot and blows out, showering the street in sparks and dead glass."

    "The crowd flinches as one, hands flying to ears, weapons dipping."

    z "That's enough."

    "Her voice comes through the speakers and the alley behind them at the same time—calm, amused."

    # VISUAL: Zira steps out, glove faintly sparking.
    "A woman steps out of a shadowed alley, hood back, eyes sharp. Contacts on her glove still flicker with residual charge."

    z "These two are with me."
    z "Anyone here want to find out what happens if I flip the rest of the block to overload?"

    man "Who the hell are you?"

    z "The reason your heart monitor isn't flatlining right now."
    z "Back off. Go home. Tell your friends Glass already owes you."

    "The man's eyes move from Zira to the ruined sign to the watching crowd."

    athought "Anger doesn't vanish, but survival does the math for him."

    man "(to Aeron) This isn't over."
    "The street gives ground with him—tension thinning without disappearing."

    # VISUAL: Zira closes the distance to Aeron and Lyra.
    z "You two are terrible at subtlety."

    a "Zira—"

    if flag_has("Zira", "contacted_in_scene1"):
        z "Save it. You pressed send. I pressed go."
        z "Ghostline lit up the second your message hit. I've been riding your shadow for two hours."
    else:
        z "Save it. I've been watching since you stepped off Aeries."
        z "You hovered over that little relay on your desk, then wiped the drive like a good officer."
        a "You were watching me?"
        z "Whenever something interesting happens topside, the Ghostline pays attention."
        z "Congratulations. You're officially interesting."

    z "Now move. Patrols love an audience."

    # ========== EVASION & GHOSTLINE ROUTE TO SAFEHOUSE ==========

    # VISUAL: Zira cuts into a narrow side alley.
    "She turns and slips into a gap between two stalls that barely qualifies as an alley."

    "The noise of the market drops away behind them, replaced by dripping pipes and the low thrum of buried power."

    z "Stay close. If you lose sight of me, assume you're already dead or arrested."

    # SFX: Patrol drone whine overhead.
    "A patrol drone's whine cuts through the air above the alley. Its searchlight sweeps past the opening."

    z "(low) Wall. Now."

    "Damp concrete presses cold against his back as Zira taps her glove against a corroded junction box."

    "Sparks jump from the contact and a streetlight at the alley mouth stutters into a strobe pattern that sends the drone's sensors chasing ghosts."

    z "Ghostline says, 'Look over there, not here.'"

    "The drone veers, beam drifting away. Zira is already moving before the light finishes turning."

    # VISUAL: Secondary market used as cover.
    "The second market is narrower, rougher—less polish, more desperation in the air."

    z "Heads down. Don't stare. Don't bump. Don't talk unless I ask you a question."

    "Zira brushes a rusted panel with one hand as she passes."

    athought "She moves like she's walked this route a hundred times."

    # VISUAL: Hidden access hatch.
    "At the end of the row, she stops in front of what looks like a dead maintenance hatch."

    "Her glove touches the surface and a muted chime sounds. A seam appears in the metal."

    z "Welcome to the part of Solveil the maps pretend doesn't exist."

    "The hatch slides just wide enough to let them through one by one."

    # VISUAL: Interior corridor leading to safehouse.
    "Inside, the noise of the markets cuts off. The corridor is narrow, lined with exposed conduit, the air thick with ozone and dust."

    "Zira leads them down a short flight of metal stairs to an unmarked door."

    z "Home, for now."

    # VISUAL: Door opens onto Zira's safehouse.
    "She unlocks it with a code and a touch, and the door swings inward."

    "The room is bare—concrete walls, a barred window, one overhead bulb. A space designed to be overlooked."

    athought "Not home. Not yet. But shelter—and shelter is the only luxury we can afford."

    # --- SCENE WRAP ---
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_01_descent
# cann.when_in_timeline:
#   - Immediately after rooftop Purge witness; opening beat of Act II, before first full night in the Unders.
# cann.what_happened:
#   - Aeron and Lyra leave the rooftop, collect essentials, and wipe Aeron's Echelon records.
#   - Player chooses whether Aeron activates Zira's relay (reach out) or pockets it (stay dark), nudging OB/EMP via `choice_and_dev`.
#   - They descend from Aeries through Mid Levels to the Lower Spans, seeing propaganda reframing the Purge as a "contained terrorist attack."
#   - Sector 6 locals confront Aeron over the Sweep; he responds with either honest uncertainty or stripped-down "I followed orders."
#   - A mob begins to form; Zira intervenes using Ghostline tech (PA feedback + neon overload), not a gunshot.
#   - Zira demonstrates her command of the Unders via a Ghostline-guided evasion route (drone misdirection, hidden access hatch).
#   - Scene ends at the threshold of her safehouse, setting up Act2_02 as the first full "in the box" recovery/briefing scene.
# cann.aeron_state:
#   - OB-lean baseline but visibly fractured; still defaults to procedure under pressure but can admit uncertainty/sorrow in EMP-gated variants.
#   - "Glass" used sparingly as a label from others, not as constant internal self-naming.
# cann.path_tracking:
#   - Single binary choice with `choice_and_dev`:
#       • `_a2_01_contact_zira` → EMP drift (seeking help), factor=2.
#       • `_a2_01_ignore_device` → OB drift (self-reliance, signal paranoia), factor=2.
#   - No extra empathy adjustments outside choices; gates only affect flavor, not metrics.
#   - Running empathy range at scene end: -7 to -3 (depending on Act I + this choice).
# cann.thematic_flags:
#   - Motifs: Descent, narrative control, nobody/cover, Ghostline as invisible infrastructure.
#   - Zira is positioned firmly as "Ghostline Architect" — she uses systems and circuits, not raw firepower.
# cann.block_status:
#   - ANCHOR scene; single alignment choice, no branching outcomes yet.
# cann.requires_followup:
#   - Next: `act2_02_reality_check` picks up inside the safehouse with exhaustion, rules of the Unders, and first real decompression.
