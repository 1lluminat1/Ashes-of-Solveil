# =======================================================
# ACT 2 - Scene 2: The Unders - Reality Check
# File: act2_02_reality_check.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_02_reality_check"
$ scene_mark(_current_scene_id, "entered")

label act2_02_reality_check:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 28–35mm interior; mostly static with slow 3–4% drift; occasional push-in on Zira "reality" lines.
    # LIGHTING: Single warm bulb vs cold window spill; high contrast; corners fall off into shadow.
    # SFX: Loop — distant machinery, city hum; one-shots — door beeps, lock clicks, supply bags hitting concrete.
    # FX/COMP: Light dust/smoke pass on window; no exterior vistas (keep safehouse claustrophobic).
    # BLOCKING/PROPS: Concrete box, barred window, door, supply pile, fake IDs, Bands.
    # FACE: Aeron/Lyra mostly in ¾ profile; Zira gets sharper CUs on "rules of the Unders" and "stop calling yourself Glass".

    # VISUAL: Zira's safe house. Evening. Dim light. Small, cramped, functional.
    "That evening."

    # VISUAL: Aeron and Lyra against the wall; small space, barred window, locked door.
    athought "We've spent hours in the dark. Just waiting, thinking, trying to survive."
    athought "The safe house is small and cold, but it's still shelter."
    athought "Shelter matters when the rest of the city wants you dead."

    # VISUAL: Aeron staring at nothing; Lyra checking her Band on reflex.
    if empathy_band() == "obedience":
        athought "I quietly catalog exits, angles, and timings, treating every feeling as noise to filter out."
    else:
        athought "I count my breaths until the room finally feels steady again."

    athought "Seven hours since we left Aeries. It already feels like seven years."
    athought "Everything we had is gone. Everything we were burned with those sectors."
    athought "Now we're here, waiting for someone else to decide if we get to live."

    # VISUAL: Lyra's fingers brush the Band, checking it again.
    "Lyra's hand drifts to her wrist, fingers brushing the Band."

    athought "She checks it again and again, even here. Afraid it'll fail the second she looks away."

    l "(quiet) Do you think she's coming back?"
    a "Zira? Yeah. She said she would."
    l "People say a lot of things."

    if pass_tier("OB2", "OB3"):
        a "She already saved us twice. Patterns hold until they don't."
    else:
        a "She already saved us. Twice. Why go that far just to disappear now?"

    l "(hollow laugh) Why go that far for anything? None of this makes sense anymore."

    athought "Silence returns and settles over us like extra weight on our ribs."

    a "We can't stay here forever."
    l "Where else would we go?"
    a "I don't know. But this is temporary. Zira made that pretty clear."
    l "Then what? We just wander the Unders and hope we don't die?"
    a "We survive. Then we plan. Then we—"
    l "(cuts him off) We what, Aeron? We're two people."
    l "Echelon has thousands. They have weapons, resources, control."
    l "What do we honestly think we're going to do to that?"

    # VISUAL: Aeron looks at her; same exhaustion, same doubt.
    a "...I don't know. But we said we'd burn them."
    l "We said a lot of things on that rooftop."
    l "That was rage and grief, not a strategy."
    a "Then we turn it into a strategy."
    l "With what? We don't have anything."

    # VISUAL: Aeron scans the bare room.
    athought "She's right—we don't have anything."
    athought "No weapons, no intel, no allies, no future. Just two burnt-out soldiers in a concrete box."

    # SFX: Door lock beeps and clicks.
    "The lock beeps, then clicks open."

    athought "Both of us freeze. No weapons—just our hands. And hands don't stop bullets."

    # VISUAL: Zira steps in with bags, kicks the door shut behind her.
    z "Still alive. Good. That's progress."
    if flag_has("Zira", "contacted_in_scene1"):
        z "(glances at Aeron) And this time you didn't ping me three times in a row. Growth."
    else:
        z "(side-eye at their clothes) You two still look like a cautionary poster."

    # VISUAL: She drops supplies on the floor.
    z "Here. Clothes, food, water, fake IDs. Enough to keep you breathing for a few days."
    z "After that, you're on your own."

    # State updates for supplies & disguises
    $ add_item_counter("food", 2)
    $ add_item_counter("water", 2)
    $ grant_disguise("unders")
    $ scene_mark(_current_scene_id, "zira_supplied_kits")

    l "Fake IDs?"
    z "You really think you can walk around as yourselves?"
    z "Echelon plastered your faces across every feed they control. There's a bounty on both of you."
    z "It's big enough to make half this city do something stupid."

    a "How big?"
    z "Fifty thousand credits. Each. Dead or alive."
    z "(grins) Personally, I'd take dead. Less paperwork."

    $ STATE["player"]["bounty"]["aeron"] = 50000
    $ STATE["player"]["bounty"]["lyra"] = 50000

    athought "Fifty thousand credits is a fortune down here."
    athought "Everyone we meet is now a potential killer with a price tag."

    l "Why haven't you turned us in?"
    z "Because fifty thousand credits disappears fast. But what you are?"
    z "That might be worth more."
    a "What exactly are we?"
    z "Depends who you ask. Hope, maybe."
    z "Or the start of a really entertaining disaster."
    z "Either way, I want to see how it plays out."

    # VISUAL: Zira drops down, cross-legged, at ease.
    z "Alright. Reality check. You two need to understand where you are."
    z "The Unders aren't Aeries. The rules are different, the culture's different, and survival works on a different axis."

    a "We know it's dangerous—"
    z "(cuts him off) No, you don't."
    z "You ran one operation down here. One night. Escorted the whole way."
    z "That's not knowing the Unders. That's taking a guided tour."

    if empathy_band() == "obedience":
        z "(to Aeron) And right now you still sound like you're writing a field report."
    else:
        z "(to Aeron) And for once you actually look like you feel it."

    # VISUAL: She leans in, making sure this lands.
    z "The Unders don't run on Echelon law. We have our own system—barter, favors, debts, reputation."
    z "Your Aeries credits barely matter unless you find the right fixer to convert them."
    z "Finding that fixer means talking to the wrong people and asking the right questions, and that paints a target on your backs."

    l "What do we do for money?"
    z "You earn it. You trade anything you can offer—skills, labor, information."
    z "Or you steal it, but theft down here ends in a pool of blood, not a court date."
    z "Nobody fines you. They just make sure you don't try it again."

    # VISUAL: Aeron and Lyra listen; the room feels smaller.
    a "What about allies?"
    z "Allies need trust. Trust takes time. Time requires survival."
    z "You've been here for seven hours and almost died twice."
    z "Locals hate you, Echelon's hunting you, and you have zero leverage."

    a "Then how do we survive at all?"
    z "You stop drawing attention. You keep your mouths shut. You don't trust anyone."
    z "You stay hidden until I say it's safer."
    z "And that day might never come, so get used to this room."

    # VISUAL: Lyra picks up the clothes — plain, worn.
    l "How long have you been doing this?"
    z "Doing what?"
    l "Surviving down here. Helping people. Playing both sides."
    z "(pause) Long enough to know when someone might be worth the risk."

    if empathy_band() == "obedience":
        z "(adds) Don't make me regret the math."
    else:
        z "(adds, softer) Try not to waste the chance I'm giving you."

    # VISUAL: Zira at the window, looking out into the unseen city.
    z "The Unders are fifty levels of people crushed together and then forgotten."
    z "Echelon looks down and sees waste—criminals, liabilities, bodies to burn."
    z "What they don't like to admit is that we're the foundation. The city stands on us."
    z "If we stop holding it up, everything above us comes crashing down."

    a "Is that what you want? For the whole city to fall?"
    z "(looks back at him) I want the people standing on our necks to fall."
    z "The city itself? The people? Most of them are just trying to survive."
    z "Same as you. Same as me. Same as everyone under their boots."

    # VISUAL: She moves back to the door.
    z "I have contacts. People who might help you, if I can convince them."
    z "But you need this clear—nobody's going to welcome you."
    z "You're Echelon. You're Glass. You killed their families."
    z "You don't talk your way out of that. You bleed your way out of it."

    l "What does that even look like?"
    z "It means you prove yourselves. You take hits you don't have to. You put something on the line for people who hate you."
    z "You want allies? Earn them. You want a safe place to sleep? Fight for it."
    z "The Unders don't hand out anything for free, least of all second chances."

    # VISUAL: Hand on door; she hesitates, then continues.
    z "There's one person left who matters. Rebel leader. Her cell got shredded in the Purge."
    z "Most of her people died in Sector 10."

    # VISUAL: Aeron and Lyra tense at the name.
    a "(carefully) Is she going to help us?"
    z "Help you? Her first instinct's going to be putting a bullet in your heads."
    z "But she's the only real resistance left. Everyone else either died or scattered."
    z "If you want to fight Echelon instead of just hiding from them, you need her."

    a "What's her name?"
    z "Selene. And before you ask—yes, she knows exactly who you are."
    z "I already told her. I wanted to see how she'd react."
    z "Right now she's thinking about it. That's the closest thing to a favor you're getting."

    $ flag_on("Selene", "mentioned_by_zira")
    $ canon_set("met_selene", False)

    l "When do we meet her?"
    z "Moving high-value targets across sector lines is suicide right now. We need the heat to die down."    
    z "Echelon's flooding the Lower Spans with patrols. They're tearing through everything down here."
    z "Marcus wants you badly enough that he's willing to set the Unders on fire to flush you out."

    athought "Father's hunting me in public—loud and aggressive, no quiet disappearance, no training accident, no cover story."
    athought "He wants me dead, and he wants everyone to watch."

    a "What is he telling people?"
    z "That you betrayed Echelon. That you worked with terrorists."
    z "That the Purge was necessary because of leaks and sabotage."
    z "He's putting a hundred thousand deaths on resistance activity and pinning the spark on you."
    z "(bitter) And people are swallowing it, same as they always do."

    l "He's rewriting the whole thing. We're the monsters now."
    z "Of course you are. That's how Echelon works."
    z "Truth is just raw material. Narrative is the weapon."

    # VISUAL: Door half-open; hallway beyond dark.
    z "Stay here. Don't leave. Don't answer the door for anyone."
    z "I'll be back tomorrow. Maybe with good news."
    z "More likely with bad news, so brace for that instead."

    a "Zira. Thank you. For all of this."
    z "(pauses) Don't thank me yet. You might not live long enough to make it mean anything."
    z "But... you're welcome. I guess."
    z "(almost leaves, stops) And Glass?"
    a "Yeah?"
    z "Stop calling yourself that. You're not just a tool anymore."
    z "Figure out what you are before the city gives you an answer you don't like."

    $ scene_mark(_current_scene_id, "called_out_identity")

    # VISUAL: Door shuts; lock engages; silence returns.
    "The door closes behind her. The lock clicks back into place."

    athought "We're alone again. Surrounded by concrete, supplies, warnings, and the kind of hope that feels dangerous to touch."

    # VISUAL: Aeron and Lyra with the gear pile between them.
    l "We're fucked."
    a "We already covered that."
    l "No, I mean really fucked. Did you hear everything she just said?"
    l "Echelon's hunting us. The locals hate us. We don't have money."
    l "And the one person who might be able to help us wants us dead."
    l "Explain to me how we walk out of that alive."

    # VISUAL: Aeron looks at the clothes, the food, the ID cards.
    a "One day at a time. Like Zira said."
    l "That's not a plan."
    a "It's the only one we have right now."

    if empathy_band() == "obedience":
        athought "I file it under triage: survive first, fix everything else later."
    else:
        athought "I try to believe that sometimes surviving one more day really is enough."

    # VISUAL: He picks up one of the ID cards.
    athought "Kade Voss. That's supposed to be me now."
    athought "Lower Spans worker, Sector 6, unremarkable and forgettable."
    athought "Not Glass, not Rylan, not Echelon. Just nobody. And maybe that's the only way forward."
    athought "Just another body trying not to disappear."

    $ STATE["player"]["fake_names"]["aeron"] = "Kade Voss"
    $ STATE["player"]["fake_names"]["lyra"] = "Mira Chen"
    $ scene_mark(_current_scene_id, "fake_ids_received")

    l "(picks up her ID) Mira Chen. Sector 7."
    l "(hollow laugh) Ironic. Sector 7."
    a "What?"
    l "Nothing. Just... ghosts everywhere."

    # VISUAL: Two IDs on the floor between them.
    athought "Kade Voss. Aeron Rylan died on that rooftop."
    athought "Glass shattered in the Purge."
    athought "Whatever's left, I haven't named it yet."

    l "I don't know how to do this."
    a "Do what?"
    l "Be nobody. I've been Echelon my whole life."
    l "Perfect soldier. Model citizen. Proof the system works."
    l "Now I'm... Mira Chen. Worker. Nobody. Nothing."
    l "I don't know how to be nothing."

    if empathy_band() == "obedience":
        a "Then we learn together."
        a "Neither of us knows how to do this, but we're here."
        a "As long as we're here, we're not nothing."
    else:
        a "Then we learn together."
        a "Neither of us knows how to do this, but we're here."
        a "As long as we're here, we're not nothing."

        athought "I let the silence sit between us. Something protective instead of punishment."

    l "(quiet) What are we, then?"
    a "...Survivors. For now, that's enough."

    "Lyra's weight settles against his shoulder—warm, solid, real."

    athought "Two people in a concrete box, hunted and hated by both sides—but not dead. Not yet."

    l "Do you think we'll make it?"
    a "I don't know."
    l "Honest answer. Thank you."
    a "We made it this far. That counts for something."
    l "Does it? Or are we just dragging out the inevitable?"

    athought "I don't have an answer. Only breath and heartbeat and the weight of the room."

    a "Get some rest. Tomorrow might be worse."
    l "Worse than today?"
    a "Always assume worse. Prepare for worse. Hope for better."
    l "(bitter laugh) You sound like a resistance fighter already."
    a "Do I?"
    l "No. You sound terrified. Like me."

    # VISUAL: They settle on the floor with makeshift bedding.
    "The thin bedding does nothing against the cold concrete, but exhaustion doesn't care."
    athought "Tomorrow, Zira comes back—maybe with Selene, maybe with hope. Tonight, all we have is survival, breathing, and the fact that we still exist."

    athought "From Aeries to the Unders, from Glass to Kade, from being everything to being no one. Zira's right—I need to figure out what I am now, before this city decides for me."

    athought "Two people against a city, impossible odds—but we're still here, still alive. Tomorrow brings either hope or death. Tonight is just darkness, and for now, that's enough."

    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_02_reality_check
