# =======================================================
# ACT 3 - Scene 16: Command and Surrender (Empathy Path)
# File: a3_s16_command_and_surrender_emp.rpy
# Type: SELENE FIRST EROTIC
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s16_command_and_surrender_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s16_command_and_surrender_emp:


    # Gallery — unlock this scene in the character replay grid.
    $ gallery_unlock("a3_s16_command_and_surrender_emp")
    $ show_timeline("DAY 37", "23:00", "Phoenix Base — Selene's Quarters")
    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 32mm, handheld with minimal drift. The steadiness matches Selene's composure —
    #         and the handheld catches when that composure cracks.
    #         Opening: over-shoulder from Aeron's POV as she reports. Clinical distance.
    #         Her quarters: the camera finds domestic details — the plant, the cipher, her jacket on the chair.
    #         Intimacy: slow, locked two-shot. No cutting during the consent gates. Trust the frame.
    #         Aftercare: wider. Breathing room. Dawn light as visual punctuation.
    # LIGHTING: Corridor: overhead strips, institutional cool. Her face caught between shadow and function.
    #           Her quarters: single amber lamp. The windowsill catches whatever light filters from outside.
    #           The plant on the windowsill is backlit — the one living thing in the room that isn't her.
    #           Intimacy: lamp only. Warm. The cipher on the nightstand catching glints.
    #           Aftercare: dawn through the window. Gradual. The plant in new light.
    # SFX: Loop — quarters ambient: base hum muffled by walls, ventilation tick, distant night.
    #      One-shots — door latch, jacket off shoulders, lamp click, breath against skin.
    #      The cipher: set down on the nightstand. The specific weight of metal on wood.
    # FX/COMP: Her quarters: austere but lived-in. Military cot, desk, the plant on the sill.
    #          The cipher — their shared command token — present throughout.
    #          The wound at her ribs: recent stitches. Tessa's work. Visible when the jacket comes off.
    # BLOCKING: Corridor: standing. Professional distance. She's reporting, he's receiving.
    #           Quarters: she sits on the cot. He stands by the door. The distance closes through conversation.
    #           Intimacy: the professional distance dissolves. She reaches for the cipher (grounding habit).
    #           He takes her hand instead. That's the pivot.
    # CANON: FIRST EROTIC scene for Selene. Follows the first kiss (s14).
    #        Triggered by a close call — she took a risk that almost killed her. The vulnerability breaks through.
    #        The carry scene callback: same quarters, same cot. Last time she was unconscious. This time she chooses.
    #        Callbacks: a3_s14 cipher/kiss, the wound from the raid, the plant on the sill.
    # CONSENT: 3-gate framework. (A) Vulnerable admission. (B) Matching vulnerability. (C) Explicit.

    # ========= VOICE BASELINE =========
    # EMP cadence: Contractions, warmth, sensory weight.
    # Selene: Shaken but controlling it. The control is the tell — she's working too hard to be steady.
    # Aeron: Reading her. He knows what the cost looks like now. Post-kiss awareness changes everything.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - CORRIDOR / SELENE'S QUARTERS - NIGHT]
    # After Noelle's revelation (s19) — the Purge data is confirmed.
    # Marcus's signature is on the kill order. The corridor is quiet.
    # Selene is walking back from processing the data. Aeron intercepts.

    #scene bg_corridor_night_emp with dissolve
    #play ambient "sfx/ambient/base_night_corridor.ogg" fadein 2.0

    # ========== PHASE 1 — POST-REVELATION ==========

    "Noelle's data finished processing an hour ago. The Purge authorization chain is confirmed — every signature, every relay, every order that moved the machine."

    "The briefing room is empty now. Everyone has left to absorb what they learned."

    athought "Selene is the last to leave. She always is."

    "Selene is walking the corridor toward her quarters. Her stride is measured. Controlled. The same precision she applies to everything."

    athought "But her left arm is held close to her body. Not slung — braced. The jacket hangs differently on that side."

    athought "She took a hit during the breach. Thermal charge debris. She ordered Tessa to patch it in the field and kept moving."

    athought "No one else noticed. I noticed."

    a "Selene."

    "She stops. Half-turns. The corridor light catches the set of her jaw."

    sel "Debrief is filed. Sector 11 node is confirmed down. Noelle estimates seventy-two hours before Echelon reroutes."

    a "I read the debrief."

    sel "Then you know it was clean."

    a "I know you stepped in front of a thermal charge."

    "The pause. Selene's pauses are never empty — they're calculations."

    sel "The charge was heading for the structural support. If it hit, the ceiling comes down. If the ceiling comes down, Zira's underneath it."

    a "So you body-blocked a thermal charge."

    sel "I deflected it. With my arm."

    a "With your ribs."

    sel "My arm was in front of my ribs. Technically."

    athought "She's doing the Selene thing. Precision as deflection. Reframe the action until the recklessness disappears into the geometry."

    a "How bad?"

    sel "Tessa says two bruised ribs and a laceration. Nothing that affects operational capacity."

    a "That's what Tessa says. What do you say?"

    "Another pause. Longer."

    sel "It hurts when I breathe deep."

    athought "That admission cost her more than the injury."

    # ========== PHASE 2 — HER QUARTERS ==========

    "Her quarters. He walks her there. She doesn't protest — doesn't invite, either. Just doesn't close the door when he follows."

    #scene bg_selene_quarters_night with dissolve
    #play ambient "sfx/ambient/quarters_quiet_warm.ogg" fadein 2.0

    "The room is Selene. Austere but not empty. Military cot, tight corners. A desk with operational maps folded in a neat stack. The plant on the windowsill — the one that Lyra gave her three weeks ago. Small, persistent. It's growing."

    athought "Same cot. Same room."

    athought "Last time I was here, she was unconscious. The raid had taken her down and I carried her back."

    athought "She doesn't know I sat in the chair by the door for four hours, watching her breathe, counting the intervals to make sure they didn't stop."

    athought "She doesn't know. But I think she suspects."

    "She lowers herself to the cot. Careful. The movement catches — ribs protesting."

    sel "Don't."

    a "I wasn't going to—"

    sel "You were going to offer to help. Don't."

    athought "She's right. I was."

    "She manages. Sits. Exhales through her teeth."

    "He takes the chair by the door. The same chair."

    # --- THE CONVERSATION ---

    a "You jumped in front of that charge like you were expendable."

    sel "I jumped in front of it because the math was simple. One person takes the hit, or three people take the collapse."

    a "That's the math. I'm asking about the instinct."

    sel "The instinct is the same as the math."

    a "No, it isn't."

    "She looks at him. The lamp on the desk throws amber across her face. The wound at her ribs is hidden by the jacket, but the way she holds herself — angled, protective — tells the story."

    a "You calculated the ceiling risk in real time. That's tactical. But you didn't delegate. You didn't shout a warning. You moved."

    a "That's not math, Selene. That's reflex. And the reflex says you think you're the one who takes the hits."

    sel "Old habit."

    a "Nineteen years old."

    athought "She flinches. Not visibly — but I've learned to read the micro-expressions. The jaw tightens. The fingers still."

    athought "I just referenced the war room. The night she told me about carrying the weight alone."

    athought "The night she kissed me."

    sel "Some habits are load-bearing. You don't remove them until you're sure the structure holds without them."

    a "Does the structure hold?"

    sel "I don't know yet."

    "She reaches for the cipher on the nightstand. Her grounding habit — the metal disk in her palm, turning it with her thumb."

    "He moves. From the chair to the cot. Not close. At the far end. Respecting the distance she needs."

    "She watches him do it."

    sel "You're not at the door anymore."

    a "No."

    sel "Good."

    # --- THE PIVOT ---

    "Her hand turns the cipher. Once. Twice."

    "He reaches across the space between them and takes her hand. Not the cipher — her hand. His fingers close over hers, stilling the turning."

    athought "The cipher is pressed between our palms. Metal between skin."

    athought "She doesn't pull away."

    sel "Aeron."

    a "Yeah."

    # --- CONSENT GATE A: Vulnerable Admission ---

    sel "I haven't done this in a long time."

    athought "Her voice is low. Not the command voice. Not the briefing voice."

    athought "Something underneath both of those. The voice she doesn't use in rooms with more than one person."

    sel "The sector coordinator. Galan District. That was the last time I—"

    "She stops. Breathes. The breath catches on the bruised ribs."

    sel "Nineteen years is a long time to go without letting someone close enough to see where it hurts."

    athought "She's not talking about the ribs."

    # --- CONSENT GATE B: Matching Vulnerability ---

    a "Neither have I."

    sel "You had relationships."

    a "I had proximity. The Glass Academy didn't teach intimacy. It taught performance."

    a "Everything I did before this — before you — was following a script someone else wrote."

    sel "And now?"

    a "There's no script for this."

    "She looks at their hands. The cipher between them."

    sel "I'm not good at this part. The part where the plan ends and you just... trust it."

    a "I know."

    sel "I need you to know that. Before."

    "His hand moves across the table. Past the cipher. Onto hers."

    # --- CONSENT GATE C: Explicit ---

    sel "If this is a bad call—"

    a "It's the best call we've made all week."

    "She almost laughs. Not quite — the ribs won't let her. But the sound is close enough."

    sel "That's a low bar. This week has been terrible."

    a "Then we're improving."

    "She sets the cipher on the nightstand. Deliberately. Her hand free now."

    "She turns to him. Her free hand — the one that planned operations and held revolutions together and carried nineteen years of solitary weight — comes to rest on his chest."

    sel "Stay."

    "It's not a command. It's not a request."

    "It's a decision."

    # VISUAL: She kisses him. This time it's different from the war room — slower. The urgency is underneath,
    # not on the surface. The lamp catches the scar at her temple. His hand finds the small of her back —
    # careful of the wound, careful of everything.
    # CAMERA: Two-shot. Hold. No cuts.

    athought "She kisses me like she's been thinking about it since the war room."

    athought "Like the nineteen years compressed into the space between the first kiss and this one."

    athought "My hand finds the small of her back. Careful — the wound is on the left side, and I've mapped it without touching it."

    athought "She leans into the contact. Not yielding — choosing."

    athought "Selene doesn't yield. She decides."

    # [INTIMATE CONTENT HERE]

    # ========== PHASE 3 — AFTERCARE ==========

    "After."

    "The lamp is still on. The amber light hasn't changed, but the room feels different. Warmer. Smaller. More hers."

    "Selene lies on her side — the uninjured side. Her back against his chest. His arm over her waist, careful of the ribs."

    athought "Her breathing has changed. Not the measured command cadence. Something slower. Less controlled."

    athought "She's letting the structure hold without her for a minute."

    sel "Don't let this change how we lead."

    a "It already has."

    sel "Aeron—"

    a "We lead better when we trust each other. We trusted each other before tonight. Now we trust each other more."

    a "That's not a complication. That's a resource."

    "She's quiet for a moment. Processing. He can almost hear the assessment running."

    sel "A resource."

    a "That's how you'll file it if you need to justify it to yourself. And it's true."

    sel "You're getting better at reading me."

    a "You're getting worse at hiding."

    athought "She makes a sound. Not quite a laugh. The ribs still won't allow it."

    athought "But it's close."

    "The cipher is on the nightstand. The plant on the windowsill. Dawn is still hours away, but there's a faint paling at the edge of the window — the city's light cycle bleeding through."

    sel "The cipher stays ours."

    a "It was always ours."

    sel "I mean — in the briefing room, in the field, in front of the team. We're co-commanders. That hasn't changed."

    a "Nothing about the command structure has changed. Something else has started."

    "She turns her head. Meets his eyes over her shoulder."

    sel "Started. Not finished."

    a "Not finished."

    athought "She turns back. Settles. Her hand finds mine and threads our fingers together."

    athought "The cipher catches the first gray hint of light through the window."

    athought "The plant on the sill is growing. Slow, persistent. The way everything worth keeping grows."

    "The dawn comes. Gradual. The amber of the lamp gives way to the gray-blue of morning."

    athought "She falls asleep before I do. Her breathing evens out against my chest."

    athought "I stay awake a while longer."

    athought "Not counting her breaths. Not watching for threats."

    athought "Just here."

    #stop ambient fadeout 4.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Selene", trust=2, affection=2)
    $ flag("selene_first_intimate", True)
    $ nudge_poly(1)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s16_command_and_surrender_emp
