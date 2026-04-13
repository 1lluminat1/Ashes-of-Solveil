# =======================================================
# ACT 3 - Scene 04: Shared Ground (Empathy Path)
# File: a3_s04_shared_ground_emp.rpy
# Type: OPERATION
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s04_shared_ground_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s04_shared_ground_emp:

    $ show_timeline("16th of Cipher, 388 A.C.", "05:00", "Sector 4 — Supply Convoy")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, steady handheld. Opens wide on the command table — Selene and Aeron side by side.
    #         Briefing: clean two-shots, over-shoulder bias. Execution: tighter, faster cuts — 28mm.
    #         Aftermath: slow wide pullback. The team together. Breathing room.
    # LIGHTING: Briefing — amber command-post practicals, green tactical glow on faces.
    #           Field — pre-dawn grey-blue, fog diffusion. Headlamps off, ambient city-glow only.
    #           Aftermath — first true morning light bleeding amber through broken skylights.
    # SFX: Loop — base hum (briefing), wind and distant machinery (field), quiet aftermath.
    #       One-shots — datapad taps, bolt cutters, radio clicks, convoy engine rumble, crate impacts.
    # FX/COMP: Tactical displays cycling convoy routes. Fog rolling through Sector 4 corridors.
    #          Zira's charges flashing in sequence. Lyra's scope glint from the rooftop.
    # BLOCKING: Briefing — full cast around command table. Two chairs at the head.
    #           Field — split positions: Zira forward, Aeron and Selene mid, Lyra high, Noelle comms, Tessa rear.
    #           Aftermath — regrouping at extraction point. Standing in a loose circle.
    # FACE: Briefing — Selene sharp, Aeron focused, both completing each other's tactical thoughts.
    #        Field — controlled tension. No panic. Competence under pressure.
    #        Aftermath — relief that doesn't quite settle. Aeron's eyes already on the next problem.

    # ========= VOICE BASELINE =========
    # EMP cadence. Contractions. Sensory language. Warm but operationally crisp.
    # This scene is fast — military rhythm. Short exchanges. Trust visible in the gaps.

    # ========== BRIEFING — WAR ROOM ==========

    #scene bg_war_room_emp with dissolve
    #play ambient "sfx/ambient/base_activity_warm.ogg" fadein 2.0

    "The tactical display throws green light across six faces. Convoy route. Timetable. Three supply vehicles moving through Sector 4 at 0530."

    sel "Standard Echelon resupply. Armored cab, soft cargo bed, two outriders on rotary bikes."

    "She taps the display. The route pulses."

    sel "They'll cross the Halcourt overpass here — single-lane bottleneck, no lateral escape. That's our window."

    a "Fourteen seconds."

    "Selene glances at him."

    sel "Fourteen?"

    a "From the lead vehicle entering the bottleneck to the rear outrider clearing the approach ramp. Fourteen seconds of overlapping vulnerability."

    athought "I've been staring at this route since midnight. The number is certain."

    sel "Then we build the operation around fourteen seconds."

    athought "She doesn't question the math. Doesn't ask me to show my work."
    athought "That's new. That's trust."

    # --- ASSIGNMENTS ---

    sel "Zira. The approach ramp."

    z "Thermite on the support struts. Three charges, staggered detonation. The ramp drops behind the convoy — no retreat."

    a "How long to set?"

    z "Twenty minutes if nobody interrupts me. Fifteen if Noelle keeps the drone sweeps off my back."

    n "I can loop the northern patrol's sensor feed for eighteen minutes. After that, the checksum resets and they'll know."

    sel "Eighteen is enough. Lyra?"

    l "Overwatch from the Gradin rooftop. Sightlines cover the full bottleneck and three hundred meters of approach."

    a "If the outriders break pattern and split east—"

    l "I'll track the eastern rider. The western one enters Zira's killzone anyway."

    athought "She's already thought it through. The answer was waiting before the question."

    sel "Tessa, you're on standby triage at the extraction point. If anyone takes fire—"

    t "I'll be there. Kit's already packed."

    sel "Nobody takes fire. That's the plan."

    t "Plans are what happen before the bleeding starts."

    "Selene almost smiles."

    sel "Fair."

    # --- THE SHARED RHYTHM ---

    a "Comms check at 0515. Radio silence from 0525 until the charges blow. After that, Noelle coordinates extraction callsigns."

    sel "Agreed. Callsigns?"

    a "Keep them simple. Zira is Torch. Lyra is Span. Noelle is Switch. Tessa is Mend."

    sel "And us?"

    a "You're Ward. I'm Glass."

    "A beat. The old Echelon callsign, the one that meant broken. He uses it without flinching."

    athought "I'm done running from the name. Might as well make it useful."

    z "Cute. Can we go blow something up now?"

    sel "0430 departure. Get some sleep."

    z "Sleep is for people who aren't wiring thermite charges in the dark."

    "She's already halfway out the door."

    #stop ambient fadeout 1.5

    # ========== FIELD — SECTOR 4, PRE-DAWN ==========

    #scene bg_sector4_fog with dissolve
    #play ambient "sfx/ambient/city_predawn_fog.ogg" fadein 2.0

    "Fog sits heavy in the Sector 4 corridors. The kind that swallows sound whole."

    "They move in pairs through the grey. Selene and Aeron at center. No lights. No words. Hand signals and the quiet certainty of people who've rehearsed the silence."

    athought "The fog tastes like condensation and old metal. My boots find the grating by memory — three years of Echelon patrols along this exact route."

    athought "Back then I was the convoy. Now I'm the thing the convoy should fear."

    # --- ZIRA SETS CHARGES ---

    "Zira reaches the approach ramp seventeen minutes ahead of the convoy. Her hands move in the dark with the precision of someone who talks to machines better than people."

    #play sound "sfx/one_shot/bolt_cutter_soft.ogg"

    "Bolt cutters. Access panel. Three shaped charges placed along the support struts — close enough to chain-react, spaced enough to ensure total structural failure."

    z "(over comms, barely a whisper) Torch set. Three hot. Waiting on your go."

    # --- NOELLE ON COMMS ---

    n "(over comms) Northern patrol feed is looped. Sixteen minutes remaining on the window."

    sel "(over comms) Copy. All positions, confirm ready."

    l "(over comms) Span is set. Eyes on the approach."

    t "(over comms) Mend is ready. Please don't need me."

    a "(over comms) Glass is in position."

    "Selene's voice, steady as the fog."

    sel "(over comms) Ward confirms. All positions hold. Weapons tight until the lead vehicle hits the bottleneck."

    # --- THE CONVOY ---

    "They hear it before they see it. Low engine vibration through the grating. The particular growl of armored Echelon transports running heavy."

    athought "Three vehicles. Two outriders. Right on schedule."
    athought "Echelon keeps its timetables. That's doctrine. Predictability as efficiency."
    athought "Predictability as vulnerability."

    "The lead vehicle noses into the bottleneck. Headlamps cutting white cones through the fog."

    athought "Fourteen seconds. Starting now."

    # --- EXECUTION ---

    a "(over comms) Mark."

    "Everything happens at once."

    #play sound "sfx/one_shot/thermite_sequence.ogg"

    "Zira's charges fire in sequence — a stuttering crack-crack-CRACK that drops the approach ramp in a cascade of concrete and rebar. Dust blooms behind the convoy like a curtain drawn shut."

    "The rear outrider brakes hard, bike skidding on debris. The lead vehicle accelerates on instinct — straight into the roadblock Aeron positioned three hours ago."

    sel "(over comms) Torch, confirm ramp."

    z "(over comms) Ramp is down. They're boxed."

    "From the rooftop, Lyra's voice."

    l "(over comms) Eastern outrider is dismounting. He's going for the comm unit on his bike."

    a "(over comms) Noelle."

    n "(over comms) Already jamming. He'll get static."

    athought "Fourteen seconds from mark to containment. The convoy is sealed. No casualties. No shots fired."

    # --- THE CARGO ---

    "Selene moves first. Aeron flanks."

    "The convoy drivers surrender without resistance. Arms raised, faces blank with the particular confusion of soldiers who expected a routine run and got a wall instead."

    sel "Medical crates first. Zira, check the manifest against Noelle's intel."

    z "Antibiotics, surgical supplies, field rations — it's all here. Better than the intel suggested."

    "Aeron checks the third vehicle. Pauses."

    a "Selene."

    sel "What?"

    a "Empathy suppressants. Four crates. Military grade."

    "The war room goes quiet over comms."

    athought "They're shipping suppressants to the front. Dulling their own soldiers' capacity to feel."
    athought "I wore that dose for years. It made me efficient. It made me hollow."

    sel "Take them."

    a "Destroy them?"

    sel "Take them. Tessa can use the base compounds for legitimate medicine. The rest we document and broadcast."

    athought "She's thinking three moves ahead. Seize the supply. Repurpose what heals. Weaponize the proof."

    a "Copy."

    # --- EXTRACTION ---

    "The transfer takes six minutes. Clean. Efficient. Everyone in position, everyone in rhythm."

    n "(over comms) Window closing. Northern patrol feed resets in four minutes."

    sel "(over comms) All teams, extract. Mend, confirm no casualties."

    t "(over comms) Zero casualties. Ours or theirs."

    "Selene's exhale is audible over the comms. Relief wearing the mask of confirmation."

    sel "(over comms) Copy. All teams move to Rally Point Bravo. Good work."

    #stop ambient fadeout 1.5

    # ========== AFTERMATH — EXTRACTION POINT ==========

    #scene bg_rally_point_morning with dissolve
    #play ambient "sfx/ambient/morning_wind_warm.ogg" fadein 2.0

    "Morning light finds them at the rally point. Six people standing in a loose circle, breathing the particular air that comes after something works."

    "Tessa checks pulses anyway. Habit."

    t "Everyone's heart rate is elevated but stable. Except Zira, whose resting pulse appears to be caffeine."

    z "It's adrenaline. And talent."

    "Lyra sets down her rifle. Her hands are steady."

    l "Clean operation. No wasted motion."

    n "Twelve minutes and forty-one seconds from mark to full extraction. Seven percent faster than projected."

    z "You're welcome."

    n "I was crediting the fog cover, but sure."

    "Selene leans against a support column. The tension in her shoulders has shifted — not gone, recalibrated."

    sel "That was good. All of it."

    athought "She's right. It was good."
    athought "Not lucky. Not desperate. Good."

    # --- THE CONCERN ---

    "Aeron stands apart, studying the tactical feed on Noelle's datapad. The convoy route. The patrol schedules."

    a "Noelle."

    n "Already looking at it."

    a "The patrol pattern on the northern perimeter. It's different from last week."

    n "Compressed. Twelve percent tighter intervals. And the drone sweep altitude has dropped by forty meters."

    athought "They're adapting. The convoy was predictable because they didn't know we were watching."
    athought "After today, they'll know."

    a "Selene."

    "She reads his expression before he speaks."

    sel "They're adjusting."

    a "Patrol compression. Lower drone altitude. They'll tighten the Sector 4 corridor within forty-eight hours."

    sel "Meaning today's window won't exist tomorrow."

    a "Meaning we succeeded. And they noticed."

    "She nods. Slow. The weight of it settling."

    sel "Then we stay ahead. Noelle, I want a full pattern analysis by tonight. Every corridor, every patrol rotation."

    n "I'll have it by 1800."

    sel "Good."

    athought "Phoenix isn't hiding anymore. We're hunting."
    athought "The question is whether we can keep hunting faster than they can adapt."

    # --- CLOSING ---

    "The team disperses. Zira slings a crate of medical supplies over her shoulder like it weighs nothing. Lyra walks beside Tessa, their conversation low and easy."

    "Selene falls into step with Aeron. The rally point empties behind them."

    sel "(quietly) Fourteen seconds. You were right."

    menu:
        "You taught me how to see the window.":
            $ rel_bump("Selene", trust=1)
            sel "(small nod) I taught you the window. You chose to step through it."
        "We got it right together.":
            $ rel_bump("Selene", affection=1)
            sel "We did."
        "I'm good at counting.":
            sel "You're good at more than counting."

    athought "The fog is burning off. The city is waking up."
    athought "Somewhere in the Aeries, an Echelon logistics officer is about to have a very bad morning."

    "They walk back toward the base. Side by side. Two chairs at the head of the table, two people sharing the weight."

    #stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ canon_set("first_shared_op_success")
    $ flag("echelon_adapting_noted", True)
    $ flag("suppressants_seized", True)
    $ npc_remember("Zira", "flawless_demolition_work", tone="professional_pride")
    $ npc_remember("Lyra", "clean_overwatch_sector4", tone="quiet_confidence")
    $ npc_remember("Noelle", "comms_coordination_flawless", tone="satisfied_precision")
    $ npc_remember("Tessa", "zero_casualties_confirmed", tone="relief")
    $ npc_remember("Selene", "shared_command_field_tested", tone="trust_confirmed")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s04_shared_ground_emp
