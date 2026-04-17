# =======================================================
# ACT 3 - Scene 01: Back from the Edge (Empathy Path)
# File: a3_s01_back_from_edge_emp.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s01_back_from_edge_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s01_back_from_edge_emp:

    $ show_timeline("15th of Cipher, 388 A.C.", "06:00", "Phoenix Base — War Room")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Wide establishing on war room → medium group shots during briefing → close-ups during private Selene/Aeron conversation.
    # LIGHTING: Warm amber command-post lighting. Green-tinted tactical displays. Softening to intimate warmth for the private scene.
    # SFX LOOP: Base activity ambient — warm, purposeful hum. Distant footsteps, muffled comms chatter.
    # SFX ONE-SHOTS: Datapad taps, chair scrape, tactical display cycling, handshake.
    # BLOCKING: War room. Full cast around command table. Two chairs at the head — Selene and Aeron side by side. Cast disperses. Final scene: Selene and Aeron alone.
    # FX/COMP: Tactical displays cycling supply routes, patrol schedules, civilian corridors. Green pins on the maps.
    # FACE: Selene — composed but still pale, jaw tightening when stitches pull. Aeron — watchful, steady. Both softening in private moment.

    # ========== WAR ROOM — FULL BRIEFING ==========

    #scene bg_war_room_emp with dissolve
    # play ambient "sfx/ambient/base_activity_warm.ogg" fadein 2.0

    "The war room is full. Not crowded — full. The difference matters."

    "Tactical displays cycle through supply routes, patrol schedules, civilian evacuation corridors. The maps are marked with green pins now. Saves, not losses."

    "Selene stands at the head of the table, datapad in hand. Her left hand rests on the edge — taking weight she won't admit she needs to offload."

    "There's a second chair now. Pulled up beside hers."

    "Mine."

    athought "She offered to share command. I thought she was delirious from blood loss."
    athought "Turns out she meant it."

    sel "Sector Four supply cache. Zira, status?"
    z "Intact. I ran a drone sweep last night — no Echelon presence within two klicks. We can hit it tomorrow if we move fast."
    sel "Aeron?"

    athought "She's asking me. In front of everyone. Not for permission — for input."

    a "Tomorrow works, but I'd push it to early morning. Fog cover in that sector until 0900. Gives us a buffer if something goes wrong."

    "Selene nods. Not perfunctory — considering."

    sel "Agreed. Zira, adjust the timeline. 0600 departure, hard extract by 0830."
    z "Got it."

    athought "That's how it works now. She leads. I advise. Sometimes it's the other way around."
    athought "It shouldn't work. Two people making command decisions. Too many voices, too slow."
    athought "Except it does work. Because we're not fighting each other for control."

    t "Medical update. We're down to three days of antibiotics, maybe four if I ration. The supply run needs to prioritize the clinic on Forty-Second."
    sel "That's civilian territory. Risky."
    t "It's also the only place with surgical-grade supplies this side of the Aeries."

    athought "She's not wrong. But the route passes through two Echelon checkpoints."

    a "What if we split the team? Half on the cache, half on the clinic run. Smaller footprint, less attention."
    t "That thins our cover."
    l "I can provide overwatch on the clinic route. The rooftops there have good sightlines."

    "Lyra's voice is steady. She's not asking permission — she's offering a solution."

    athought "A month ago, she would've waited for someone to assign her. Now she's volunteering."
    athought "Something's changed. In all of us."

    sel "Noelle, probability assessment?"
    n "Split operation increases individual risk by twelve percent but reduces total exposure time by thirty-one percent. Net positive, assuming competent execution."
    n "Which, given present company, I'm willing to assume."

    "Was that a compliment? From Noelle?"

    z "Did she just say something nice? Someone check her for fever."
    n "I said 'assuming.' That's not a compliment. That's a conditional."
    z "Sure it is."

    "Tessa laughs. Actually laughs. The sound is so unexpected that everyone pauses."

    t "Sorry. It's just... we're arguing about supply runs. Not funerals. Not who we lost."
    t "It feels..."
    l "Normal?"
    t "I was going to say 'strange.' But normal works too."

    athought "Normal. When did that become strange?"
    athought "When did hope become something we had to relearn?"

    # ========== BRIEFING CLOSE — THE QUIET SHIFT ==========

    "The briefing continues. Assignments, timelines, contingencies. The machinery of survival."
    "At some point, Selene's hand brushes against Aeron's on the table. Brief. Unplanned."
    "Neither of them pulls away."

    athought "She's still pale. Still moving slower than she'd admit. The stitches in her side pull when she turns too fast — I can see it in the way her jaw tightens."
    athought "But she's here. Leading. Fighting."
    athought "We almost lost her. We almost lost everything."
    athought "Instead, we found... this. Whatever this is."

    sel "(quiet, just to him) You're staring."
    a "(quiet) Counting."
    sel "Counting what?"
    a "Days since you almost died. We're at seven."
    sel "That's morbid."
    a "That's gratitude. I'm bad at expressing it."

    "Something softens in her expression. Just for a moment."

    sel "You're getting better."

    # ========== WAR ROOM — AFTER THE BRIEFING ==========

    "The briefing ends. People disperse to their assignments. The war room empties slowly, naturally — not the abrupt scattering of people fleeing tension."
    "Zira lingers by the door, trading jabs with Noelle about probability models. Tessa and Lyra walk out together, heads bent in quiet conversation."
    "And then it's just the two of them. Selene and Aeron. The command table between them."

    sel "It's working."
    a "The supply plan?"
    sel "The... all of it. Shared command. I wasn't sure it would."
    a "You offered it."
    sel "I was also half-dead and full of painkillers. Not my most strategic moment."

    athought "She's joking. But there's something under it. Uncertainty. Vulnerability."
    athought "Selene Ward, uncertain. That's new."

    a "Having regrets?"
    sel "No. That's what surprises me."
    sel "I spent years building this. Alone. Convincing myself that's how it had to be."
    sel "Turns out I was wrong."

    athought "She's looking at me like she's seeing something she didn't expect."
    athought "I know the feeling."

    # ========== THE ACCOUNTABILITY PROMISE ==========

    sel "Aeron."
    a "Yeah?"
    sel "Don't let me become what I'm fighting."

    athought "The words land heavier than they should. Like she's been carrying them for days."

    a "What do you mean?"
    sel "I mean... it's easy. To justify things. To say 'this cruelty serves the cause' or 'these deaths buy us tomorrow.'"
    sel "I've watched it happen. Good people, convincing themselves that the mission matters more than the methods."
    sel "I don't want to wake up one day and realize I became the thing I swore to destroy."

    athought "She's not talking about hypotheticals. She's talking about herself. About me."
    athought "About what we could become if we stop paying attention."

    a "Then we watch each other."
    sel "What?"
    a "That's the point of this, right? Shared command. Two sets of eyes. Two people who can say 'stop' when the other one goes too far."
    a "You watch me. I watch you. And if either of us starts crossing lines..."
    sel "The other one pulls them back."

    athought "She's quiet for a moment. Processing. Then something shifts in her posture. Tension releasing."

    sel "Deal."
    a "Deal."

    "She extends her hand. Formal. Almost ceremonial."
    "He takes it. The handshake lasts longer than it needs to."

    athought "Don't let me become what I'm fighting."
    athought "I'm going to hold her to that. And she's going to hold me."
    athought "That's the promise. That's what makes this work."
    athought "Not control. Not hierarchy. Accountability."
    athought "Maybe that's what the rebellion needed all along."

    # ========== CLOSING ==========

    "Outside the war room, the base hums with activity. People moving with purpose, not fear."
    "It's not peace. It's not victory. But it's something."
    "It's back from the edge."

    # stop ambient fadeout 2.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ flag("shared_command_active", True)
    $ canon_set("shared_command", True)
    $ flag("accountability_promise", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s01_back_from_edge_emp
# cann.chapter: Act III, Chapter I — Consolidation (Empathy Path)
# cann.chapter_start: True
# cann.when_in_timeline:
#   - One week after Selene's near-death / medbay crisis (end of Act 2).
#   - Shared command is newly established. First full briefing under the new structure.
# cann.what_happened:
#   - War room briefing: Selene and Aeron co-lead for the first time publicly.
#   - Supply run planned for Sector Four cache (0600 departure, Zira on point).
#   - Split operation proposed: half on cache, half on clinic run for medical supplies.
#   - Lyra volunteers overwatch. Noelle provides risk assessment. Tessa raises medical urgency.
#   - Quiet moment: Selene and Aeron's hands brush at the table.
#   - Private conversation after briefing: Selene asks Aeron to hold her accountable.
#   - The Accountability Promise: mutual agreement to watch each other, prevent corruption.
#   - Handshake seals the deal — shared command formalized through trust, not hierarchy.
# cann.aeron_state:
#   - Steady. Watchful. Grateful Selene survived. Stepping into advisory role naturally.
#   - Counting days since her near-death — processing trauma through vigilance.
# cann.path_tracking:
#   - Empathy path scene. No branching choices — this is a consolidation/establishment beat.
#   - flag("shared_command_active") and canon_set("shared_command") for future gating.
#   - flag("accountability_promise") for callback in later moral-crisis scenes.
# cann.thematic_flags:
#   - Shared command as antidote to authoritarian structure.
#   - Accountability over hierarchy. "Two sets of eyes."
#   - Hope as something that must be relearned.
#   - "Don't let me become what I'm fighting" — central Act 3 tension.
# cann.character_moments:
#   - Selene: Leading while still recovering. Vulnerable in private — asks to be held accountable.
#   - Aeron: Advisory role feels natural. Counting days since her near-death.
#   - Lyra: Volunteering without being asked — growth from earlier passivity.
#   - Zira: Operational, reliable. Trading jabs with Noelle post-briefing.
#   - Noelle: Backhanded compliment ("assuming competent execution"). Softening.
#   - Tessa: Laughs for the first time. Notes the shift from funerals to supply runs.
# cann.block_status:
#   - Act 3 opener (empathy path). Establishes shared command and accountability framework.
# cann.requires_followup:
#   - Supply run execution scene (Sector Four cache + clinic split operation).
#   - The accountability promise will be tested when moral compromises arise.
#   - Selene's recovery arc — still pale, stitches pulling, not fully healed.
#   - Shared command dynamics under pressure (when Selene and Aeron disagree).
