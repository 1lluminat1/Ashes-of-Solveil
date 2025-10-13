# act1_20_marcus_call.rpy


# =======================================================
# ACT 1 - Scene 20: Marcus Holo-Call Debrief
# =======================================================


label act1_marcus_call:
    # VISUAL: Aeron's apartment — sterile, blue-white; auto-lights rise as door seals.
    # SOUND: faint hum of filtration system; distant thunder from city below.
    # LIGHTING: stark contrast to the red haze of the sweep scene.

    "{i}Later that night...{/i}"
    "{i}The door seals behind him. The room wakes on its own — a ritual of obedient light.{/i}"

    # VISUAL: Holo projection stabilizes; Marcus already on the line, posture rigid.
    # SFX: Soft holo-pop, faint distortion.
    m "You're late."

    if aeron_defied_orders:
        a "Had to stay behind. The sweep didn't go as clean as your report promised."
    else:
        a "Grid Six-Two was secured. Resistance minimal. You'll have the footage within the hour."

    m "Sector Ten was {i}reconnaissance{/i}, not engagement."
    a "(frowns) Reconnaissance? The order said 'Sweep. Secure. Eliminate.'"
    m "Classified terminology. You're not cleared for operational semantics."
    a "Operational semantics? That's a body count, not a briefing error."
    m "Mind your tone. You misread an order. It happens."

    # ========== NEW CONTENT START (SECTION 1) ==========

    a "I didn't misread anything. I watched them execute unarmed civilians."
    m "Containment protocols—"
    a "(cuts him off) There was a boy. Maybe ten years old. Hiding under debris with his sister."
    m "(pause) Collateral is unfortunate but—"
    a "His sister was shot in the back while running away. She wasn't armed. She wasn't a threat. She was a child."

    # VISUAL: Marcus's jaw tightens; hologram flickers slightly.
    m "War creates difficult choices."
    a "We're not at war."
    m "Aren't we?"

    # VISUAL: Aeron's hands clench; knuckles white.
    "{i}The air thickens. Static hums beneath the silence.{/i}"

    a "You sent me there knowing what would happen."
    m "I sent you there to {i}observe{/i}. What the Enforcers did was within their mandate."
    a "Their mandate is genocide?"
    m "(sharp) Their mandate is {i}stability{/i}. Do not confuse compassion with competence."

    # ========== NEW CONTENT END (SECTION 1) ==========

    a "I watched them execute unarmed civilians, Father."
    m "Containment of contamination is not execution. You of all people should know the difference."

    # VISUAL: Marcus's image flickers; static crawls across his jawline.
    m "Those were containment protocols. Breaches compromise the city's stability."
    a "You call them breaches. I call them people."
    m "Words don't change necessity. Discipline sustains peace."

    # CAMERA: push on Aeron's face — the light from the holo bleaches his expression.
    a "Peace built on ash isn't peace. It's silence."
    m "Spoken like someone who's never commanded a city of millions."

    # ========== NEW CONTENT START (SECTION 2) ==========

    m "You think sentiment makes you noble. It makes you weak."
    a "And what does obedience make me?"
    m "(cold) Useful."

    # VISUAL: The word lands like a slap; Aeron's expression hardens.
    "{i}Useful. Not valued. Not trusted. Useful.{/i}"

    a "Is that what Kael was? Useful? Right up until he wasn't?"
    m "(dangerous quiet) Do not bring your brother into this."
    a "Why not? You brought me into it. You kept him in the Aeries after his Band failed. Protected him. Just like you're protecting me."
    m "I gave you both opportunities—"
    a "You gave us cages and called them mercy."

    # VISUAL: Marcus leans forward; hologram distorts slightly at the edges.
    m "I saved you from exile. From the Unders. From becoming another forgotten name in a sector report."
    a "Maybe Kael would've preferred the Unders to living under your 'mercy.'"
    a "(bitter) He jumped to get to the Unders. Faster than waiting for your paperwork."

    # VISUAL: Marcus freezes; the hologram glitches violently for a frame.
    "{i}The words hit like a blade. Marcus's composure cracks—just for a second.{/i}"

    m "(dangerously quiet) ...What did you say?"
    a "You heard me."
    m "(ice) Your brother was {i}broken{/i}, Aeron. The Band didn't fail him. He failed it."
    a "And me? What's my excuse?"

    # VISUAL: Silence; the holo crackles faintly.
    "{i}Marcus doesn't answer. The silence says enough.{/i}"

    a "{i}Same failure. Different cage. Same ending.{/i}"

    if tessa_rel >= 1:
        a "Someone out there still tries to fix what we break. She risked her life to save them."
        m "A medic? An idealist. They always think compassion is currency."
        a "Maybe it's the only thing left that's still worth something."

    # Marcus hardens; voice lowers.
    m "You're not paid to {i}feel{/i}, Aeron. You're paid to ensure outcomes. Do you understand?"
    a "I understand what I saw. And I'm not sure I want to understand you."

    # SOUND: brief pop; holo signal crackles.
    m "Careful how you speak to me."
    a "You taught me to tell the truth."

    # VISUAL: Marcus leans forward; hologram glitch splits his image for a frame.
    m "Truth is a luxury for those who aren't responsible for survival. You think this job is clean? It never was."
    a "Then maybe the system is already dead — you're just keeping the corpse standing."

    # SOUND: electronic crack; connection spike.
    m "Enough. Finish your report. No commentary. No speculation. Submit and await reassignment."

    a "And if I refuse?"
    m "Then you'll prove what they whisper — that I raised a liability, not a soldier."

    # VISUAL: Marcus turns slightly, as if someone off-screen addresses him.
    m "We'll speak when you remember who you are."

    # SFX: holo snap-off; sudden silence.
    # LIGHTING: apartment auto-dims to blue-grey; faint hum of city below.
    "{i}Silence. The room exhales, relieved to stop listening.{/i}"

    a "{i}'Remember who you are.'{/i}"
    a "{i}Maybe that's the problem.{/i}"

    # TRANSITION: Match cut to rooftop hatch handle turning (lead-in to Lyra rooftop scene).
    return