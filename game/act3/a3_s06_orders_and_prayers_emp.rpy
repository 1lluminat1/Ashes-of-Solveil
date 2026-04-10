# =======================================================
# ACT 3 - Scene 06: Orders and Prayers (Empathy Path)
# File: a3_s06_orders_and_prayers_emp.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s06_orders_and_prayers_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s06_orders_and_prayers_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 32mm lens (EMP warmth). Three-shot framing: Lyra, Selene, Aeron between.
    #         When Lyra and Selene argue, camera favors two-shots that exclude Aeron —
    #         he's in the room but not in the frame. Their conflict. His job: hold the space.
    #         Slow lateral tracking during the moral argument. No cutting — let it breathe.
    # LIGHTING: War room: tactical greens from holo-displays, amber practicals along walls.
    #           The map casts uplight on faces — makes them look like they're arguing by firelight.
    #           When they reach agreement, warmer key. Not resolution — détente.
    # SFX: Loop — war room ambient: low electronics, ventilation, distant base activity.
    #      One-shots — map zoom, datapad tap, chair shift, palm on table.
    # FX/COMP: Holo-map showing Sector 9 industrial zone. Civilian density overlay in orange.
    #          Strike vectors in blue. The overlap is the problem.
    # BLOCKING: War room table. Selene standing, leaning on the table — command posture.
    #           Lyra standing opposite — not subordinate, equal. Arms crossed, then uncrossed.
    #           Aeron seated between them. Mediator position. He doesn't stand until they need him to.
    # CANON: Pair Anchor A3_P08 (Lyra x Selene). These two have circled each other since Act 2.
    #        This is where they stop circling and start building.
    #        The guardrails they set here govern ALL remaining Act 3 EMP operations.
    # FACE: Selene — controlled intensity, jaw set, hands flat on the table.
    #        Lyra — quiet fire, composure fraying at the edges, conviction underneath.

    # ========= VOICE BASELINE =========
    # EMP cadence: Contractions, emotional availability, but sharpened by the stakes.
    # Selene: Tactical. Direct. Not cruel but not sentimental. She sees the map.
    # Lyra: Moral. Precise. Not naive but not willing to pay certain prices. She sees the people.
    # Aeron: Mediator. He holds space for both. Doesn't decide — facilitates.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - DAY]
    # The holo-table shows Sector 9's industrial zone. Blue strike vectors.
    # Orange civilian density overlay. The two colors bleed into each other.

    #scene bg_war_room_emp with dissolve
    #play ambient "sfx/ambient/war_room_active.ogg" fadein 2.0

    # --- OPENING: THE BRIEFING ---

    "The map is the problem."

    "Sector 9 industrial zone. An Echelon supply node feeding three patrol districts. Take it out, and the eastern checkpoints go blind for seventy-two hours."

    "The blue strike vectors are clean. Efficient. Three teams, coordinated entry, controlled demolition."

    "The orange civilian overlay is the complication."

    sel "Twelve hundred workers in the adjacent processing plant. Shift change at 0300 gives us a ninety-minute window with minimal foot traffic."

    sel "Minimal. Not zero."

    athought "She's being honest about the margin. That matters."

    n "Current projections estimate between forty and sixty civilians in the blast proximity zone during the optimal window. Mostly overnight maintenance crews and transport workers."

    l "Forty to sixty people."

    sel "In the proximity zone. Not the kill zone. The structural analysis shows—"

    l "Forty to sixty people who didn't choose to be near an Echelon supply node."

    athought "And there it is. The line drawn in the air between them."

    athought "Selene sees vectors. Lyra sees faces."

    athought "They're both right. That's the problem."

    # --- THE ARGUMENT ---

    # VISUAL: Selene leans forward on the table. Lyra uncrosses her arms.
    # CAMERA: Two-shot excluding Aeron. Their conversation.

    sel "We've been over this. The eastern checkpoints supply three detention facilities. Every day those checkpoints operate, people are processed through them."

    sel "Processed. Your word, Lyra. You know what that means better than anyone at this table."

    athought "That lands. Lyra's jaw tightens."

    l "I know exactly what it means. Which is why I'm not willing to become the thing that processes people."

    sel "No one is being processed. We're disrupting a supply chain."

    l "With forty to sixty people in the proximity zone."

    sel "Proximity. Not impact."

    l "Proximity is impact for anyone standing in it."

    "Silence. The map rotates slowly. Blue and orange bleeding together."

    athought "They're not wrong. Either of them."

    athought "Selene's calculus is correct — the checkpoints feed detention, and detention feeds the machine."

    athought "Lyra's principle is correct — the moment we accept civilian proximity as an acceptable variable, we've become what we're fighting."

    athought "I'm sitting between two moral frameworks that don't have a shared unit of measurement."

    # --- SELENE PUSHES ---

    sel "What's the alternative? We wait? The checkpoints stay active. People keep being taken."

    sel "That's not neutrality, Lyra. That's a choice. Inaction is a body count too."

    l "I'm not arguing for inaction. I'm arguing for precision."

    sel "We are being precise. This is the most precise plan we have."

    l "Then we need a better plan."

    sel "We don't have time for a better plan. The supply rotation changes in four days."

    "Lyra turns to the map. Studies it. The analyst in her is visible — the part that used to read Echelon logistics for a living."

    l "What if we moved the window? Not 0300 — 0100. The maintenance crews rotate at midnight. The transport workers don't arrive until 0230."

    n "That narrows the civilian estimate to eight to fifteen. But it also reduces our operational window to forty minutes."

    sel "Forty minutes for a three-team coordinated strike. That's dangerously tight."

    l "Dangerously tight is not the same as impossible."

    athought "She's not wrong."

    athought "Neither is Selene."

    # --- AERON MEDIATES ---

    # VISUAL: Aeron stands. Not asserting — bridging. He moves to the map.
    # CAMERA: Three-shot returns. He's in the frame again.

    a "Can I say something?"

    sel "You've been quiet long enough."

    a "That's because this isn't my argument. It's yours."

    athought "They both look at me."

    a "Selene, you're right that inaction costs lives. The checkpoints are a machine, and every day we leave them running, someone goes through them."

    a "Lyra, you're right that the moment we accept civilian casualties as a planning variable, we've lost something we can't get back."

    a "You're both right. And that means the answer isn't in the math."

    sel "Then where is it?"

    a "In the rules you set together. Right now. Before the pressure makes the decision for you."

    # --- THE NEGOTIATION ---

    # VISUAL: Selene and Lyra facing each other across the map. The light from below
    # casting upward shadows. Two women building a framework in real time.

    athought "The room changes. Not the temperature — the posture."

    athought "They stop arguing at each other and start building with each other."

    sel "What are you proposing?"

    l "Guardrails. Hard limits. Not guidelines — rules we don't break."

    sel "Such as?"

    l "Minimum civilian clearance. If the proximity estimate exceeds a threshold, we don't proceed. We find another way or we don't go."

    sel "What threshold?"

    l "Zero in the kill zone. Fewer than ten in the proximity zone. Non-negotiable."

    sel "Ten is tight."

    l "Ten is ten human beings."

    "Selene studies her. The tactical mind weighing the moral argument."

    sel "Five operations in, we'll hit a target where ten is impossible. What then?"

    l "Then we don't hit that target."

    sel "Even if leaving it active costs more than ten lives downstream?"

    athought "The hardest question. The one that doesn't have a clean answer."

    l "If we cross that line, we discuss it. Together. Both of us, plus Aeron. Full consensus. No unilateral calls."

    sel "You're asking me to share tactical authority on moral questions."

    l "I'm asking you to admit that tactical questions are moral questions."

    "The silence stretches. Selene's fingers drum once on the table. She stops them."

    sel "And what counts as unacceptable loss?"

    l "Any loss we wouldn't be willing to explain to the faces in the proximity zone."

    l "If you can't look at a maintenance worker and tell them why their life was an acceptable variable, then it wasn't acceptable."

    athought "Selene is quiet for a long time."

    athought "Not calculating. Listening."

    athought "That might be the most important thing she's done since I met her."

    # --- AGREEMENT ---

    sel "Alright."

    l "Alright?"

    sel "Guardrails. Zero in the kill zone. Ten or fewer in proximity. Full consensus for anything above the threshold."

    sel "And we revisit the rules every two weeks. Conditions change. The rules should be able to change with them."

    l "Agreed. But changes require the same consensus. No one loosens the guardrails alone."

    sel "Agreed."

    athought "They look at each other across the table."

    athought "Not friends. Not yet. Something harder and more useful."

    athought "Allies who trust each other's disagreement."

    "Selene extends her hand across the map. Lyra takes it."

    athought "The handshake is brief. Firm. No warmth in it — no pretense either."

    athought "This isn't affection. This is architecture."

    # --- THE REVISED PLAN ---

    sel "Now. The 0100 window. Noelle, run the forty-minute scenario."

    n "Already running it. Preliminary assessment: viable, with a twelve percent margin reduction on the extraction phase."

    l "What brings that margin back up?"

    n "A fourth team on overwatch. Dedicated to civilian corridor monitoring."

    sel "We don't have a fourth team."

    l "We do if I run it."

    athought "Selene looks at her."

    sel "You're volunteering for overwatch on a strike you spent twenty minutes arguing against?"

    l "I'm volunteering to make sure the guardrails hold in the field. Not just on the map."

    athought "Something shifts in Selene's expression. Not softness — recognition."

    sel "Alright. Four teams. 0100 window. Lyra on civilian overwatch."

    sel "Aeron, you're on point for the primary strike team."

    a "Copy."

    sel "And Lyra?"

    l "Yes?"

    sel "If the count goes above ten, you call it. No arguments. We pull back."

    l "You're giving me abort authority?"

    sel "I'm giving you what you earned."

    athought "Lyra blinks. Once."

    athought "I don't think she expected that."

    l "I won't waste it."

    sel "I know."

    # --- SCENE CLOSE ---

    # VISUAL: Wide shot. The three of them around the map. The blue and orange overlay
    # still bleeding together — but now there are lines drawn through it. Boundaries. Structure.

    "The briefing continues. Details, timelines, contingencies. The architecture of a strike built on shared principles."

    athought "This is what shared command looks like in practice."

    athought "Not consensus on every point. Consensus on the rules."

    athought "Selene brings the calculus. Lyra brings the conscience. And I hold the space between them."

    athought "It's messy. It's slower than unilateral command."

    athought "It might be the only thing worth fighting for."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ scene_mark(_current_scene_id, "anchor_seen")
    $ flag("civilian_guardrails_set", True)
    $ canon_set("civilian_guardrails", True)
    $ rel_bump("Lyra", trust=1)
    $ rel_bump("Selene", trust=1)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s06_orders_and_prayers_emp
