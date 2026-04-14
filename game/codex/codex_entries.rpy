# ===================================================
# Solveil Codex Entries — authoring file
# Register here; the system file will ingest on start.
# ===================================================

init 1 python:
    CODEX_ENTRIES = {
        "ghostline": {
            "title": _("Ghostline"),
            "category": _("Systems"),
            "tags": ["mesh","relay","Unders"],
            "body": [
                _("Encrypted relay mesh stitched through forgotten Unders infrastructure."),
                _("Traffic rides on industrial noise bursts ('ghost hops')."),
                _("Access rotates via beacons curated by Zira."),
            ],
        },
        "beacon_chip": {
            "title": _("Beacon Chip"),
            "category": _("Artifacts"),
            "tags": ["token","credential","Zira"],
            # staged example: stage 0 → vague; stage 1 → full
            "stages": [
                { "body": [ _("A sealed credential token. Purpose unclear.") ] },
                { "body": [
                    _("Not storage—credential. Later authenticates Aeron on Ghostline."),
                    _("Contains a signed attest shard related to the purge."),
                ]},
            ],
        },
        "obsidian_bridge": {
            "title": _("Obsidian Bridge"),
            "category": _("Places"),
            "tags": ["Sector 10","carrier hiss","meet site"],
            "body": [
                _("Decommissioned black composite span in Sector 10."),
                _("Wind shear generates a carrier hiss Zira uses to mask comms."),
                _("Path evaluation happens here [r1](criteria withheld)[/r]."),
            ],
        },
        "purge_8_10": {
            "title": _("Purge — Sectors 8–10"),
            "category": _("Events"),
            "tags": ["state action","containment","atrocity"],
            "body": [
                _("Coordinated sweep executed without public pre-notice."),
                _("Aeron and Lyra do not know beforehand; witnessing it reorients their moral axis."),
            ],
        },
        "harmony_cores": {
            "title": _("Harmony Cores"),
            "category": _("Artifacts"),
            "tags": ["resonance","relic","instability"],
            "body": [
                _("Resonance relics of Verdant/Ethereal unity—fossilized coherence, not batteries."),
                _("Instability grows the further use departs from harmony."),
            ],
        },
        "lineages": {
            "title": _("Verdant & Ethereal Lineages"),
            "category": _("Lore"),
            "tags": ["Aeron","Lyra","unity"],
            "body": [
                _("Verdant: attuned to living systems (embodied empathy)."),
                _("Ethereal: attuned to structure/clarity (disciplined purpose)."),
                _("Union theme: harmony as relationship."),
            ],
        },
        "bands": {
            "title": _("Resonance Bands"),
            "category": _("Systems"),
            "tags": ["haptic","intercept","tuning","rejection"],
            "stages": [
                { "body": [
                    _("Passive wrist transducers (coil + micro-capacitive array)."),
                    _("They intercept lineage resonance and translate it to haptic/thermal feedback (tune/dampen/spike)."),
                ]},
                { "body": [
                    _("Passive wrist transducers (coil + micro-capacitive array)."),
                    _("They intercept lineage resonance and translate it to haptic/thermal feedback (tune/dampen/spike)."),
                    _("The Cathedral's archived term for Band rejection was not 'failure.' It was 'excess.' The archives were sealed after Wing Seven."),
                    _("Some rejections are immediate. Others take years. The reasons for the difference are not publicly understood."),
                ]},
            ],
        },
        "solveil_tiers": {
            "title": _("Solveil — Aeries / Middle / Unders"),
            "category": _("Places"),
            "tags": ["city-state","strata"],
            "body": [
                _("Aeries (elite terraces above the clouds)."),
                _("Middle (industrial stacks)."),
                _("Unders (derelict strata and ghostlines)."),
            ],
        },
        "glass": {
            "title": _("Glass (Aeron)"),
            "category": _("Motifs"),
            "tags": ["dissociation","shame","mask"],
            "body": [
                _("Aeron’s dissociative shell—transparent, empty, sharp when needed."),
                _("Returns as a faint metallic ping when shame flares."),
            ],
        },
        "ghost_hop": {
            "title": _("Ghost Hop"),
            "category": _("Systems"),
            "tags": ["burst","transmission","ambient"],
            "body": [
                _("A single-burst transmission that skips across Ghostline nodes like a stone over water."),
                _("Each hop rides an ambient noise band—rail hum, coolant fans, the wind along the Bridge."),
                _("The message is short by design: 'Here.' 'Safe?' 'Now.' Long enough to save a life, too brief to trace."),
            ],
        },
        "carrier_hiss": {
            "title": _("Carrier Hiss"),
            "category": _("Systems"),
            "tags": ["ambient","masking","Obsidian Bridge"],
            "body": [
                _("Engineers call it a nuisance band. Runners call it cover."),
                _("On the Obsidian Bridge, certain crosswinds create a stable hiss that eats most sensor sweeps."),
                _("Zira learned to 'retune' the air with a snap of her fingers, training ears to hear signal inside noise."),
                _("Once you know the hiss, you can't unhear it—it's the sound of a city pretending to sleep."),
            ],
        },

        # =============================================
        # CHARACTERS — LOVE INTERESTS
        # Each entry has 4 stages. Stage 0 unlocks on first
        # appearance; Stages 1–3 unlock via codex_reveal() as the
        # player earns more of the character's shape.
        # =============================================

        "lyra_vashar": {
            "title": _("Lyra Vashar"),
            "category": _("Characters"),
            "tags": ["love interest", "Ethereal", "devotion", "priest", "childhood"],
            "stages": [
                {
                    "body": [
                        _("Ethereal-lineage. Priest. The composure of a woman taught to hold still in expensive rooms."),
                        _("Aeron knew her before the Academy. She is the only one at the gala who knocks softly instead of announcing."),
                    ],
                },
                {
                    "body": [
                        _("Speaks in small, patient lines. Lets silence do the work most voices would crowd."),
                        _("Lights her own cigarettes. Keeps her hands composed unless something truthful is happening — then they fold and unfold."),
                        _("She carries a Band she was bound to at twelve. It fits. Aeron's rejected him the same year."),
                    ],
                },
                {
                    "body": [
                        _("Aeries-raised, but trained in the cathedrals — the Old Tongue from age eleven, morning prayer before daylight."),
                        _("The devotion is not decoration. It was the first tool that worked on a child who grew up watching her people be measured and priced."),
                        _("She carries two words that Aerenine has no clean translation for. {i}Anayet{/i} — something like 'witness-of-the-hurt.' {i}Seren{/i} — 'to hold what will break you.'"),
                        _("She tells herself she is serving an order. The truth underneath: the order was her shape for loving one specific, dangerous man."),
                    ],
                },
                {
                    "body": [
                        _("She has stopped being devotional-at-a-distance. Devotion became something she does with her hands and her body, at the cost of the rules that taught her devotion."),
                        _("On the empathy path: she unbuckles the Band in front of him and says {i}Anayet{/i} aloud, the first time the word has left her mouth outside a temple."),
                        _("On the obedience path: she cinches the Band past comfort and prays through the horror of what he is becoming. She does not look away. She chooses to stay present inside the thing that should have broken her."),
                        _("What she could not see before: that {i}Seren{/i} was never about enduring the worst alone. It was about being in the room when it happens to someone else and refusing to leave."),
                    ],
                },
            ],
        },

        "zira": {
            "title": _("Zira"),
            "category": _("Characters"),
            "tags": ["love interest", "ghostline", "runner", "Unders", "fixer"],
            "stages": [
                {
                    "body": [
                        _("A hooded figure at an access plate, rerouting drain energy to keep a shelter warm. Hands that know practice, not panic."),
                        _("Calls him {i}Glass{/i} before he gives her a name. Street currency says she knows every rumor about him already."),
                    ],
                },
                {
                    "body": [
                        _("Sarcasm as armor; speed as grammar. The jokes are sharper when she is scared."),
                        _("Taught him the Ghostline rhythm one beacon at a time. Handed him the chip and did not say what it cost her."),
                        _("Has a pressed flower folded inside an oilskin she keeps in the workshop. It is {i}from before{/i}. She does not explain {i}before{/i}."),
                    ],
                },
                {
                    "body": [
                        _("Ashmarket raised. The forgery hands and the knife grip are not two different skill sets — they are one survival, learned early."),
                        _("She learned three separate signatures by thirteen and has never volunteered whose. The cipher in her voice is older than her allegiance to any cause."),
                        _("The thing she will not say: at some point she decided cynics who help are more honest than idealists who don't, and she built a whole life on that thesis."),
                        _("The lie she tells herself: she stays because the Ghostline needs her. The truth: she stays because proximity is the only way she knows to prove she is not better than the people she helps."),
                    ],
                },
                {
                    "body": [
                        _("She became a door-keeper. Not a fighter, not a fixer — a woman who builds exits."),
                        _("On the empathy path: she forges him an exit plan with three aliases, a four-stop chain map, and a sealed letter. Only his name is on the door. She builds it knowing he will not use it, and she builds it anyway."),
                        _("On the obedience path: she does not build a door. She stays inside the thing with him. She will not be the one who proves herself cleaner than him by leaving."),
                        _("What she can see now that she could not at the catwalk: the exit is not the point. The offering of it is. The drawer she puts the plan in does not lock."),
                    ],
                },
            ],
        },

        "tessa": {
            "title": _("Tessa"),
            "category": _("Characters"),
            "tags": ["love interest", "medic", "Phoenix", "clinic", "the board"],
            "stages": [
                {
                    "body": [
                        _("A field medic in an underground clinic that everyone just calls {i}Tessa's{/i}. Amber lamp over a metal brace. Hands that do not stop moving."),
                        _("Reads the room in one sweep. Asks two questions — your name and whether you are trouble or useful — and waits for the answer before deciding."),
                    ],
                },
                {
                    "body": [
                        _("Speaks the way she triages. Short sentences. The phrase {i}plain as teeth{/i} is hers and she means it."),
                        _("Threadbare cloth, basin of boiled water, a lockbox she wears the key to. Nothing in the clinic is wasted because nothing in the clinic is extra."),
                        _("Keeps a board at the back of the clinic. Two columns: LIVING and DEAD. She updates it herself, with a single fine-tip marker she has never replaced."),
                    ],
                },
                {
                    "body": [
                        _("She ran a line clinic through the worst of the yard years before Phoenix gave her walls. The people on her cots are not abstractions — she has pulled most of them out of a machine herself."),
                        _("The rule of three: when she remembers an operator she lost, she says their name three times. Out loud. In the room. She will not explain where the rule came from and she has never once broken it."),
                        _("Her mentor was a field doctor named — she does not say. The last thing that doctor taught her was how to tell someone they were not going to make it without making the telling cruel."),
                        _("The lie: that detachment is what keeps her good at this. The truth: she has been quietly naming every patient since year one, and the naming is the whole of the practice."),
                    ],
                },
                {
                    "body": [
                        _("Her arc is the movement from {i}clinical{/i} to {i}held{/i}. She said the line {i}held, not fixed{/i} with a hand on a sternum in a quiet medbay and meant it as a whole philosophy."),
                        _("Liora Rylan is written on both columns of her board — LIVING and DEAD — because Tessa does not know where else to put her, and Tessa will not pretend to know."),
                        _("On the obedience path, her board is overwritten to read {i}OPERATIONAL{/i}. The rewrite is not by her hand. She will have to choose: resist in place or withdraw in silence, and the choice turns on whether a specific apology has been spoken to her."),
                        _("What she sees now: the count is not for the dead. The count is for the living, who need someone to have done the counting so that the dead were not only numbers on the way through."),
                    ],
                },
            ],
        },

        "noelle_korr": {
            "title": _("Noelle Korr"),
            "category": _("Characters"),
            "tags": ["love interest", "analyst", "Echelon defector", "strategist", "the name mechanic"],
            "stages": [
                {
                    "body": [
                        _("A voice over a Ghostline terminal. A silhouette deliberately obscured. Female form, slender, precise breath."),
                        _("Clinical to the millimeter. Says she does not do research — she does analysis — and means the distinction as a creed."),
                    ],
                },
                {
                    "body": [
                        _("Echelon-trained. Defected with her own files. The defection was an equation she solved — the solution was leaving."),
                        _("Practices a habit she calls the Name Mechanic: she names things — people, events, doctrines — because naming is the first step toward modeling, and modeling is the first step toward control."),
                        _("Keeps a stylus moving before she sits down. Treats every conversation as a test case whose outcome she has already partially derived."),
                    ],
                },
                {
                    "body": [
                        _("She was raised inside a doctrine that taught her feeling was a variable to be isolated and zeroed out. The training worked for eleven years. Then it didn't."),
                        _("Her arc has a name for itself — {i}Empirical Tenderness{/i}. The private thesis that care is a measurable variable and that measurement is not the enemy of care."),
                        _("Her first failed model was her mother's death, which she tried to reduce and could not. She has not told anyone this directly. She has told it to three different framework documents instead."),
                        _("The lie: she can stay a neutral observer. The truth: she was never neutral — the classification system was the place she hid the part of her that was implicated."),
                    ],
                },
                {
                    "body": [
                        _("Her classification system breaks against feeling, and the breaking is the scene she spent four acts building toward."),
                        _("On the empathy path: she signs a strategist framework above her own name, says out loud {i}I am not a neutral observer anymore{/i}, and then — later, quieter — {i}I said it as a variable before. I am saying it as a sentence now.{/i} The sentence is {i}I love you{/i}, and she is aware that calling it a sentence is a concession her earlier self would not have let her make."),
                        _("On the obedience path: she drafts the civilian-targeting doctrine. She signs it. She says, afterward, that her doctrine did not fail because the doctrine was wrong — it failed because she was an analyst when she should have been a weapon. She reclassifies herself."),
                        _("What she could not see before: that the person inside the model is always at least partly the modeler, and that pretending otherwise was the only real bias she ever had."),
                    ],
                },
            ],
        },

        "selene_valen": {
            "title": _("Selene Valen"),
            "category": _("Characters"),
            "tags": ["love interest", "Phoenix", "commander", "shared authority", "Kael"],
            "stages": [
                {
                    "body": [
                        _("Phoenix commander. Nineteen years in the rebellion. Bronze eyes in ember light and her mother's scorched, copper-stitched gloves on a map table."),
                        _("Asks Aeron why she shouldn't have him shot. Not theatrical — genuine. Waits for an answer that is honest enough to work with."),
                    ],
                },
                {
                    "body": [
                        _("Compact force. A spring wound tight enough to kill and the discipline not to spend the spring casually."),
                        _("Runs a command post out of an old transit control room. She does not waste words and she will not waste yours. She is reading you the whole time."),
                        _("Her brother Kael mentored Aeron once, in another life, under Marcus. That is a piece of information she gives slowly and on her own timing."),
                    ],
                },
                {
                    "body": [
                        _("She learned command from Marcus, the same way Aeron did. Her disagreement with Marcus is older and deeper than the rebellion she runs."),
                        _("Kael died on a riverbank in the third district, in an eleven-minute window that was actually a nine-minute window. Selene did not flag the window because Marcus had taught her that disagreement is not the same as wrong, and she was trying to let her subordinate run his own plan. The thesis she carries now is called {i}delegate the question{/i}, and Kael is the reason it has a name."),
                        _("She has a sister named Ilene, in a distant sector, unreachable. She has been teaching the rebellion as a way of keeping Ilene alive in her own head — a letter she keeps writing without sending."),
                        _("The lie: that command is a posture. The truth: she has been looking, for nineteen years, for someone she could hand a question to without the hand shaking."),
                    ],
                },
                {
                    "body": [
                        _("[r1]On the empathy path: she finishes the Kael story in a room neither of them commands and hands Aeron a question that has been in her mouth for a day. She writes a letter to Ilene for the first time in a year and leaves it open on the table for him to see if he wants to. He sees her, in that room, as a woman rather than a commander, and the seeing is mutual.[/r]"),
                        _("[r1]On the obedience path: she is gone. She fell in the Act Two finale to a man who now cannot name her without flinching. She lives only inside the memories of the people who were in the command post the night she asked him why she shouldn't have him shot — and in the shape of every decision Aeron now makes without her.[/r]"),
                        _("What she sees now that she could not at the map table: that shared authority is not a concession to weakness. It is the hardest thing a commander ever learns, and it is the only part of command that outlives the commander."),
                    ],
                },
            ],
        },

        "nyra": {
            "title": _("Nyra"),
            "category": _("Characters"),
            "tags": ["love interest", "OB-exclusive", "Echelon defector", "co-command", "the oath"],
            "stages": [
                {
                    "body": [
                        _("(Obedience path only.) Echelon political officer. Defected with seventeen soldiers who move in perfect unison and speak only when addressed."),
                        _("Iron-blue palette. Parade-ground posture. She reorganized Phoenix's patrol schedules in a single night without being asked."),
                    ],
                },
                {
                    "body": [
                        _("Speaks in temperature, not names. Her briefings are the diction of a surgeon describing an incision — no affect, no pride, just architecture."),
                        _("Does not argue. Validates the suspicion against her, then asks for time to prove it wrong. It works because it is internally honest."),
                        _("Carries the fractured crest of her former commanding officer — the one she killed — wrapped in cloth. One half for what the Order was. One half for what it became."),
                    ],
                },
                {
                    "body": [
                        _("Trained in the Veran rhetorical pattern — the open, the pause, the reframe — eight hundred years old, taught at the same Echelon academy Aeron came up through. She uses it on him knowing he will recognize it and asking him to take it seriously anyway."),
                        _("The oath she swore to him was not a gesture. It was a structure: my soldiers follow me, I follow you, that chain is unbroken from this moment. She eroticizes obedience because obedience was the first thing in her life that did not lie to her."),
                        _("She has a sister in a distant sector whose name she will not say in the war room. The existence of the sister is a thing she has decided is tactically irrelevant."),
                        _("Her thesis: {i}the pause is a myth a certain kind of woman needs to believe in to survive men like us.{/i} She is the solvent — the woman who reframes Aeron's unraveling as doctrine and, by naming it doctrine, makes it possible to continue."),
                    ],
                },
                {
                    "body": [
                        _("She attempts, once, a doctrinal seduction of Aeron in the strategic room at oh-oh-forty-seven. It is not a seduction in the body register. It is a seduction in the framing register — an offer of an interpretation of his mother's letter that would let him put the letter down without guilt."),
                        _("He takes the offer halfway and refuses to take it all the way. The halving is the scene. It is the first time OB-Aeron has articulated a cost to his own clarity, and Nyra — who came to win — is impressed by the not-winning."),
                        _("What she sees now that she could not at the oath: that the man she pledged herself to has a limit, and the limit is not a flaw in her doctrine. It is what the doctrine was for."),
                    ],
                },
            ],
        },

        # =============================================
        # CHARACTERS — FAMILY + ANTAGONISTS + PROTAGONIST
        # =============================================

        "marcus_rylan": {
            "title": _("General Marcus Rylan"),
            "category": _("Characters"),
            "tags": ["Echelon","general","father","Rylan","antagonist"],
            "stages": [
                {
                    "body": [
                        _("High Commander of Echelon's Military Division. Thirty years a general, one lifetime a father. Calm in the way weather is calm before it decides."),
                        _("His hand sealed the ceremonial wound at his son's branding. The seal was efficient. The cauterizer did not shake."),
                    ],
                },
                {
                    "body": [
                        _("He does not raise his voice. He compresses it. Forty years of command has taught him that a room pushes in on its own when the man at the window is reading."),
                        _("His doctrine fits in a single breath: faith grants belief; training grants tools. Aeron became a tool at twelve because Marcus had no other ceremony to offer a drowning child."),
                    ],
                },
                {
                    "body": [
                        _("The ritual that shaped him was his own teacher putting him across a table from a stranger and telling him the two of them would share a corridor for nine months or neither would ever command alone. He carried the grudge for a decade before admitting the grudge was grief in the wrong shape."),
                        _("The spire behind his command chair holds a cabinet. The cabinet holds one letter, from Aeron at nineteen after a cadet exam he thought was a regression. The letter says, {i}I will be better next cycle, sir.{/i} It is the only letter he ever received. He has read it three times in twenty years."),
                        _("He says {i}that was acceptable{/i} when he means {i}I expected better.{/i} He taught his son to hear the difference. His son heard it exactly, and learned the wrong lesson."),
                    ],
                },
                {
                    "body": [
                        _("On the Empathy ledger he is the shape Aeron refuses. He reads his son's shared command as a surface, four-seamed, and signs Rhea Vestin's dispatch without hesitation. The lamp on the table beside the empty chair stays on. It has stayed on for twenty years. The waiting is the love he is capable of."),
                        _("On the Obedience ledger he is Aeron's mirror. He reads the intercepts and recognizes every move. {i}He is building something I understand very well.{/i} The door is the door he built. The threshold has his son's boot-print on it now. Disappointment, not anger — anger would imply there had been another door."),
                        _("He speaks to the empty reading chair the way a man speaks to a window. {i}Come home the long way, son. I can wait.{/i} He is aware his son will not come home at all."),
                    ],
                },
            ],
        },

        "kael_rylan": {
            "title": _("Kael Rylan"),
            "category": _("Characters"),
            "tags": ["Rylan","brother","Band-failed","ghost","Selene"],
            "stages": [
                {
                    "body": [
                        _("Aeron's older brother. Dead before the story begins. A name in a younger brother's silences and a scar on a father who does not name scars."),
                        _("The only Rylan son the Band ever accepted, and only for three years."),
                    ],
                },
                {
                    "body": [
                        _("He was fifteen on a rooftop at dusk, rubbing his wrist like a bruise he did not want a name for. He said the Band felt like pressure from the inside. He said nothing works forever — not even faith."),
                        _("The promise he extracted from his ten-year-old brother was two-part: remember who I was, and don't let Father turn you into a weapon just because you can't be a believer. Aeron kept half of it."),
                    ],
                },
                {
                    "body": [
                        _("Branded at twelve. Rejected at fifteen. Kept in the Aeries by his father's strings — {i}mercy{/i} Kael called the cage. The whispers followed him: {i}protected failure, the General's broken son.{/i} At seventeen he stood on the same rail and let go."),
                        _("He had been Selene's command protégé at twenty-six — her lieutenant on Operation Stillwater, before the name Kael became a file she sealed shut with the efficiency of a woman who had already lost too much. She remembers him holding a standard-issue coffee cup with both hands, like a small bird he did not want to crush. Nothing she ever had to file."),
                        _("The lie: Kael was the one who couldn't carry the weight. The truth: two of the people who loved Aeron most were already grieving him in Kael's shape before Aeron arrived."),
                    ],
                },
                {
                    "body": [
                        _("He remains the reliable witness. The voice Aeron hears at 390 operations. The boy who said {i}person first, not a tool{/i} into a wind that has not stopped blowing."),
                        _("Aeron is trying to be him. Selene is trying to save everyone who reminds her of him. Neither of them is entirely wrong about what the other is doing, and neither of them says it aloud."),
                        _("He is the shape the Rylan house left empty. The house has not learned how to stop arranging itself around the emptiness."),
                    ],
                },
            ],
        },

        "liora_rylan": {
            "title": _("Liora Rylan"),
            "category": _("Characters"),
            "tags": ["Rylan","Ethereal","story-keeper","mother","pause"],
            "stages": [
                {
                    "body": [
                        _("Aeron's mother. Ethereal lineage. Gone from the Rylan house long before the story opens. A woman Aeron knows mostly as an absence his father does not explain."),
                        _("The Outlands contacts have a name for her. They call her the story-keeper."),
                    ],
                },
                {
                    "body": [
                        _("She married Marcus when Marcus was still a man who hesitated. She fell in love with the half-second before his pen touched a page — the place where the decision and the signature had not yet married. She called it the pause."),
                        _("She walked out when the pause stopped arriving. She took the pause with her. She gave it to her son before she left, and has been using it herself for nineteen years in the same breath."),
                    ],
                },
                {
                    "body": [
                        _("She keeps six thousand names. Every person Echelon erased, every family, every child — ledgers moved through the same courier network Phoenix learned to protect. Tessa counts the living; Liora counts the erased. Parallel methodologies of care across different geographies."),
                        _("Her letter, left in a dead drop and found years late, is exact text and was never sent: {i}Aeron has your discipline. I hope he also has whatever it was in you that used to hesitate before signing. I fell in love with the pause.{/i}"),
                        _("She did not keep her own son's name in her ledger. She thought he did not need keeping. She was wrong about that too."),
                    ],
                },
                {
                    "body": [
                        _("On the Empathy ledger she is the chosen cost. Captured through the same courier channels Aeron's compassion kept alive. Executed on the Aeries platform at 1400, public broadcast, Marcus present and watching the monitors instead of her face. She does not beg. The drop mechanism runs on a timer. The machine runs itself."),
                        _("On the Obedience ledger she is the refusal. She walks into a safe house, sits across the table, refuses to rise for her son. She tells him she left because she could not watch his father finish becoming what he was becoming. She tells him she cannot watch him finish either. She slaps him once — not from rage, from recognition — and walks out at her own pace, the same pace she walked through the Outlands for nineteen years. The door closes. No one adjusts her rhythm."),
                        _("Either way, she is the loss that rewrites the route. Either way, she saw him before he saw himself, and named what she saw."),
                    ],
                },
            ],
        },

        "rhea_vestin": {
            "title": _("Commander Rhea Vestin"),
            "category": _("Characters"),
            "tags": ["Echelon","surgical","antagonist","Fourteenth Exigency","window"],
            "stages": [
                {
                    "body": [
                        _("Echelon's scalpel. Fourteen years running what the internal documents call targeted command-node interventions, and what every other army on the continent calls the thing Rhea Vestin does to people you are counting on."),
                        _("Marcus held her in reserve until his hypothesis about his son resolved. When the hypothesis resolved, he signed without hesitation."),
                    ],
                },
                {
                    "body": [
                        _("Thirty-one. Fourteenth Exigency. Seven confirmed engagements, none of them longer than ninety minutes. A longer engagement is, in her doctrine, a planning failure. She holds her planners to ninety."),
                        _("She does not require a briefing. She requires the window. She does not salute inside the spire because inside the spire the protocol is the specific absence of formality the Aeries reserves for its senior command. Her uniform is pressed by her own hand. She does not trust a subordinate to press it."),
                    ],
                },
                {
                    "body": [
                        _("She studies how Phoenix thinks more than where Phoenix moves. She works on twelve-to-thirty-six-hour pattern-match windows. She does not gloat about the dead — the dead are a list executed, an instrument awaiting reassignment."),
                        _("She does not flinch at civilian inclusion. The not-flinching is not exceptional — it is the baseline. She has not built a part of herself that flinches. Everything else is the exception."),
                        _("The lie: she is cold. The truth: she is early-warning weather. Competence that stopped being philosophical and became atmospheric."),
                    ],
                },
                {
                    "body": [
                        _("On the Empathy ledger she cuts one: Davel Ostra, senior runner, off the board at 0557. Marcus's intercept reaches the ops table inside the hour by design — {i}the subject is going to know inside the hour that the cut was shaped around her own work. I want her to know. That is part of the shape.{/i} Noelle's framework becomes the target template."),
                        _("On the Obedience ledger she cuts seven at the Sector 9-North forward base in a single strike. Siri Ondel, nineteen, the medic trainee Tessa had been mentoring. Jara Neese, who ran the Sector 12 sweep roster Aeron authorized a week prior. Five more names populate the OPERATIONAL-WITHDRAWN column while Aeron stands at the head of the ops table and does not move. The non-movement is the fracture."),
                        _("She is the answer to a question Phoenix did not know had been asked. The question was whether Marcus had been taking his time. The answer is that Marcus had been."),
                    ],
                },
            ],
        },

        "aeron_dossier": {
            "title": _("Dossier: Glass"),
            "category": _("Characters"),
            "tags": ["protagonist","Verdant","Band-rejected","Glass","Rylan"],
            "stages": [
                {
                    "body": [
                        _("Aeron Rylan, twenty-seven. Rylan son. Echelon's butcher. The precision instrument the Aeries points at the Unders when the Aeries wants a clean report."),
                        _("Called {i}Glass{/i} by the men who signed his file, and by himself when he is counting. Transparent, unbreakable, useful. A weapon his father built because his father had nothing else to offer a child the ritual refused."),
                    ],
                },
                {
                    "body": [
                        _("Under the mask there is a body that still flinches at applause. The rooftop in Act 1 is the first real crack: he stands where his brother stood, counts the same rail, and discovers that {i}tired{/i} is a sharper word than {i}angry{/i}."),
                        _("He does not speak in full sentences when he is alone. He speaks in the shape of the orders he was given at twelve: {i}smile when they applaud, be useful, or be nothing.{/i} The orders were survival instructions. Fifteen years later they are still the only language the interior runs on."),
                    ],
                },
                {
                    "body": [
                        _("Act 2 sets the seams. He is a Rylan, and he is Verdant, and he is in a room across a table from Selene, and none of those three things can be subordinated to the others without breaking him differently."),
                        _("The wound is legible now. He wants to be his brother. He wants to be forgiven by his mother. He wants his father's acceptable to have meant acceptable. He is a man keeping three ledgers and refusing to net them out."),
                        _("The pause he inherited from his mother is the hinge. His father trained it out of every command he ran for Echelon. Selene is teaching him how to put it back in."),
                    ],
                },
                {
                    "body": [
                        _("On the Empathy ledger he keeps choosing humanity after learning exactly how expensive it costs. The framework is a vulnerability. The courier network killed his mother. The mercy call costs names he will not let himself stop saying. He delegates instead of centralizing — which is, in his father's grammar, the one decision a broken commander cannot make. The decision is the answer. He is not broken. He is building a surface."),
                        _("On the Obedience ledger he is the man his father trained and his mother could not save. He signs the sweep. He does not flinch when Rhea reports. He corrects Nyra when Nyra names Marcus, because the correction is the only honesty left in the voice. The door is the door Marcus built; the threshold has his boot-print on it now. His mother looked at him across a safe-house table and saw Marcus, and the recognition was worse than the execution would have been."),
                        _("Both versions are the same dossier with one sentence moved. The sentence is: {i}the pause held{/i}, or {i}the pause did not.{/i} The analyst does not recommend. The analyst documents."),
                    ],
                },
            ],
        },

        # =============================================
        # CONCEPTS, EVENTS, PLACES, MOTIFS
        # =============================================

        "echelon": {
            "title": _("The Echelon"),
            "category": _("Lore"),
            "tags": ["regime","human-led","supreme court","high commanders"],
            "stages": [
                {
                    "body": [
                        _("The ruling order of Solveil. Supreme Court at the apex, High Commanders beneath, Aether Bands on every wrist."),
                        _("Presents itself as pageantry and paperwork — uniforms, inspections, recited maxims."),
                        _("No hidden architect. Every order traces back to a name in a chair."),
                    ],
                },
                {
                    "body": [
                        _("After the sweeps, the pageantry reads as choreography."),
                        _("An apparatus designed to make planned erasure legible as procedure."),
                        _("Compliance is not enforced in the streets. It is tuned at the wrist."),
                    ],
                },
                {
                    "body": [
                        _("The horror is that there is no monster at the center — only a succession of specialists."),
                        _("Marcus taught the doctrine. Rhea refines it. Each one cleaner than the last."),
                        _("Every hand that signs the order is human. That is the cost of looking closely."),
                    ],
                },
            ],
        },

        "phoenix_rebellion": {
            "title": _("The Phoenix"),
            "category": _("Factions"),
            "tags": ["rebellion","Unders","Selene","shared command"],
            "stages": [
                {
                    "body": [
                        _("A network of cells operating out of the Unders — runners, medics, defectors, the unbranded."),
                        _("Aeron arrives to a group that has no name for itself. Only habits, routes, trusted hands."),
                        _("Command is shared. No single throat for the Echelon to cut."),
                    ],
                },
                {
                    "body": [
                        _("Selene names it in the Doctrine scene: the Phoenix."),
                        _("The word lands like a flag planted — and a target designation drawn."),
                        _("Base of operations anchors near the old substation in the deep Unders. Sectors 8 through 12 move under its protection."),
                    ],
                },
                {
                    "body": [
                        _("A named thing can be hunted. The Echelon now has a silhouette to aim at."),
                        _("Ethics are written on the inside of the name: no civilians as shields, no mercy used as leverage, no lies among the cells."),
                        _("The rebellion pays for its name in people. Every survivor carries the weight of who the word has cost."),
                    ],
                },
            ],
        },

        "breaking_point": {
            "title": _("The Breaking Point"),
            "category": _("Events"),
            "tags": ["Aeron","balcony","fracture","precision"],
            "stages": [
                {
                    "body": [
                        _("A private night. A cold balcony. An order Aeron could not finish cleanly."),
                        _("The precision mask slips in public for the first time."),
                        _("Lyra sees it. The city sees it. The Echelon files it."),
                    ],
                },
                {
                    "body": [
                        _("What he refused to know: that the crack did not begin on the balcony."),
                        _("It began three years earlier, on a photo of Kael, on a chair he would not sit in."),
                        _("The balcony only gave it somewhere to show."),
                    ],
                },
                {
                    "body": [
                        _("Every later scene refers back to this one. The arc calls it the beginning."),
                        _("Marcus dates his son's failure from this night. Lyra dates her loyalty from the same."),
                        _("The Breaking Point is the moment the glass remembered it was glass."),
                    ],
                },
            ],
        },

        "doctrine_declaration": {
            "title": _("The Doctrine Declaration"),
            "category": _("Events"),
            "tags": ["council","Aeron","Phoenix","principles"],
            "stages": [
                {
                    "body": [
                        _("Act 2. A table under low light. Every cell leader in one room, for the first and last time."),
                        _("Aeron stands and says how he will fight. Not what they will do — how."),
                        _("A doctrine spoken slowly enough to be remembered."),
                    ],
                },
                {
                    "body": [
                        _("Lyra listens like prayer. Zira listens like a blade being measured."),
                        _("Selene names the thing they are. Tessa writes nothing down; she does not need to."),
                        _("Nobody agrees out loud. Nobody disagrees either."),
                    ],
                },
                {
                    "body": [
                        _("A doctrine only binds the one who keeps it. Every choice afterward either honors the words in that room or does not."),
                        _("The people at the table remember which. They will remember for him, when he forgets."),
                        _("The price of saying a thing out loud is that the room can hold you to it."),
                    ],
                },
            ],
        },

        "sector_10_sweep": {
            "title": _("Sector 10 — Operation 391"),
            "category": _("Events"),
            "tags": ["sweep","mercy","defection","civilians"],
            "stages": [
                {
                    "body": [
                        _("Briefing language: sector-wide clearance. Zero tolerance. Lethal force authorized. Acceptable collateral within mission parameters."),
                        _("Eight hundred civilians logged on the ground. Dawn deployment."),
                        _("Aeron's three hundred ninety-first operation. Also his last."),
                    ],
                },
                {
                    "body": [
                        _("On the ground, the briefing language did not hold."),
                        _("Corridors were left unfired. Shelter doors were not kicked. A breach charge was miscounted on purpose."),
                        _("The number the Echelon filed and the number that walked out were not the same number."),
                    ],
                },
                {
                    "body": [
                        _("The hinge of the arc. How many Aeron saved in Sector Ten is the number Zira reads before she speaks to him on the Obsidian Bridge."),
                        _("But the number he carries is not the number that lived."),
                        _("It is the number that did not."),
                    ],
                },
            ],
        },

        "tier_hall_branding": {
            "title": _("Tier Hall"),
            "category": _("Places"),
            "tags": ["branding","ritual","Aeries","rejection"],
            "stages": [
                {
                    "body": [
                        _("A white room above the Aeries. Surgical light. One chair. A family in the observation ring."),
                        _("At twelve, every Aeries child is brought here and bound to an Aether Band. The ritual is supposed to sing."),
                        _("A bare wrist leaving the hall is a sentence, not a failure."),
                    ],
                },
                {
                    "body": [
                        _("When the Band rejects, the light goes out. The hum stops. The room learns a new silence."),
                        _("Aeron's Band rejected. Reassigned to unbranded track. The word for it in the family was 'residue.'"),
                        _("Rejection is rare. Rare enough that the ritual prints its own refusal into the record."),
                    ],
                },
                {
                    "body": [
                        _("Kael was branded here at twelve. Three years later his Band turned on him at fifteen."),
                        _("Aeron was branded here at twelve. His Band would not take him at all."),
                        _("Two sons. Two refusals. The father still wears a general's collar. The Rylan line is a statistical impossibility in a room that was built to never produce one."),
                    ],
                },
            ],
        },

        "rule_of_three": {
            "title": _("Rule of Three"),
            "category": _("Motifs"),
            "tags": ["Tessa","counting","keeping","grief"],
            "stages": [
                {
                    "body": [
                        _("Tessa's counting ritual. When someone important is lost, the survivor says the name three times."),
                        _("Aloud or silent. It does not matter which. It matters that it is three."),
                        _("A small discipline for a field medic who ran out of pockets to put the dead in."),
                    ],
                },
                {
                    "body": [
                        _("The first time the player sees it applied to Aeron, Tessa says his name three times into a room he can barely stay inside of."),
                        _("'Aeron. Aeron. Aeron.' Not a summons. A keeping."),
                        _("The rule moves a name from the noise of the day into the quiet shelf where names are held."),
                    ],
                },
                {
                    "body": [
                        _("The theory is simple: counting is how the living keep the dead from becoming weather."),
                        _("The rule has a capacity. Tessa invented it knowing it did."),
                        _("Some names, when you try to say them three times, stop your mouth on the first. The rule does not break then. It only admits what it always knew."),
                    ],
                },
            ],
        },
    }

    # Register with the system (also gets picked up via global in bootstrap)
    if "codex_register_entries" in renpy.store.__dict__:
        renpy.store.codex_register_entries(CODEX_ENTRIES)