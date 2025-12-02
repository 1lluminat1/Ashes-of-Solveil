# ======================================================
# ACT 1 — Scene 08: Flashback — Aeron & Lyra on the Hill
# File: act1_08_hill_flashback.rpy
# ======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_08_hill_flashback"
$ scene_mark(_current_scene_id, "entered")

label act1_08_hill_flashback:

    # ---------- Stage directions (cinema-first) ----------
    # CAMERA: 35mm shoulder-height two-shot; city in soft bokeh. Occasional 70mm inserts on hands/grass.
    # LIGHTING: Golden hour; low, warm key; gentle back rim; acceptable lens flare.
    # SFX: Soft wind, far-off perimeter buzz, distant city hum. No rain (outside Aeries but clear).
    # FX/COMP: Subtle grain; chromatic warmth; grass ripple cards for parallax.
    # BLOCKING/PROPS: Perimeter fence way off; scuffed Academy uniforms; blade of grass fidget prop.
    # Keep faces in profile for most of the scene; save a direct eye-line for late “don’t forget me.”
    # -----------------------------------------------------

    # VISUAL: Golden hour over a grassy hill beyond the perimeter fence.
    # COSTUME: Academy uniforms, slightly scuffed from sneaking out.

    athought "Years ago... before the Branding. Before Glass. Before everything broke."
    athought "We were both ten. Two years before our Brandings would define us."
    athought "There was this hill. Far enough for trouble. Close enough to still matter..."
    athought "...but rules never meant much to Lyra."

    # CAMERA: Static two-shot seated, city in the far bokeh.
    yl "If you could fly anywhere—no tech, no Band—just wings... where?"
    ya "Anywhere but here."
    yl "Lame answer."
    ya "...Somewhere with real trees. Not the plastic ones."

    yl "(grins) Nature boy, huh?"
    ya "Better than being stuck in a glass tower pretending it's perfect."
    yl "Glass tower. I like that. Transparent and empty."
    ya "And sharp if you're not careful."
    yl "(laughs) Everything in Aeries is sharp if you're not careful."

    # VISUAL: Lyra leans back on her hands; looks at the sky.
    yl "You know what I hate most about the Aeries?"
    ya "The people?"
    yl "(laughs) Well, yes. But also... the silence."
    ya "It's not silent. There's always music, chatter, broadcasts—"
    yl "Exactly. Noise pretending to be life. But no one actually says anything real."

    # VISUAL: Young Aeron looks at her—something shifts in his expression.
    ya "You say real things."
    yl "(surprised) Do I?"
    ya "All the time. It's kind of terrifying."
    yl "(smiles) Good. Someone should be."

    # VISUAL: Wind moves through the grass; both watch it ripple like water.
    "The grass bends and rises, a green ocean rolling under the sun."

    ya "Do you ever think about what happens after?"
    yl "After what?"
    ya "After we're Branded. After we're assigned. After we become... whatever they decide we are."
    yl "(quiet) Every day."

    # VISUAL: She pulls a blade of grass, twirls it between her fingers.
    yl "My mother says the Band will make me complete. That I'll finally understand my purpose."
    ya "Do you believe her?"
    yl "(pause) ...I don't know. Do you believe your father?"
    ya "I don't know either."
    ya "What if it doesn't work? The Branding?"
    yl "Why wouldn't it work?"
    ya "I don't know. Kael's worked. But... what if mine doesn't?"
    yl "Then we figure it out. Together."
    ya "You promise?"
    yl "I promise. Two years from now, we both get Branded. And whatever happens, we're still us."

    # VISUAL: Lyra's fingers still; the grass blade falls.
    yl "(softly) What if the Band changes us?"
    ya "What do you mean?"
    yl "What if it makes us into people we wouldn't recognize? People who don't... feel the same things."
    ya "(careful) Like what things?"

    # VISUAL: She looks at him directly; vulnerability breaking through her usual confidence.
    yl "Like this. Sitting here. Saying real things. What if after the Branding, this becomes... frivolous?"
    ya "It's not frivolous."
    yl "How do you know?"
    ya "Because nothing that matters is frivolous. And this matters."

    # VISUAL: Her mask slips; something raw underneath.
    "Her mask slips. Just for a moment. Something raw underneath."

    yl "(barely audible) Does it? Matter?"
    ya "To me it does."

    # VISUAL: Silence; the sun drops lower, painting everything gold.
    "The light shifts. Everything glows. Like the world is holding its breath."

    # VISUAL: Their shoulders are close—almost touching. Neither pulls away.
    "They sit closer now. Not quite touching. Almost."

    yl "What if we don't get Branded to the same division?"
    ya "Then we find each other anyway."
    yl "You make it sound simple."
    ya "Isn't it?"
    yl "(softly) I hope so."

    # VISUAL: Young Aeron shifts slightly; their shoulders touch.
    "He moves. Just slightly. Their shoulders meet. Warm contact through fabric."
    "Neither pulls away."

    yl "(quiet) What are you most afraid of?"
    ya "Failing. You?"
    yl "Succeeding."
    ya "(confused) Why would that scare you?"
    yl "Because if I succeed at what they want, I might lose what I want."
    ya "What do you want?"
    yl "(looks at him) I don't know yet. But I think... it's something like this."

    # VISUAL: The moment stretches; neither moves.
    "The city hums in the distance. Up here, it feels like another world."

    ya "We could come back here. After. No matter what happens."
    yl "Promise?"
    ya "Promise."
    yl "(small smile) Then I'll hold you to it."

    # NEW/REVISED: More visceral almost-touch with future Glass parallel
    # VISUAL: Lyra's hand rests in the grass between them; Aeron's hand inches closer.
    "Her hand rests in the grass. His moves toward it—slow, uncertain."
    # VISUAL: Fingers almost touch—close enough to feel the warmth.
    "The space between them narrows. An inch. Less."
    athought "Even then, we were glass leaning toward glass."
    athought "Close enough to touch. Afraid of shattering."

    # VISUAL: Then Lyra pulls away, standing suddenly.
    yl "(standing quickly) We should head back before they notice we're gone."
    ya "(disappointed) Yeah. Probably."

    # BLOCKING: Lyra pops up to stand; offers hand.
    yl "We'll run away someday. You and me."
    ya "You serious?"
    yl "(nods) Dead serious."

    athought "Back then it felt real. Like we could run and leave the city behind. No father. No duty. Just wind."

    yl "Promise me—if the world turns to ash, we still find a place like this. Ours."
    ya "(softly) I promise."

    # VISUAL: Lyra pulls him to his feet; they stand face to face, close.
    "She pulls him up. For a moment, they stand too close. Eyes meet."

    yl "(barely a whisper) When everything changes..."
    yl "...don't forget me."
    ya "I won't. I couldn't."
    yl "(sad smile) Everyone says that."
    ya "I'm not everyone."
    yl "(touches his arm briefly) No. You're not."

    # NEW: Physical lingering with Glass parallel
    # VISUAL: Her hand lingers for a heartbeat—then lets go.
    "Her fingers slip away. The warmth remains."

    athought "I should have held on. Should have known this was the last time we'd be whole."

    # VISUAL: She steps back; the moment breaks but doesn't shatter.
    "She steps back. The moment hangs in the air like the last note of a song."

    # CAMERA: Close on hands; grass moving in wind.
    athought "For a moment, the city didn't exist. Just us, and the wind."
    athought "I should have held tighter to that moment."

    # NEW: Connection to broken promises and Glass
    athought "We promised to find a place like that hill. Somewhere ours."
    athought "Instead, we found duty. Orders. Distance."
    athought "She became Echelon's proof. I became Glass."
    athought "Two polished surfaces. Both see-through. Both empty."
    athought "But tonight, on the balcony, we almost remembered."
    athought "Glass leaning toward glass. Just like this hill. Just like always."

    # TRANSITION: Gentle white bloom → next memory (Branding at 12).
    athought "Then the day came—two years later, we both turned twelve—and everything changed."

    # canon_note: Both are 10 in this flashback; two years pre-Branding (at 12).
    # canon_note: Same cohort, same academy; promise to “find a place like this” echoes balcony scene.
    # canon_note: Early “Glass” foreshadow; fear of failing (Aeron) vs fear of succeeding (Lyra).

    $ set_scene_flag(_current_scene_id, "completed")

    return

# ========= CANON NOTES =========
# cann.scene_id: act1_08_hill_flashback
# cann.when_in_timeline: Childhood (age 10), two years pre-Branding; intercut after Balcony for resonance.
# cann.what_happened:
#   - Aeron & Lyra sneak beyond perimeter to a hill; trade hopes/fears; make two promises.
#   - “Glass” metaphor seeded; almost-touch motif mirrors Balcony.
# cann.aeron_state: VO reflective (adult Aeron) vs diegetic child dialogue (`ya`/`yl`).
# cann.path_tracking: No choices; no deltas. This is a pure resonance plate.
# cann.thematic_flags: Glass / Promise / Wind (breath) / Silence vs Noise.
# cann.block_status: ANCHOR plate; feeds Branding flashback and Balcony callbacks.
# cann.true_path_integration: none (non-menu rule).
# cann.visual_plate_economy: One exterior plate; B-roll inserts (hands/grass) reusable for future flashbacks.
# cann.requires_followup: Next memory: Branding at 12 (Tier Hall); echo the “don’t forget me” line’s inversion.