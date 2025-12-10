# =======================================================
# ACT 2 - Scene 17: Building Something
# File: act2_17_building_something.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_17_building_something"
$ scene_mark(_current_scene_id, "entered")

label act2_17_building_something:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Mix of montage coverage and intimate moments. Wide shots for community scenes, tight two-shots for key interactions.
    # LIGHTING: Varies by base selected—Cathedral (warm gold), Relay (electric blue), Vault (silver), Clinic (green/amber). Growing warmer as community builds.
    # SFX: Loop — base ambient (varies by selection), people working, conversations in background. One-shots — tools, laughter, training sounds.
    # FX/COMP: Passage of time indicators—subtle lighting shifts, equipment appearing, more people in backgrounds.
    # BLOCKING/PROPS: The chosen base filling with life—crates, equipment, people. Named NPCs in the community.
    # FACE: Aeron gradually relaxing. Zira vulnerable in private moments. Community members becoming individuals.

    # ========== THE BASE — DAYS 8-14 (TIME PASSAGE) ==========

    "The days blur together in a rhythm of work and purpose."

    # --- DYNAMIC DESCRIPTION BASED ON BASE CHOICE ---
    if STATE["world"]["base_location"] == "cathedral":
        "The Cathedral comes alive."
        "Light filters through cracked stained glass, painting the floors in fragments of color. The old pews become workbenches, the altar a command table."
        "Lyra spends hours in the side chapels, not praying—just listening to the silence that used to hold something holy."
    elif STATE["world"]["base_location"] == "relay":
        "Relay Station Sigma-7 hums with new purpose."
        "Zira's cables spread through the infrastructure like roots, connecting them to every corner of the Unders. The cramped space fills with screens, terminals, the pulse of information."
        "It's ugly and uncomfortable and perfect."
    elif STATE["world"]["base_location"] == "vault":
        "Archive Vault Delta-9 wakes from its false death."
        "Noelle moves through the halls like a ghost revisiting her past, reactivating systems she once helped design. The climate control sighs back to life."
        "The walls that once held secrets now hold survivors."
    else:  # clinic
        "The Mercy Ward opens its doors."
        "Tessa works with quiet intensity, organizing supplies, cleaning equipment, turning abandoned space into something that can heal."
        "Patients start arriving within days—word travels fast in the Unders."

    # ========== THE PEOPLE ==========

    "The rebellion grows. Not in dramatic surges, but in the steady accumulation of people with nowhere else to go."

    # VISUAL: Montage of faces—workers, families, former Echelon deserters, people who lost everything in the Purge.

    # --- NAMED COMMUNITY MEMBERS (will make the strike personal) ---

    "There's Dren—a former machinist whose workshop was destroyed in Sector 9. He rebuilds anything mechanical with hands that never stop moving."

    "Sera's daughter, Kira—twelve years old, orphaned by the Purge. Zira found her hiding in a Ghostline node, talking to static because she thought her mother might still be transmitting."

    "Old Tomás—a retired infrastructure worker who knows the tunnels better than anyone alive. He draws maps from memory, correcting Noelle's databases."

    "And others. Dozens of others. Each one a story, a loss, a reason to fight."

    if empathy_band() == "obedience":
        athought "Assets. That's what I should see. Combat potential, logistical support, intelligence value."
        athought "But Kira is twelve. She brings Zira tea she can't afford to spare."
        athought "That's not an asset. That's something else."
    else:
        athought "Every face is someone who chose to be here. Who looked at what we're building and decided it was worth the risk."
        athought "I'm not sure I've ever been trusted like this. By strangers. By people who have every reason to hate what I was."

    # ========== TRAINING DAY ==========

    # VISUAL: Aeron running training exercises. Former workers learning combat basics.
    "Selene assigns him training duty. His tactical knowledge, finally useful for something other than destruction."

    "Twenty volunteers. Most have never held a weapon properly."

    "He teaches them what he knows. Not Echelon doctrine—something simpler. How to survive. How to run. When to fight and when fighting just gets you killed."

    a "(to the group) The goal isn't to win battles. The goal is to live through them."
    a "Every confrontation you can avoid is a victory. Every day you survive is a win against a system that wants you dead."

    "A young man—barely eighteen—raises his hand."

    recruit "But what if we have to fight? What if running isn't an option?"

    a "Then you fight smart. You fight together. And you remember what you're fighting for."
    a "Not revenge. Not glory. The people behind you. The ones who can't fight for themselves."

    if pass_tier("OB2", "OB3"):
        athought "These words don't feel like mine. They sound like something Tessa would say. Or Lyra."
        athought "But I mean them. That's the strange part."
    else:
        athought "I believe what I'm saying. When did that start happening?"

    # ========== QUIET MOMENT WITH ZIRA ==========

    # VISUAL: Late night. The base is mostly asleep. Aeron finds Zira at her terminal, but she's not working—she's watching something.
    "The base settles into night rhythms. Most people asleep. A few guards on rotation."

    "Aeron finds Zira at her terminal, but the screens are dark except for one."

    "A recording. Looped. A young man's face, speaking to camera."

    "He recognizes the eyes before he recognizes anything else. Zira's eyes, in a younger face."

    a "(quiet) Renn?"

    "She doesn't startle. Just nods."

    z "The only recording I have of him. Thirty-seven seconds."
    z "He was explaining how to reset a relay junction. Nothing important."
    z "But it's his voice."

    "The recording loops. Renn's voice, calm and patient, explaining something technical."

    z "Kira reminds me of him. The way she talks to machines like they can hear her."
    z "He used to do that. Said it helped him think."

    "She closes the recording. The screen goes dark."

    z "I told you about Sera's dead node. I didn't tell you why I kept it on the map."

    a "Why?"

    z "Because Kira is Sera's daughter."
    z "When I found her in that node, she was whispering to the static. 'Mom? Mom, are you there?'"
    z "I should have told her the truth. That the signal was dead. That no one was coming."
    z "But I couldn't."

    "Her voice cracks. Just for a moment."

    z "I told her sometimes signals take a long time to arrive. That we just have to keep listening."

    if empathy_band() == "obedience":
        athought "She lied. A kind lie, but still a lie."
        athought "I've told worse lies for worse reasons. At least hers was about hope."
    else:
        athought "She gave Kira something to hold onto. Even if it wasn't true."
        athought "Sometimes that's all we can do."

    a "You did the right thing."

    z "(surprised) The right thing was to lie to a twelve-year-old about her dead mother?"

    a "The right thing was to give her time to be ready for the truth."
    a "Some things you can't hear until you're strong enough to survive hearing them."

    "Zira looks at him. Really looks. Something shifting behind her eyes."

    z "When did you get wise?"

    a "I'm not wise. I'm just... learning."

    z "Learning what?"

    a "That efficiency isn't the only thing that matters."
    a "That sometimes the inefficient choice is the human one."

    "She laughs. Small, wet, surprised."

    z "God, you sound like a different person."

    a "Maybe I am."

    # --- ZIRA KISS GATE ---
    # Check: Ghostline access given (A2_06), accepted with weight, trust threshold met

    if scene_has("act2_06_hand_off_the_wire", "accepted_with_weight") and flag_has("Zira", "ghostline_access_granted"):

        # VISUAL: The moment shifts. Something changes in the space between them.
        "The silence changes shape. The space between them becomes something else."

        z "(very quiet) You know, when I pulled you out of that market..."
        z "I thought I was saving a useful asset. Someone who could help the rebellion."
        z "I didn't expect to actually... like you."

        a "Is that what this is? Liking?"

        z "I don't know what this is."
        z "I don't let myself want things, Aeron. Wanting gets you killed down here."
        z "But I keep..."

        "She stops. Looks away."

        z "Forget it. I'm tired. I'm saying stupid things."

        # --- PLAYER CHOICE: Kiss or hold back ---
        menu:
            "She's pulling away. What does Aeron do?"

            "Don't let her retreat—close the distance.":
                $ record_choice_once(
                    _current_scene_id, "_kiss_zira",
                    note="Aeron initiates first kiss with Zira."
                )
                $ scene_mark(_current_scene_id, "zira_first_kiss")
                $ flag_on("Zira", "first_kiss_complete")
                $ rel_bump("Zira", trust=1, affection=2)
                $ npc_remember("Zira", "first_kiss_at_terminal", tone="surprised_happy")

                "He reaches out. Catches her hand before she can turn away."

                a "Zira."

                z "Don't. I'm being—"

                a "You're being honest. That's rare."
                a "Don't take it back."

                "She looks at their hands. His fingers around her wrist. The pulse point where her heart betrays her."

                z "I don't know how to do this. The... wanting part."
                z "I'm good at running. At hiding. At keeping people at arm's length."
                z "This is new territory."

                a "Then we figure it out together."

                "She laughs. Half sob, half release."

                z "You said that to Lyra. I heard you through the wall."

                a "I meant it then too."

                z "So I'm not special."

                a "You're both special. Different, but special."
                a "I'm not good at this either. But I know I don't want you to pull away."

                "She doesn't respond with words."

                "She responds by closing the distance herself. Her lips finding his in the dark, tasting like recycled air and something electric."

                "The kiss is brief. Intense. A question and an answer in the same breath."

                z "(pulling back, breathless) ...Okay."

                a "Okay?"

                z "Okay, we figure it out together."
                z "But if you break my heart, I have access to every surveillance system in the Unders."
                z "I will make your life very uncomfortable."

                a "Noted."

                z "(small smile) Good."

            "Let her have space—this isn't the moment.":
                $ record_choice_once(
                    _current_scene_id, "_give_space",
                    note="Aeron lets Zira retreat, respects her pace."
                )
                $ scene_mark(_current_scene_id, "zira_kiss_delayed")
                $ rel_bump("Zira", trust=1)

                a "You don't have to forget it."
                a "But we don't have to figure it out tonight either."

                z "(surprised) You're not going to..."

                a "Push? No."
                a "You said it yourself—wanting gets you killed down here."
                a "I'm not going to be the reason you feel unsafe."

                "She stares at him. Something complex moving across her face."

                z "That's... not the response I expected."

                a "What did you expect?"

                z "I don't know. Something smoother. More certain."

                a "I'm not smooth. And I'm definitely not certain."
                a "But I know I'd rather wait than have you regret something."

                z "(very quiet) ...Thank you."

                a "Get some sleep, Zira. Tomorrow's going to be long."

                z "Yeah. You too."

                "She doesn't move immediately. Just watches him go."

                "The moment lives in the space between them. Unresolved. But safe."

    else:
        # If trust seeds weren't planted, more casual ending
        z "Anyway. Thanks for... listening. I guess."

        a "Anytime."

        z "Don't make promises you can't keep."

        a "I don't."

        "She turns back to her terminal. The moment passes."

        athought "There's something there. Something she's not saying."
        athought "Maybe someday. When we've both earned it."

    # ========== CLOSING — TWO WEEKS IN ==========

    "Two weeks. The base has become a home."

    "Not comfortable—the Unders is never comfortable—but alive. Full of people working toward something they can almost believe in."

    if STATE["world"]["base_location"] == "cathedral":
        "The Cathedral echoes with voices now. Prayers, maybe, of a different kind."
    elif STATE["world"]["base_location"] == "relay":
        "The relay station hums with purpose. Information as heartbeat."
    elif STATE["world"]["base_location"] == "vault":
        "The vault holds more than data now. It holds futures."
    else:
        "The clinic heals more than bodies. It heals the idea that someone still cares."

    "Tomorrow, Selene wants to discuss command structure. Aeron's role going forward."

    "But tonight, there's just this: a community, a purpose, and the fragile hope that they might actually survive."

    # --- SCENE WRAP ---
    $ scene_mark(_current_scene_id, "community_established")
    $ flag_on("world", "base_community_built")
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_17_building_something
# cann.chapter: Act II, Chapter III — Proving Ground
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Days 8-14. Montage period. Base establishment and community building.
# cann.what_happened:
#   - Time passage: Two weeks of building the chosen base.
#   - Named community members introduced:
#       • Dren (machinist), Kira (Sera's daughter, 12), Old Tomás (tunnel expert).
#   - Training montage: Aeron teaching survival combat to volunteers.
#   - Zira quiet moment: She shows Renn's recording, explains Kira's connection to Sera.
#   - Kiss gate: If trust seeds planted (A2_06 accepted_with_weight), Zira opens up.
#   - Player choice: Kiss Zira or give her space.
#   - Closing: Two weeks in, base feels like home, community established.
# cann.aeron_state:
#   - Gradually becoming part of something. Training people, being trusted.
#   - Internal tension: Still thinking in tactical terms, but meaning is seeping in.
# cann.path_tracking:
#   - Kiss gate requires: A2_06 "accepted_with_weight" AND Ghostline access granted.
#   - If kissed: `first_kiss_complete` flag, trust+1, affection+2 for Zira.
#   - If space given: trust+1 for Zira (respecting her pace).
#   - Running empathy range at scene end: -16 to +6 (unchanged).
# cann.thematic_flags:
#   - Community as something worth fighting for—named individuals with stories.
#   - Kira as Sera's daughter—connects Zira's grief to living hope.
#   - "Sometimes the inefficient choice is the human one."
#   - The base becoming home—not comfortable, but alive.
# cann.character_moments:
#   - Zira: Most vulnerable we've seen her. Renn's recording. Kira connection. Opening up about wanting.
#   - The kiss (if chosen): "If you break my heart, I have access to every surveillance system."
#   - Aeron's training speech: "The people behind you. The ones who can't fight for themselves."
# cann.community_npcs:
#   - Dren: Former machinist, rebuilds anything mechanical.
#   - Kira: 12, Sera's daughter, talks to machines, found in Ghostline node.
#   - Old Tomás: Retired infrastructure, knows tunnels, corrects Noelle's databases.
#   - These characters will be affected by the Echelon strike in Movement IV.
# cann.block_status:
#   - Community building complete. Named NPCs established for later stakes.
#   - First Zira kiss gate complete (if seeds were planted).
# cann.requires_followup:
#   - A2_18: Command Temperature with Selene (junior command).
#   - Kira, Dren, Tomás should appear again before the strike (make them matter).
#   - If kiss happened, Zira's warmth should be notably different.
#   - The community makes the counter-strike personal—these people will be hurt.
