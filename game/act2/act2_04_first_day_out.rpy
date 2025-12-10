# =======================================================
# ACT 2 - Scene 4: First Day Out
# File: act2_04_first_day_out.rpy
# =======================================================

define foreman = Character("Foreman")
define w1 = Character("Worker")
define w2 = Character("Worker 2")

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_04_first_day_out"
$ scene_mark(_current_scene_id, "entered")

label act2_04_first_day_out:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 24–28mm for streets (crowd compression), 35mm for yard interiors; handheld drift with occasional 3–4% push on threat beats.
    # LIGHTING: Unders morning haze; sodium-vapor spill, cold skylight shafts; yard interior is harsh white work-lights with deep hard shadows.
    # SFX: Loop — crowd murmur, distant machinery, vendor calls; yard — clanging metal, hydraulic hiss, shouted orders.
    # FX/COMP: Light particulate in air, occasional steam bursts; conveyor belts with looping VFX.
    # BLOCKING/PROPS: Narrow corridors, maintenance ladders, sliding panels, yard gate, ID scanner, conveyor lines, lift cranes, tool racks.
    # FACE: Aeron/Lyra get more human, less "Glass armor"; Foreman is all impatience and calculation.

    # VISUAL: Safehouse, morning. Thin light through barred window; city hum higher than last night.
    athought "Morning in the Unders isn't sunrise. It's noise getting louder."

    athought "The safe house smells like cold concrete, old wiring, and leftover ration wrappers."
    athought "Outside, the city grinds awake. Inside, two fugitives pull on borrowed lives."

    # VISUAL: Aeron lacing up work boots; Lyra tying her hair back, folding Band under sleeve.
    athought "Day two as Kade Voss."
    athought "Feels like pretending to be a ghost inside my own skin."

    l "(checking her sleeve) It shows?"
    a "Band's covered. You look like everyone else down here."
    l "I've never been 'everyone else' before."
    a "Welcome to the club."

    # VISUAL: The lock beeps. Zira slips in, light on her feet, carrying a small satchel.
    z "Morning, wage labor."
    z "You ready to be underpaid and overworked like the rest of us?"

    a "Define 'ready'."
    z "Still breathing and upright. That's all Foreman Rusk cares about."

    # VISUAL: She tosses Aeron and Lyra simple work jackets; muted colors, local tags.
    z "Jackets. Yard tags stitched on the inside. Don't lose them."
    z "Remember: Kade Voss, Sector 6 machine tech. Mira Chen, parts runner."

    if empathy_band() == "obedience":
        z "(to Aeron) And Kade doesn't stand like command. Shoulders down. Eyes normal. Try it."
    else:
        z "(to Aeron) And if Kade looks like he's expecting a firing squad, people will notice. Breathe."

    # VISUAL: Corridor outside safehouse — narrow, cables overhead, pipes sweating condensation.
    # They step out; the city closes around them.
    "The corridor swallows them—cables overhead, pipes sweating condensation, the city pressing in from every angle."

    athought "The air feels heavier than last night. Somehow busier."

    # VISUAL: Tight space opens into a busier walkway — vendors, kids, workers, improvised stalls.
    athought "The walkway ahead is a river of bodies and noise. Vendors shout over each other, kids weave through legs, someone argues about stale bread in three different languages."

    l "(low) This is all below Aeries?"
    z "Fifty levels like this, give or take. You just never looked down long enough to see it."

    # VISUAL: Zira walks like she owns the route; she knows exactly where to put her feet.
    "Zira moves fast but never rushes."

    athought "She slips through gaps that seem to appear just for her."

    # VISUAL: Chalk marks and small tags on walls.
    athought "I start to notice marks on the walls — chalk symbols, scratched metal, bits of colored tape."
    athought "Ghostline writing. Routes only certain people can read."

    # SFX: Distant drone whine building.
    "A high whine cuts through the street noise."

    l "(tensing) Patrol drone?"
    z "Yeah. And it doesn't care about your new names."

    # VISUAL: Zira grabs a small panel on the wall, slides it aside to reveal a narrow service passage.
    z "In here. Now."

    # VISUAL: Tight service corridor, barely one person wide. Steam, cables, dim maintenance lights.
    "The passage is barely wide enough for one body—steam hisses from joints overhead, cables brush against shoulders, and the air tastes like burnt dust and oil."

    "Zira pulls the panel half-closed, leaving a thin slit to the main walkway."

    # VISUAL: Drone shadow gliding past the opening; faint searchlight flicker.
    "A patrol drone glides past outside, searchlight cutting over faces in the crowd."

    if empathy_band() == "obedience":
        athought "Route, timing, noise profile—I catalog it out of habit."
        athought "Old training clinging to a life that doesn't exist anymore."
    else:
        athought "My hand tightens around nothing—no rifle, no orders, just the knowledge that one wrong look out there ends us."

    # VISUAL: Drone sound fades.
    z "Okay. Show's over. This way."

    # VISUAL: Zira leads them through the maintenance maze — ladders, grates, low beams.
    "Rungs cold under palms, then ducking under pipes, then the hum of a moving conduit vibrating through boot soles."

    z "This is what 'knowing the Unders' looks like."
    z "Main streets are for people who can afford to be seen."

    # VISUAL: Exit panel opens to a side alley overlooking a large industrial yard.
    # Massive machines, conveyor belts, cranes; workers in faded gear.
    "The panel opens onto a narrow ledge, and the Sector 6 machine yard spreads out below—cranes swinging over conveyor belts, workers in faded gear moving between machines."

    athought "Like part of the machinery. Patterns that look almost rehearsed."

    z "Welcome to honest work."
    z "Foreman runs a tight operation. He doesn't ask many questions as long as you do the job and don't start fights."

    a "Any other rules?"
    z "Don't flash your Bands, don't talk about Aeries, don't act like you're better than anyone here."
    z "Down there, boring survives."

    # VISUAL: Yard gate — a metal cage with a card reader and a bored guard.
    z "Gate's ahead. I'll walk you up. After that, you're on your own."

    # VISUAL: At the gate; a scanner on a post, a bored guard with a data-slate.
    foreman "You're late."
    z "You're early, Rusk. This is Kade and Mira. The ones I messaged you about."
    foreman "(eyes them) They look soft."
    z "They'll harden. Or break. Either way, you'll get the labor you paid for."

    # VISUAL: Zira hands over the IDs. Foreman runs them across the scanner.
    foreman "(studying display) Kade Voss. Mira Chen. Sector 6 shifts."

    menu:
        foreman "You two ever worked a yard before?"
        "Stick close to the cover story.":
            $ record_choice_once(_current_scene_id, "_foreman_cover_honest")

            a "Not this yard. But I know machines."
            foreman "Knowing them and keeping them running are different, kid."
            foreman "I don't care if you're a saint or a sinner. I care if you're slow."

        "Lean on command posture out of habit.":
            $ record_choice_once(_current_scene_id, "_foreman_command_slip")

            a "I've managed heavier hardware than this."
            foreman "(snorts) Then this'll be a vacation for you, commander."
            foreman "As long as you remember you're not in command of anything here."

    # VISUAL: Foreman hands them their IDs back.
    foreman "Clock's running. Kade, you're on Line B. Mira, parts run for B and C."
    foreman "Lose a tool, you pay for it. Slow the line, I dock your pay. Got it?"

    a "Got it."
    l "Understood."

    z "(to Aeron and Lyra, low) I'll be around."
    z "Not on the floor, but… listening. Try not to get killed before lunch."

    # VISUAL: Zira peels away into the crowd outside the fence.
    "Zira disappears back into the maze of alleys and ladders."

    athought "Like she was never there."

    # VISUAL: Inside the yard. Noise spikes; machines dominate the frame.
    athought "Inside the fence, the world compresses to metal and movement."

    "Conveyors rattle. Lifts hiss. Workers shout over the din."

    athought "The air tastes like hot metal and oil and old smoke."

    # VISUAL: Aeron joins Line B — long conveyor, mechanical arms, crates of parts.
    "Aeron takes his place along Line B. Crates slide toward him on a belt with tired bearings."

    athought "Lift, check, pass—the same motion over and over. Nothing tactical about it, nothing heroic, just work."

    # VISUAL: Lyra moving between Lines B and C with a parts tray.
    "Lyra passes between lines with a parts tray, her posture too straight at first."

    if empathy_band() == "obedience":
        athought "She forces herself into a more relaxed pattern, copying the way other runners move."
    else:
        athought "She watches the other runners and gradually lets her shoulders drop, borrowing their rhythm."

    # VISUAL: Time passes — quick montage of repetitive tasks.
    athought "Minutes smear into something that might be an hour."
    athought "Sweat, noise, the ache in my arms. For the first time in my life, my 'mission' is to keep a belt from backing up."

    # VISUAL: A shout from further down the line.
    w1 "Hey! Careful with that—!"

    # SFX: Metal screech, a heavy thud, someone crying out in pain.
    "Steel shrieks against steel. A crate tilts, then drops off the belt onto a worker's leg."

    w1 "(choked) Shit—! My leg—!"

    # VISUAL: The line doesn't stop. Crates keep coming.
    "The belt keeps moving. Crates slide inexorably toward the jam."

    foreman "(shouting from the catwalk) Keep the line moving!"
    foreman "We stop, we lose the shift! Someone drag him clear and get back to work!"

    # VISUAL: Nearby workers hesitate — torn between the belt and the injured man.
    "Workers look at each other, then back at the belt."

    athought "Everyone knows the math: line stops, everyone loses."

    # --- PLAYER CHOICE: HELP THE INJURED WORKER OR PROTECT THE LINE ---
    menu:
        "A worker is pinned under the crate as the belt pushes more weight toward him.":
        "Break position and help him.":
            $ choice_and_dev(
                _current_scene_id, "_help_injured_worker", "EMP", factor=1,
                note="Aeron prioritizes a stranger's pain over cover-perfect performance."
            )
            $ scene_mark(_current_scene_id, "helped_injured_worker")

            # VISUAL: Aeron steps out of his spot, grabs the crate, muscles straining.
            athought "I step out of my slot without thinking, hands already on the crate pinning the man."

            a "On three. Push with me."
            w1 "(gasping) I—I can't—"

            # VISUAL: Two nearby workers jump in, seeing someone commit.
            w2 "Come on, he's got it. One, two—heave!"

            "Together they lever the crate up just enough for the injured worker to drag his leg free."

            w1 "(groaning) Fuck. I think it's broken."
            a "Don't stand on it. Sit. Breathe."

            # VISUAL: Crates piling up behind them; belt groans under the backlog.
            "Crates stack up behind us. The belt groans."

            athought "Trying to shove metal through a human moment."

            foreman "(from above) Line B! Why are you stopped?"
            foreman "(sees it) …Of course."
            foreman "(down to Aeron) You planning to run a charity ward, Voss?"

            a "He wasn't getting out on his own."
            foreman "(grim) No, he wasn't."

            # VISUAL: Foreman signals to shut down their segment briefly; other workers scramble to clear the backlog.
            "The foreman slams a palm on a nearby cutoff. The belt in their segment shudders to a halt while others hustle to clear the jam."

            foreman "(to w1) Clinic. Now. Don't argue."
            foreman "(to Aeron) You just cost me ten minutes and made sure Line C's going to hate you."

            if empathy_band() == "obedience":
                athought "I can already hear the penalty in his tone. Docked pay, docked trust."
                athought "Worth it."
            else:
                athought "Ten minutes against a shattered leg."
                athought "I'll take that trade again."

            foreman "(after a beat) But… the man still has a leg."
            foreman "Next time, shout for a cutoff before you play hero."
            foreman "Back on the line, Voss."

        "Stay in place and keep the line moving.":
            $ choice_and_dev(
                _current_scene_id, "_protect_the_line", "OB", factor=1,
                note="Aeron stays locked to procedure and cover, letting others handle the fallout."
            )
            $ scene_mark(_current_scene_id, "stayed_on_line")

            # VISUAL: Aeron's hands move on reflex, keeping his section from backing up.
            athought "My fingers tighten around the next crate. I keep it moving, keeping my section from backing up."

            athought "If I jam the line, everyone pays for it."
            athought "One man down versus an entire shift losing work. That's the equation."

            # VISUAL: Another worker rushes in to help the injured man, struggling alone with the crate.
            w2 "(straining) Come on, help me get this off him!"
            w1 "(pained) I can't feel my toes—"

            # VISUAL: A couple more workers peel off, but slower; everyone glances at the belt, then at the foreman.
            "Two others finally peel off to help, casting quick looks at the belt and then at the foreman on the catwalk."

            foreman "(barking) You—three—get him loose! Everyone else, keep that metal moving!"
            foreman "(eyes Aeron's section) That's right. B doesn't stop."

            if empathy_band() == "obedience":
                athought "Foreman sees discipline. He reads it as reliability, not cowardice."
                athought "He's wrong. I know which one it is."
            else:
                athought "My arms move on their own while someone screams two stations down."
                athought "This feels less like survival and more like hiding behind the math."

            # VISUAL: After a struggle, they pull the injured worker free. His leg is obviously ruined.
            "The injured man comes free, deadweight against their shoulders."

            athought "His leg bends in a way it shouldn't."

            foreman "(to w1) Clinic. If they can't fix it, find something you can do sitting down."
            foreman "(to the line) Back to work. We're already behind."

    # --- POST-ACCIDENT RHYTHM RESUME ---
    # VISUAL: The belt finds its rhythm again. The noise swallows the incident.
    "The line finds its rhythm again."

    athought "Swallowing the incident like it never happened."

    if scene_has(_current_scene_id, "helped_injured_worker"):
        "A few workers along Line B nod at me when they think the foreman isn't looking."

        athought "Not gratitude exactly. More like… acknowledgment."
    else:
        "A few workers along Line B glance at me, then away."

        athought "Not blame exactly. More like they've decided what kind of man Kade Voss is."

    # VISUAL: Lyra passes by with another tray; she's seen at least part of what happened.
    l "(quiet, as she passes) You okay?"
    if scene_has(_current_scene_id, "helped_injured_worker"):
        a "Yeah."
        l "He'll walk again because you moved."
        a "Or he'll limp because I was too slow."
        l "Maybe both. But he's alive to find out."
    else:
        a "I kept the line moving."
        l "(soft) I know."
        l "Doesn't mean you're okay with it."
        a "It means we get to come back tomorrow."
        l "(after a beat) I'm not sure if that's comfort or a threat."

    # VISUAL: Time skip — later in the shift; sweatier, dirtier, everything louder.
    athought "By the time the shift whistle finally screams, my arms feel like they belong to someone else."

    # VISUAL: Yard edge; workers lining up at a pay window — scrip chits handed out.
    "At the edge of the yard, workers line up at a reinforced window."

    athought "One by one, they collect narrow strips of scrip. An entire day of not getting crushed or fired, reduced to paper."

    foreman "(to Aeron at the window) Voss."
    if scene_has(_current_scene_id, "helped_injured_worker"):
        foreman "Docked you half an hour for stopping the line."
        foreman "Could've been worse if he'd lost the leg."
        foreman "(eyes him) You see the math yet?"
        a "I see a man who still has a chance to stand on both feet."
        foreman "(grunt that might be respect) Don't make a habit of it. This place eats martyrs."
    else:
        foreman "Full shift. No penalties."
        foreman "Belt never backed up at your station."
        foreman "(studies him) You keep that up, you'll last longer than most."
        a "Lasting's the goal, right?"
        foreman "Down here? Lasting is victory."

    # VISUAL: Foreman hands them their scrip.
    "Thin strips of printed scrip slide into my hand."

    athought "They feel lighter than the crates. Heavier than the day."

    # VISUAL: Outside the yard fence; Zira leaning against a railing, pretending she's just passing through.
    "Outside the fence, Zira leans against a railing, flipping a small tool between her fingers."

    z "Look at that. Still alive. Still have all your limbs."
    z "Foreman didn't throw you out. I'll call that a success."

    l "It was… a lot."
    z "Welcome to the Unders. Nobody gets to be special here. You work or you starve."

    if scene_has(_current_scene_id, "helped_injured_worker"):
        z "(low, to Aeron) Rusk grumbled about downtime."
        z "But word'll get around that you pulled someone out from under the crate."
        z "That kind of thing sticks. People remember who grabbed the metal and who watched."
    else:
        z "(low, to Aeron) Rusk likes that you kept the belt clean."
        z "Down here that reads as reliable. Some people will respect it."
        z "Some will decide you're the kind of man who looks away when it hurts."

    # VISUAL: They start walking back toward the safehouse; city closing in again.
    "The maze of alleys and service corridors closes around them again—familiar now in a way it wasn't this morning."

    athought "A day ago, my value was measured in confirmed kills and completed operations."
    athought "Today, it's in crates moved and seconds of downtime."

    if empathy_band() == "obedience":
        athought "Different metrics, but the pressure feels the same."
        athought "The faces on this side of the line are harder to ignore, though."
    else:
        athought "Same grind from a different angle."
        athought "When the machine chews people this openly, it's harder to pretend it isn't there."

    # VISUAL: Safehouse door. Same concrete box. Different weight walking back into it.
    "The safehouse door closes behind them."

    athought "It feels heavier than it did this morning."

    l "So that's work."
    a "That's one day of it."
    l "How many days do we have to do this?"
    a "Until we're not the most suspicious faces in the room."

    z "Or until Selene decides whether she wants to use you or shoot you."
    z "(shrugs) Either way, days like this are how you convince the Unders you're more than the bounty on your heads."

    # VISUAL: Zira at the door, about to leave again.
    z "Get cleaned up. Eat. Rest."
    z "Tomorrow, we tackle a different problem."
    z "You did okay today. Try not to let it go to your heads."

    # VISUAL: She slips out. Lock engages. Just the two of them again.
    "The lock clicks. Zira fades back into the noise outside."

    # VISUAL: Aeron and Lyra in the quiet, uniforms dirty, scrip in hand.
    "The scrip is thin and worn in his palm. Lyra looks just as tired as he feels."

    l "We actually earned something today."
    a "Feels… strange."
    l "Not medals. Not commendations."
    l "Just proof that we showed up and didn't die."

    athought "Kade Voss gets scrip for moving metal."
    athought "Aeron Rylan used to get medals for moving bodies."
    athought "I'm not sure which life is heavier."

    "The scrip lands on the crate they've been using as a table—two fugitives, one day of honest work, a city that still wants them gone."

    # --- WRAP ---
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_04_first_day_out
# cann.when_in_timeline:
#   - Morning/afternoon after act2_03_safe_house_planning; second full calendar day in the Unders.
# cann.what_happened:
#   - Zira escorts Aeron and Lyra from the safehouse through Unders back-routes (maintenance corridors, panels) to a Sector 6 machine yard, dodging a patrol drone and showing "how she moves" in the city.
#   - Aeron and Lyra use their cover identities (Kade Voss / Mira Chen) for the first time with an Unders employer (Foreman Rusk).
#   - They complete a full shift of manual labor in the machine yard: Aeron on Line B, Lyra as a parts runner.
#   - Mid-shift accident: a worker's leg is pinned by a crate; the belt continues moving while the foreman prioritizes keeping the line running.
#   - Player choice:
#       • EMP: Aeron breaks position to help free the worker, stopping the line briefly and earning a small financial penalty but soft respect from some workers.
#       • OB: Aeron stays on task, keeping the line clean and earning foreman approval, but some workers quietly judge his willingness to let others handle the pain.
#   - Zira debriefs the outcome lightly at the gate, framing it in terms of how the Unders will read "Kade Voss."
#   - Aeron and Lyra receive their first scrip payout, then return to the safehouse with one day of "boring survival" under their belts.
# cann.aeron_state:
#   - Still OB-lean baseline, but the workday forces him into a role measured by labor and downtime rather than kill counts.
#   - EMP branch: Aeron prioritizes immediate human harm over cover-perfect behavior, accepts the cost, and reads the trade as worth it.
#   - OB branch: Aeron frames his inaction as protecting the group's survival and cover but recognizes internally that it feels like hiding behind math.
# cann.path_tracking:
#   - One `choice_and_dev` decision:
#       • `_help_injured_worker` → EMP +1 weight.
#       • `_protect_the_line`    → OB +1 weight.
#   - `record_choice_once` logs how Aeron initially presents himself to the foreman (strict cover vs command slip) for future flavor.
#   - Scene flags: `helped_injured_worker` vs `stayed_on_line` allow later Unders NPC reactions / callbacks.
#   - Running empathy range at scene end: -9 to -1 (prior range ±1 from this choice).
# cann.thematic_flags:
#   - Motifs: work as survival, "boring survives," Unders as foundation for the city above, math of harm vs downtime, reputation built one small moment at a time.
#   - Mirrors: Yard belt vs Echelon machine; foreman's "lasting is victory" line as a grounded echo of Aeries rhetoric.
#   - Emotional pivot: first time Aeron's moral tension is framed in a non-combat context (industrial accident instead of battlefield).
# cann.block_status:
#   - ANCHOR scene with a single binary choice; external outcome (job retained, first day completed) is the same, but social and moral framing diverges.
# cann.requires_followup:
#   - Next scenes can:
#       • Call back `helped_injured_worker`/`stayed_on_line` through Unders NPC gossip, clinic presence of the injured worker, or changed yard atmosphere.
#       • Build toward clinic/intel/reputation scenes where this day is referenced as "the day Kade pulled a guy out" or "the day Kade kept his head down."
#   - Persist flags: `helped_injured_worker` / `stayed_on_line`, `_foreman_cover_honest` / `_foreman_command_slip`, `act2_04_first_day_out.completed`.