# cann.when_in_timeline:
#   - Direct follow-up to Descent safehouse arrival (Act2_01); first full night in the Unders.
# cann.what_happened:
#   - Aeron & Lyra process the immediate fallout of defection in Zira's safehouse.
#   - Zira returns with supplies, clothes, and fake IDs: Kade Voss (Aeron), Mira Chen (Lyra).
#   - Bounty established at 50,000 credits each; everyone in the Unders becomes a potential threat.
#   - Zira explains Unders rules: barter/favors/debts/reputation; Aeries credits mostly useless.
#   - Zira names Selene as the surviving rebel leader from Sector 10 and confirms she knows who Aeron is.
#   - Marcus's public narrative: Aeron as traitor; Purge framed as response to "intel leaks."
#   - Zira tells Aeron to stop clinging to "Glass," pushing the identity crisis into the open.
#   - Aeron/Lyra accept "nobody" roles via fake IDs while privately grappling with being stripped of status.
# cann.aeron_state:
#   - Early Act II: OB-lean baseline but fully aware of loss and identity fracture.
#   - Scene only *reads* alignment (OB vs EMP) for flavor; it does not change the empathy score.
# cann.path_tracking:
#   - No `choice_and_dev` decisions in this scene; no direct empathy adjustments.
#   - Alignment only impacts line flavor via `empathy_band()` / `pass_tier()` branches.
#   - Running empathy range unchanged from Scene 1: -7 to -3.
# cann.thematic_flags:
#   - Motifs: False names, narrative control vs truth, Unders as foundation for Aeries, earned redemption.
#   - Echo lines: "You don't talk your way out of that. You bleed your way out of it." / "Figure out what you are."
# cann.block_status:
#   - ANCHOR scene; no branching choices, purely tonal variation by alignment.
# cann.visual_plate_economy:
#   - REUSE: Single safehouse plate with lighting variations; window angle for "foundation" VO.
#   - PROPS: IDs recur later as a close-up motif whenever identities are tested.
# cann.requires_followup:
#   - Next scene should pick up on "next day in safehouse" → waiting, early Unders adaptation, first steps toward Selene contact.
#   - Persist flags: zira_supplied_kits, fake_ids_received, called_out_identity, Selene mentioned_by_zira.
