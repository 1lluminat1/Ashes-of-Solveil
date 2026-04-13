# ================================================================
# CODEX LORE DIALOGUES — short exchanges per LI topic
# File: game/codex/codex_lore_dialogues.rpy
# ----------------------------------------------------------------
# Each label is called from the li_lore_check menu system when the
# player asks an LI about a topic. 5-15 lines per topic. The
# codex_reveal() call happens in the caller (li_lore.rpy), not here.
# ================================================================


# === LYRA (4 topics) ===

label lore_lyra_old_tongue:
    a "The words you use in prayer — the Old Tongue. What is it?"
    l "The language the Ethereal lineage spoke before Solveil standardized everything."
    l "Not a secret language. A forgotten one. The Cathedral kept it alive because the rituals required it."
    a "And Anayet? Seren?"
    l "Anayet means 'to arrive without expectation.' Seren means 'to hold what will break you.'"
    l "The Old Tongue doesn't have a word for 'endure.' Every word for surviving includes the cost."
    a "That's heavy."
    l "(small smile) The language was made by people who thought honesty about weight was more important than pretending to be light."
    return

label lore_lyra_the_six:
    a "The Six. You mention them in prayer. Who are they?"
    l "Not gods. Not people. The Six are... resonance states. The Cathedral teaches that the world holds six frequencies of harmony, and each one is a way of being alive."
    l "Mercy. Witness. Stillness. Motion. Naming. Forgetting."
    a "Forgetting is a resonance state?"
    l "The sixth one. The one most people avoid. The Six teach that to truly hold something, you must also be able to release it."
    l "They don't grade mercy. They count it. That's different."
    a "How?"
    l "Grading asks whether the mercy was deserved. Counting asks whether it happened. The Six only care about whether it happened."
    return

label lore_lyra_the_band:
    a "The Band. What does it actually do?"
    l "It's a transducer. Coil and micro-capacitive array. Passive. It intercepts lineage resonance and translates it to feedback — heat, vibration, pressure."
    l "The bonding ritual at twelve aligns it to your specific frequency. If it takes, you feel the world differently. Colors are slightly richer. Sounds have texture."
    a "And if it doesn't take?"
    l "(quiet) Then the Band rejects you. It heats until the metal blisters. The symbols crack and fade."
    l "But Aeron — the rejection isn't what the Aeries tells you it is."
    a "What do you mean?"
    l "The Band is a container. It channels lineage resonance into something manageable. If the resonance is too strong, the container can't hold it."
    l "Your Band didn't reject you because you were broken. It rejected you because you're pure Verdant. The resonance overwhelmed the device. Instantly."
    l "Kael's held for three years because he carried the bloodline but wasn't pure. The Band fought the resonance until it lost."
    a "So the rejection is the lineage being too much."
    l "The rejection is the Band being too little. The Aeries calls it failure because admitting the truth — that the technology is insufficient for the bloodline — would undermine everything the Branding Program is built on."
    l "The same force that broke your Band is the force that kept Kael alive when he fell. The resonance doesn't obey containers. It protects its own."
    a "No one ever told me that."
    l "No one in the Aeries would. I learned it from Elisse, in the Cathedral archives, in a section they sealed after Wing Seven."
    return

label lore_lyra_cathedral:
    a "The Cathedral. Wing Seven. What happened?"
    l "Wing Seven held the oldest Harmony Cores — the ones from before the collapse. Resonance relics. Fossilized unity."
    l "My mentor Elisse was High Cantor. She spent her life studying how the Cores maintained stability. She believed they were relationships, not power sources."
    l "The containment field ruptured during a calibration exercise. Elisse used her body to shield me."
    a "She died protecting you."
    l "She died proving her theory. The Core destabilized because someone tried to extract power from it without maintaining the relationship. It screamed."
    l "(touches pendant) This shard is all that survived of Wing Seven's primary Core. I wear it because she was right."
    return


# === ZIRA (4 topics) ===

label lore_zira_ghostline:
    a "The Ghostline. How does it actually work?"
    z "Encrypted relay mesh stitched through the city's forgotten infrastructure. Vent fans, rail current, wind in broken spans."
    z "The traffic rides on industrial noise bursts. If you're listening for a signal, you hear static. If you're listening for static, you hear the Ghostline."
    a "You built this?"
    z "I built the current version. The infrastructure was already there. Someone laid the relay paths before me. I just... made them speak."
    z "Access isn't a password. It's trust. The network only answers when it recognizes a keyed beacon and a pattern of behavior."
    a "Pattern of behavior."
    z "You can't hack your way in. You have to earn it by being the kind of person the network wants to talk to."
    return

