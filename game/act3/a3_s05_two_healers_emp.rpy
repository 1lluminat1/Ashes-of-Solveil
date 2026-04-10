# =======================================================
# ACT 3 - Scene 05: Two Healers (Empathy Path)
# File: a3_s05_two_healers_emp.rpy
# Type: PAIR ANCHOR (Lyra x Tessa)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s05_two_healers_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s05_two_healers_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35mm, handheld with intent. Opens on the medbay from the doorway — Aeron's POV,
    #         peripheral. Tightens to two-shots of Lyra and Tessa as they work. Close-ups on hands —
    #         Tessa's surgical, Lyra's ritualistic. Never cuts to Aeron during the core sequence;
    #         this belongs to them. Returns to his POV only at the bookends.
    # LIGHTING: Mixed — surgical overhead strips (5600K harsh) on the treatment area, amber
    #           practicals (2800K) at the edges where supplies are stacked. Lyra's hands occasionally
    #           catch warm light when she moves between stations. Tessa stays in the white.
    # SFX: Loop — medbay ambient: ventilation, rattling breath from wounded, IV drip, generator hum.
    #       One-shots — bandage tear, water pour, mortar-and-pestle grind, soft chanting under breath,
    #       patient groan, metal tray set down.
    # FX/COMP: Steam from boiled dressings. Lyra's herbal preparations — green and amber in ceramic bowls.
    #          Tessa's instruments — clean, improvised, efficient. The contrast of their workstations
    #          tells the story before anyone speaks.
    # BLOCKING: Medbay. Three patients on cots — one serious, two stable. Lyra and Tessa move between them.
    #           Aeron in the doorway initially, then seated on a supply crate at the edge. Watching.
    # FACE: Lyra — focused, gentle, her movements slower and more deliberate than Tessa's but equally precise.
    #        Tessa — efficient, warm, hands never stopping. Eyes checking Lyra's work without judgment.
    #        Aeron — peripheral. Quiet recognition of something he doesn't fully understand yet.

    # ========= VOICE BASELINE =========
    # EMP cadence. Aeron-peripheral — he observes but doesn't drive.
    # Lyra: Measured. The cadence of someone taught that healing begins with presence.
    # Tessa: Direct but warm. Hands-first, explanation-second.
    # The emotional core is mutual respect between two different healing traditions.

    # ========== MEDBAY — POST-OPERATION ==========

    #scene bg_medbay_emp with dissolve
    #play ambient "sfx/ambient/medbay_warm.ogg" fadein 2.0

    "Three patients from the corridor extraction. One with a broken collarbone from a collapsed access hatch. Two with exposure symptoms — dehydration, mild hypothermia, the particular exhaustion of people who spent seventy-two hours waiting to be saved."

    "Tessa has the collarbone. Lyra has the exposure cases."

    "Aeron stands in the doorway. He came to check on the wounded. He stays because of what he sees."

    # --- TESSA: THE SURGEON ---

    "Tessa's hands are already moving. Splint materials laid out in order of use — padding, rigid support, binding. Her fingers test the break through the skin, reading the fracture like text."

    t "Clean break. No displacement. You're lucky."

    "The patient — a middle-aged woman with dust in her hair and terror still fading from her eyes — grips the edge of the cot."

    t "I'm going to set the splint now. It'll hurt for about ten seconds and then less. Breathe through it."

    "No preamble. No false comfort. Just the truth and the hands to back it up."

    # --- LYRA: THE RITUALIST ---

    "Across the medbay, Lyra works differently."

    "She kneels beside the first exposure patient — a young man, barely conscious, lips cracked and grey. A ceramic bowl in her hands, steam rising from something that smells like crushed herb and clean water."

    l "Can you hear me?"

    "A faint nod."

    l "Good. I'm going to warm you from the inside first. Small sips. Don't rush."

    "She lifts his head. Steady. Patient. The bowl tilts and he drinks — slow, shallow pulls that she monitors with the focus of someone counting heartbeats."

    athought "She holds him like he's the only person in the room."

    # --- THE CONTRAST ---

    "Aeron settles onto a supply crate near the door. He didn't decide to sit. His body made the choice."

    athought "They work differently. Tessa moves like triage is a language she dreams in — fast, efficient, every motion earning its place."

    athought "Lyra moves like healing is a form of prayer. Slower. More deliberate. Each step carrying the weight of intention."

    "Tessa finishes the splint. Checks the binding tension with two fingers. Nods to herself."

    t "You'll wear this for six weeks. If the pain sharpens instead of fading, find me immediately."

    "She's already turning to the supply shelf. Gauze. Antiseptic. A cloth soaked in something that stings — Aeron can smell it from the doorway."

    "Lyra finishes the broth. Sets the bowl down. Presses two fingers to the patient's wrist. Holds them there, eyes closed, lips moving without sound."

    athought "She's counting his pulse. Or praying over it. Maybe both."

    # --- THE INTERSECTION ---

    "The second exposure patient is worse. Shivering despite the blankets. Skin clammy, breathing shallow."

    "Tessa reaches her first. Pulls back the blanket, checks pupil response, presses her palm flat against the patient's sternum."

    t "Core temp is dropping. She needs warming and fluids, but the IV line is occupied."

    "She looks across the medbay."

    t "Lyra. What's in that bowl?"

    l "Yarrow and ginger root in boiled water. It dilates the peripheral vessels — draws blood back to the surface."

    t "How fast?"

    l "Fifteen minutes for the first flush. Thirty for sustained effect."

    "Tessa pauses. Her hand still on the patient's sternum, reading the data through skin."

    t "I don't have anything in my kit that works that fast without an IV push."

    "A beat. The two healers look at each other across the patient."

    l "I can prepare a second dose."

    t "Do it. I'll monitor her vitals while it takes effect."

    # --- WORKING TOGETHER ---

    "What happens next is the thing Aeron will remember."

    "Lyra prepares the infusion. Mortar and pestle grinding the dried root. Water heated over the portable burner. Her hands move through the steps with the precision of ritual — each motion practiced, inherited, old."

    #play sound "sfx/one_shot/mortar_grind_soft.ogg"

    "Tessa monitors. Pulse. Respiration. Core temperature estimated through skin contact and the particular knowledge of someone who has treated hypothermia in the field with nothing but instinct and stubbornness."

    "Lyra brings the bowl. Tessa lifts the patient's head. Lyra tips the liquid. Tessa watches the throat for swallow reflex."

    "They move around each other without collision — Lyra's ritual, Tessa's medicine, the patient between them."

    $ nudge_poly(1)

    athought "They've never rehearsed this. There's no protocol for what they're doing."

    athought "Tessa adjusts the blanket while Lyra tilts the bowl. Lyra steps back as Tessa leans in to check the pulse. Their hands pass in the same space without touching, without hesitation."

    athought "Like instruments in the same piece of music, written in different keys, somehow finding the same chord."

    # --- THE TURN ---

    "Ten minutes. The patient's shivering slows. Color creeps back into her face — faint, but present."

    t "Peripheral circulation is improving. Pulse is stronger."

    "She looks at Lyra."

    t "That infusion. Where did you learn it?"

    l "The Order. It was part of the caretaking discipline. We used it for pilgrims who collapsed during the mountain crossings."

    t "Mountain crossings. How cold?"

    l "Cold enough that conventional warming wasn't always available. The ritual predates modern field medicine by two hundred years."

    "Tessa's eyebrows rise. Not skepticism — the genuine surprise of someone encountering a tool she didn't know existed."

    t "Two hundred years. And it dilates the peripheral vessels."

    l "Among other things. The yarrow is also a mild coagulant. Useful when you're treating people who tend to injure themselves on frozen rock."

    t "Lyra."

    l "Yes?"

    t "That's brilliant."

    "Lyra blinks. Whatever she expected, it wasn't that."

    l "It's just... what I was taught."

    t "What you were taught is two hundred years of field-tested vasodilation therapy that I've been trying to replicate with synthetic compounds we can't afford."

    "She reaches for Lyra's mortar. Picks up a pinch of the dried root. Smells it. Rolls it between her fingers."

    t "How much of this do you have?"

    l "Enough. I cultivate the yarrow in the base garden. The ginger root I can source from the lower market."

    t "Show me the preparation steps. All of them. I want to understand the dosing ratios."

    # --- THE REVELATION ---

    "Lyra does. Step by step. Grinding, steeping, temperature, timing."

    "Tessa takes notes on a scrap of bandage wrapping. Her handwriting is terrible. Lyra's corrections are gentle."

    l "The water should be just below boiling. Not at boiling — the active compounds break down above ninety-five degrees."

    t "Ninety-five. Got it."

    l "And the steeping time matters. Four minutes for mild cases. Seven for severe. Past ten minutes, the concentration becomes counterproductive."

    t "Counterproductive how?"

    l "The vasodilation overshoots. Blood pressure drops instead of stabilizing."

    t "So there's a therapeutic window. Just like pharmaceutical dosing."

    l "We didn't call it that. We called it listening to the preparation."

    "Tessa laughs. Quiet. The exhausted laugh of a healer who just found an ally she didn't expect."

    t "Listening to the preparation. I like that."

    l "Tessa."

    t "Hmm?"

    l "Your splint technique. The way you test the binding tension with two fingers."

    t "What about it?"

    l "In the Order, we were taught to immobilize fractures with cloth wrapping and prayer. The prayer was supposed to promote bone knitting."

    t "Did it work?"

    l "The cloth wrapping worked. The prayer was... optional."

    "Tessa grins."

    l "Your method is faster. More precise. The binding tension check — it accounts for swelling that the traditional method ignores."

    l "Could you teach me?"

    "Tessa stares at her."

    t "You want me to teach you splinting?"

    l "I want to learn what you know. So that when you're not here, I can still help."

    "Something crosses Tessa's face. Aeron has seen it before — on the balcony, in the war room, in the quiet moments when someone says the thing that matters without knowing it matters."

    t "Yeah. I can teach you."

    # --- THE THESIS ---

    "They stand over the sleeping patient. The second exposure case is stable now — color returning, breathing steady, the infusion doing its quiet work."

    l "Your discipline saved her life."

    t "Your ritual gave me the tool to do it."

    "A pause. Neither of them needs to name it."

    l "Discipline serves care. Not the other way around."

    "Tessa nods. Slow."

    t "Discipline serves care."

    t "I should write that on the medbay wall."

    l "In your handwriting? Nobody would be able to read it."

    "Tessa's laugh is startled. Real. The sound fills the medbay and doesn't disturb a single patient."

    # --- AERON: PERIPHERAL CLOSE ---

    athought "I've been sitting on this crate for forty minutes."

    athought "I came to check on the wounded. I stayed because of them."

    athought "Tessa's medicine and Lyra's ritual aren't competing. They never were. The framework is different. The purpose is the same."

    athought "Discipline serves care."

    athought "I think that might be true for more than medicine."

    "He stands. Quiet. Neither of them notices him leave."

    "In the doorway, he pauses. Looks back."

    "Lyra is demonstrating the mortar technique. Tessa is watching her hands with the attention she usually reserves for wound assessment. Their shoulders are close. Lyra says something and Tessa tilts her head, and for a moment they exist in the particular stillness of two people discovering they speak the same language."

    athought "Something is building there. I don't have a name for it yet."

    athought "I don't think they do either."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ scene_mark(_current_scene_id, "anchor_seen")
    $ npc_remember("Lyra", "taught_tessa_herbal_medicine", tone="quiet_pride")
    $ npc_remember("Tessa", "learned_lyra_vasodilation_technique", tone="professional_excitement")
    $ npc_remember("Lyra", "asked_tessa_splint_training", tone="earnest_humility")
    $ npc_remember("Tessa", "lyra_complimented_splint_method", tone="surprised_warmth")
    $ rel_bump("Lyra", affection=1, trust=1)
    $ rel_bump("Tessa", affection=1, trust=1)
    $ flag("two_healers_seen", True)
    $ flag("discipline_serves_care", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s05_two_healers_emp
# cann.chapter: Act III, Phase I — Proving Ground
# cann.chapter_start: False
# cann.when_in_timeline:
#   - After corridor extraction (whether Silence path or standard approach from a3_s04a).
#   - Wounded from the operation are being treated. Lyra and Tessa co-treating.
# cann.what_happened:
#   - Three patients from the corridor extraction. One broken collarbone, two exposure cases.
#   - Tessa treats the fracture (surgical efficiency). Lyra treats exposure (herbal ritual).
#   - The second exposure case is severe. Tessa lacks IV supplies. Lyra's yarrow-ginger infusion
#     provides vasodilation therapy that Tessa can't replicate with available synthetics.
#   - They co-treat: Lyra prepares, Tessa monitors, seamless collaboration without rehearsal.
#   - Mutual discovery: Lyra's 200-year-old Order technique is field-tested vasodilation therapy.
#     Tessa's splint method accounts for swelling the traditional Order wrapping ignores.
#   - They agree to teach each other. Lyra wants Tessa's splinting. Tessa wants Lyra's herbalism.
#   - Scene thesis: "Discipline serves care. Not the other way around."
#   - Aeron is peripheral — observes but does not drive the scene.
#   - Poly foreshadowing nudge: "They move around each other without collision."
# cann.aeron_state:
#   - Peripheral observer. Came to check on wounded, stayed because of Lyra and Tessa.
#   - Recognizes something building between them. Doesn't name it. Neither do they.
# cann.path_tracking:
#   - No player choice — pair anchor (observational for Aeron, catalytic for Lyra/Tessa).
#   - scene_mark("anchor_seen") for pair anchor tracking.
#   - rel_bump: affection+1, trust+1 for both Lyra and Tessa.
#   - nudge_poly(1) fires during the seamless co-treatment sequence.
#   - flag("two_healers_seen"), flag("discipline_serves_care") for callbacks.
# cann.thematic_flags:
#   - "Discipline serves care. Not the other way around." — Scene thesis.
#   - Two healing traditions: Tessa's empirical medicine, Lyra's ritual herbalism.
#     Different frameworks, same purpose. Complementary, not competing.
#   - Mirror of a2_s18_the_patient (Tessa x Noelle): care as unmodeled variable.
#     Here: tradition as unrecognized medicine.
#   - "Like instruments in different keys, somehow finding the same chord."
#   - Poly foreshadowing: physical synchronization without rehearsal, mutual teaching,
#     the "something building" that Aeron can see from the outside.
# cann.character_moments:
#   - Lyra: Quiet pride in what she was taught. Humble enough to ask Tessa for splinting.
#     Her ritual is not superstition — it is two hundred years of field-tested medicine.
#     "We called it listening to the preparation." — Her framework in one sentence.
#   - Tessa: Genuine surprise at Lyra's technique. Professional enough to recognize it.
#     "That's brilliant." — No hedging, no qualification. Direct respect.
#     Terrible handwriting. Lyra's gentle corrections. The humor that lives between them.
#   - Aeron: "I don't think they do either." — Sees the poly formation before anyone names it.
# cann.block_status:
#   - PAIR ANCHOR (Lyra x Tessa). Both paths compatible.
# cann.requires_followup:
#   - Lyra and Tessa teaching each other — should appear in subsequent medbay scenes.
#   - "Discipline serves care" as a recurring line through Act 3 EMP.
#   - Poly arc: nudge_poly(1) is the first seed. Future scenes should increment.
#   - Yarrow-ginger infusion as a recurring medical tool in Phoenix operations.
#   - Lyra's base garden — established here as a resource, explorable in future scenes.