# cann.chapter: Act III, Phase II - Deepening (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase II. After the first kiss (s14) and the Sector 11 operation.
#   - Night after a close call on the op. The vulnerability breaks through.
# cann.what_happened:
#   - Selene took a thermal charge during the Sector 11 breach — two bruised ribs, laceration.
#     She deflected it to protect Zira from a ceiling collapse. "Old habit."
#   - Post-op: Aeron reads the injury she's hiding. Follows her to her quarters.
#   - Conversation about risk, expendability, and the nineteen-year habit of absorbing all the damage.
#   - The pivot: she reaches for the cipher (grounding habit). He takes her hand instead.
#   - Consent gates: vulnerable admission ("I haven't done this in a long time"), matching vulnerability
#     ("Neither have I"), explicit ("If this is a bad call..." / "Best call we've made all week").
#   - Intimacy in her quarters. Same cot as the carry scene — last time she was unconscious, this time she chooses.
#   - Aftercare: professional decompression. "Don't let this change how we lead." / "It already has."
#     The cipher on the nightstand. The plant catches dawn light.
# cann.aeron_state:
#   - Post-kiss awareness. He reads Selene's composure as a tell, not a truth.
#   - "There's no script for this." — the Glass Academy trained performance, not intimacy.
#   - Careful of the wound. Maps it without touching it.
# cann.path_tracking:
#   - rel_bump("Selene", trust=2, affection=2). flag("selene_first_intimate").
#   - nudge_poly(1) — third seed. Selene's vulnerability opens capacity for later group dynamics.
#   - Requires a3_s14 (first kiss) to have occurred.
# cann.thematic_flags:
#   - Motifs: Cipher (partnership symbol, present on nightstand), the plant (growing, persistent),
#     the wound (vulnerability made physical), dawn light (transition, beginning).
#   - "Old habit." / "Nineteen years old." — the pattern she carries and is learning to set down.
#   - Command and surrender: the title's double meaning. She commands operations. She surrenders control here.
#     Not weakness — choice. "Selene doesn't yield. She decides."
#   - The carry scene callback: same room, same cot. Unconscious then, choosing now. Arc completion.
#   - "A resource." — how she'll justify this to herself. And it's true.
# cann.character_moments:
#   - Selene: Precision as deflection (reframing the charge into geometry). The grounding cipher habit.
#     "Nineteen years is a long time to go without letting someone close enough to see where it hurts."
#     She sets the cipher down — letting go of the symbol to reach for the person.
#   - Aeron: Reads her without pushing. Moves from the chair to the cot — respects the distance.
#     "You're getting worse at hiding." — affection as observation.
# cann.callbacks:
#   - a3_s14: First kiss. "This changes things." / "It already changed." Echoed in aftercare.
#   - a3_s04: Shared command. The trust that makes this possible.
#   - a3_s07: Selene studying the attack pattern. "He didn't plan for you to stay."
#   - The carry scene: same quarters, same cot. The chair Aeron sat in for four hours.
#   - Lyra's plant: growing on Selene's windowsill. Connection between the relationships.
# cann.block_status:
#   - FIRST EROTIC (EMP). No branching. Intimate content marker present.
# cann.requires_followup:
#   - "Started. Not finished." — the relationship is ongoing, not resolved.
#   - The cipher as recurring symbol: command table and nightstand. Professional and personal.
#   - Selene's wound: ribs heal, but the habit of absorbing damage persists. Future testing.
#   - nudge_poly seeds: Selene's capacity for trust is growing. Key for later group dynamics.
#   - The plant: Lyra's gift, growing in Selene's room. Cross-relationship symbolism.
