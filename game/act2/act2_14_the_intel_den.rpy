# =======================================================
# ACT 2 - Scene 14: The Intel Den
# File: act2_14_the_intel_den.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_14_the_intel_den"
$ scene_mark(_current_scene_id, "entered")

label act2_14_the_intel_den:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Wide establishing shot of the den, then medium shots. Noelle often framed through data screens. Push-in when she says something unexpectedly human.
    # LIGHTING: Silver-blue from multiple screens. Cold, clinical, but with warm spots from tea steam or small personal items. Her data crystal catches light.
    # SFX: Loop — soft hum of processors, keyboard clicks, cooling fans. One-shots — data chimes, her stylus tapping, tea being poured.
    # FX/COMP: Data walls with scrolling analysis, holo-threads connecting information, patrol maps, behavioral models.
    # BLOCKING/PROPS: Noelle's workspace—converted server room. Screens everywhere. A single plant (barely alive). Tea setup. Data crystal on wrist.
    # FACE: Noelle analytical, guarded, but with moments of curiosity that crack the mask. Aeron being studied. Zira comfortable here.

    # ========== THE INTEL DEN — DAY 7 ==========

    "The Intel Den exists in the gaps between systems."

    "An old server room, abandoned when the data routes shifted upward. Now it hums with repurposed purpose—screens covering every wall, cables running like veins through the infrastructure."

    # VISUAL: Aeron and Zira entering. The space is cramped but organized. Every surface covered with data.
    "Zira leads him through a narrow access corridor into the heart of it."

    z "Don't touch anything. She has a system."

    a "I can see that."

    "The room is chaos organized into meaning. Patrol routes on one wall, behavioral models on another, a web of connections linking names and places and probabilities."

    "And at the center of it all, her back to them, sits Noelle Korr."

    # VISUAL: Noelle at her workstation. Silver-blue screens reflecting off her face. Data crystal on her wrist. Smaller than expected.
    "She's smaller than he imagined. The voice on the comms had carried such precision, such weight—he'd pictured someone imposing."

    "Instead, she's slight. Sharp features softened by the glow of her screens. Dark hair pulled back with practical efficiency."

    "On her wrist, a data crystal catches the light. The fragment of truth she carried out of Echelon."

    n "(without turning) You're four minutes early. Consistent with your approach pattern from the depot."

    a "You've been tracking my approach patterns?"

    n "I track everything, Captain. That's the point."

    "She turns."

    # VISUAL: Noelle facing them. Eyes like analysis—measuring, categorizing, filing. A flicker of something human underneath.
    "Her eyes are the color of the screens behind her. Gray-blue. Assessing."

    "She doesn't smile. She observes."

    n "Noelle Korr. Former Cognitive Division. Currently... freelance."

    a "I know who you are."

    n "You know a voice on a comm channel. This is different."
    n "In person, I can observe micro-expressions, body language, respiratory patterns."
    n "You're more nervous than you were during the operation. Interesting."

    z "(sighing) Noelle, can we skip the diagnostic and get to the debrief?"

    n "The diagnostic is the debrief, Zira. His performance tells me more than any report."

    if empathy_band() == "obedience":
        athought "She's profiling me. Again. But this time I can profile her back."
        athought "The plant on the corner—barely alive but still there. The tea setup. Signs of humanity she hasn't eliminated."
    else:
        athought "She's measuring me. But she's also nervous—the way she keeps touching the data crystal."
        athought "We're both performing versions of ourselves."

    # ========== THE DEBRIEF ==========

    "Noelle pulls up the depot operation on her main display. Every movement tracked, every decision logged."

    n "The operation was a success. Supplies secured, no pursuit, minimal evidence trail."
    n "But the interesting data isn't the outcome. It's the methodology."

    "She highlights a section of the timeline."

    if scene_has("act2_12_proof_of_intent", "guard_spared"):
        n "Here. The checkpoint complication. A replacement guard in your exit path."
        n "Standard tactical doctrine says eliminate the obstacle. Cade was ready to execute."
        n "You took a four-minute detour through a drainage system instead."

        a "There was another way. I found it."

        n "You found it because you were looking for it."
        n "The drainage grate wasn't in any operational database. You remembered a budget argument from two years ago."
        n "That's not tactical efficiency. That's..."

        "She pauses. Searching for the word."

        n "...Conscience. You have one. Active, not dormant."

        z "Is that a diagnosis?"

        n "It's an observation. Conscience in a field operative is usually a liability."
        n "But you made it work. The mission succeeded and the guard survived."
        n "That's the anomaly I keep finding in your data, Captain. You shouldn't work, but you do."

        if scene_has("act2_08_the_analyst", "admitted_break"):
            n "You told me something broke on that rooftop. I'm beginning to understand what replaced it."
        else:
            n "You deflected when I asked what happened on that rooftop. But I'm starting to see the answer anyway."

    else:
        n "Here. The checkpoint complication. Replacement guard, eliminated efficiently."
        n "Standard tactical doctrine, executed without hesitation. Cade confirmed the takedown was clean."

        a "He was in the way. The mission required movement."

        n "Yes. That's the expected response from someone with your training."
        n "But I observed something interesting in the post-operation data."

        "She highlights another section."

        n "Your vocal stress patterns after the elimination. Elevated for approximately ninety seconds."
        n "Consistent with suppressed emotional response, not tactical processing."

        a "You're reading a lot into breathing patterns."

        n "I'm reading what the data shows, Captain. You made the efficient choice, but it cost you something."
        n "That cost is interesting. Glass wouldn't have felt it."

        if scene_has("act2_08_the_analyst", "admitted_break"):
            n "You told me something broke. I'm seeing evidence of what's trying to grow in its place."
            n "Even when you make the cold choices, they're not cold to you anymore."
        else:
            n "You deflected my question about the rooftop. But the answer is in your data."
            n "Something changed. You're not Glass anymore, even when you act like him."

    # ========== PROTOCOL VERDANT ==========

    n "Now. The more pressing matter."

    "She pulls up another display. Encrypted files, partial decryption, fragments of text."

    n "I've made progress on Protocol Verdant."

    "Aeron stiffens. Zira notices."

    z "That's the bloodline thing you mentioned?"

    n "It's considerably more than a 'bloodline thing.'"
    n "The fragments I've recovered reference something called the Verdant Concordat. Pre-Echelon documentation."
    n "It appears to be a genetic designation tied to Harmony Core compatibility."

    a "Compatibility with what?"

    n "That's the question. The data is heavily redacted, but certain phrases recur."
    n "'Resonance potential.' 'Synchronization threshold.' 'Viable conductor.'"

    "She pulls up another fragment."

    n "And this: 'The last viable candidate must be preserved for Protocol completion.'"
    n "Your name is attached to seventeen references, Captain. Your father's signature is on all of them."

    if empathy_band() == "obedience":
        athought "Marcus has been planning something with my bloodline. Something the Branding was supposed to prepare me for."
        athought "The Branding that didn't take. That 'failed.'"
        athought "Or did it?"
    else:
        athought "My whole life—the training, the Branding, the pressure to be perfect..."
        athought "It wasn't just about making me into a soldier. It was about making me into... what?"

    a "What does 'Protocol completion' mean?"

    n "Unknown. But the documentation treats it as an endpoint, not a process."
    n "Whatever your father has planned, you're central to it."
    n "Which explains why he's hunting you so aggressively. You're not just a traitor to him."
    n "You're an asset he can't afford to lose."

    z "That's... actually more terrifying than him just wanting to kill you."

    a "Thanks for that, Zira."

    z "I call it like I see it."

    # ========== THE HUMAN MOMENT ==========

    "Noelle turns back to her screens. Then pauses. Something shifts in her posture."

    n "Tea?"

    a "What?"

    n "I have tea. It's a habit I retained from the Cognitive Division."
    n "The ritual of preparation helps me process. You look like you could use processing time."

    "Zira raises an eyebrow at Aeron. This isn't typical Noelle behavior."

    z "(mouthing) She likes you.

    "Noelle's ears turn slightly pink. She heard that."

    n "I don't 'like' anything, Zira. I observe and categorize."
    n "The Captain's stress indicators suggest caffeine would be beneficial. That's all."

    if empathy_band() == "empathy":
        a "I'd like some tea. Thank you."

        "Something flickers across her face. Surprise, maybe. Or something she doesn't want to categorize."

        n "It's nothing elaborate. Standard Unders ration blend."

        a "That's fine. The offer is what matters."

        "She prepares the tea. Her movements are precise but not mechanical—ritual, like she said."

        "When she hands him the cup, their fingers brush. She pulls back quickly."

        n "The steam."

        a "What about it?"

        n "It's... aesthetically notable. The way it curls."
        n "I find myself tracking it sometimes. The patterns."

        athought "She's nervous. The data analyst who measures everything is nervous because our fingers touched."
        athought "That's more human than anything she's said since I walked in."

        $ npc_remember("Noelle", "tea_moment_steam_curl", tone="flustered")
        $ scene_mark(_current_scene_id, "steam_curl_moment")

    else:
        a "I'm fine. But thank you."

        "She nods. Files the rejection away like another data point."

        n "Noted. The offer stands if you change your assessment."

        athought "She was reaching out. In her way."
        athought "And I shut it down. Maybe that was the right call. Maybe not."

    # ========== CLOSING — THE ANALYST'S ASSESSMENT ==========

    n "One more thing, Captain."

    a "What?"

    n "Selene has reviewed my analysis of the depot operation."
    n "Combined with Cade and Mira's field reports, she's... satisfied."

    a "Satisfied isn't the same as trusting."

    n "No. But it's closer than you were yesterday."
    n "She wants to discuss next steps. Base acquisition, resource allocation, command structure."

    z "Which means she's thinking long-term. That's new."

    n "The rebellion has been in survival mode for years. A tactical asset like the Captain changes the calculus."
    n "She's beginning to imagine a future where they do more than just endure."

    "Noelle looks at him. Direct. Analytical. But with something else underneath."

    n "You're an anomaly, Captain Rylan. You defy my models."
    n "I find that professionally frustrating and personally..."

    "She doesn't finish the sentence. Just turns back to her screens."

    n "Zira will show you out. I have data to process."

    z "(to Aeron) That's Noelle for 'I need to think about my feelings and I don't know how.'"

    n "I heard that."

    z "I know."

    # VISUAL: Aeron and Zira leaving the Intel Den. Noelle already absorbed in her screens again, but her hand resting on the data crystal.
    "They leave her surrounded by data. The glow of screens. The fragment of truth on her wrist."

    "But just before the door closes, Aeron sees her touch the tea setup."

    "A small gesture. A human one."

    athought "She's not just an analyst. She's someone who fled her own mind and is still trying to find her way back."
    athought "We have that in common, maybe."

    # --- SCENE WRAP ---
    $ encounter_inc("Noelle")
    $ flag_on("Noelle", "met_in_person")
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_14_the_intel_den
# cann.chapter: Act II, Chapter III — Proving Ground
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Day 7. Post-depot operation debrief. First in-person meeting with Noelle.
# cann.what_happened:
#   - Aeron and Zira visit Noelle's Intel Den—converted server room, screens everywhere.
#   - Noelle is smaller than expected. Data crystal on wrist. Analytical but human underneath.
#   - Debrief covers depot operation—Noelle analyzes the guard decision from A2_12.
#   - EMP/spared: She notes his "active conscience" as the anomaly that shouldn't work but does.
#   - OB/eliminated: She notes his elevated stress patterns—"the cold choice still cost you something."
#   - Protocol Verdant update: Genetic designation, Harmony Core compatibility, "last viable candidate."
#   - Tea moment: Noelle offers tea (human gesture). EMP path gets the "steam curl" moment. OB path deflects.
#   - Selene's verdict: "Satisfied" with the operation. Thinking long-term now.
#   - Noelle admits Aeron "defies her models"—"professionally frustrating and personally..."
# cann.aeron_state:
#   - Being analyzed in person, but starting to see the human beneath Noelle's data armor.
#   - Callbacks to A2_08 (admitted break vs deflected) and A2_12 (guard decision).
# cann.path_tracking:
#   - No empathy choices in this scene—it's reactive to prior choices.
#   - Callbacks to: A2_08 (admitted_break vs deflected_break), A2_12 (guard_spared vs guard_eliminated).
#   - `steam_curl_moment` flag set only if EMP band + accepts tea.
#   - NPC memory stored if steam curl moment occurs.
#   - Running empathy range at scene end: -16 to +6 (unchanged from A2_12).
# cann.thematic_flags:
#   - Motifs: Data as armor, the steam curl as unexpected beauty, truth fragments.
#   - Noelle's humanity breaking through: the plant, the tea ritual, touching the data crystal.
#   - "You defy my models" — her intellectual framework challenged by feeling.
#   - Protocol Verdant deepening—Aeron is central to something Marcus has planned.
# cann.alignment_flavor_points:
#   - Opening: Different internal reads on Noelle's space
#   - Debrief: Different analysis based on A2_12 guard choice
#   - Protocol Verdant: Different internal processing
#   - Tea moment: Accept (EMP) vs decline (OB)
# cann.character_moments:
#   - Noelle: Analytical mask cracking. The tea offer is huge for her. "Steam curl" shows capacity for beauty.
#   - Zira: Comfortable here, teasing Noelle, "She likes you."
#   - The unfinished sentence: "professionally frustrating and personally..."
# cann.worldbuilding:
#   - Intel Den: Converted server room in the gaps between systems.
#   - Protocol Verdant: Verdant Concordat (pre-Echelon), genetic designation, Core compatibility.
#   - "Last viable candidate" — Aeron is meant for something specific.
# cann.block_status:
#   - Noelle full introduction complete. Steam curl moment (EMP) sets up later intimacy path.
# cann.requires_followup:
#   - Protocol Verdant will need further exploration (possibly Lyra connection—Ethereal heritage).
#   - Steam curl can echo in later Noelle intimate scenes.
#   - Selene meeting (base acquisition, command structure) is next major beat.
#   - A2_15: Zira×Noelle pair scene follows naturally from this setting.
