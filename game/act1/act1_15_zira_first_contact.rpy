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
    # NEW: Glass observation
    a "{i}Or perfect place for Glass to finally see what it's been cutting.{/i}"

    # VISUAL: Glitched vending machine sparks nearby. A figure half-lit in shadow, crouched near an access panel. Hooded. Female.
    # A hacking device flickers in her hand, wires like veins into the wall.
    "{i}Movement. Just past the broken light. Someone tampering with the infrastructure—quick hands, steady posture.{/i}"

    a "Stop right there."
    # The figure doesn't flinch. Instead:
    z "If you were going to shoot, you would've already."
    a "Turn around. Slowly."

    # Zira stands, hood halfway falling back. Her face is sharp, eyes lit by the interface glow.
    z "Relax. I'm not armed. Not stupid either. So don't be."

    # Brief pause. Static buzz.
    a "You're interfering with city systems. That's a high offense."
    z "And you're dressed too clean to be down here. So what's the offense, really?"
    a "Who are you?"
    z "Someone who keeps the grid from swallowing this sector whole."
    z "Also someone with very little patience for Echelon hounds, so unless you're lost—"

    # Aeron steps closer.
    a "I'm not with the enforcers. Not tonight."
    z "Then you're either rogue or stupid. And you don't look stupid."
    # NEW: Glass recognition
    z "(studies him) Wait. You're Glass, aren't you?"
    a "(tense) What did you say?"
    z "Glass. Marcus Rylan's weapon. 390 operations. Zero failures."
    z "Everyone in the Unders knows about Glass."
    a "And what do they say?"
    z "That Glass is sharp. Glass is empty. And Glass always cuts."
    z "(tilts head) But you're down here. Night before a sweep. That's not what Glass does."

    # Pause. Sparks flicker from the panel she was working on.
    a "What were you doing just now?"
    z "Re-routing drain energy to keep a shelter from freezing overnight."
    a "So... you're a vigilante now?"
    z "I'm alive. That's already illegal down here."
    # NEW: Tomorrow's mission
    z "Especially after tomorrow. After your sweep."
    a "(sharp) How do you know about that?"
    z "I know everything that happens in Sector 10. Including your orders."
    z "200 to 500 targets. Dawn deployment. Zero tolerance."
    z "(bitter) 'Acceptable collateral.' That's what the brief says, right?"

    # VISUAL: Drone hum approaches in distance.
    "{i}A low thrum echoes from above — patrol drone. Noticed the energy spike, maybe. Too late to run.{/i}"

    a "They're sweeping the area. You triggered a ping."
    z "No, your dumb boots did."

    # She flips her glove closed, sparks die.
    z "Fine. I'm out. Try not to get killed, Glass."

    # She turns — but pauses.
    menu:
        "Stop her":
            $ zira_rel += 1
            a "Wait. I need information."
            z "That'll cost you."
            a "Money?"
            z "No. Honesty."
            a "...I'm listening."
            z "Why are you really here? Night before you're ordered to kill everyone in this sector?"
            a "(pause) Because I wanted to see their faces first."
            z "(surprised) ...Glass said that?"
            a "Maybe Glass is cracking."
            z "(studies him) You're not what I expected."
            a "What did you expect?"
            z "Another Aeries puppet. But you... you're asking questions."
            a "Is that dangerous?"
            z "(grins) Lethal. I like it."
            
        "Let her go":
            $ zira_rel -= 1
            a "Fine. Walk away."
            z "Suit yourself. But if you're down here for truth, you're already bleeding."
            z "(over shoulder) Glass doesn't bleed. But people do."
            z "Figure out which one you are before tomorrow."

    # Regardless, a second drone shrieks closer. Both characters duck under cover.
    "{i}The drone passes overhead. Searchlights rake the alley but miss their mark.{/i}"

    a "You know this area well."
    z "Better than your briefing packet did."
    # NEW: Mission specifics
    a "I need someone who can tell me what's really happening in Sector 10."
    a "My orders say organized resistance. Rebel networks."
    z "(laughs bitterly) Organized resistance? Try families hiding from debt collectors."
    z "Try kids who can't afford Branding fees."
    z "Try people who just want to survive without Echelon's boot on their throat."
    a "The intelligence reports—"
    z "Are lies. Sector 10 isn't a rebel stronghold. It's a settlement Father wants erased."
    z "Too many unregistered citizens. Too much independence. Too much... humanity."

    # VISUAL: Aeron's expression shifts—something clicking into place.
    a "{i}Not a military target. A civilian purge.{/i}"
    a "{i}Glass has been cutting civilians for 390 operations.{/i}"
    a "{i}But this... this is different. This is deliberate erasure.{/i}"

    a "How do you know this?"
    z "Because I track everything. Data flows. Population movements. Energy usage."
    z "Sector 10's energy consumption is residential. Not industrial. Not military."
    z "It's families, Glass. Just families."
    a "(quiet) Why tell me this?"
    z "Because you came here tonight. Glass doesn't do reconnaissance."
    z "Glass just obeys. But you... you wanted to see."
    z "(leans in) That means there's still something human under all that empty."

    # VISUAL: Aeron processes this; jaw tight.
    a "{i}She's right. Glass doesn't question. Glass doesn't investigate.{/i}"
    a "{i}But I'm here. The night before. Asking questions.{/i}"
    
    z "You're not what I expected, Glass."
    a "What did you expect?"
    z "Another Aeries puppet. Empty. Obedient."
    z "But you're down here asking questions. That's dangerous."
    a "Dangerous for who?"
    z "(grins) For you. For me. For anyone who thinks Glass might still be human."
    z "But I like dangerous."
    
    # NEW: Tomorrow's mission urgency
    z "If you really want answers, you need to see something."
    z "Tomorrow at dawn, you sweep this sector. Your orders say 200 to 500 casualties."
    z "But tonight, right now, there are 800 people sheltering in the sublevels."
    a "800?"
    z "Families. Elders. Children. Unregistered, yes. But alive."
    z "Your orders say eliminate all targets. That's 800 lives, Glass."
    z "Still think it's about organized resistance?"

    # VISUAL: Aeron's hands clench; something breaking in his expression.
    a "{i}800 people. The vendor. The child. The families around fires.{/i}"
    a "{i}All of them. Gone by noon tomorrow.{/i}"
    a "{i}Glass obeys. Glass doesn't question.{/i}"
    a "{i}But I'm questioning now.{/i}"

    z "Tomorrow at dawn, you sweep this sector. 800 people."
    z "You can't refuse. Marcus owns you. I know that."
    z "But you CAN choose HOW you obey."
    z "Warn people. Fake reports. Look the other way. Find the cracks."
    z "Glass follows orders. Humans find ways to resist even while obeying."
    z "Show me which one you are."

    a "And if I can't save them all?"
    z "No one can. But trying matters."
    z "(softer) 390 operations, you've been Glass. Perfect obedience."
    z "Tomorrow, try being human. Even if it's messy. Even if it's not enough."

    z "Meet me at Obsidian Bridge. Midnight tomorrow."
    z "If you fought for them—even if you lost—I'll be there."
    z "If you just followed orders without fighting... don't bother coming."

    # Zira disappears into the dark. Aeron remains, watching the shadows.
    "{i}She's gone before he can second-guess himself. But the hum in his chest hasn't faded — adrenaline or something else.{/i}"

    a "(quietly) What the hell am I getting into..."
    # NEW: Mission weight
    a "{i}800 people. Dawn deployment. My orders.{/i}"
    a "{i}Glass obeys. Glass always obeys.{/i}"
    a "{i}But if I obey tomorrow... what's left of me afterward?{/i}"
    a "{i}Is there anything left to save? Or is Glass all that remains?{/i}"
    
    # canon_note: Zira knows about Glass - reputation in the Unders
    # canon_note: Sector 10 isn't military target - it's civilian purge
    # canon_note: 800 people, not 200-500 - Marcus's intel is deliberately understated
    # canon_note: Zira's ultimatum - "don't come if you go through with sweep"
    # canon_note: Forces moral choice - can't meet Zira AND complete sweep
    # canon_note: "Glass or human" - core choice for entire story
    # canon_note: Aeron now knows sweep is murder, not military operation
    # canon_note: Sets up next scene - does he report to Marcus? Prepare for sweep? Defy?

    return