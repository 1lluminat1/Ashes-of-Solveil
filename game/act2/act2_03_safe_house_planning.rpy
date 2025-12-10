# =======================================================
# ACT 2 - Scene 3: Safe House Morning / Zira's Plan
# File: act2_03_safe_house_planning.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_03_safe_house_planning"
$ scene_mark(_current_scene_id, "entered")

label act2_safe_house_planning:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 28–35mm; mostly static with slow 3–4% drift; closer on Zira for "you can't hide" beats.
    # LIGHTING: Gray morning through the barred window; single bulb still on; flat, tired light.
    # SFX: Loop — distant machinery, muffled voices from the Unders; one-shots — lock beeps, door, supply packets.
    # FX/COMP: Slight fogged window; no exterior vista (keep claustrophobic).
    # BLOCKING/PROPS: Bedrolls on floor, small supply pile from last night, Bands, fake IDs near the wall.

    # VISUAL: Safehouse interior, morning after Reality Check.
    "Day 2."

    athought "Concrete under my back, stale air, the taste of metal and dust."

    "Aeron blinks up at the ceiling, then rolls to his side."

    # VISUAL: Lyra already awake, sitting against the wall, knees pulled up.
    "Lyra's already sitting against the wall, staring at nothing."
    "Her hand drifts to her Band again, thumb tapping the edge on reflex."

    athought "Second day in the Unders."
    athought "Still alive, still hunted, still trapped in a concrete box with no good options."
    athought "That has to count for something. Even if it doesn't feel like it."

    l "(quiet) Did you sleep at all?"
    a "Some. You?"
    l "Closed my eyes. My head didn't get the memo."
    a "Purge?"
    l "Purge. Sweep. The rooftop. Take your pick."

    athought "We sit in the same silence as last night—different weight, less shock, more gravity."

    # SFX: Lock beep + mechanical click.
    "The door beeps."

    athought "Both of us tense like we've been wired that way since birth."

    # VISUAL: Zira steps in with a small bag; kicks the door shut.
    z "Morning, fugitives."
    z "Good news, you're still breathing. Bad news, so is everyone who wants you dead."

    # VISUAL: She drops the bag between them; protein bars, water pouches.
    z "Breakfast. Try not to complain, it's better than half this building gets."
    a "You didn't have to—"
    z "I did. If you collapse in the street, it reflects badly on my reputation."

    # VISUAL: Aeron and Lyra take the food; exhausted, wary.
    athought "The bars are dry and tasteless, but they're calories. Water burns all the way down."

    athought "First meal as Kade Voss. Doesn't taste different."
    athought "Just cheaper."

    z "Alright. Reality check, day two."
    z "You got the speech last night. Bounty, fake names, everybody hates you. Any of that magically change while I was gone?"
    l "Doesn't feel like it."
    z "Right. So here's the part you didn't want to hear."

    # VISUAL: Zira leans against the wall near the door, eyes sharp.
    z "You can't stay in this room."
    z "Hide too long, people start asking questions. 'Who's paying for that door?' 'Who's Zira keeping in there?'"
    z "Questions get you killed down here as fast as bullets."

    a "We were letting things settle."
    z "You were stalling."
    z "Understandable. Still going to get you killed."

    # VISUAL: She nudges the pair of fake IDs with her boot.
    z "You wanted out of Aeries. Congratulations, you got it."
    z "Now you have to do the boring part—existing."
    z "Work, neighbors, people who'll vouch that Kade and Mira aren't walking execution orders."

    l "You think anyone down here is going to vouch for us?"
    z "Not for Glass and Lyra Rylan. For Kade Voss and Mira Chen? Maybe."
    z "If you don't screw it up."

    # VISUAL: Zira pulls a small slate from her jacket, flicks through something.
    z "There's a machine yard in Sector 6. Freight haulers, lift repairs, basic grunt work."
    z "Owner owes me three favors and needs warm bodies who can lift without crying."
    z "Today, that's you."

    a "You already set it up."
    z "Of course I did. You think I brought breakfast just to chat?"
    z "You go in as Kade and Mira. You keep your heads down, you don't talk about Aeries, and you do the work."
    z "If it goes well, you walk out with scrip and a boss who'll tell anyone asking that you've been around a while."

    athought "A job. In the Unders. Like none of the last seven years happened."
    athought "Glass doesn't clock in for shift work."
    athought "Kade Voss will have to."

    l "What if someone recognizes us?"
    z "Most people down here have better things to do than memorize Echelon rosters."
    z "But if someone does look twice, you lean on the cover. Sector 5 transfer. Lost your papers in the chaos. Whatever."
    z "The important part is you don't flinch."

    # --- PLAYER CHOICE: how does Aeron take this? ---
    menu:
        athought "Zira watches me, weighing whether I'm going to break or bend."
        "Admit you're not ready for this.":
            $ choice_and_dev(
                _current_scene_id, "_a2_03_admit_not_ready", "EMP", factor=1,
                next_scene_label="act2_04_first_day_out",
                note="Names fear instead of hiding behind procedure; small vulnerability in front of Zira and Lyra."
            )

            a "...I don't know how to do this."
            z "Do what? Hold a wrench? You've held worse."
            a "Be nobody. Walk into a yard and pretend I've always been there."
            a "I've spent seven years being exactly what they wanted. Now I have to pretend none of that happened."

            "Lyra looks at him."

            athought "Something like relief flickering through the exhaustion."

            l "We'll figure it out. Together."
            z "(softer, just a little) Good. Start by keeping your head up and your mouth shut."
            athought "She heard me and didn't mock me for it. That shouldn't feel strange, but it does."

        "Lock it down and treat it like an operation.":
            $ choice_and_dev(
                _current_scene_id, "_a2_03_treat_like_op", "OB", factor=1,
                next_scene_label="act2_04_first_day_out",
                note="Frames Unders job as mission; clings to familiar procedural mindset."
            )

            a "Give me parameters and a timeline. I'll execute."
            z "(snorts) There it is. The field report voice."
            a "You said this is about existing. Fine. I'll exist on schedule."
            l "(quiet) It's not a mission, Aeron."
            a "Everything's a mission now. Objective: survive the week."

            athought "Zira studies me, deciding if that answer is going to keep me alive or get me shot."

            z "Just remember, missions down here talk back. And they don't read your reports."

    # --- POST-CHOICE COMMON BEAT ---
    # VISUAL: Zira pushes off the wall, crosses to the door again.
    z "Shift starts in an hour."
    z "Change into something that doesn't scream 'Aeries enforcer', then follow my lead."
    z "You're Kade and Mira the second we hit the street. Say it."

    a "Kade Voss."
    l "Mira Chen."
    z "Good. Keep repeating it until it feels boring. Boring survives down here."

    # VISUAL: She opens the door; corridor beyond, dim and narrow.
    athought "The hallway outside is a tunnel of peeling paint and bad wiring. Voices echo from the stairwell two floors down."

    athought "From Glass to Kade. From command decks to shift schedules."
    athought "If this is what it takes to stay alive long enough to burn them, then this is where it starts."

    # VISUAL: Aeron and Lyra step up beside Zira, ready to leave.
    l "(quiet, to him) One day at a time."
    a "One day at a time."

    "Zira doesn't look back as she leads them out."
    "The door to the safehouse shuts behind them with a hollow metal thud."

    # TRANSITION: Cut to black / exterior establishing before machine yard
    athought "Time to see if Kade Voss survives his first day."

    $ scene_mark(_current_scene_id, "completed")

    # Hand off to the first Unders-work scene.
    jump act2_04_first_day_out

