# act1_10_brothers_rooftop.rpy


# ======================================================
# ACT 1 - Scene 10: Flashback: Brothers on the Rooftop
# ======================================================


label act1_brothers:

    # VISUAL: Same rooftop as act1_09_breaking_point, but years earlier.
    # LIGHTING: Late afternoon—golden hour fading to dusk; warmer palette.
    # SOUND: Distant city hum; wind softer, less oppressive; no sirens.

    a "{i}Before the ritual. Before the rejection. Before everything broke.{/i}"
    "{i}There was a time when this rooftop felt like freedom.{/i}"

    # VISUAL: Two figures seated at the rail—young Aeron (14) and his brother Kael (17).
    # Brother wears casual Aeries clothing; silver Band visible on his wrist, still new.

    define k = Character("Kael")

    k "You ever think about what's past the edge?"
    ya "(looks out) Past Solveil?"
    k "Past everything. The ruins. The dead cities. Whatever's left out there."
    ya "Father says there's nothing. Just ash and ghosts."
    k "(smirks) Father says a lot of things."

    # NEW/REVISED: Kael's Band with nervous gesture
    # VISUAL: Kael's Band catches the fading sunlight—prismatic glint.
    "{i}His Band gleams like a promise. Three months old. Still perfect.{/i}"
    # VISUAL: Kael touches it absently—a gesture young Aeron doesn't understand yet.
    "{i}He touches it often. Like checking a wound.{/i}"

    ya "Does it still hurt?"
    k "(glances at his wrist) The Band? Nah. Not anymore."
    k "First week was hell, though. Felt like it was burning from the inside."
    ya "(quietly) But it stopped?"
    k "Yeah. Once it syncs, it's like... it's always been there."

    # VISUAL: Young Aeron stares at his own bare wrist.
    ya "{i}Two years. Two years until my turn.{/i}"

    k "Hey." 
    # VISUAL: Kael nudges his shoulder.
    k "You're gonna be fine. Better than fine."
    ya "How do you know?"
    k "'Cause you're a Rylan. It's in the blood."

    # VISUAL: Kael stands, stretches, walks to the edge—closer than safe.
    ya "(alarmed) Kael—"
    k "(laughs) Relax. I'm not gonna jump."
    k "Just seeing how close I can get before instinct kicks in."

    # VISUAL: He stands at the very edge, arms spread, wind tugging at his sleeves.
    k "You know what's weird? Up here, I feel like I could actually fly."
    k "Like if I just... let go, the city would catch me."
    ya "(uneasy) That's not how physics works."
    k "(grins back at him) Physics. Listen to you, little professor."

    # VISUAL: Kael steps back from the edge, sits back down beside Aeron.
    "{i}Relief floods through young Aeron's chest.{/i}"

    # NEW/REVISED: Deeper "playing a part" exchange
    k "(serious now) You ever feel like you're not really... you?"
    ya "What do you mean?"
    k "Like... you're playing a part. Reading lines someone else wrote."
    ya "All the time."
    k "(nods slowly) Yeah. Me too."
    # VISUAL: Kael looks out at the city; jaw tight.
    k "(quieter) Sometimes I wonder what happens when you forget the lines."
    ya "You improvise?"
    k "(hollow laugh) Or you fall off the stage."

    # VISUAL: Silence; city lights begin to flicker on below as dusk deepens.
    "{i}The city wakes below them—a thousand lights igniting like distant stars.{/i}"

    # NEW/REVISED: More urgent promise moment
    k "Promise me something."
    ya "What?"
    k "If I ever lose myself—if I ever stop being me—you'll remember who I was."
    ya "(confused) Why would you—?"
    k "Just promise, Aeron."
    # VISUAL: Kael's hand grips young Aeron's shoulder—urgent, almost desperate.
    "{i}His grip is tight. Too tight. Then he lets go.{/i}"
    ya "(hesitant) ...I promise."

    # VISUAL: Kael's expression softens; he ruffles Aeron's hair—older brother affection.
    k "Good. 'Cause I'm gonna need someone to tell the truth when Father starts rewriting history."
    ya "(half-smile) You think he'd do that?"
    k "(dry laugh) I think he already has."

    # VISUAL: They sit in comfortable silence; wind carries distant music from below.
    k "Two years, huh? Then you'll get your Band."
    ya "Yeah."
    k "You scared?"
    ya "(honest) Terrified."
    k "Good. Means you're paying attention."

    # VISUAL: Kael stands, offers his hand to pull Aeron up.
    k "Come on. Dinner's in twenty. Father hates it when we're late."
    ya "(takes his hand, stands) Kael?"
    k "Yeah?"
    ya "Thanks. For... this."
    k "(grins) Anytime, little brother. Anytime."

    # VISUAL: They walk toward the rooftop door together.
    # CAMERA: Hold on the empty rooftop as they leave—wind stirs, city hums.

    # TRANSITION: Slow dissolve to present-day rooftop—same angle, empty, colder lighting.
    a "{i}Three months later, his Band rejected him.{/i}"
    a "{i}Father pulled strings. Kept him in the Aeries. Called it mercy.{/i}"
    a "{i}Kael called it a cage.{/i}"
    a "{i}The whispers followed him everywhere. 'Protected failure.' 'General's broken son.'{/i}"
    a "{i}Six months after that, he stood here alone.{/i}"
    a "{i}And he jumped.{/i}"

    # NEW/REVISED: Explicit bridge to breaking point
    # VISUAL: Present-day Aeron standing at the same rail, same position Kael once stood.
    a "{i}I kept my promise. I remembered who you were.{/i}"
    a "{i}But I never understood why you had to leave.{/i}"
    a "{i}Now... I think I'm starting to.{/i}"
    # VISUAL: Present Aeron looks at the edge where Kael stood.
    a "{i}The cage. The whispers. Father's 'mercy.' The weight of being saved when you wanted to fall.{/i}"
    a "{i}I understand now.{/i}"

    "{i}The memory fades. But the weight remains.{/i}"
    "{i}Present day. His apartment.{/i}"

    # canon_note: Kael's foreshadowing ("if I lose myself") becomes tragic in hindsight.
    # canon_note: Marcus's intervention for Kael mirrors his intervention for Aeron—protection as prison.
    # canon_note: "Rewriting history" line plants Marcus's narrative manipulation.
    # canon_note: This scene gives emotional weight to act1_09_breaking_point.

    return