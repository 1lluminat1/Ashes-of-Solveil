# act2_20_tessa_late_night_clinic.rpy


# =======================================================
# ACT 2 - Scene 20: Tessa - Late Night Clinic Visit (Trust Foundation)
# =======================================================


label act2_tessa_late_night_clinic:

    # VISUAL: Base. Late evening. Training concluded. Minor injury sustained. Nothing serious.
    # LIGHTING: Artificial light. Medical area bright. Rest of base dimming for night.
    # SOUND: Base settling. Voices quiet. Medical equipment humming softly.

    #scene bg_base_evening with fade

    "{i}Training session. Sparring. Went well until it didn't. Caught an elbow to the ribs. Probably just bruised. But protocol says check with medical. Make sure nothing's broken. Make sure I'm operational. Besides, good excuse to see Tessa. Haven't talked to her properly in weeks. Been meaning to.{/i}"

    # VISUAL: Walking toward medical station. Hand on ribs. Not severe but uncomfortable. Limping slightly.
    "{i}Ribs hurt. Not bad. Just annoying. Sharp pain when breathing deep. Probably bruised, maybe cracked. Either way, Tessa will know. She always knows. Has that skill. That instinct for what's wrong and how to fix it. Medical and human. Both.{/i}"

    # VISUAL: Medical station ahead. Light on. Someone moving inside. Tessa. Always there. Always working.
    #scene bg_medical_station_night with fade

    "{i}Medical station. Light on. Of course. Tessa's always here. Morning. Noon. Night. Always present. Always available. Always healing. She doesn't just work here. She lives here. Medical station is her home more than her quarters. That's dedication. Or addiction. Maybe both.{/i}"

    # VISUAL: TESSA organizing supplies. Humming softly. Peaceful. In her element. Notices Aeron.
    t "(looking up, smiling) Aeron. Evening. What brings you to my humble medical establishment? Let me guess—training injury? You're favoring your left side and breathing shallow. Ribs?"

    # VISUAL: Aeron nodding. Impressed. She diagnosed him from across the room.
    a "Caught an elbow during sparring. Pretty sure it's just bruised but protocol says verify."
    t "Protocol is wise. Bruised ribs and cracked ribs feel similar initially but diverge significantly in recovery time and complication risk. Let's take a look. Shirt off, sit on the exam table."

    # VISUAL: Aeron complying. Removing shirt. Sitting. Tessa approaching with professional focus.
    t "This is going to hurt a bit. I need to palpate the area, check for fractures. Deep breath for me?"

    # VISUAL: Aeron breathing deep. Sharp pain. Visible wince. Tessa noting reaction.
    t "Sharp pain on inspiration. That's consistent with intercostal bruising or possible rib fracture. Let me check..."

    # VISUAL: She examines carefully. Gentle but thorough. Fingers pressing specific points. Reading his reactions.
    t "(pressing) Here?"
    a "(wincing) Yeah. That's the spot."
    t "(pressing another area) And here?"
    a "Less painful but still tender."
    t "Good news—no crepitus, no deformity, no signs of fracture. This is deep tissue bruising, probably intercostal muscle strain. Painful but not dangerous. You'll be operational in three to five days with proper care."

    # VISUAL: Tessa moving to supply cabinet. Retrieving pain medication, anti-inflammatory, bandage.
    t "I'm going to wrap your ribs for support. It'll help with the pain and prevent further aggravation. Take these twice daily—pain management and inflammation reduction. No heavy lifting, no intense training for five days. Light duty only."
    a "Five days? We're in the middle of recruiting. Can't take five days off."
    t "You can and you will. Light duty doesn't mean no duty. It means no stupid duty. Interview recruits? Fine. Lift heavy equipment? Stupid. Sparring? Very stupid. Patrol? Acceptable with caution. Clear?"

    # VISUAL: Aeron accepting. She's right. Always is about medical things.
    a "Clear. Five days. Light duty. No stupidity."
    t "Good patient. Now hold still while I wrap this."

    # VISUAL: She wraps his ribs. Professional. Efficient. But also gentle. Caring. Not just fixing injury. Caring about person.
    "{i}She wraps carefully. Firm but not constricting. Supportive but not limiting. She's done this hundreds of times. Thousands maybe. But she treats each patient like it matters. Like they matter. That's Tessa. That's why people trust her. She makes you feel cared for, not just treated.{/i}"

    # VISUAL: Wrapping complete. Tessa stepping back. Evaluating work. Satisfied.
    t "There. That should help. Remember—five days, light duty, medication twice daily. Come back if pain worsens or breathing becomes difficult. Unlikely but protocol requires I mention it."
    a "Will do. Thanks, Tessa. Appreciate it."

    # VISUAL: Tessa washing hands. Then turning. Looking at him. Considering something.
    t "You're welcome. But while you're here... can I ask you something? It's not medical. It's personal."

    # VISUAL: Aeron curious. Tessa rarely asks personal questions. Usually gives advice but doesn't pry.
    a "Sure. Ask."

    # VISUAL: She sits. Across from him. Equal level. Not doctor-patient. Person-person.
    t "I asked you to bring me names. Remember? Back when we first met. After you helped with that injured child. I said keep track of people you save. Bring me their names. Count the living instead of counting the dead."
    t "Have you been doing that? Keeping track?"

    # VISUAL: Aeron nodding. Reaches into pocket. Pulls out folded paper. Worn. Handled often. Names written. List kept.
    a "Yeah. I've been keeping track. Every person. Every name. Every life saved since I defected. Since I became Aeron instead of Glass. It's... it's not many. But it's something."

    # VISUAL: Hands paper to Tessa. She unfolds it. Reads. Face softening. Emotion showing.
    t "(reading) Lyra Kade. Target 391. Zira Veyne. Daven Cress. Elara Venn. Senna Thrace. Kael Duren..."
    t "(voice catching) You actually did it. You've been counting. You've been keeping track. Twenty-two names. Twenty-two people alive because of you."

    # VISUAL: She looks up. Eyes wet. Not crying but close. Moved. Genuinely moved.
    t "Most people don't do this. They say they will but they don't. Promises are easy. Action is hard. But you did it. You kept track. You counted the living."
    t "That matters. That means something. That means you're not just running from Glass. You're building Aeron. One saved life at a time. One name at a time."

    # VISUAL: Aeron uncomfortable with praise. Deflecting. Minimizing.
    a "It's just a list. Just names. Doesn't undo the Sweep. Doesn't erase 390 deaths. Twenty-two saved versus 390 killed. Math still looks bad."
    t "Math isn't the point. Direction is the point. You're moving toward saving instead of killing. That's change. That's growth. That's redemption happening in real time."

    # VISUAL: She stands. Walks to wall. Points to something Aeron hadn't noticed before.
    # VISUAL: Board on wall. Names written. Dozens. Maybe hundreds. Tally marks. Organized. Maintained.

    t "See this? This is my count. Every person I've saved. Every patient who lived when they should have died. Every life I protected. Every name that matters."
    t "Started keeping track after my mother died. After I couldn't save her. I thought if I could save everyone else, maybe her death would hurt less. Maybe I could balance the scales. Spoiler alert—it doesn't work that way."

    # VISUAL: She touches board. Gentle. Reverent. Sacred to her.
    t "But I keep counting anyway. Because these names matter. These lives matter. Maybe they don't erase my mother. Maybe they don't balance cosmic scales. But they're real. They're alive. They're proof that I'm doing something good even when everything else feels broken."

    # VISUAL: Turning back to Aeron. Understanding. Shared experience. Shared pain. Shared coping mechanism.
    t "You lost 390 people. I lost my mother. We're both trying to save people we've already lost. That's impossible. Logically impossible. But we try anyway."
    t "And in trying, we actually save people who aren't lost yet. People who matter. People whose names go on lists and boards and memories. That's not nothing. That's everything."

    # VISUAL: Aeron staring at board. Hundreds of names. Tessa's life work. Visible. Counted. Remembered.
    a "How many? How many have you saved?"
    t "Three hundred forty-seven. Documented. Verified. Names I know. Patients I remember. That's not counting the ones I treated and released without getting names. Or the ones who left before I could ask. Just the ones I'm certain about."
    t "Three hundred forty-seven reasons I keep going. Keep healing. Keep counting. Because each name is proof that what I do matters. That I matter. That my mother's death wasn't meaningless if it led me here. To this. To them."

    # VISUAL: She returns to sitting. Facing Aeron. Vulnerable. Open. Sharing burden with someone who understands.
    t "You have twenty-two. That's twenty-two more than most people. Twenty-two reasons to keep going. Keep fighting. Keep building Aeron instead of being Glass."
    t "And that number will grow. You're recruiting. You're leading. You're building resistance. How many lives will you save when we take down Echelon? Hundreds? Thousands? Your twenty-two is just beginning."

    # VISUAL: Aeron processing. Her optimism. Her belief. Her count. Her hope. Infectious. Necessary.
    a "You really believe that? That we can take down Echelon? That twenty-two becomes thousands?"
    t "I believe that trying matters. I believe that counting the living beats mourning the dead. I believe that you wouldn't be here, keeping that list, if you didn't believe it too. Somewhere. Buried. But there."

    # VISUAL: Silence. Comfortable. Shared understanding. Mutual burden. Mutual hope.
    "{i}She gets it. Gets the guilt. Gets the counting. Gets the impossible need to save people who are already gone by saving people who aren't. She's been doing this longer. Has bigger list. More experience. But same wound. Same coping. Same hope masquerading as logic.{/i}"

    # VISUAL: Tessa reaching out. Taking the paper with names. Standing. Walking to her board.
    t "Can I add these? To my board? Your twenty-two become part of my count? We'll share them. Our collective count. Our reminder that we're saving people together."

    # VISUAL: Aeron nodding. Yeah. Shared burden. Shared hope. Shared count. That works.
    a "Yeah. Add them. Make them part of ours. Not just mine. Ours."

    # VISUAL: Tessa writing names carefully. One by one. Adding Aeron's twenty-two to her three forty-seven. Collective count. Shared mission.
    t "Three hundred sixty-nine. That's our count now. Together. Every name here matters. Every person saved is proof we're doing something right. Something good. Something worth continuing."

    # VISUAL: She finishes writing. Steps back. Looking at expanded board. Satisfied. Hopeful.
    t "Thank you. For keeping the list. For bringing me the names. For trusting me with this. Not everyone understands the counting. But you do. That matters. You matter."

    # VISUAL: Turning back to Aeron. Smiling. Genuine warmth. Connection. Trust.
    t "Your ribs will heal. Five days, light duty, you'll be fine. But this—this list, this counting, this proof that you're building something good—this heals something deeper. This heals the Glass wound. This heals the Sweep guilt. This heals you."
    t "Keep counting, Aeron. Keep saving. Keep building your list. And bring me the names. Always bring me the names. I'll keep adding them. We'll count together. Count the living. That's how we win. That's how we heal. That's how we become more than our wounds."

    # VISUAL: Aeron standing. Ribs bandaged. Heart less heavy. Burden shared. Hope rekindled.
    a "I'll keep counting. Keep saving. Keep bringing you names. That's a promise. One I'll actually keep."
    t "I know you will. You're good at keeping promises. That's one of your better qualities. Among many."

    # VISUAL: She's looking at him differently. Not just patient. Not just resistance member. Something more. Respect. Trust. Maybe beginning of something deeper. Foundation laid.
    "{i}She trusts me. Actually trusts me. Shared her board. Her count. Her three hundred forty-seven reasons to keep living. That's intimate. That's vulnerability. That's trust I haven't earned yet but she's giving anyway. That matters. That's foundation. That's beginning.{/i}"

    # VISUAL: Moving toward door. Leaving. But moment lingers. Connection made. Trust established.
    a "Thanks again. For the ribs. For the talk. For the board. For understanding. For all of it."
    t "Anytime. That's what I'm here for. Healing bodies and souls. Counting the living. Building hope. That's my job. And I'm good at it."
    a "The best. Definitely the best."

    # VISUAL: She smiles. Warm. Real. Beautiful. Then returns to work. Always working. Always healing. Always counting.
    "{i}Leaving medical station. Ribs bandaged. List shared. Count joined. Burden lighter. Tessa gets it. Gets the guilt. Gets the need to save people already lost. Gets me. That's rare. That's valuable. That's trust. And trust is foundation for everything else. Everything good starts with trust.{/i}"

    # TRANSITION: Walking back to quarters. Night settling. Base quiet. But hope louder. Count continues. Living counted. Forward movement.
    #scene bg_base_night with fade

    "{i}Twenty-two names. Now part of three hundred sixty-nine. Collective count. Shared mission. Proof we're doing something that matters. Something good. Something worth continuing. Tessa's right. Math isn't the point. Direction is. And we're moving right direction. Together. Counting. Saving. Living. That's enough. That's everything.{/i}"

    # VISUAL: In quarters. Preparing for sleep. Looking at empty hand where paper was. Names now on Tessa's board. Shared burden. Shared hope.
    "{i}Names are gone from my pocket. But not gone. On her board. Part of collective count. Part of us. Twenty-two became three sixty-nine. Tomorrow maybe three seventy. Or eighty. Or more. Keep counting. Keep saving. Keep building list. That's how we win. That's how we heal. That's how Glass becomes Aeron. One name at a time.{/i}"

    # Mark scene complete
    $ scenes["tessa_late_night_clinic"] = True
    $ characters["tessa"]["trust"] += 3
    $ characters["tessa"]["shared_count"] = True
    $ characters["tessa"]["count_the_living_bond"] = True
    
    # Update collective count
    $ collective_count = 369  # Tessa's 347 + Aeron's 22
    $ characters["tessa"]["personal_count"] = 347
    $ characters["aeron"]["personal_count"] = 22
    
    # Set foundation for potential romance
    $ characters["tessa"]["romance_foundation"] = True
    $ canon["count_the_living_established"] = True

    # TRANSITION: Sleep coming easier. Nightmares quieter. Names on board standing guard. Count continues. Hope persists.
    scene black with fade

    return

    # canon_note: Scene 14 complete - Tessa trust foundation, "Count the Living" bond
    # canon_note: Aeron kept list (22 names) - Lyra, 391, Zira, recruits from Scene 12
    # canon_note: Tessa's board revealed - 347 saved lives, documented, remembered
    # canon_note: Collective count established - 369 total (347 + 22)
    # canon_note: Tessa's trauma shared - lost mother, couldn't save her, saves everyone else
    # canon_note: Mutual understanding - both trying to save people already lost
    # canon_note: "Count the living" philosophy = shared coping mechanism, shared mission
    # canon_note: Trust deepened - Tessa shares vulnerable count, Aeron shares his list
    # canon_note: Foundation for romance - respect, understanding, shared wound, trust
    # canon_note: Medical scene grounded - rib injury, proper treatment, protocol followed
    # canon_note: Redemption quantified - 22 saved vs 390 killed, direction matters more than math
    # canon_note: Board as sacred object - physical manifestation of purpose, hope, healing
    # canon_note: Theme: Healing through counting, redemption through saving, hope through action
    # canon_note: Sets up deeper Tessa relationship (Scene 18 mercy death crisis, Scene 20+ potential romance)