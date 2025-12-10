# =======================================================
# ACT 1 - Scene 10: Flashback: Brothers on the Rooftop
# File: act1_10_brothers_rooftop.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_10_brothers"
$ scene_mark(_current_scene_id, "entered")

define k  = Character("Kael")
define ya = Character("Young Aeron")


label act1_10_brothers:

    # ========= STAGE DIRECTIONS =========
    # CAMERA: Slow shoulder-height dolly to the rail; keep faces 3/4 for first half.
    # LIGHTING: Late afternoon → dusk; warm rim from sun, cool lift from city bounce.
    # SFX LOOP: Distant city hum; soft wind; no sirens.
    # SFX ONE-SHOTS: Occasional turbine flutter.
    # BLOCKING: Same rooftop as act1_09_breaking_point, but years earlier. Two silhouettes at rail.
    # FX/COMP: Warm color grade for flashback; match cut to present (cool palette) at end.

    #scene bg_rooftop_brothers_flashback with fade

    # ========= OPENING — THE MEMORY =========

    athought "Before the ritual, before the rejection, before everything broke—there was a time when this rooftop felt like freedom."

    athought "I was ten. Kael was fifteen. His Band had been working for three years."

    # ========= BROTHERS AT THE RAIL =========
    # VISUAL: Two silhouettes at the rail; Kael's silver Band catches the fading sun.

    k "You ever think about what's past the edge?"

    ya "(looks out) Past Solveil?"

    k "Past everything. The ruins. The dead cities. Whatever's left out there."

    ya "Father says there's nothing. Just ash and ghosts."

    k "(smirks) Father says a lot of things."

    # VISUAL: Kael rubs his Band like a hidden bruise—an unconscious tell.

    "His Band gleams—three years old, still working. Barely. He touches it more than he used to, like checking a wound."

    ya "Does it still hurt?"

    k "(glances at his wrist) The Band? ...Sometimes. Lately."

    ya "Lately?"

    k "Started a few weeks ago. Like... pressure. From the inside."

    ya "(worried) Did you tell Father?"

    k "(bitter laugh) Tell Father his perfect son is glitching? No thanks."

    # VISUAL: Young Aeron looks at his bare wrist.

    ya "{i}Two years. Two years until my turn.{/i}"

    ya "What if mine doesn't work?"

    k "It will. You're a Rylan."

    ya "So are you."

    k "(pause) ...Yeah. I am."

    # ========= KAEL AT THE EDGE =========
    # VISUAL: Kael drifts closer to the edge; wind tugs at his sleeves.

    ya "(alarmed) Kael—"

    k "(laughs) Relax. I'm not gonna jump."

    k "Just seeing how close I can get before instinct kicks in."

    k "You know what's weird? Up here, I feel like I could actually fly."

    k "Like if I just... let go, the city would catch me."

    ya "(uneasy) That's not how physics works."

    k "(grins back) Physics. Listen to you, little professor."

    "He steps back."

    athought "Relief loosens my chest."

    k "(serious) You ever feel like you're not really... you?"

    ya "What do you mean?"

    k "Like you're playing a part. Reading lines someone else wrote."

    ya "All the time."

    k "(nods) Yeah. Me too."

    k "(quieter) The Band was supposed to make me whole. Give me purpose."

    k "But lately... I don't know. Feels like it's taking something instead."

    ya "Taking what?"

    k "Me. The parts that used to be mine."

    k "(eyes the wrist) Sometimes I wonder what happens when you forget the lines."

    ya "You improvise?"

    k "(hollow laugh) Or you fall off the stage."

    # ========= THE PROMISE =========
    # VISUAL: The city wakes below—a thousand lights igniting like distant stars.

    "The city wakes below—a thousand lights igniting like distant stars."

    k "Promise me something."

    ya "What?"

    k "If I ever lose myself—if the Band fails, or if I become something I'm not—you'll remember who I was."

    ya "(confused) Why would the Band fail? It's been working for three years."

    k "Nothing works forever. Not even faith."

    k "(grips his shoulder) Just promise, Aeron."

    "His grip is tight—too tight—then it eases."

    ya "(hesitant) ...I promise."

    k "(softer) And if Father ever tries to make you into something you're not..."

    k "...don't let him. Fight it. Stay you."

    ya "I don't understand."

    k "You will. Someday. Just... remember this conversation."

    # ========= WARMTH BEFORE THE END =========
    # VISUAL: Kael ruffles Aeron's hair; dusk deepens behind them.

    k "Good. 'Cause I'm gonna need someone to tell the truth when Father starts rewriting history."

    ya "(half-smile) You think he'd do that?"

    k "(dry) I think he already has."

    k "Two years, huh? Then you'll get your Band."

    ya "Yeah."

    k "You scared?"

    ya "(honest) Terrified."

    k "Good. Means you're paying attention."

    k "But listen... if it doesn't work. If the Band rejects you."

    k "Don't let Father turn you into a weapon just because you can't be a believer."

    ya "What?"

    k "Just... remember you're a person first. Not a tool."

    k "Come on. Dinner's in twenty. Father hates it when we're late."

    ya "(takes his hand, stands) Kael?"

    k "Yeah?"

    ya "Thanks. For... this."

    k "(grins) Anytime, little brother. Anytime."

    # ========= EXIT — HOLD ON EMPTY RAIL =========
    # VISUAL: They exit frame; hold on the empty rail against the darkening sky.

    "The wind stirs. The city hums. The edge remains."

    # ========= MATCH CUT — PRESENT DAY =========
    # VISUAL: Same angle, colder palette. Present-day rooftop.

    athought "Six months later, his Band rejected him completely. Age fifteen."

    athought "Father pulled strings—kept him in the Aeries. Called it mercy."

    athought "Kael called it a cage."

    athought "The whispers followed him everywhere. 'Protected failure.' 'General's broken son.'"

    athought "Two years after that, he stood here alone. Age seventeen. And he jumped."

    athought "I kept my promise. I remembered who you were."

    athought "But I didn't understand what you meant—not then."

    athought "'Don't let Father turn you into a weapon,' you said."

    athought "Two years after your jump, my Band failed. Age twelve."

    athought "And Father did exactly what you warned me about."

    athought "He made me transparent, empty, useful—a weapon without faith, a tool without purpose."

    athought "390 operations. Ten years of becoming what you told me to fight."

    athought "The cage, the whispers, Father's 'mercy'—the weight of being saved when you wanted to fall."

    athought "You knew. You tried to warn me. I didn't hear it until too late."

    athought "But now... now something is cracking."

    athought "Maybe I can still fight it. Maybe it's not too late."

    athought "Maybe breaking is how I finally keep my promise to you."

    # ========= RETURN TO PRESENT =========

    "The memory fades, but the weight remains."

    "Present day. His apartment."

    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_10_brothers