# cann.chapter: Act III, Phase I — Proving Ground
# cann.chapter_start: False
# cann.when_in_timeline:
#   - After Breath of Faith. First field operation under shared command.
#   - EMP path. Selene alive, shared command active, team functional.
# cann.what_happened:
#   - Supply interdiction on Echelon convoy in Sector 4. Fourteen-second window.
#   - Briefing: Aeron and Selene co-plan, completing each other's tactical thoughts.
#   - Zira runs advance demolition (approach ramp). Lyra provides overwatch. Noelle jams comms
#     and loops patrol feeds. Tessa on standby triage.
#   - Execution: flawless. Zero casualties on both sides. Convoy boxed and stripped.
#   - Discovery: empathy suppressants in the cargo — military-grade. Selene orders them seized
#     for repurposing (Tessa's medicine) and documentation (propaganda).
#   - Aftermath: success, but Aeron notices Echelon patrol patterns compressing — they're adapting.
#   - The operation demonstrates shared command working under live fire.
# cann.aeron_state:
#   - EMP operational confidence. Uses "Glass" callsign without flinching — reclaiming the name.
#   - Tactical brilliance on display (fourteen-second window calculation).
#   - Already reading the next problem before the current success settles.
# cann.path_tracking:
#   - No player choice — showcase scene demonstrating team competency.
#   - canon_set("first_shared_op_success") for future gating.
#   - flag("echelon_adapting_noted") seeds escalation in upcoming scenes.
#   - flag("suppressants_seized") for Tessa medical subplot and propaganda arc.
# cann.thematic_flags:
#   - "Phoenix isn't hiding anymore. We're hunting." — Act 3 EMP thesis shift.
#   - Empathy suppressants: the thing that hollowed Aeron now becomes medicine and evidence.
#   - "Glass" callsign reclaimed — the broken designation worn as chosen identity.
#   - Shared command under fire: Selene calls strategy, Aeron reads tactics, seamless handoff.
#   - Zero casualties on both sides — EMP path distinguishes itself from OB through restraint.
# cann.character_moments:
#   - Selene: Tactical patience. Three moves ahead (seize, repurpose, broadcast). Trusts Aeron's math.
#   - Aeron: Fourteen-second window. Former Echelon knowledge weaponized against Echelon.
#   - Zira: Professional demolition pride. "Sleep is for people who aren't wiring thermite."
#   - Lyra: Already answered the question before it was asked. Quiet competence.
#   - Noelle: Comms mastery. Credits the fog cover instead of accepting Zira's self-congratulation.
#   - Tessa: "Plans are what happen before the bleeding starts." Zero casualties as vindication.
# cann.block_status:
#   - OPERATION (EMP). Showcase scene. No branching.
# cann.requires_followup:
#   - Echelon adaptation (patrol compression) pays off in next planning scene (a3_s04a).
#   - Suppressants seized — Tessa repurposing arc, propaganda broadcast arc.
#   - "Glass" callsign as recurring identity marker through Act 3.
#   - Shared command field-tested — the accountability promise from a3_s01 now has operational proof.
