# act1_06_balcony.rpy


# ===================================================
# ACT 1 - Scene 6: The Balcony
# ===================================================


label act1_balcony:

    # VISUAL: Neon-lit skyline beyond the rail; rain tapering to mist.
    # Atmosphere: cooler palette than the gala; city hum below.
    "{i}The city's glow cuts hard lines across the stone.{/i}"

    a "{i}They look down at the Unders like another species. Still human. All of us.{/i}"
    # NEW: Glass perspective
    a "{i}Glass doesn't care about altitude. Glass just reflects what's in front of it.{/i}"

    # VISUAL: Cigarette beat (keep as narration + implied prop).
    "{i}Aeron lights a cigarette. Smoke threads into the neon.{/i}"

    # VISUAL: Footfalls approach from the doorway—measured, unhurried.
    "{i}Footfalls in the archway—measured, unhurried.{/i}"

    # Lyra arrives — keep voice formal (few/no contractions).
    l "Got a light?"
    a "(wry) I didn't think Echelon's exemplar smoked."
    l "(a faint smile) If you know a better way to breathe in there, I'm listening."
    # NEW: Recognition between them
    a "Glass and glass. You said we should compare cracks."
    l "I did. Are you ready to show me yours?"
    a "Are you ready to show me yours?"
    l "(pause) Perhaps we start with smaller truths first."

    # --- MICRO-CHOICE: share the light (intimacy distance) ---
    menu:
        "Lyra steps in close, waiting for the flame."
        "Lean in and light it for her.":
            $ aeron_shares_light = True
            "{i}He lifts the flame. She leans in; her eyes do not leave his.{/i}"
            a "{i}Close enough to see the cracks. In both of us.{/i}"
            
        "Offer the lighter and step back.":
            $ aeron_shares_light = False
            "{i}He hands her the lighter. Distance holds.{/i}"
            a "{i}Glass doesn't touch. Glass maintains distance.{/i}"
    # ----------------------------------------------------------

    # Optional glance beat up close.
    menu:
        "For a breath, she remains close."
        "Hold her gaze.":
            $ aeron_holds_her_gaze = True
            a "{i}Color on smoke. For once, no audience.{/i}"
            a "{i}She's not looking at Glass. She's looking for what's underneath.{/i}"
            
        "Look past her to the city.":
            $ aeron_holds_her_gaze = False
            a "{i}The skyline answers for me.{/i}"
            a "{i}Easier to look at lights than at someone who might actually see.{/i}"

    # Callback to earlier micro-exchanges inside the gala.
    if aeron_spoke_to_lyra_gala:
        l "You didn't keep me waiting."
        if aeron_moves_toward_lyra:
            l "Crossing the floor like that—bold, considering the room."
            a "Why be subtle in a place built to be seen?"
            l "(faint smile) Fair point. Though Glass is rarely subtle."
            a "You know what they call me."
            l "Everyone knows what they call you."
        else:
            a "You said five."
            l "And you listened. Glass follows orders."
            a "Is that what you think I am? Just orders and obedience?"
            l "I think you are more than that. The question is whether you still believe it."
    else:
        l "You skipped the introductions."
        a "Crowd was not my scene."
        l "It never is. Glass does not socialize. Glass performs."
        a "You seem to know a lot about Glass."
        l "I recognize my own reflection."

    # Optional nod if he confronted the whisperers
    if aeron_confronts_elites:
        l "I saw you correct the record."
        a "They were loud."
        l "Most people are, until someone looks back."
        l "Glass looking back. That must have been unsettling for them."
        a "Good."

    # Quiet beat at the rail.
    "{i}They stand at the rail; the city's noise folds over itself below.{/i}"

    if aeron_moves_toward_lyra != True:
        l "I didn't expect to find you out here."
        a "I didn't expect you to leave a spotlight unattended."
        a "I figured you would be inside, charming anyone with a title."
    else:
        a "Shouldn't you be inside, charming anyone with a title instead of mingling with me?"
        
    l "(soft) Please. I would rather jump."
    a "(half-smile) Careful. They might call that sedition."

    # NEW: Shared understanding of performance
    l "Take away the performance and there's not much left."
    a "{i}Her voice drops. Just for a second.{/i}"
    a "{i}Not the formal Lyra. Something underneath. Something exhausted.{/i}"
    a "You've done it your whole life."
    l "Since I could walk. That doesn't mean I'm blind."
    # NEW: Glass reference
    l "They call me the system's proof. Polished. Perfect. Pristine."
    l "I call it glass. Transparent enough to see through. Empty enough to break."
    a "So you know."
    l "Of course I know. Glass recognizes glass."

    a "Then tell me—what do you see now?"

    l "(studies him) A room drunk on power it barely understands."
    l "People who will do anything to feed a machine that eats the rest."
    l "And one person out here—"
    l "—pretending he's forgotten how to care."
    # NEW: But she sees through it
    l "(softer) But the pretending is getting harder, is it not?"

    a "{i}Her words land like a memory I didn't ask for.{/i}"
    a "You always read between the lines."

    l "I hear the rumors, and I know they are far from the truth."
    # REVISED: New rumors about Glass
    l "They say Glass is perfect. Glass is empty. Glass does not feel."
    a "And?"
    l "And I think Glass is lying to itself."
    
    a "They've been whispering since I was twelve."
    # NEW: What the whispers changed from
    a "Used to be about failure. About the Branding. About the son who couldn't."
    a "Now it's about the soldier who does. 390 operations. Zero failures."
    a "Not sure which whispers are worse."
    
    l "Let them. Fear is loud when it's small."
    a "They just respect my father."
    a "I'm just a rumor. An heir to a name that doesn't fit."
    a "{i}Rylan. Heavy word. Hollow sound.{/i}"

    # --- MICRO-CHOICE: ash over the city (defiance) or keep tidy (control) ---
    menu:
        "The ember brightens at the tip."
        "Flick ash over the rail.":
            $ aeron_flicks_ash = True
            "{i}Ash falls and vanishes into neon.{/i}"
            a "{i}Let it fall. Glass doesn't hold onto anything anyway.{/i}"
            
        "Tap ash into the tray.":
            $ aeron_flicks_ash = False
            "{i}He taps the tray's edge; the ember settles.{/i}"
            a "{i}Controlled. Contained. Like everything else.{/i}"
    # -------------------------------------------------------------------------

    a "Why are you really out here?"
    l "Because in a room full of polish, you're the only one not pretending."
    # NEW: Correction
    a "I'm always pretending. Glass is nothing but pretense."
    l "No. Glass is what they made you pretend to be."
    l "The person asking that question is the one I came to see."

    "{i}They smoke in the hush between gusts of wind.{/i}"

    a "How long are you back from assignment?"
    l "Not long. High value means high surveillance."
    l "They let me breathe when it's useful."
    a "And tonight?"
    l "Parade duty. Proof the machine still works."
    # NEW: Shared burden
    l "They parade me. They parade you. Two perfect soldiers."
    l "Except neither of us believes a word of it anymore."

    a "They think everything belongs to them."
    a "The dark tells the truth."
    a "And you—"
    a "—you don't belong to anyone."

    # NEW/REVISED: Proximity moment with more physical detail and Glass metaphor
    # VISUAL: The space between them narrows—neither moves, but distance shrinks.
    "{i}She does not step away. Neither does he.{/i}"
    a "{i}The city hums below. Up here, the silence is louder.{/i}"
    # NEW: Glass metaphor
    a "{i}Two pieces of glass, leaning close enough to touch.{/i}"
    a "{i}Wondering if contact will shatter both.{/i}"

    l "(quiet) Always so serious."
    l "And here I thought I was the dramatic one."

    # --- MICRO-CHOICE: risk a question about her leash (pressure vs restraint) ---
    menu:
        "Say nothing—or press."
        "Press her about the leash she is on.":
            $ aeron_presses_topic = True
            a "Who holds the leash tonight—Council or Command?"
            l "(a beat) Does it matter, if they pull the same direction?"
            a "{i}She looks away. Jaw tight. Breath unsteady.{/i}"
            a "{i}She's not deflecting. She's drowning.{/i}"
            a "{i}And I almost missed it.{/i}"
            a "It matters if you're the one being pulled."
            l "(studies him) And what about you? Who pulls your leash?"
            a "Father. Always Father."
            l "Then we are both dogs on strings."
            l "Wondering if cutting them means freedom or falling."
            
        "Let the moment breathe.":
            $ aeron_presses_topic = False
            a "{i}I leave the question where it belongs—in the smoke.{/i}"
            a "{i}Glass doesn't pry. Glass reflects.{/i}"
    # ---------------------------------------------------------------------------

    "{i}Two faint sparks hang in the night—then dim with the wind.{/i}"
    
    # NEW: Vulnerability moment
    l "(quietly) Do you ever wonder what we would be without the uniforms?"
    a "Every night."
    l "And?"
    a "I don't have an answer. Just questions Glass isn't supposed to ask."
    l "Then perhaps Glass is already breaking."
    a "(looks at her) Is that what you want? For me to break?"
    l "I want you to remember what it feels like to be whole."
    l "Even if that means shattering first."

    # NEW: Closing emotional beat with mission weight
    "{i}For a moment, the world feels smaller. Just two people. Just smoke and silence.{/i}"
    a "{i}Six hours ago, I killed four people.{/i}"
    a "{i}And right now, standing here with her, that's the first time I've felt it.{/i}"
    a "{i}The weight. The wrongness. The crack spreading.{/i}"
    a "{i}Maybe that's what she means. Maybe feeling it is how Glass breaks.{/i}"
    
    # VISUAL: Fade out to next scene.

    # canon_note: Lyra sees through Glass identity - recognizes shared emptiness
    # canon_note: "Glass recognizes glass" - both are polished weapons
    # canon_note: First time Aeron admits Glass might be breaking
    # canon_note: Mission weight (six hours ago) finally hitting him
    # canon_note: Proximity choices matter - testing if Glass can connect
    # canon_note: Lyra plants seed: "breaking might mean remembering wholeness"

    return