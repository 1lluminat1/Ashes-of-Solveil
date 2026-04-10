# ===================================================
# ACT 1 - Scene 6: The Gala  [PILOT — Political Fluency Pass]
# File: a1_s06_gala_PILOT.rpy
# ===================================================
# This is a targeted voice recalibration of a1_s06_gala.rpy.
#
# Core shift: Aeron is not an outsider observing alien architecture.
# He is a native of this room — fluent in etiquette, attentive to
# micro-politics, reading the ledger of favors and rivalries the
# way he reads patrol patterns. The exhaustion isn't from being
# overwhelmed by the environment. It's from the cost of maintaining
# the performance in an environment he has completely mastered.
#
# The Band absence is not shame. It's a calibration tool — he deploys
# it as political leverage because Marcus trained him to turn the
# wound into a weapon. Every glance at his wrist is a ledger entry.
#
# Choice architecture, state calls, and flags are preserved exactly.
# Only voice, texture, and named-official beats are new.
# ===================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a1_s06_gala"
$ scene_mark(_current_scene_id, "entered")

define e1 = Character("Elite 1")
define e2 = Character("Elite 2")
define e3 = Character("Elite 3")
define ye1 = Character("Young Elite 1")
define ye2 = Character("Young Elite 2")
define ye3 = Character("Young Elite 3")
define cadet = Character("Daren")

# NEW: Recurring named Aeries figures. These are people Aeron has
# histories with — not strangers, not ciphers. They should feel like
# part of the court he grew up navigating.
define varnix = Character("Councilor Varnix")
define kessler = Character("Commander Kessler")


