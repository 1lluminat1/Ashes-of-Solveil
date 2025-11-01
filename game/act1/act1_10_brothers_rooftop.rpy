# act1_10_brothers_rooftop.rpy


# ======================================================
# ACT 1 - Scene 10: Flashback: Brothers on the Rooftop
# ======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "act1_10_brothers"
$ scene_mark(_current_scene_id, "entered")

define k  = Character("Kael")
define ya = Character("Young Aeron")


label act1_10_brothers:

    # VISUAL: Same rooftop as act1_09_breaking_point, but years earlier.
    # CAMERA: Slow shoulder-height dolly to the rail; keep faces 3/4 for first half.
    # LIGHTING: Late afternoon → dusk; warm rim from sun, cool lift from city bounce.
    # SOUND: Distant city hum; soft wind; no sirens; occasional turbine flutter.

    a "{i}Before the ritual. Before the rejection. Before everything broke.{/i}"
    a "{i}Before Glass.{/i}"
    a "{i}There was a time when this rooftop felt like freedom.{/i}"
    a "{i}I was ten. Kael was fifteen. His Band had been working for three years.{/i}"

    # Two silhouettes at the rail; Kael’s silver Band visible.
    k "You ever think about what's past the edge?"
    ya "(looks out) Past Solveil?"
    k "Past everything. The ruins. The dead cities. Whatever's left out there."
    ya "Father says there's nothing. Just ash and ghosts."
    k "(smirks) Father says a lot of things."

    # Kael’s Band catches the fading sun; he rubs it like a hidden bruise.
    "{i}His Band gleams. Three years old. Still working. Barely.{/i}"
    "{i}He touches it more than he used to. Like checking a wound.{/i}"

    ya "Does it still hurt?"
    k "(glances at his wrist) The Band? ...Sometimes. Lately."
    ya "Lately?"
    k "Started a few weeks ago. Like... pressure. From the inside."
    ya "(worried) Did you tell Father?"
    k "(bitter laugh) Tell Father his perfect son is glitching? No thanks."

    # Young Aeron looks at his bare wrist.
    ya "{i}Two years. Two years until my turn.{/i}"
    ya "What if mine doesn't work?"
    k "It will. You're a Rylan."
    ya "So are you."
    k "(pause) ...Yeah. I am."

    # Kael drifts closer to the edge; wind tugs sleeves.
    ya "(alarmed) Kael—"
    k "(laughs) Relax. I'm not gonna jump."
    k "Just seeing how close I can get before instinct kicks in."
    k "You know what's weird? Up here, I feel like I could actually fly."
    k "Like if I just... let go, the city would catch me."
    ya "(uneasy) That's not how physics works."
    k "(grins back) Physics. Listen to you, little professor."

    "{i}He steps back. Relief loosens my chest.{/i}"

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

    "{i}The city wakes below—a thousand lights igniting like distant stars.{/i}"

    k "Promise me something."
    ya "What?"
    k "If I ever lose myself—if the Band fails, or if I become something I'm not—you'll remember who I was."
    ya "(confused) Why would the Band fail? It's been working for three years."
    k "Nothing works forever. Not even faith."
    k "(grips his shoulder) Just promise, Aeron."
    "{i}His grip is tight. Too tight. Then it eases.{/i}"
    ya "(hesitant) ...I promise."
    k "(softer) And if Father ever tries to make you into something you're not..."
    k "...don't let him. Fight it. Stay you."
    ya "I don't understand."
    k "You will. Someday. Just... remember this conversation."

    # Brother warmth; a ruffle of hair; dusk deepens.
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

    # They exit; hold on empty rail.
    "{i}The wind stirs. The city hums. The edge remains.{/i}"

    # Match cut: present-day angle; colder palette.
    a "{i}Six months later, his Band rejected him completely. Age fifteen.{/i}"
    a "{i}Father pulled strings. Kept him in the Aeries. Called it mercy.{/i}"
    a "{i}Kael called it a cage.{/i}"
    a "{i}The whispers followed him everywhere. 'Protected failure.' 'General's broken son.'{/i}"
    a "{i}Two years after that, he stood here alone. Age seventeen.{/i}"
    a "{i}And he jumped.{/i}"

    a "{i}I kept my promise. I remembered who you were.{/i}"
    a "{i}But I didn't understand what you meant. Not then.{/i}"
    a "{i}'Don't let Father turn you into a weapon,' you said.{/i}"
    a "{i}Two years after your jump, my Band failed. Age twelve.{/i}"
    a "{i}And Father did exactly what you warned me about.{/i}"
    a "{i}He made me Glass. Transparent. Empty. Useful.{/i}"
    a "{i}A weapon without faith. A tool without purpose.{/i}"
    a "{i}390 operations. Ten years of becoming what you told me to fight.{/i}"
    a "{i}The cage. The whispers. Father's 'mercy.' The weight of being saved when you wanted to fall.{/i}"
    a "{i}You knew. You tried to warn me. I didn't hear it until too late.{/i}"
    a "{i}But now... now Glass is cracking.{/i}"
    a "{i}Maybe I can still fight it. Maybe it's not too late.{/i}"
    a "{i}Maybe breaking is how I finally keep my promise to you.{/i}"

    "{i}The memory fades. But the weight remains.{/i}"
    "{i}Present day. His apartment.{/i}"

    $ set_scene_flag(scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: act1_10_brothers
# cann.when_in_timeline: Flashback (Aeron 10, Kael 15) intercut before present rooftop/breaking-point thread.
# cann.what_happened:
#   - Kael confesses early Band “pressure” and identity drift; seeds failure at 15.
#   - Brothers make two promises: (1) Remember who I was; (2) Don’t let Father make you a weapon.
#   - Kael warns about Marcus rewriting history; Aeron agrees to be the memory.
#   - Epilogue stinger: Kael’s failure at 15; jump at 17; Marcus’s “mercy” as cage.
# cann.aeron_state: VO reflective; descriptive narration kept in third-person braces; no alignment gating in this flashback.
# cann.path_tracking:
#   - Scoring: NEU (no empathy/obedience adjustments; no menus).
#   - Incoming running range: (carry from prior operational scene) unchanged.
#   - Outgoing running range: unchanged (flashback does not alter math).
# cann.flags: completed (flashback audit only).
# cann.thematic_flags:
#   - Motifs: Edge/Flight, Performance/Lines, Glass origins, Mercy-as-Cage.
#   - Echo lines: “Don’t let Father turn you into a weapon.” “Nothing works forever. Not even faith.”
# cann.block_status: ANCHOR-LORE (no branch); supports emotional load for act1_11_breaking_point and later Marcus confrontations.
# cann.true_path_integration: none (non-menu memory; if you later tag VO acceptances for TP, this scene is a reference, not an increment).
# cann.visual_plate_economy:
#   - REUSE: Rooftop master plate from present; warm pass for flashback, cool pass for present stinger.
#   - HERO: Macro of Kael’s fingers on the Band (hairline rainbow glint); empty-rail hold after exit.
# cann.requires_followup:
#   - Later scenes should echo Kael’s “person first, not a tool” line; unlock a recognition beat if player resists an “easy shot” in Sector 10.
# cann.consistency_asserts:
#   - Aeries altitude: no precip; use wind/pressure/condensation language only.
#   - Ages/timing: Kael 12→Band, 15→failure, 17→jump; Aeron 12→failed Branding → “Glass.”
# cann.qa_hooks:
#   - Ensure label/scene_id/_current_scene_id are 1:1 (“act1_10_brothers”).
#   - Log flashback completion with `set_scene_flag(scene_id, "completed")` for recap screens.