label lore_zira_unders:
    a "What's it actually like? Living in the Unders?"
    z "Wet. Dark. Full of people who learned to breathe where the city pretends there's no city."
    z "The tiers are a verdict. Aeries gets sunlight. Middle gets surveillance. Unders gets what falls through."
    z "But there's something in the Unders that the upper tiers killed off: community by necessity. You share because you have to. You trust because starving alone is worse than trusting wrong."
    a "The Ashmarket?"
    z "Black market that isn't black. It's just... the market. The only economy that works below the waterline. Favors, information, skills. Credits are useful. Relationships are currency."
    return

label lore_zira_beacon_chip:
    a "The chip you gave me. What is it really?"
    z "Not storage. Not data. It's a cryptographic beacon keyed to the Ghostline's rotating seeds."
    z "When the network is listening, the beacon announces a presence and asks to be let in. Once."
    z "In Act I it was a mark of intent. When synchronization completes, it can surface signed fragments. Proof without context."
    a "Proof of what?"
    z "Enough to tip a conscience. Not enough to convict in a court. The chip doesn't carry evidence — it carries authenticity."
    z "That's the difference between a spy and a witness."
    return

label lore_zira_couriers:
    a "The courier network that Liora used. You built on top of it?"
    z "I didn't know at first. I thought I was laying new relay paths through empty infrastructure."
    z "Then I found the older marks. Pre-Ghostline. Someone had been moving information through the same conduits for years. Not tactics. Stories."
    z "Names. Ledgers. Personal histories of people Echelon erased. Six thousand names, as far as I can count."
    a "She was doing what you do."
    z "She was doing it first. Smaller. Slower. One woman instead of a network."
    z "I built the Ghostline on her ghost. I didn't know it until the courier marks matched."
    return


# === TESSA (3 topics) ===

label lore_tessa_the_board:
    a "The board. The two columns. Why do you keep it?"
    t "Because someone has to count."
    t "The living column is the column I maintain. Every name on it is a person who is alive because of what we built. The dead column is the column I witness."
    a "And the rule of three?"
    t "My mother's rule. Say a name three times. Once to hear it. Twice to mean it. Three times to keep it."
    t "Anything less and the name is noise. Anything more and the ritual replaces the name."
    t "Three is where saying becomes keeping. I learned that at a kitchen table when I was seven."
    return

label lore_tessa_foundry_wards:
    a "The Foundry Wards. Where you grew up."
    t "Middle Levels. Industrial sector. My mother worked the fabrication line. My father maintained coolant systems."
    t "The Wards teach you two things: everything breaks, and someone has to fix it. That's the whole philosophy."
    t "I became a medic because fixing people felt more honest than fixing machinery. The machinery doesn't know it's broken."
    a "What was it like?"
    t "Loud. Hot. Full of people who went home with burns and came back the next morning. The clinic was the only quiet place in the sector."
    t "I learned to love quiet places. That's why the medbay is mine."
    return

label lore_tessa_field_medicine:
    a "Field medicine. How is it different from what Echelon teaches?"
    t "Echelon medicine is efficiency. Triage by tactical value. The officer gets treated before the conscript. The specialist before the grunt."
    t "Field medicine under rebellion is the opposite. You treat the most hurt first. Not the most valuable. The most hurt."
    t "That sounds obvious. It is not obvious when you have four wounded and one of them is your commander."
    a "Have you had to make that choice?"
    t "Every day since I joined Phoenix. Every single day."
    return


# === NOELLE (3 topics) ===

label lore_noelle_cognitive_arch:
    a "Echelon's cognitive architecture. What is it?"
    n "A behavioral modeling framework designed to predict and shape civilian compliance."
    n "Every person in Solveil has a compliance profile. Updated in real time from surveillance data, transaction records, movement patterns, social connections."
    n "The system doesn't punish deviance. It predicts it. Then it reshapes the environment so the deviance never occurs."
    a "That's..."
    n "Elegant. Horrifying. Both are accurate descriptions."
    n "I designed the prediction layer for Sectors 4 through 8. I was very good at it."
    n "When I realized the system was being used to engineer the conditions for the Purge — not just predict unrest, but create it — I walked out."
    return

label lore_noelle_compliance:
    a "The compliance framework you built. Tell me about it."
    n "I modeled human behavior as a system of weighted variables. Trust, fear, routine, social pressure, resource access."
    n "The framework could predict with 94%% accuracy whether a person would comply with a given directive within 72 hours."
    n "The remaining 6%% were the anomalies. People who didn't fit the model."
    a "People like me."
    n "People like you. The 6%% are the ones who make choices the framework can't predict. That's why I defected."
    n "I spent my career eliminating anomalies from the data. Then I realized the anomalies were the only honest data points."
    return