label a1_s06_gala:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: 35-38mm stabilized glide. Aeron's face is composed and visible from entry —
    #         the mask is on, the mask is working, and we see the cost running beneath it
    #         through voice-over, not posture. Push 2-3% on political micro-exchanges.
    # LIGHTING: Performative warmth (3000K chandeliers) over cold marble base (5200K bounce);
    #           3:1 key/fill; soft rim from sconces.
    # SFX LOOP: Strings + low conversation bed (-18 LUFS).
    # SFX ONE-SHOTS: Glass clinks, soft heel clicks, hinge sighs, the specific sound of
    #                silk gowns brushing marble.
    # FX/COMP: Subtle specular blooms, reflection cards on floor, dust motes in chandelier light.
    # BLOCKING: Chandelier cluster, portrait wall spill, holo-feeds rotating above bar,
    #           Council attachés orbiting. Aeron moves through the space with the deliberate
    #           ease of someone completing choreography he has performed a hundred times.
    # FACE: He wears the ballroom the way he wears the uniform — fluently, exhaustingly,
    #        without tell. Only his internal monologue shows the strain.

    # ========= OPENING — THE BALLROOM =========
    # VISUAL: Aeron enters on cue. Doesn't hesitate at the threshold. Doesn't scan.
    #         The posture of someone walking into his own building.

    "The ballroom is the same as it was six months ago. Same chandelier cluster. Same arrangement of sconces. Same strings the Council pays extravagantly for because the Council always pays extravagantly for strings."

    pause 0.5

    athought "Third chandelier from the north wall still has a bulb out. They never replace it. Nobody is willing to admit they noticed."

    # VISUAL: Aeron accepts a glass from a passing servant without looking. The servant
    #         doesn't break stride. Familiar choreography.

    athought "Delvenne white. Same vintage as the last Council dinner. They're either economizing or sending a signal I haven't decoded yet."

    athought "Both are possible. Both are interesting."

    # ========= THE READ =========
    # NOTE: Aeron takes the room apart in the first ninety seconds the way he'd clear
    #        a hallway before a breach. Same skill, different weapons.

    athought "Councilor Varnix is here — left side, near the wine. He brought the younger Vexne daughter instead of his wife, which means the wife is either ill or he's signaling displeasure with the Vexne alignment. Probably the second. She was supposed to introduce a finance bill last week and didn't."

    athought "Commander Kessler is absent. Kessler never arrives before the General. Kessler is a man who measures his entrances."

    athought "Ambassador Kaine pretends not to see me — courtesy, not insult. She doesn't owe me the acknowledgment tonight. Three months ago she owed it. That means something shifted and I missed the paperwork."

    # ========= THE FIRST TRANSACTION =========
    # VISUAL: A deputy — middle-aged woman, senior Council staff — inclines her head
    #         as Aeron passes. He returns it with precise reciprocal depth. Neither slows.

    "Three steps. A nod to Deputy Serrin — she returns it a fraction slower than last time."

    athought "Which means she's heard something about Sector Seven. She isn't sure whether to adjust her alignment yet. She will be by tomorrow morning."

    "Five steps. A servant he doesn't recognize recovers from a near-collision and inclines his head a degree deeper than protocol demands."

    athought "New hire. Trained by someone who told him to show extra deference to the Rylan name. I should find out who trained him. The name is useful."

    athought "Six hours ago I killed four people in Sector Seven. Now I'm cataloging the household staff of the Aeries central kitchens because one of them bowed three degrees too deep."

    athought "Both things are practiced. Neither gets noticed unless I let it show."

    # ========= COUNCILOR VARNIX =========
    # VISUAL: Councilor Hale Varnix separates from his group with the smoothness of a man
    #         who has been doing this for forty years. Wine in his left hand, right hand free.
    #         He crosses to Aeron with the deliberate path of someone initiating a conversation
    #         by design, not by chance.

    varnix "Aeron. I was beginning to wonder if you'd grace us tonight."

    a "Councilor Varnix."

    # VISUAL: The handshake is brief and firm. Varnix's cuff pulses faintly — a senior Band,
    #         ceremonial level, signaling rank rather than tactical capability.

    athought "His eyes don't drop to my wrist. They used to, the first few years. He trained himself out of it. That's a compliment — one of the subtler ones available in this room. Also a ledger entry I don't get to settle."

    varnix "Sector Seven. Pre-dawn. And you're upright in formal dress before the entrées."

    a "Recovery is for officers who need it, Councilor."

    varnix "(small smile) Your father said almost the same thing at my commissioning. Almost."

    athought "He's telling me three things at once. One: he knew Marcus when Marcus was still being commissioned, which means he outranks my father in institutional memory even if not in current authority. Two: my phrasing was slightly off from Marcus's original. Three: he noticed the difference, which means I've used the line enough times for him to compare versions, which means I need to vary it."

    varnix "I'll want a word later. Section Six allocations. Your father mentioned you had views."

    a "I have whatever views the General assigns me, Councilor."

    varnix "(softer) You have more than that, Aeron. I've been watching you at these functions since you were twelve. I know the difference between recitation and position."

    # VISUAL: Something in Varnix's face is almost kind. Almost.

    athought "He's offering me something. I don't know what yet. When I figure out what he wants in return, I'll know what accepting costs."

    a "I'll make myself available, Councilor."

    varnix "Good. Enjoy the evening, Aeron."

    "He rotates away smoothly. Toward the Vexne daughter. The ledger is open but not yet written in."

    pause 0.7

    athought "That was three moves and I counted only two of them. I'm tired."

    # ========= DAREN ENCOUNTER =========
    # VISUAL: A young man in full ceremonial dress approaches — confident stride, silver
    #         Band glinting at the cuff. Nervous underneath, hiding it well enough that
    #         most people in the room wouldn't catch it. Aeron catches it in the first
    #         second because Aeron catches everything.

    cadet "Aeron Rylan. Thought that was you."

    # VISUAL: Aeron turns. Different face than the one he showed Varnix — warmer by a
    #         fraction, the Academy-peer greeting rather than the Council protocol.

    a "Daren."

    cadet "Been a while."

    a "Three years. Since the promotion cycle. You made Cadet-Captain."

    # VISUAL: Handshake. Daren's Band pulses brighter than Varnix's — newer, lower rank,
    #         but active capability rather than ceremonial.

    athought "I remember other people's promotions. Marcus taught me it's cheaper than flowers and more useful than prayer."

    cadet "(pleased someone noticed) Three months ago. I didn't think you tracked cycles."

    a "I track everything I'm expected to acknowledge, Daren. It's how the room stays oriented."

    cadet "(glances at medals, impressed) Heard about your last operation. Sector Nine?"

    a "Sector Seven. This morning."

    cadet "(surprised) This morning? And you're here tonight?"

    a "Here is the assignment."

    athought "That was sharper than it needed to be. Daren doesn't deserve the edge. He's the same boy who shared his rations the week of the Academy purity drills."

    athought "I should remember that. I keep forgetting to remember that."

    # VISUAL: Daren recovers. His hand drifts — almost involuntarily — to his own Band.
    #         Touching it like a talisman. Aeron sees the gesture and files it.

    cadet "Your record is insane. 390 operations, zero failures?"

    a "Metrics don't lie."

    cadet "That's... that's impossible. In seven years?"

    a "Not impossible. Just expensive."

    cadet "(uncomfortable) I didn't mean—"

    a "You did. And you're not wrong. The word you were reaching for was inhuman. It's the standard compliment at these functions. You don't have to apologize for using it."

    # VISUAL: Daren's Band hand freezes mid-gesture. He's realizing that Aeron noticed the
    #         talisman touch. Realizing that Aeron notices everything.

    athought "The gesture tells me he's afraid I'm contagious. That the absence is something he could catch. That's not his fault. He was raised on the same doctrine I was."

    athought "I should let him off the hook. Instead I'm watching him discover that I can see the fear he didn't know he was showing."

    athought "This is how Marcus trained me to handle people who touch their Bands near me. Never comment. Never flinch. Just see it, and let them see that I saw. The asymmetry is the point."

    pause 0.7

    cadet "Your father must be... proud."

    a "He has expectations. I meet them."

    cadet "That's... that's all any of us can do, right?"

    a "(looks at him directly) Is it?"

    "For a moment, something passes between them — not quite understanding, just distance made visible."

    pause 0.8

    # ========= PLAYER CHOICE — DAREN RESPONSE =========

    menu:
        athought "Daren's smile wavers. I can reset the room or I can let it stay cracked."

        "Respond with cold courtesy.":
            $ choice_and_dev(
                _current_scene_id, "_daren_cold_courtesy", "OB", factor=1,
                next_scene_label="a1_s07_balcony",
                note="Reasserts performance persona; reinforces fear/respect myth."
            )

            a "Enjoy the gala, Daren."

            # VISUAL: Aeron smooths the interaction closed with the precision of a man
            #         returning a chess piece to its starting square.

            cadet "Yeah. You too. Stay... stay sharp."

            "He retreats into the crowd, grateful for the exit."

            pause 0.7

            athought "He'll tell the story tomorrow. 'Rylan, at the gala, six hours after a kill, talked to me for two minutes, didn't blink.' He'll tell it wrong and it will flatter both of us. That's fine. That's the trade."

        "Acknowledge the awkwardness.":
            $ choice_and_dev(
                _current_scene_id, "_daren_acknowledge", "EMP", factor=1,
                next_scene_label="a1_s07_balcony",
                note="Permits vulnerability without breaking form; micro-connection."
            )
            $ scene_mark(_current_scene_id, "acknowledge_daren")
            $ tp_seed("a1.gala.daren_ack")

            if pass_tier("EMP1", "EMP2", "EMP3"):
                a "You don't have to do this."
                cadet "(confused) Do what?"
                a "(softer) Pretend we're still who we were. We're not."
            else:
                a "You don't have to pretend. We're not friends anymore."

            cadet "(pause) …No. I guess we're not."

            "For a moment, something real passes between them—fragile, brief, almost painful."

            pause 0.8

            cadet "(quieter) Take care of yourself, Aeron. If you still can."

            a "I'll try."

            athought "That was me refusing to deploy a skill I'm supposed to deploy. Marcus would call it a lapse."
            athought "I'm going to let him call it that."

            jump a1_s06a_daren_flashback

    # ========= POST-DAREN AMBIENT =========

    if scene_has(_current_scene_id, "acknowledge_daren"):
        "The music resumes like it never stopped. Conversations blur back into motion."

        pause 0.7

        athought "The past is always closer than I think."

    # ========= COMMANDER KESSLER =========
    # VISUAL: Commander Kessler has arrived. Aeron noted it peripherally — the specific
    #         weight shift when the General's rival enters. Kessler is sixty, silver-haired,
    #         political smile permanent. Military uniform slightly more decorated than
    #         strictly protocol allows.

    "Commander Dreya Kessler catches his eye from across the bar. She lifts her glass — a quarter-inch tilt, not quite a toast, not quite nothing."

    athought "Kessler. Fourth Fleet. My father's chief rival inside the Military Division."

    athought "The quarter-tilt means 'I acknowledge your presence and we should speak later, but not publicly.' She's invited me to a private conversation and pre-emptively denied having invited me, all in one gesture."

    athought "She's been using me as a proxy for Marcus since I was nineteen. She thinks the fact that I notice makes the game more interesting."

    athought "She's right."

    # VISUAL: Aeron returns the gesture — a micro-nod — without breaking stride.

    athought "I'll find her later. Or she'll find me. Or we'll pass each other and exchange one sentence that contains three different statements. Any of those outcomes is acceptable. All of them cost me something I don't have a word for."

    # ========= ELITE WHISPERS — REFRAMED =========
    # NOTE: In the pilot rewrite, the whispers aren't about Aeron being observed.
    #       They're about Aeron parsing political signals being transmitted
    #       through "whispers" that are meant for him to overhear.

    "Nearby, a cluster of mid-tier officials. Their voices drop just low enough to pretend they're private."

    pause 0.5

    e1 "...Marcus Rylan's son."
    e2 "390 operations. Zero failures."
    e1 "Is that strength... or vacancy?"

    athought "They're not whispering about me. They're whispering FOR me — close enough to hear, loud enough to be intentional. The question isn't rhetorical. It's a probe."

    athought "Whoever asked it wants to see how I'll respond. Do I look up? Pretend not to hear? Smile?"

    # ========= BRANCHING — INTERNAL RESPONSE =========

    if pass_tier("OB2", "OB3"):
        athought "I let them wonder. A wondering court is a careful court, and a careful court doesn't interfere."
        athought "Fear as infrastructure."
    elif pass_tier("OB1", "NEU"):
        athought "The probe is too clumsy for anyone important. A junior staffer testing an angle for their patron."
        athought "I'll ignore it. The ignoring itself will be reported. That's the useful part."
    else:
        athought "They want a myth. I keep giving them the cracks instead."
        athought "Tonight I'm too tired to correct the myth. Let it slip a little."

    # ========= MARCUS ENTRANCE =========
    # VISUAL: Marcus entrance — ceremonial armor; Enforcers flank; room tension rises.
    # CAMERA: Wide shot of the room pivoting toward the entrance. Everyone notices.

    "General Marcus Rylan steps into the light — armor flawless, formation exact, presence absolute."

    pause 0.7

    "The room exhales. Every conversation pauses. Every eye tracks."

    pause 0.7

    athought "I've seen this entrance a hundred times. It still works. That's what makes it an entrance."

    athought "Kessler straightens half a degree. Varnix doesn't move at all — the refusal is its own statement. Three separate attachés reorient toward the Council wing, which means at least one pending motion just died on the floor."

    athought "The real work of this room happens in the three seconds after Marcus arrives. Everyone who matters is adjusting to him right now. I could name the adjustments by watching the shoulder blades."

    # ========= BRANCHING — MARCUS'S REACTION =========

    if pass_tier("OB2", "OB3"):
        athought "His gaze finds mine for the briefest second — a subtle nod, approval measured in microseconds."
        athought "He's read the reports: Sector Seven, the body count, no hesitation noted."
        athought "This is what he wanted. Precision, purity, obedience."
        athought "I should feel something about that."
        $ scene_mark(_current_scene_id, "marcus_approval")

    elif pass_tier("OB1", "NEU"):
        athought "His gaze meets mine, unreadable — a flicker that could be approval or warning."
        athought "Hard to tell anymore. Harder to care."
        $ scene_mark(_current_scene_id, "marcus_uncertain")

    else:
        athought "His eyes sweep past mine — no pause, no nod, just calculation."
        athought "He's read the report. Saw the hesitation. Noted the deviation from protocol."
        athought "This isn't what he trained me for."
        $ scene_mark(_current_scene_id, "marcus_disapproval")

    # ========= LYRA SIGHTING =========
    # VISUAL: Lyra across the hall with a Councilwoman — composed, precise, unmissable.
    # CAMERA: Mid-shot; chandelier bokeh; her posture is perfect but her eyes are tired.

    "Across the hall, Lyra stands with a Councilwoman — composed, precise, unmissable."

    pause 0.7

    athought "She's being displayed. The Councilwoman is Varnix's junior ally, which means Lyra is tonight's proof that the Aether Bands still produce exemplary citizens. They want her in this exact spot so that anyone looking my way has to see her first."

    athought "The framing is deliberate. I'm supposed to be reminded."

    "Her eyes flick to Aeron for a heartbeat — then back, deliberate, controlled."

    pause 0.6

    # ========= PLAYER CHOICE — ACKNOWLEDGE LYRA =========

    menu:
        athought "Lyra's eyes meet mine for a heartbeat. The room will read whatever I do next."

        "Acknowledge her.":
            $ choice_and_dev(
                _current_scene_id, "_ack_lyra", "EMP", factor=1,
                next_scene_label="a1_s07_balcony",
                note="Micro-acknowledgment; tests willingness for connection under surveillance."
            )
            if pass_emp():
                $ rel_bump("Lyra", affection=1)
            $ scene_mark(_current_scene_id, "acknowledge_lyra")

            athought "I nod. Barely. The room notes it and files it."

            athought "So do I."

        "Look away.":
            $ choice_and_dev(
                _current_scene_id, "_ignore_lyra", "OB", factor=1,
                next_scene_label="a1_s07_balcony",
                note="Maintains performance seal; avoids signaling under optics."
            )
            $ scene_mark(_current_scene_id, "ignored_lyra")

            athought "I let the moment pass. Safer that way. No signal to be read, no exchange to be logged."

            athought "Varnix will notice. So will Kessler. They'll each draw a different conclusion. That's fine. Ambiguity is also a position."

    # ========= BRANCHING — LYRA READ =========

    if pass_emp():
        athought "She sees it — not the medals, not the posture. The strain underneath."
        athought "Maybe she remembers what I was before the edges hardened."
    else:
        athought "She sees exactly what they built and doesn't flinch. No pity, no softness — just recognition."

    # ========= YOUNGER ELITES — THE REAL WHISPERS =========
    # NOTE: This group is different. They're not sending signals — they're gossiping
    #       because they think they're anonymous. This is the whisper with teeth.

    ye1 "I heard he's done nearly 400 operations."
    ye2 "In seven years? That's impossible."
    ye1 "Not impossible. Just inhuman."
    ye3 "They say Rylan stripped the belief right out of him. Now there's nothing left but the edge."
    ye2 "The edge?"
    ye3 "Cold, efficient — cuts when you need it."
    ye1 "(quietly) Has he ever failed?"
    ye3 "Not yet. But they say he's starting to hesitate."
    ye2 "How can you tell if something that cold is breaking?"
    ye3 "You can't. Not until it turns on you."

    athought "They're not wrong."

    athought "Six hours ago I executed four people. Now I'm holding wine."

    # ========= PLAYER CHOICE — APPROACH LYRA =========
    # VISUAL: Lyra momentarily alone as the Councilwoman steps away.

    menu:
        athought "Across the room, Lyra is momentarily alone."

        "Cross the floor toward her.":
            $ choice_and_dev(
                _current_scene_id, "_approach_lyra", "EMP", factor=1,
                next_scene_label="a1_s07_balcony",
                note="Chooses connection under optics; seeds balcony rendezvous."
            )
            $ scene_mark(_current_scene_id, "approach_lyra")

            "The crowd parts around him — silk and medals, perfume and wariness — as he closes the distance."

            pause 0.5

            athought "Nine meters. I'll pass three conversations. Two of them will pretend not to see me. One will pretend harder. Varnix is watching. Kessler is watching. The junior staffer who ran the probe earlier is watching."

            athought "I am crossing this room in front of every person who matters. That is the entire political statement. The conversation with Lyra hasn't even started yet and it has already been noted by the people who take notes."

            # VISUAL: Councilwoman lingers, then steps aside. Lyra pivots to face him.

            a "Lyra."

            "She pivots, posture precise, eyes reading him in a single beat."

            pause 0.7

            l "Precise. I calculated you would approach within three minutes."

            athought "Her voice is steady, but her eyes aren't. How long since she slept? Days? Weeks?"

            if pass_tier("EMP2", "EMP3"):
                a "Funny. I still remember the lines. Doesn't mean I believe them."
                l "Belief was never required. Only performance."
                a "You've heard the stories."
                l "Everyone has. But stories change in retelling."
            elif empathy_band() == "obedience":
                a "On time is the same as willing."
                l "That's what they say. And what they need."
                a "And you?"
                l "I don't need belief. I need results."
            else:
                a "On time, not exactly willing."
                l "Willingness was never part of the design."
                a "(half-smile) I'm starting to notice."

            "A council attaché leans in with a whisper. Lyra's attention splits — only for a moment."

            pause 0.7

            l "The balcony. Five minutes."

            a "I'll be there."

            l "(softer) I want to see what's behind the uniform."

            "She's gone before the room notices she moved."

            pause 0.7

            athought "She sees it."

            $ scene_mark(_current_scene_id, "balcony_meet_set")

        "Keep your distance.":
            $ choice_and_dev(
                _current_scene_id, "_keep_distance", "OB", factor=1,
                next_scene_label="a1_s07_balcony",
                note="Avoids connection; preserves performance shell."
            )

            "The moment passes. The distance stays."

            pause 0.7

            athought "I don't need connection. I function alone."

            athought "...So why does that feel wrong tonight?"

    # ========= TRANSITION TO BALCONY =========
    # VISUAL: The crowd shifts. Music fades. Cold air bleeds in from somewhere.

    "The crowd shifts again — music fading, conversations thinning. Aeron feels the familiar exhaustion that comes after two hours of maintaining the room. His jaw aches from the micro-expressions. His wrist is visible and has been visible all night and every person in the building has noticed and not mentioned it and the not-mentioning is its own kind of work."

    pause 0.7

    "Somewhere, doors open. Cold air rushes in."

    pause 0.7

    athought "Time to breathe."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a1_s06_gala
