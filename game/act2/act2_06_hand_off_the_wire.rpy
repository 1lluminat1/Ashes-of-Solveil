# =======================================================
# ACT 2 - Scene 6: Hand Off the Wire
# File: act2_06_hand_off_the_wire.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act2_06_hand_off_the_wire"
$ scene_mark(_current_scene_id, "entered")

label act2_06_hand_off_the_wire:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 35–50mm; tighter than previous scenes. Handheld with subtle drift. Push-ins on Zira when she reveals something vulnerable. Two-shots when they're working together at the node.
    # LIGHTING: Night in the Unders. Blue-black shadows cut by amber Ghostline node lights and distant neon bleed. Zira's face half-lit when she's being honest.
    # SFX: Loop — deep Unders hum, distant dripping, occasional pipe groan. One-shots — node interface chimes, data transfer whispers, Zira's glove sparking softly.
    # FX/COMP: Ghostline node glow (amber pulse), faint data visualization hovering over the interface, steam from nearby vents.
    # BLOCKING/PROPS: Safehouse interior (brief), narrow maintenance corridor, hidden alcove with Ghostline relay node, interface panel, cables, Zira's glove/tools.
    # FACE: Zira oscillates between guarded humor and brief flashes of real vulnerability. Aeron attentive, uncertain how to read her openness.

    # ========== SAFEHOUSE - NIGHT ==========

    "Day three in the Unders."

    athought "The safehouse has started to feel less like a trap and more like a foxhole. Still cramped, still cold, but familiar now in a way it wasn't before."

    # VISUAL: Lyra asleep on her bedroll, exhausted. Aeron sitting against the wall, awake.
    athought "Lyra's breathing has finally evened out. She's been asleep for an hour, maybe two."

    athought "First real rest since the Purge."

    if empathy_band() == "obedience":
        athought "I should sleep too. Conserve energy. But my head won't stop running scenarios."
    elif empathy_band() == "empathy":
        athought "I keep thinking about the clinic. Tessa's hands, steady even when everything else is falling apart."
        athought "I used to have hands like that. I'm not sure what they're for now."
    else:
        athought "Sleep won't come. Too many faces behind my eyes when I close them."

    # SFX: Soft tap at the door. Three beats, pause, two beats. A pattern.
    "A tap at the door. Three, pause, two."

    athought "Zira's knock."
    athought "I'm up before I think about it, moving quiet so Lyra doesn't wake."

    # VISUAL: Door opens a crack. Zira in the corridor, hood up, eyes catching the dim light.
    "Zira's leaning against the opposite wall, arms crossed."

    athought "She looks like she's been there a while."

    z "(low) You awake enough to walk?"

    if empathy_band() == "obedience":
        a "I wasn't sleeping. What's the operation?"
        z "(slight smirk) Not everything's an operation, Glass."
        z "But yeah. Something like that."
    else:
        a "Wasn't really sleeping anyway. What's up?"
        z "Need to show you something. Just you."

    a "Lyra—"

    z "Let her rest. She needs it more than you do right now."
    z "Besides, this is... a you thing. Not a group thing."

    if pass_tier("OB2", "OB3"):
        athought "Separating me from Lyra. Could be a trap. Could be a test."
        athought "Could be trust. Hard to tell with her."
    elif pass_tier("EMP2", "EMP3"):
        athought "She's asking for something. I can hear it under the words."
        athought "The least I can do is listen."
    else:
        athought "Whatever this is, she's been thinking about it. Might as well find out."

    "I glance back at Lyra, then step into the corridor and pull the door shut behind me."

    a "Lead the way."

    # ========== THROUGH THE UNDERS - NIGHT ==========

    # VISUAL: Narrow corridors, darker than daytime routes. Zira moves differently at night—slower, more deliberate.
    athought "She takes me through routes I haven't seen before—narrower and darker, the kind of paths that don't exist on any map."

    athought "The Unders at night is a different animal. Quieter, but not safer. The silence has weight."

    z "(walking, not looking back) You handled the clinic okay."

    a "Tessa did most of the work."

    z "I meant the way you handled Tessa."
    z "She doesn't let people in easy. You got past the door on day one. That's rare."

    if empathy_band() == "obedience":
        a "I gave her what she needed to hear. Pragmatic approach to a pragmatic person."
        z "Mm. That what you think you did?"
    else:
        a "I just told her the truth. Or part of it."
        z "The hard part, though. That's what she listens for."

    # VISUAL: They pass through a section with exposed pipes, steam venting from cracks.
    "Steam hisses from a cracked pipe. Zira doesn't flinch, just angles her body to avoid it without breaking stride."

    z "You know why I pulled you out of that market? When they were about to tear you apart?"

    a "You said we might be worth more than fifty thousand credits."

    z "That's what I said. Not why I did it."

    athought "She doesn't elaborate. Just keeps walking."

    if empathy_band() == "obedience":
        athought "She's feeding me information in pieces. Controlling the flow. I've done the same thing in interrogations."
        athought "Difference is, she's not trying to break me. She's trying to decide something."
    else:
        athought "She's circling something. Whatever this is, she needs to get there her own way."

    # VISUAL: They stop at what looks like a dead end—corroded wall panel, no obvious door.
    "The wall ahead looks like every other wall—rust, grime, decades of neglect."

    z "Watch."

    # VISUAL: Zira touches specific points on the panel. A seam appears. Hidden door slides open.
    "Her fingers find spots in the corrosion—deliberate touches in a specific sequence."

    "A seam appears. A panel slides sideways, revealing a narrow alcove beyond."

    z "Welcome to the Ghostline."

    # ========== THE GHOSTLINE NODE ==========

    # VISUAL: Small alcove, maybe 3 meters square. Cables running up the walls. Central node with amber pulsing light. Interface panel. The heart of something hidden.
    athought "The space is barely big enough for two people, but it hums with quiet power."

    athought "Cables run up the walls like veins, converging on a central node that pulses with soft amber light."

    "Screens flicker with data streams. A small interface panel glows beneath the main relay."

    if empathy_band() == "obedience":
        athought "Communications hub. Surveillance blind spot. This is how she moves through the Unders unseen."
        athought "And she's showing it to me."
    elif empathy_band() == "empathy":
        athought "It's beautiful, in a strange way. A whole hidden network, built in the cracks of the city."
        athought "Her life's work, maybe. And she's letting me see it."
    else:
        athought "This is the Ghostline. The thing she's been hinting at since we met."
        athought "I'm looking at her secret, and I don't know what that means yet."

    z "Ghostline's my network. Thirty-seven nodes like this one, scattered through the Unders and the Lower Spans."
    z "Surveillance gaps, communication relays, data taps. Took me six years to build."

    a "Six years?"

    z "Started when I was nineteen. Didn't have anything better to do with my anger."

    # VISUAL: She runs her hand along the cables, almost affectionate.
    "Her hand traces one of the cables, following it up toward the central node."

    athought "The gesture is almost tender."

    z "Echelon thinks they see everything. They don't."
    z "Every time a patrol misses someone, every time a message gets through they didn't intercept, every time someone disappears before the sweep arrives..."
    z "That's Ghostline."

    if empathy_band() == "obedience":
        a "How many people know about this?"
        z "Three. Now four."
        a "That's a significant operational security risk, showing me."
        z "(flat) I know."
    else:
        a "Why are you showing me this?"
        z "Getting there."

    # VISUAL: Zira pulls up a simple interface. A map of the Unders with nodes marked as amber dots.
    "The interface flickers to life at her touch—a holographic map blooming in the air, the Unders rendered in wireframe with amber dots marking each node."

    z "The Purge hit us harder than anyone up top knows."
    z "I lost two nodes in Sector 10. One in Sector 8. Runners who maintained them, too."
    z "People I'd known for years. Gone in one night."

    athought "Her voice doesn't crack, but something behind it tightens."

    z "That's eleven dead runners. Four nodes dark. And Echelon doesn't even know they won."

    if empathy_band() == "obedience":
        athought "Losses. She's quantifying them like assets. But her voice says they were more than that."
    else:
        athought "Eleven people. She says it like a number, but it isn't. Not to her."

    a "I'm sorry."

    z "(sharp) Don't. Not yet. You haven't earned sorry."

    athought "The words sting. But she's not wrong."

    z "You want to know why I saved you in that market? Really?"
    z "Because I watched you during the Sweep."

    a "You were watching me during the Sweep?"

    z "Ghostline watches everything, Aeron. That's the point."
    z "I saw you pull people out. I saw you hesitate. I saw you break pattern."
    z "And then I saw you on that rooftop, watching the Purge, and I saw something shatter."

    # VISUAL: She turns to face him fully. First time she's looked at him directly since they entered.
    "The amber light catches her eyes as she turns, makes them look almost gold."

    z "That's why I showed up. Because I saw Glass crack, and I wanted to see what was underneath."

    if pass_tier("OB2", "OB3"):
        athought "She's been profiling me. Longer than I realized. I should be angry."
        athought "I'm not. I'm just... tired of being watched by enemies. Being watched by her feels different."
    elif pass_tier("EMP2", "EMP3"):
        athought "She saw me break. She saw everything."
        athought "And she showed up anyway."
    else:
        athought "She's been watching since the Sweep. Since before I knew I was going to run."
        athought "Maybe she knew before I did."

    # ========== THE OFFER ==========

    z "Here's the thing."
    z "I can't run this network alone anymore. Not with eleven runners dead and Echelon getting smarter."
    z "I need someone who can think tactically. Someone who knows how Echelon moves."
    z "Someone I can trust."

    a "And you trust me?"

    z "I trust that you're not Echelon anymore. That's a start."
    z "The rest? We'll see."

    # VISUAL: She pulls a small device from her pocket—same type as the relay she gave him in Act 1.
    "Something small emerges from her jacket—a Ghostline relay, like the one she gave me before."

    z "This one's different. Paired to the network. With this, you can access any node in range."
    z "You can see patrol patterns, blind spots, communication channels."
    z "You can see what I see."

    "The relay sits in her open palm, small and inert."

    z "I'm giving you the keys to six years of my life, Aeron."
    z "If you burn me, I lose everything. Not just the network. My people. My purpose."
    z "Everything."

    athought "The relay sits in her palm, small and inert."
    athought "But heavy with everything it represents."

    # --- PLAYER CHOICE: How does Aeron receive this trust? ---
    menu:
        athought "She's handing me something irreplaceable. How do I take it?"

        "Accept it with weight—acknowledge what this means.":
            $ choice_and_dev(
                _current_scene_id, "_accept_with_weight", "EMP", factor=1,
                note="Aeron acknowledges the emotional weight of Zira's trust, treats the relay as more than a tool."
            )
            $ npc_remember("Zira", "aeron_accepted_trust_with_weight", tone="cautious_hope")
            $ scene_mark(_current_scene_id, "accepted_with_weight")
            $ rel_bump("Zira", trust=2, affection=1)

            athought "I don't take it immediately. Let it sit in her palm for a moment."

            a "You barely know me."

            z "I know enough."

            a "You know what I was. Glass. Echelon's weapon."
            a "You're handing me the one thing that could destroy everything you've built."
            a "Why?"

            z "(quiet) Because someone has to go first."
            z "Trust doesn't happen if everyone's waiting for the other person to prove themselves."
            z "I'm going first. That's all."

            if pass_tier("OB1", "OB2", "OB3"):
                athought "She's making herself vulnerable on purpose. Tactically, it's insane."
                athought "But it's not tactics. It's something else. Something I used to understand, before they trained it out of me."
            else:
                athought "Someone has to go first."
                athought "When was the last time anyone went first for me?"

            "The relay is cool against his palm—lighter than expected."

            athought "Like it might break if I hold it wrong."

            a "I won't burn you."

            z "I know."

            a "How?"

            z "(small smile) Because you didn't say 'I promise.' You just said it."
            z "Promises are cheap. You just... said it. That's different."

            athought "Something in her posture eases as she turns back to the interface."

            z "Come here. Let me show you how it works."

        "Accept it professionally—focus on the tactical value.":
            $ choice_and_dev(
                _current_scene_id, "_accept_professionally", "OB", factor=1,
                note="Aeron treats the relay as a tactical asset, maintains professional distance from the emotional weight."
            )
            $ npc_remember("Zira", "aeron_accepted_trust_professionally", tone="guarded")
            $ scene_mark(_current_scene_id, "accepted_professionally")
            $ rel_bump("Zira", trust=1)

            "The relay is solid in his hand, edges worn smooth from use."

            a "Range?"

            z "(beat, something flickering across her face) ...Three hundred meters to the nearest node. From there, network-wide."

            a "Encryption?"

            z "Rolling cipher. Changes every four hours. The relay syncs automatically."

            a "And if Echelon captures it?"

            z "Dead switch. Two wrong inputs and it bricks itself, sends a warning to the network."

            if pass_tier("EMP1", "EMP2", "EMP3"):
                athought "I'm asking the wrong questions. She just handed me her life and I'm treating it like a field manual."
                athought "But this is safer. For both of us."
            else:
                athought "Good design. She knows what she's doing."
                athought "And now I know what I'm holding. That's the important part."

            "The relay is cold and heavy in his palm before it disappears into his pocket."

            athought "Secure and professional—nothing more."

            a "I'll keep it safe."

            z "(flat) That's it? 'I'll keep it safe'?"

            a "What do you want me to say?"

            z "(long pause) ...Nothing. Forget it."
            z "Come here. Let me show you how it works."

            athought "Whatever door was opening, I feel it close halfway as she turns back to the interface."

    # ========== LEARNING THE WIRE ==========

    # VISUAL: Zira at the interface, Aeron beside her. She's teaching him the system.
    "For the next hour, the Ghostline unfolds in front of him—patrol pattern overlays, surveillance blind spots, communication channels that exist in the gaps between official frequencies."

    z "This node covers Sectors 5 and 6. Range overlaps with nodes 7 and 12."
    z "If you need to move through here unseen, you route through the blind spot at junction 5-C."
    z "Patrol passes every eighteen minutes. You have a four-minute window."

    if empathy_band() == "obedience":
        athought "I'm memorizing it like a briefing. Patrol timing. Coverage gaps. Escape routes."
        athought "But underneath that, I keep thinking: she built this. All of it. Alone."
    else:
        athought "Every node is a person who agreed to risk their life for her network."
        athought "Eleven of them are dead now. And she's still going."

    z "Your relay will update automatically when you're in range. You don't have to do anything except not get caught."

    a "And if I see something you need to know?"

    z "Double-tap the side. Opens a direct channel to me."
    z "Don't use it unless it matters. The channel's secure, but nothing's perfect."

    # VISUAL: She pulls up a specific node on the map—one that's grayed out, inactive.
    "A grayed-out node pulses on the map—Sector 10, one of the ones lost in the Purge."

    z "This one was run by a woman named Sera. She'd been with me since the beginning."
    z "Two kids. Husband. All gone."

    "Her voice is steady. Her hand hovers over the dead node."

    z "I keep it on the map because... I don't know. Feels wrong to delete it."

    if scene_has(_current_scene_id, "accepted_with_weight"):
        a "It's not wrong. They mattered."
        z "(quiet) Yeah. They did."
        $ npc_remember("Zira", "aeron_acknowledged_sera", tone="grateful")
    else:
        a "Operational security says you should remove it. Creates false patterns."
        z "(long pause) ...Yeah. I know."
        athought "The node stays on the map."

    # ========== CLOSING — THE WIRE BETWEEN THEM ==========

    # VISUAL: They exit the node. Door seals behind them. Back in the dark corridor.
    "The node door seals behind them with a soft hiss. The amber glow disappears, leaving only the dark."

    athought "The darkness presses in, thick and close, before my eyes start to adjust."

    z "You're in the Ghostline now. That means something."

    a "What does it mean?"

    z "Means if you die, I'll notice."
    z "Means if I die, you can keep the network running."
    z "Means we're tied together now, whether we like it or not."

    if empathy_band() == "obedience":
        a "Interdependence as operational necessity."
        z "(snorts) You really know how to make a girl feel special."
        a "Would you prefer I lie?"
        z "No. Just... remind me why I thought this was a good idea."
    elif empathy_band() == "empathy":
        a "I've had worse things to be tied to."
        z "(surprised laugh) That might be the nicest thing you've said to me."
        a "Don't get used to it."
        z "Wouldn't dream of it."
    else:
        a "Tied together. That's one way to put it."
        z "You have a better way?"
        a "...No. That works."

    # VISUAL: They start walking back toward the safehouse. Side by side now, not leader and follower.
    "The dark corridors swallow them again—side by side this time, not leader and follower."

    z "Aeron."

    a "Yeah?"

    z "Thanks for not making this weird."

    if scene_has(_current_scene_id, "accepted_with_weight"):
        a "You handed me your life. The least I can do is hold it carefully."
        z "(quiet) ...Yeah. Okay."

        athought "She doesn't say anything else, but the space between us shrinks a little."
    else:
        a "It's a tactical arrangement. Nothing weird about that."
        z "Right. Tactical."

        athought "She doesn't say anything else. The silence is heavier than before."

    # VISUAL: Safehouse door. Same corridor as before. Different weight between them.
    "The safehouse door appears ahead, the same rust and dim light as before."

    athought "Something's different, though. The space between us has changed shape."

    z "Get some sleep. Tomorrow I want to show you the node in Sector 7."
    z "It's closer to Echelon patrol routes. Good practice for not getting us both killed."

    a "Looking forward to it."

    z "(pauses at the corner) Aeron."

    athought "Something she wants to say, maybe. Then thinks better of it."

    z "...Never mind. Sleep well, Kade Voss."

    "The corridor swallows her before he can respond."

    # VISUAL: Aeron at the safehouse door, relay in his pocket, processing.
    "The relay is a small weight in his pocket. The safehouse door waits."

    if empathy_band() == "obedience":
        athought "She gave me access to her entire network. Strategically, that's leverage."
        athought "But it doesn't feel like leverage. It feels like..."
        athought "Trust. The word sits wrong in my head. Like a tool I've forgotten how to use."
    elif empathy_band() == "empathy":
        athought "Someone has to go first."
        athought "She went first. Now it's my turn to figure out what that means."
        athought "What I do with it. What I owe her. What I want to be."
    else:
        athought "The Ghostline. Thirty-seven nodes. Six years of her life."
        athought "And now part of mine."
        athought "I'm not sure what that makes us. But it's something."

    "The door opens quietly. Lyra's still asleep, breathing steady."

    athought "Tomorrow, more lessons. More nodes. More of Zira's world becoming mine."

    "The dark presses in, the relay's weight solid against his chest."

    athought "The wire's in my hands now. All I have to do is not let go."

    # --- SCENE WRAP ---
    $ flag_on("Zira", "ghostline_access_granted")
    $ grant_tool("ghostline_relay")
    $ scene_mark(_current_scene_id, "completed")
    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act2_06_hand_off_the_wire