label lore_noelle_name_mechanic:
    a "The Name Mechanic. You mentioned a test in your framework — a name field?"
    n "The framework uses identity markers as anchoring variables. There's a specific test: if a subject provides their real name voluntarily during an unmonitored interaction, the framework classifies it as a trust signature."
    n "Category zero. It means: the subject has chosen to be vulnerable. The framework has no protocol for what to do with voluntary vulnerability."
    a "What happens when someone triggers it?"
    n "The framework processes the input correctly. The analyst does not."
    n "The first time a subject gives you their real name — not a title, not a callsign, not a role — the framework says 'this person trusts you.' And then you have to decide what to do with the fact that your model works and your heart doesn't."
    a "Did that happen with me?"
    n "(quiet) That is a question I am not going to answer with words."
    return


# === SELENE (3 topics) ===

label lore_selene_kael:
    a "Kael. Tell me about him."
    sel "Kael Rylan. Your brother. Born the same year as me."
    sel "His Band worked for three years. Then it turned on him at fifteen. Marcus kept him in the Aeries. Called it mercy."
    a "Kael called it a cage."
    sel "You remember."
    a "He told me. Before the rooftop."
    sel "(quiet) He jumped. You know that. Age seventeen. From the same rail you stood at."
    sel "What you don't know is that he survived."
    a "What?"
    sel "I was there. I was scouting the Aeries — looking for kids who were fracturing, kids the system was breaking. I was seventeen too. Running courier routes for cells that didn't have names yet."
    sel "I saw him on the rail. I saw him go over. And something — his bloodline, the Verdant resonance, something in the fall itself — he didn't die."
    sel "I pulled him out of the wreckage at the base of the span. He was broken in six places but he was breathing."
    a "He never told me."
    sel "He couldn't. Marcus reported him dead. The official record says suicide. Kael let the record stand because a dead man can't be caged."
    sel "He took the survival as fate. He said: 'If the fall didn't kill me, the cage wasn't supposed to hold me.'"
    sel "He gave me nine years after that. Nine years as the best second I ever had. And then the nine-minute window."
    return

label lore_selene_nineteen_years:
    a "Nineteen years. What was the rebellion like before all of this?"
    sel "Smaller. Slower. We lost people and we didn't have enough people to afford losing them."
    sel "The first five years were survival. The next five were structure. The five after that were recruitment. The last four have been... this."
    sel "Before you arrived, Phoenix was a name on a wall. After Liora's courier network started feeding us intelligence, it became a heartbeat."
    a "And you carried it alone."
    sel "I carried the name. The people who died carrying it with me — they carried the weight."
    sel "There were 247 names on the ledger before you joined. Each one of them built the room you walked into."
    return

label lore_selene_shared_command:
    a "Shared command. Where did you learn it?"
    sel "From Kael. He never wanted to lead alone. He said single-point leadership was 'a religion with one priest — doomed to collapse at the first funeral.'"
    sel "After he died, I spent years leading alone. Not because I wanted to. Because nobody else survived long enough to share it with."
    sel "When you arrived and started making decisions that weren't mine, I hated it. Then I realized: this is what Kael was talking about."
    sel "Shared command isn't trusting someone to make the right call. It's trusting them to carry the weight of the wrong one."
    a "Is that what you're teaching me?"
    sel "I'm teaching you what Kael taught me. I'm just nineteen years late delivering it."
    return


# === NYRA (3 topics) ===

label lore_nyra_order_division:
    a "Order Division. What did you do?"
    ny "Population control. Sector discipline. Compliance enforcement."
    ny "The Order Division is the hand inside the glove. Echelon presents a clean facade — infrastructure, services, governance. The Order Division is the mechanism that ensures the facade holds."
    ny "I commanded 340 personnel across four sectors. My unit's compliance rate was 99.2%%. The remaining 0.8%% were... resolved."
    a "Resolved."
    ny "The word means what you think it means. I am not going to soften it."
    return

label lore_nyra_purge_inside:
    a "The Purge. You were there. From the inside."
    ny "I was deployed to Sector 8's eastern perimeter. The briefing said 'containment.' The field said 'extermination.'"
    ny "I am not a woman who flinches. I did not flinch that night."
    ny "What I did was count. I counted the bodies that did not match the threat profile. Children. Elderly. People who were running toward the checkpoints because they thought the checkpoints meant safety."
    ny "The checkpoints did not mean safety."
    a "That's when you defected."
    ny "That is when I decided the regime's sin was not cruelty. The regime's sin was sloppiness. Undirected violence. Waste."
    ny "I left because the machine was broken. Not because it was cruel."
    return

label lore_nyra_doctrine:
    a "Doctrine. What does obedience actually mean to you?"
    ny "Structure. Not servitude. Structure."
    ny "Obedience to a person is worship. Obedience to a system is engineering. I am an engineer."
    ny "When the system I served became sloppy, I left it. When I found a man building a disciplined alternative, I joined him."
    a "Me."
    ny "You. Not because you are good. Because you are clear. Clarity is the rarest thing in a city that runs on obfuscation."
    ny "I do not need you to be kind. I need you to be consistent. Consistency is the skeleton of trust."
    return