# ========= CANONICAL NOTES =========
# cann.scene_id: act2_03_safe_house_planning
# cann.when_in_timeline:
#   - Morning after Act2_02 Reality Check; second day in the Unders.
# cann.what_happened:
#   - Zira brings basic breakfast; reinforces that hiding in the safehouse is not sustainable.
#   - She arranges a first cover job for Aeron and Lyra at a Sector 6 machine yard.
#   - Fake IDs (Kade Voss / Mira Chen) are framed as lived identities, not just cards.
#   - Zira makes clear that "existing" in the Unders means work + neighbors + reputation.
# cann.aeron_state:
#   - Still OB-lean baseline, but shaken; choice:
#       • EMP branch: openly admits he doesn't know how to "be nobody".
#       • OB branch: frames everything as an "operation" to keep control.
# cann.path_tracking:
#   - One `choice_and_dev` decision:
#       • `_a2_03_admit_not_ready` → EMP +1 weight.
#       • `_a2_03_treat_like_op`   → OB +1 weight.
#   - Running empathy range at scene end: -8 to -2 (prior range ±1 from this choice).
# cann.thematic_flags:
#   - Motifs: Nobody/cover identities, work as survival, "boring survives".
#   - Bridges: from "we're fugitives in a box" to "we're part of the Unders whether we like it or not".
# cann.block_status:
#   - ANCHOR scene; single binary choice that nudges alignment but doesn't change external outcome.
# cann.requires_followup:
#   - Next scene: `act2_04_first_day_out` at the machine yard (work + reputation seed).
#   - Persist flags: none required beyond `completed` and whatever `choice_and_dev` logs internally.