# cann.chapter: Act I — (chapter placement unchanged)
# cann.when_in_timeline: Act I, immediately after Hallway; before Balcony rendezvous.
# cann.what_happened:
#   - Aeron enters the Gala as a fluent native of the court, not an outsider observing it.
#   - Named officials seeded: Councilor Varnix (senior, mentor-investor), Commander Kessler
#     (Marcus's rival, uses Aeron as proxy).
#   - Political micro-choreography visible: reads the room in the first 90 seconds, catalogs
#     alignments, deploys reciprocal courtesy, parses signals being transmitted through
#     "accidentally overheard" conversations.
#   - Daren encounter preserved; Aeron's voice recalibrated to someone managing the
#     interaction rather than being cornered by it.
#   - Marcus entrance: Aeron sees it as choreography he knows by heart, and watches the
#     room adjust to his father's gravity.
#   - Lyra sighting: framed as deliberate display — Aeron reads the political staging.
#   - Lyra approach: the crossing itself is a political statement; Aeron knows who's watching.
# cann.aeron_state:
#   - Fluent in Aeries political culture at the deepest level.
#   - Exhausted by the maintenance of that fluency, not overwhelmed by the environment.
#   - Band absence is weaponized as calibration leverage, not shame.
#   - His internal monologue is a running political ledger, not raw sensory processing.
# cann.path_tracking:
#   - Choice weights unchanged from original scene:
#       • Daren choice: OB (cold courtesy) vs EMP (acknowledge) → ±1 weight ×1
#       • Lyra glance: OB (look away) vs EMP (acknowledge) → ±1 weight ×1
#       • Approach Lyra: EMP (approach) vs OB (keep distance) → ±1 weight ×1
#   - TP seed preserved: a1.gala.daren_ack on EMP acknowledgment branch.
# cann.thematic_flags:
#   - Motifs: Political fluency as inherited weapon / Band absence as calibration tool
#     / Performance as ledger / Exhaustion from mastery, not from alienation
#   - Recurring lines seeded: "Six hours ago I killed four people. Now I'm holding wine."
#     retained as the scene's emotional spine.
#   - New motif: "I should find out who trained him. The name is useful." — the trained
#     habit of treating every person as a potential future lever.
# cann.character_moments:
#   - Varnix: senior Council; knew Marcus before Marcus was Marcus. His not-looking at
#     Aeron's wrist is a compliment he trained himself into.
#   - Kessler: military rival to Marcus. Uses Aeron as a proxy channel. Micro-gesture
#     exchanges with Aeron that nobody else in the room can parse.
#   - Daren: unchanged from original beats, but Aeron's voice treats him as a former
#     peer he's managing rather than a confrontation he's enduring.
#   - Lyra: framed as a political display, which is how the court sees her and how
#     Aeron has learned to see her too — even while knowing she's more than that.
# cann.block_status: ANCHOR (fixed interior flow) with VARIANT beats preserved.
# cann.true_path_integration:
#   - tp_seed("a1.gala.daren_ack") preserved on EMP acknowledgment branch.
#   - Additional TP-adjacent texture: multiple beats where Aeron notices his own political
#     fluency and is tired of it — seeding the later "refusal" arc.
# cann.visual_plate_economy:
#   - REUSE: Wide master of ballroom with lighting passes; crop/push for micro-exchanges.
#   - REUSE: Marcus entrance plate with different crowd masks.
#   - HERO: Lyra micro-CU with chandelier bokeh; Aeron crossing the floor toward her.
#   - NEW: Varnix handshake CU; Kessler quarter-tilt glass gesture.
# cann.requires_followup:
#   - If `balcony_meet_set` → load a1_s07_balcony after short breath beat. Unchanged.
#   - Varnix should recur in late Act 1 / early Act 2 if any post-defection callbacks
#     are desired. His "word later about Section Six" is an unresolved thread.
#   - Kessler should recur as a recurring named Echelon figure across Acts.
# cann.consistency_asserts:
#   - Lyra Act I diction: formal, minimal contractions.
#   - Aeron in the Aeries: fluent, exhausted, politically literate. Not alien.
#   - Band absence: calibration tool, not shame.