# cann.chapter: Act II, Chapter II — Constellation
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Night of Day 3 in the Unders, after the clinic visit (A2_05).
# cann.what_happened:
#   - Zira wakes Aeron late at night and takes him to a hidden Ghostline node.
#   - She reveals the Ghostline network: 37 nodes, 6 years to build, her life's work.
#   - She explains losing 11 runners and 4 nodes in the Purge—including Sera, a woman with her since the beginning.
#   - She offers Aeron a paired relay, giving him access to the entire network.
#   - Core choice: Aeron accepts the trust with emotional weight (EMP) or professionally/tactically (OB).
#   - Zira teaches him basic Ghostline operation: patrol patterns, blind spots, communication channels.
#   - Scene ends with them walking back side by side—a shift in their dynamic.
# cann.aeron_state:
#   - Processing what it means to be trusted with something precious.
#   - EMP branch: acknowledges the emotional weight, earns more trust/affection from Zira.
#   - OB branch: treats it professionally, still earns trust but misses the emotional connection.
#   - Internal monologue varies heavily by empathy band throughout.
# cann.path_tracking:
#   - One `choice_and_dev` decision:
#       • `_accept_with_weight` → EMP +1 weight, trust +2, affection +1 with Zira.
#       • `_accept_professionally` → OB +1 weight, trust +1 with Zira.
#   - Scene flags: `accepted_with_weight` vs `accepted_professionally` for future callbacks.
#   - NPC memories for Zira stored via `npc_remember()`.
#   - Running empathy range at scene end: -11 to +1.
# cann.thematic_flags:
#   - Motifs: Trust as vulnerability, networks as relationships, "someone has to go first."
#   - Zira's character: competent, guarded, grieving, but capable of reaching out.
#   - Ghostline as metaphor: invisible connections that keep people alive.
#   - Sera's dead node as emotional anchor—Zira keeps it on the map because deleting it feels wrong.
# cann.alignment_flavor_points:
#   - Opening: OB runs scenarios, EMP thinks about Tessa's hands, conflicted can't sleep
#   - Walking through Unders: OB notes she's controlling info flow, EMP senses she's circling something
#   - Seeing the node: OB tactical assessment, EMP sees beauty/life's work
#   - "I'm sorry": Zira rejects it—"you haven't earned sorry"
#   - Her watching during Sweep: different internal reactions by tier
#   - The offer: different internal processing by band
#   - Taking the relay: drastically different—weight vs professional
#   - Learning the system: OB memorizes briefing, EMP thinks about the people
#   - Sera's node: acknowledge vs operational security response
#   - Closing banter: three different tones
#   - Final internal: OB grapples with "trust" as unfamiliar tool, EMP focuses on what he owes
# cann.character_moments:
#   - Zira: Most vulnerable we've seen her. Grief for Sera. Deliberate choice to trust.
#   - The "someone has to go first" line is key to her philosophy.
#   - She notices and responds to how Aeron takes the relay—door opens wider or closes halfway.
# cann.inventory:
#   - Ghostline relay granted via `grant_tool("ghostline_relay")`.
# cann.block_status:
#   - A2_P01 pair anchor scene. Single alignment choice, significant Zira development.
# cann.requires_followup:
#   - Future Zira scenes can reference `accepted_with_weight` vs `accepted_professionally`.
#   - Ghostline relay becomes active tool in future scenes (patrol avoidance, communication).
#   - Sera can be referenced in Zira Deep Dive later.
#   - The "door closing halfway" in OB branch should echo in later Zira interactions.
