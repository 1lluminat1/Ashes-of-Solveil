# act1_15_zira_first_contact.rpy


# =======================================================
# ACT 1 - Scene 15: Aeron's First Encounter With Zira
# =======================================================


# VISUAL: Dimly lit street in the Unders. Neon signage flickers. Wet pavement. Trash and data-choked air.
# Low synth hum and ambient Unders sounds. Aeron walks alone, eyes scanning.

label act1_zira:
    "{i}Northeast edge. Grid Six-Two.{/i}"
    "{i}The coordinates from the message.{/i}"
    "{i}Aeron walks the crumbling spine of Sector 10's northeast edge, mission order folded in his coat like a threat.{/i}"

    a "{i}No eyes. No witnesses. No backup.{/i}"
    a "{i}Perfect place to bury the truth.{/i}"

    # VISUAL: Glitched vending machine sparks nearby. A figure half-lit in shadow, crouched near an access panel. Hooded. Female.
    # A hacking device flickers in her hand, wires like veins into the wall.
    "{i}Movement. Just past the broken light. Someone tampering with the infrastructure—quick hands, steady posture.{/i}"

    a "Stop right there."
    # The figure doesn’t flinch. Instead:
    z "If you were going to shoot, you would’ve already."
    a "Turn around. Slowly."

    # Zira stands, hood halfway falling back. Her face is sharp, eyes lit by the interface glow.
    z "Relax. I’m not armed. Not stupid either. So don’t be."

    # Brief pause. Static buzz.
    a "You’re interfering with city systems. That’s a high offense."
    z "And you’re dressed too clean to be down here. So what’s the offense, really?"
    a "Who are you?"
    z "Someone who keeps the grid from swallowing this sector whole."
    z "Also someone with very little patience for Echelon hounds, so unless you’re lost—"

    # Aeron steps closer.
    a "I’m not with the enforcers. Not tonight."
    z "Then you’re either rogue or stupid. And you don’t look stupid."

    # Pause. Sparks flicker from the panel she was working on.
    a "What were you doing just now?"
    z "Re-routing drain energy to keep a shelter from freezing overnight."
    a "So... you’re a vigilante now?"
    z "I’m alive. That’s already illegal down here."

    # VISUAL: Drone hum approaches in distance.
    "{i}A low thrum echoes from above — patrol drone. Noticed the energy spike, maybe. Too late to run.{/i}"

    a "They’re sweeping the area. You triggered a ping."
    z "No, your dumb boots did."

    # She flips her glove closed, sparks die.
    z "Fine. I’m out. Try not to get killed, ‘Not-With-The-Enforcers.’"

    # She turns — but pauses.
    menu:
        "Stop her":
            $ zira_rel += 1
            a "Wait. I need information."
            z "That’ll cost you."
            a "Money?"
            z "No. Honesty."
            a "...I’m listening."
        "Let her go":
            a "Fine. Walk away."
            z "Suit yourself. But if you're down here for truth, you're already bleeding."

    # Regardless, a second drone shrieks closer. Both characters duck under cover.
    "{i}The drone passes overhead. Searchlights rake the alley but miss their mark.{/i}"

    a "You know this area well."
    z "Better than your briefing packet did."
    a "I need someone who can track internal grid movement. Sector heat patterns, foot traffic shadows."
    z "You want someone to help you ghost the city."
    a "I want someone who sees it like you do."
    z "(studies him) You're not what I expected."
    a "What did you expect?"
    z "Another Aeries puppet. But you... you're asking questions."
    a "Is that dangerous?"
    z "(grins) Lethal. I like it."
    z "...Meet me near the Obsidian Bridge. Midnight. If you’re not followed."
    a "That’s it?"
    z "That’s everything. Don’t be early. Don’t be loud."

    # Zira disappears into the dark. Aeron remains, watching the shadows.
    "{i}She’s gone before he can second-guess himself. But the hum in his chest hasn’t faded — adrenaline or something else.{/i}"

    a "(quietly) What the hell am I getting into..."
    
    return