# cann.chapter: Act III, Phase I — Proving Ground (Empathy Path)
# cann.chapter_start: False
# cann.pair_anchor: A3_P08 (Lyra x Selene)
# cann.when_in_timeline:
#   - Act III Phase I. After Woman from Sector 7 (s05a). Before Echelon Strikes Back (s07).
#   - Sector 9 strike being planned. Operational pressure mounting.
# cann.what_happened:
#   - Lyra and Selene clash over a proposed strike on a Sector 9 supply node.
#   - The conflict: forty to sixty civilians in the proximity zone during optimal window.
#   - Selene argues tactical necessity — the checkpoints feed detention facilities.
#   - Lyra argues moral thresholds — civilian proximity as an unacceptable variable.
#   - Aeron mediates without deciding. Holds space for both frameworks.
#   - They negotiate guardrails: zero in kill zone, ten or fewer in proximity zone.
#   - Full consensus required for anything above threshold. Revisited every two weeks.
#   - Lyra volunteers for civilian overwatch on the revised plan.
#   - Selene gives Lyra abort authority — recognition of her moral standing.
#   - The guardrails govern ALL remaining Act 3 EMP operations.
# cann.aeron_state:
#   - Mediator. Holds space. Doesn't decide — bridges.
#   - "Selene brings the calculus. Lyra brings the conscience. I hold the space between them."
# cann.path_tracking:
#   - EMP baseline. No branching choices — this is a structural/relationship scene.
#   - trust+1 for both Lyra and Selene.
#   - flag("civilian_guardrails_set") and canon_set("civilian_guardrails") for future gating.
#   - anchor_seen marker for pair tracking.
# cann.thematic_flags:
#   - Motifs: Blue vectors and orange civilians bleeding together on the map.
#   - "Tactical questions are moral questions." — Lyra's thesis.
#   - "Inaction is a body count too." — Selene's thesis.
#   - Architecture, not affection — the handshake is structural, not emotional.
#   - The guardrails as living document — revisited, not fixed.
#   - Abort authority as earned trust.
# cann.character_moments:
#   - Selene: Listens. Genuinely. Gives ground not from weakness but from recognition.
#     "I'm giving you what you earned." — respect, not concession.
#   - Lyra: The analyst and the conscience unified. She doesn't just argue — she solves.
#     Volunteers for overwatch to enforce her own principles.
#   - Aeron: "This isn't my argument. It's yours." — restraint as leadership.
#   - Noelle: Running numbers in the background. Pragmatic support for both sides.
# cann.block_status:
#   - Pair Anchor complete. Guardrails established for Act 3 EMP operations.
# cann.requires_followup:
#   - The guardrails will be tested in the Sector 9 strike execution scene.
#   - Lyra's abort authority becomes critical when a future op pushes the threshold.
#   - Selene and Lyra's working relationship — "allies who trust each other's disagreement."
#   - The two-week revisit clause should surface if conditions change significantly.
#   - Callbacks: accountability_promise (s01), shared_command_active (s01).