# cann.when_in_timeline: Flashback (Aeron 10, Kael 15) intercut before present rooftop/breaking-point thread.
# cann.what_happened:
#   - Kael confesses early Band "pressure" and identity drift; seeds failure at 15.
#   - Brothers make two promises: (1) Remember who I was; (2) Don't let Father make you a weapon.
#   - Kael warns about Marcus rewriting history; Aeron agrees to be the memory.
#   - Epilogue stinger: Kael's failure at 15; jump at 17; Marcus's "mercy" as cage.
# cann.aeron_state: VO reflective; descriptive narration kept sensory; no alignment gating in this flashback.
# cann.path_tracking:
#   - Scoring: NEU (no empathy/obedience adjustments; no menus).
#   - Running range: unchanged (flashback does not alter math).
# cann.thematic_flags:
#   - Motifs: Edge/Flight, Performance/Lines, origins of Aeron's transformation, Mercy-as-Cage.
#   - Echo lines: "Don't let Father turn you into a weapon." "Nothing works forever. Not even faith."
# cann.block_status: ANCHOR-LORE (no branch); supports emotional load for act1_11_breaking_point and Marcus confrontations.
# cann.visual_plate_economy:
#   - REUSE: Rooftop master plate; warm pass for flashback, cool pass for present stinger.
#   - HERO: Macro of Kael's fingers on the Band; empty-rail hold after exit.
# cann.requires_followup:
#   - Later scenes echo "person first, not a tool" line; recognition beat if player resists "easy shot" in Sector 10.