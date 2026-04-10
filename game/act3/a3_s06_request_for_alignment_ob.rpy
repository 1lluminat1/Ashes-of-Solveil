# =======================================================
# ACT 3 - Scene 06: Request for Alignment (Obedience Path)
# File: a3_s06_request_for_alignment_ob.rpy
# Path: OB
# Character Focus: Nyra, Aeron, Zira (primary opposition), Team reactions
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s06_request_for_alignment_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s06_request_for_alignment_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm lens (OB tension), deliberate movement. Wide establishing shot of war room,
    #         then tightening coverage as tension builds. Reaction shots: Zira hostile, Lyra guarded,
    #         Tessa concerned, Noelle clinical. Two-shots of Aeron and Nyra when she speaks.
    # LIGHTING: War room tactical blue. Cooler than EMP version. Overhead strips cast sharp shadows.
    #           Nyra lit from the side -- half her face in shadow. Deliberate ambiguity.
    # SFX: Loop -- base hum (tense undertone), ventilation, distant activity.
    #      One-shots -- chair scrapes, datapad taps, door hiss, boot steps (Nyra's are precise).
    # FX/COMP: Tactical displays cycling. Nyra's soldiers visible through window -- lined up, still.
    # BLOCKING: Team seated around war table. Nyra stands at parade rest before them.
    #           Aeron at the head -- Selene's old position. The chair doesn't fit him yet.
    # CANON: Follows "Echoes in the Rain." Nyra makes her formal pitch.
    #        This is where the schism begins -- team fractures over whether to accept her.
    # FACE: All faces visible. Reactions are the drama.

    # ========= VOICE BASELINE =========
    # OB Aeron: Contractions, but clinical focus. Assessing value, not feeling.
    # Nyra: Calm, precise, reverent. Military cadence. She's auditioning, but she doesn't grovel.
    # Zira: Hostile. She doesn't trust this.
    # Lyra: Guarded. Watching Aeron more than Nyra.
    # Tessa: Concerned for what this means, not for tactical value.
    # Noelle: Analytical. Running probabilities.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - WAR ROOM - DAY]
    # The same room as "Silent Table" -- but now there's someone new standing in it.
    # Nyra Vale, at parade rest. Behind the window: her seventeen soldiers, lined up like statues.

    #scene bg_war_room_ob with dissolve
    #play ambient "sfx/ambient/base_hum_tense.ogg" fadein 2.0

    # --- OPENING: THE ROOM ---

    "The war room feels smaller with her in it."

    "Nyra Vale stands at parade rest before the tactical table. Spine straight. Hands clasped behind her back. Her uniform is patched and faded, but she wears it like dress whites."

    #show nyra war_room_standing with dissolve

    athought "Twelve hours since we brought her in. Her soldiers haven't moved from the holding area."

    athought "They haven't complained. Haven't asked for food, water, updates. They just... wait."

    athought "Like machines. Like weapons someone left on a shelf."

    "Through the reinforced window, seventeen figures stand in perfect rows. Not at attention -- at rest. But even their rest looks like readiness."

    #show zira war_room_seated with dissolve
    #show lyra war_room_seated with dissolve
    #show tessa war_room_seated with dissolve
    #show noelle war_room_seated with dissolve

    "The team is assembled. Zira leans back in her chair, arms crossed, jaw tight. Lyra sits with her hands folded -- the posture she uses when she's praying or preparing for bad news. Tessa keeps glancing at the window. Noelle's stylus hasn't stopped moving since Nyra entered."

    athought "They're waiting for me to start. I'm in Selene's chair now. That means this is my call."

    athought "I'm not sure when that happened. I'm not sure I agreed to it."

    athought "But here we are."

    # --- AERON OPENS ---

    a "You asked for a formal hearing. You have it."

    "Nyra inclines her head. A fraction of a bow."

    ny "Thank you, Commander."

    z "He's not--"

    "Zira stops herself. Looks at the empty space where Selene used to stand. Her jaw tightens further."

    athought "She was going to say I'm not the commander. She's right. But no one else is either."

    athought "Someone has to sit in this chair. Someone has to make decisions."

    athought "Right now, that someone is me."

    a "State your offer."

    # --- NYRA'S PITCH ---

    "Nyra doesn't move. Doesn't shift her weight. Her voice is level, precise -- each word measured."

    ny "I bring seventeen soldiers. All former Order Division. All combat-tested. All loyal to structure, not ideology."

    ny "We defected after Sector Eight. The purge orders were... unconscionable. We refused to comply."

    z "You refused to comply with one set of orders. That doesn't mean you won't follow worse ones from someone else."

    ny "You're right. It doesn't."

    "Zira blinks. She wasn't expecting agreement."

    ny "I'm not asking you to trust me. Trust is earned over time, through action. I'm asking for the opportunity to earn it."

    athought "She's good. She anticipated the objection and used it."

    athought "That's either impressive or dangerous. Possibly both."

    t "Why us? Why Phoenix?"

    "Nyra's gaze shifts to Tessa. Something flickers in her expression -- recognition, maybe. Respect."

    ny "Because you're still standing. Because you lost your commander three days ago and you didn't scatter. Because someone held the line."

    "Her eyes move to Aeron. Stay there."

    ny "I came for the rebellion. I'm staying for him."

    athought "For me."

    athought "Not the cause. Not the mission. Me."

    athought "That should concern me more than it does."

    # --- TEAM REACTIONS ---

    l "You said you killed your commanding officer."

    ny "I did."

    l "How do we know you won't do the same to ours?"

    "Nyra considers the question. Her head tilts slightly -- a bird examining something interesting."

    ny "Because Major Chen gave orders that violated every principle we swore to uphold. He ordered us to execute children for the crime of having parents who asked questions."

    ny "I didn't kill him because I disagreed with him. I killed him because he betrayed the structure he was supposed to serve."

    ny "If Commander Rylan gives me an order that serves the mission, I'll follow it. If he gives me an order that betrays everything we're fighting for..."

    "She pauses. The silence stretches."

    ny "I'll tell him. To his face. Before I act."

    athought "She said the same thing in the rain. 'I'll tell you. Directly. Before acting.'"

    athought "She means it. That's the terrifying part."

    n "Probability assessment."

    "Noelle looks up from her tablet. Her voice is flat, clinical."

    n "Seventeen trained soldiers represents a forty-three percent increase in our combat effectiveness. Even accounting for trust integration issues, the tactical benefit is substantial."

    z "Tactical benefit isn't everything."

    n "No. But it's not nothing, either."

    "Zira's eyes narrow. She doesn't have a counter for math."

    t "What about their... state? I've been watching through the window. They haven't moved in hours."

    ny "They're waiting for orders. That's what soldiers do."

    t "They're not machines."

    ny "No. They're better. Machines don't choose. They chose to follow me. They choose every day to maintain discipline."

    "Tessa looks uncomfortable. That's not the answer she wanted."

    athought "She's worried about them. Their humanity. Whether they're people or tools."

    athought "I should be worried about the same thing."

    athought "Instead, I'm calculating patrol rotations."

    # --- PLAYER CHOICE ---

    "The room waits. All eyes on the chair at the head of the table."

    "Selene's chair. Aeron's chair now."

    menu:
        "How does Aeron respond?"

        "Accept her offer -- provisionally.":
            jump .accept_provisional

        "Defer to the group -- put it to a vote.":
            jump .defer_vote

        "Reject her -- too much risk.":
            jump .reject_offer


    # --- BRANCH: ACCEPT PROVISIONAL ---

    label .accept_provisional:

        $ flag("nyra_accepted_provisional", True)
        $ rel_bump("Nyra", trust=1)
        $ rel_bump("Zira", trust=-1)

        athought "Forty-three percent increase. Seventeen soldiers who don't hesitate."

        athought "The math isn't complicated."

        a "Provisional acceptance. Your soldiers integrate into our patrol structure, but they answer to existing squad leads until trust is established."

        a "You report directly to me. No independent operations. No contact with external assets without clearance."

        "Nyra's expression doesn't change. But something shifts in her posture -- tension releasing."

        ny "Understood, Commander."

        z "You can't be serious."

        a "I'm always serious, Zira. That's the problem."

        z "We don't know her. We don't know them. You're handing loaded weapons to strangers."

        a "I'm handing loaded weapons to soldiers who've already proven they can follow orders. That's more than I can say for half the cells we've absorbed."

        "The words land harder than intended. Zira's jaw works."

        z "Selene would never--"

        a "Selene isn't here."

        "Silence. The kind that has weight."

        athought "I shouldn't have said that."

        athought "It's true. But I shouldn't have said it."

        "Lyra's hand moves toward Zira's arm. Stops halfway. Withdraws."

        l "What are the terms? Specifically."

        athought "She's trying to redirect. Salvage something from this."

        a "Her soldiers bunk in Section C. Supervised access to common areas. Weapons secured except during active ops. Weekly assessment for two months. After that, we revisit."

        "Noelle nods. Tessa looks uncertain. Zira stares at the table like she's considering setting it on fire."

        ny "Acceptable terms. We'll comply."

        athought "We'll comply. Not 'I'll comply.' She speaks for all of them."

        athought "Seventeen soldiers moving as one. That's not loyalty. That's something else."

        athought "I need it anyway."

        jump .scene_transition


    # --- BRANCH: DEFER VOTE ---

    label .defer_vote:

        $ flag("nyra_decision_deferred", True)

        athought "This isn't my decision to make alone. Not really."

        athought "Selene would have decided. She always decided."

        athought "But I'm not Selene."

        a "This affects everyone. We vote."

        "Zira straightens. She wasn't expecting that."

        z "...Fine. I vote no. Absolutely not."

        l "I... abstain. I don't have enough information."

        t "I vote we give her a chance. Provisionally. With oversight."

        n "I vote yes. The tactical calculus is clear."

        "Two yes. One no. One abstain. All eyes turn to Aeron."

        athought "Tied. Unless I break it."

        athought "Which means it was always my decision anyway. I just made them share the weight."

        athought "Clever. Or cowardly. Hard to tell the difference sometimes."

        a "Provisional acceptance. Same terms Tessa implied -- oversight, restricted access, probationary period."

        "Nyra inclines her head."

        ny "Understood. I appreciate the process, Commander. It shows respect for your people."

        athought "She's praising me for democracy. Why does that feel like a test?"

        z "This isn't over."

        a "No. It's not."

        $ rel_bump("Nyra", respect=1)

        jump .scene_transition


    # --- BRANCH: REJECT OFFER ---

    label .reject_offer:

        $ flag("nyra_rejected_initial", True)
        $ rel_bump("Nyra", trust=-1)
        $ rel_bump("Zira", trust=1)

        athought "Forty-three percent isn't worth the risk if I can't predict what they'll do."

        athought "Better to be weaker and certain than stronger and blind."

        a "No."

        "The word drops like a stone."

        ny "May I ask why?"

        a "You killed your last commanding officer. You say it was justified. Maybe it was. But I have no way to verify that, and I don't have time to build the kind of trust that would let me sleep with seventeen armed strangers in my base."

        a "You and your soldiers can leave. No harm. No pursuit. But you don't stay here."

        "Nyra's expression remains neutral. But something hardens in her eyes."

        ny "That's... unfortunate."

        "Zira leans forward."

        z "Is that a threat?"

        ny "No. An observation. You need soldiers. We need purpose. This could have been mutually beneficial."

        ny "But I understand caution. It's not a character flaw."

        "She turns to leave. Stops at the door."

        ny "If you change your mind, Commander... we'll be in Sector Four. For a while."

        athought "She's leaving the door open. Literally and figuratively."

        athought "Smart. Patient. Dangerous."

        athought "I made the right call."

        athought "Then why does it feel like I lost something?"

        "The door hisses shut behind her."

        l "You did the right thing."

        a "Did I?"

        l "You protected us. From an unknown variable."

        athought "Unknown variable. She's learning to speak my language."

        athought "I don't know if that's good."

        jump .scene_close_reject


    # --- SCENE TRANSITION (Accept/Defer paths) ---

    label .scene_transition:

        "Nyra offers a precise bow. Not deep -- respectful, not subservient."

        ny "I'll inform my soldiers. We'll comply with all terms."

        "She turns and walks toward the door. Her footsteps are silent on the metal floor."

        "At the threshold, she pauses."

        ny "Commander."

        a "Yes?"

        ny "Thank you. For seeing what we could be, instead of just what we were."

        "She leaves. The door hisses shut."

        athought "What we could be."

        athought "What does she think we could be?"

        athought "What does she think I could be?"

        # --- AFTERMATH ---

        "The room exhales. But the tension doesn't dissipate -- it just changes shape."

        z "I want it on record that I think this is a mistake."

        a "Noted."

        z "I mean it, Aeron. She's too clean. Too controlled. People like that don't defect -- they infiltrate."

        athought "She might be right."

        athought "But I need those soldiers. I need what they represent."

        athought "Control. Discipline. The ability to give an order and know it'll be followed."

        athought "The Phoenix fighters are loyal, but they're not... precise. Not like her people."

        a "Your objection is noted. Keep watching her. If you see anything that confirms your suspicions, bring it to me."

        z "And if I'm right?"

        a "Then we handle it. Quietly."

        "Something passes between them. An understanding that doesn't need words."

        "Zira nods once. Sharp. Then she's gone."

        # --- LYRA MOMENT ---

        "The others filter out. Noelle to her data. Tessa to her medbay. Lyra lingers."

        l "Aeron."

        a "Lyra."

        l "Are you sure about this?"

        athought "No."

        a "I'm sure we need soldiers. I'm sure she has them. Everything else is variables."

        l "That's not what I meant."

        "She moves closer. Her voice drops."

        l "She looks at you like you're something to worship. That's not... that's not healthy. For either of you."

        athought "Worship."

        athought "Is that what it is? Is that what I want?"

        a "I'll be careful."

        l "Will you?"

        "She doesn't wait for an answer. The door closes behind her."

        athought "Will I."

        athought "Good question."

        athought "I don't have a good answer."

        jump .scene_close


    # --- SCENE CLOSE (Accept/Defer) ---

    label .scene_close:

        "The war room is empty now. Just Aeron and the tactical displays."

        "And, through the window, seventeen soldiers who just became his responsibility."

        athought "Forty-three percent increase in combat effectiveness."

        athought "One woman who looks at me like I'm the answer to a question she's been asking her whole life."

        athought "One team that doesn't trust my judgment."

        athought "One chair that still doesn't fit."

        "He stands. Walks to the window. The soldiers outside don't move. Don't acknowledge him."

        "They're waiting. For orders. For purpose."

        "For him."

        athought "Selene built this rebellion on hope. On compassion. On the belief that people could be better than their worst impulses."

        athought "I don't know what I'm building."

        athought "But I know what I need."

        athought "Soldiers who don't hesitate. A structure that holds. An order that means something."

        athought "If that makes me dangerous, so be it."

        athought "At least I'll be effective."

        #stop ambient fadeout 2.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ scene_mark(_current_scene_id, "completed")
        $ flag("nyra_integrated", True)

        return


    # --- SCENE CLOSE (Reject path) ---

    label .scene_close_reject:

        "The war room settles into silence. The kind that follows difficult decisions."

        athought "I turned away forty-three percent."

        athought "I turned away certainty."

        athought "But I kept control of what's already mine. That has to count for something."

        "Zira catches his eye from across the table. Nods. Approval, or something like it."

        athought "At least someone thinks I made the right call."

        athought "I hope that's enough."

        #stop ambient fadeout 2.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ scene_mark(_current_scene_id, "completed")
        $ flag("nyra_rejected", True)

        return

# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s06_request_for_alignment_ob
# cann.chapter: Act 3
# cann.chapter_start: False
# cann.when_in_timeline: ~12 hours after "Echoes in the Rain." Nyra's formal offer.
# cann.what_happened:
#   - Nyra presents her offer to the Phoenix leadership (or what's left of it).
#   - She brings 17 soldiers, all ex-Order Division, all defected after Sector 8.
#   - Team reactions split: Zira hostile, Noelle supportive (math), Tessa concerned, Lyra wary.
#   - Player choice: Accept provisionally, defer to vote, or reject outright.
#   - Accept/Defer: Nyra integrates. Zira is tasked with watching her.
#   - Reject: Nyra leaves, but offers to remain in Sector 4 if Aeron changes his mind.
#   - Lyra warns Aeron about Nyra's "worship" -- not healthy for either of them.
# cann.aeron_state:
#   - OB functional. Making tactical calculations. Not emotional.
#   - Sits in Selene's chair. Doesn't fit yet, but he's sitting there.
# cann.path_tracking:
#   - Accept provisional: flag("nyra_accepted_provisional"), rel_bump("Nyra", trust=1), rel_bump("Zira", trust=-1)
#   - Defer to vote: flag("nyra_decision_deferred"), rel_bump("Nyra", respect=1)
#   - Reject: flag("nyra_rejected_initial"), rel_bump("Nyra", trust=-1), rel_bump("Zira", trust=1)
# cann.thematic_flags:
#   - The schism begins here -- team fractures over Nyra.
#   - "What we could be" -- Nyra's vision vs what Phoenix was.
#   - Aeron sitting in Selene's chair -- the weight of command.
#   - The 17 soldiers as metaphor: discipline, control, weapons waiting for orders.
# cann.character_moments:
#   - Nyra: "I came for the rebellion. I'm staying for him." Controlled, auditioning without groveling.
#   - Zira: Hostile. "People like that don't defect -- they infiltrate."
#   - Lyra: "She looks at you like you're something to worship." Warns Aeron.
#   - Tessa: Concerned about the soldiers' humanity. "They're not machines."
#   - Noelle: "Forty-three percent increase." Math over emotion.
# cann.block_status:
#   - ANCHOR (always plays). Choice affects Nyra integration and team trust deltas.
# cann.requires_followup:
#   - "Terms of Order" -- debate over Nyra's role (if accepted).
#   - "Chain of Two" -- private Nyra/Aeron debrief (if accepted).
#   - Zira "You Don't Get To Break" -- possessive intimacy (jealousy of Nyra's devotion).
#   - Potential Nyra return arc (if rejected).
