# =======================================================
# ACT 3 - Scene 05a: The Woman from Sector 7 (Empathy Path)
# File: a3_s05a_woman_from_sector_7_emp.rpy
# =======================================================

define hana = Character("Hana")

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s05a_woman_from_sector_7_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s05a_woman_from_sector_7_emp:

    $ show_timeline("DAY 24", "12:00", "Sector 7 — Community Hall")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 32mm lens (EMP warmth). Opens wide on mess hall bustle, then tightens to
    #         two-shot as Hana approaches. Aeron pushed to frame edge — this is Lyra's scene.
    #         Close-ups on Lyra's hands, her sleeve, her Band edge. Handheld drift on recognition beats.
    # LIGHTING: Mess hall: warm amber practicals, steam diffusion from food prep. Natural warmth.
    #           When Lyra recognizes Hana, a subtle temperature drop — same palette, cooler key.
    #           Band glow under sleeve: faint pulse, EMP green-white.
    # SFX: Loop — mess hall ambient: voices, utensils, laughter, pot clatter. Community alive.
    #      One-shots — tray set, sleeve pull, breath catch, chair scrape.
    # FX/COMP: Steam from food trays, crowd movement in soft focus. Band pulse visible under fabric.
    # BLOCKING: Long communal tables. Lyra ("Mira") distributing rations. Hana approaches from the line.
    #           Aeron at a nearby table, visible but peripheral. Not in the conversation.
    # CANON: This is LYRA's scene. Aeron observes but does not intervene.
    #        Lyra's cover identity is "Mira Chen" — a Sector 7 textile worker.
    #        The irony: she chose Sector 7 for her cover because she knew its details. Because she filed them.
    #        Hana's daughter was 8 when taken. File 7-Delta-1138. Status: "Relocated."
    # FACE: Lyra — composure fracturing in micro-expressions. Hana — kind, open, unknowing.

    # ========= VOICE BASELINE =========
    # EMP cadence: Contractions, sensory language, emotional availability.
    # Lyra: performing warmth that becomes unbearable because it's reciprocated by the wrong person.
    # Aeron: present but peripheral. Watchful. He sees Lyra break before she does.
    # Hana: Warm. Mid-forties. Textile worker's hands. No guile. No suspicion.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - MESS HALL - EVENING]
    # The communal meal. Forty-odd people at long tables. Steam rising from pots.
    # Lyra is at the distribution line, ladling portions. She's good at this —
    # the smile, the small talk, the cover identity worn like a second skin.

    #scene bg_mess_hall_emp with dissolve
    #play ambient "sfx/ambient/mess_hall_warm.ogg" fadein 2.0

    # --- OPENING: COMMUNITY MEAL ---

    "The mess hall is loud in the way that means people feel safe enough to be loud."

    "Forty voices overlapping. Spoons against tin. Someone laughing at a table near the back — real laughter, the kind that comes without checking the exits first."

    athought "Lyra's been on distribution for an hour. She volunteered."

    athought "She always volunteers for the tasks that put her in front of people. The ones that make Mira Chen feel real."

    # VISUAL: Lyra at the serving line. Sleeves rolled to the forearm — but not past the Band edge.
    # She's smiling. It looks genuine. That's what makes her dangerous.

    "Lyra ladles stew into a tin bowl, hands it across the counter with a word Aeron can't hear. The woman receiving it laughs."

    athought "She's good at this. Better than she should be."

    athought "Sometimes I forget that Mira Chen is a fiction. That's probably the point."

    # --- HANA APPROACHES ---

    # VISUAL: A woman in her mid-forties joins the line. Textile-rough hands. Hair pulled back
    # with a strip of cloth. She moves with the careful economy of someone used to standing all day.

    "A woman reaches the front of the line. Mid-forties. Hands calloused from loom work, nails cut short. She carries her tray with the patient stillness of someone who's learned not to rush."

    hana "You're Mira, right? The one who organized the blanket rotation last week?"

    l "That's me. Evening, Hana."

    hana "I just wanted to say thank you. The corner bunks get cold after midnight, and my joints aren't what they were."

    l "It's nothing. We had surplus from the Sector Four run."

    hana "It's not nothing. It's someone noticing."

    # VISUAL: Hana smiles. Warm. Unguarded. The smile of someone who still believes in small kindnesses.

    "Hana takes her bowl. Her smile is open and uncomplicated — the expression of a woman who has survived by believing that people are mostly good."

    athought "Lyra's smile doesn't change. Not visibly."

    athought "But her hand on the ladle goes still."

    # --- THE RECOGNITION ---

    # VISUAL: Close on Lyra's face. The smile fixed. Eyes calculating behind it.
    # CAMERA: Slow push. The mess hall noise drops in the mix — Lyra's world narrowing.

    #play sound "sfx/heartbeat_low.ogg"

    "Lyra watches Hana walk to a table. Sit down. Blow on her stew."

    athought "Something just happened. Lyra's hand hasn't moved."

    "The next person in line clears their throat. Lyra blinks. Serves them. The motion is automatic."

    # --- LYRA'S INTERNAL (athought — we're in Aeron's POV, so this is what he reads) ---

    athought "I've seen that look before. On operatives reviewing a target file."

    athought "Pattern recognition. The moment the data stops being data and becomes a face you know."

    # --- LATER: THE TABLE ---

    # VISUAL: Distribution ends. Lyra sits at a table with her own bowl. Untouched.
    # Aeron is two seats away. Watching without watching.

    "Distribution winds down. Lyra takes a bowl for herself and sits. She doesn't eat."

    "Her eyes find Hana across the room. Track her. The way a compass tracks north."

    athought "I move to the seat beside her. She doesn't acknowledge me."

    a "(low) You okay?"

    l "(barely audible) Fine."

    athought "She's not fine."

    athought "Her right hand has moved to her left wrist. Thumb pressed against the Band edge under her sleeve."

    athought "She does that when she's spiraling. I've learned to read it."

    a "(low) Lyra."

    l "(still watching Hana) Her name is Hana Vasik. She was a textile worker in Sector 7."

    l "She had a daughter. Maren. Eight years old."

    athought "Had."

    a "(low) How do you know that?"

    "She doesn't answer immediately. Her thumb presses harder against the Band."

    l "(flat, quiet) File 7-Delta-1138. Family unit: one adult, one minor. Minor, age eight. Status: relocated."

    l "I logged the coordinates. I filed the report. I wrote 'relocated' because that's what the form said."

    athought "Her voice doesn't crack. That's worse."

    athought "Cracking would mean she's processing it. This is recitation. This is the file speaking."

    a "(low) Lyra, that was—"

    l "Three years ago. Maren would be eleven now."

    l "If 'relocated' means what I think it means, Maren isn't anything now."

    "She picks up her spoon. Sets it down. Picks it up again."

    athought "The automatism. The loop. She's caught in it."

    # --- HANA RETURNS ---

    # VISUAL: Hana approaches their table. Carrying two cups. Still smiling.

    "Hana crosses the room with two cups of something warm. She sets one in front of Lyra."

    hana "Mint tea. Sera showed me where the wild plants grow near the east vents."

    hana "You look tired, Mira. You work too hard."

    l "Thank you, Hana."

    athought "The performance is flawless. The gratitude. The small smile. The way she wraps both hands around the cup."

    athought "No one in this room would know that the woman accepting tea just recognized the face from a file she used to send families into the dark."

    # --- THE KINDNESS THAT CUTS ---

    # VISUAL: Hana sits across from them. Settles in. The ease of someone who's found a friend.

    "Hana sits. She's comfortable here — the mess hall, the routine, the company of someone she thinks she knows."

    hana "You know, my daughter always wanted one of those."

    "She gestures at Lyra's wrist. The sleeve has ridden up. The Band edge is visible — faint pulse of light against skin."

    hana "She used to see them on the Echelon officers when they came through. Said they were beautiful."

    hana "Kids, right? They don't understand what things mean. They just see the shine."

    athought "Lyra's cup stops halfway to her mouth."

    athought "Holds there. Perfectly still. Three seconds. Four."

    athought "Then she drinks."

    l "Kids see what adults forget to look at."

    hana "That's a nice way to put it."

    athought "Lyra's left hand is under the table. I can see her fingers digging into her thigh."

    athought "The nails leaving crescents through the fabric."

    hana "Maren — that's my daughter — she drew a picture of one once. With those markers they give out at the community school."

    hana "Blue and gold. She said when she grew up, she wanted to help people the way the officers did."

    athought "Lyra is going to break. I can feel it."

    athought "Not here. Not visibly. But something behind her eyes just went out."

    l "She sounds wonderful."

    hana "She is."

    "Present tense. Hana still uses present tense."

    hana "She's been away for a while. The relocation program. They said it was temporary."

    hana "Three years now. But I keep asking. Someone will know something eventually."

    athought "Relocated. Temporary."

    athought "Lyra wrote those words. Filed the form. Moved to the next entry."

    athought "And now the mother of entry 1138 is bringing her mint tea."

    # --- HANA LEAVES ---

    "Hana finishes her stew. Stands. Touches Lyra's shoulder."

    hana "You're a good person, Mira. This place needs more like you."

    "She leaves. The touch lingers on Lyra's shoulder like a brand."

    "Lyra doesn't move. The tea goes cold."

    # --- THE CHOICE ---

    # VISUAL: The mess hall thins. Lyra and Aeron near-alone. Her hands around the cold cup.
    # CAMERA: Two-shot. Tight. The distance between them is inches but feels like miles.

    "The mess hall empties. Stragglers drift out. Someone kills the overhead, leaving only the amber strip lights along the wall."

    athought "She hasn't spoken since Hana left. Seven minutes."

    athought "I count because counting is easier than asking."

    a "(quiet) What do you want to do?"

    l "I don't know."

    a "You don't have to decide tonight."

    l "Yes I do."

    "She looks at him. The composure is gone. What's underneath isn't grief — it's something harder. Precision turned inward."

    l "Every day I don't tell her, I'm filing the report again."

    l "Every day I smile and hand her food and let her call me Mira, I'm writing 'relocated' on her daughter's life."

    menu:
        "Her eyes are dry. That's the worst part."

        "Then tell her what you can.":
            $ choice_and_dev(
                _current_scene_id, "_lyra_confess", "EMP", factor=1,
                next_scene_label=None,
                note="Lyra partially confesses to Hana. Devastating honesty. EMP-aligned."
            )
            jump .lyra_confess

        "You can't. Not like this.":
            $ choice_and_dev(
                _current_scene_id, "_lyra_hold_cover", "EMP", factor=0,
                next_scene_label=None,
                note="Lyra holds cover. Guilt spiral. Band checking peaks. OB-lean choice in EMP context."
            )
            jump .lyra_hold_cover

    # --- BRANCH: CONFESS ---
    label .lyra_confess:

        a "Then tell her what you can. Not everything. But enough."

        l "Enough to what? To ease my conscience?"

        a "Enough to stop writing that report."

        "She stares at him. Something shifts — not relief, but resolve."

        l "Stay here."

        athought "She stands. Walks out. I don't follow."

        athought "This isn't mine to witness."

        # --- LYRA AND HANA (OFFSCREEN — AERON WAITS) ---

        "Twenty minutes. The mess hall hums with the refrigeration units cycling down."

        athought "I sit with Lyra's cold tea and I wait."

        athought "I don't know what she's saying. I don't need to."

        athought "Some confessions aren't meant for an audience."

        # --- LYRA RETURNS ---

        # VISUAL: Lyra in the doorway. She looks hollowed out. Lighter and heavier at the same time.

        "The door opens. Lyra stands in the frame. Her face is drawn. Her eyes are red but dry."

        athought "She looks like someone who's been carrying a stone and finally set it down."

        athought "Set it down on someone else."

        a "What did you tell her?"

        l "That I worked for Echelon. In Sector 7. That I processed files."

        a "And?"

        l "She asked if I knew what happened to her daughter."

        athought "The longest silence of the evening."

        l "I told her I didn't know. That the files never said."

        l "That was true. The files never said. That was the point of the files."

        a "What did she do?"

        l "She looked at me for a long time. Then she stood up and walked away."

        l "She didn't say anything. She didn't need to."

        athought "Lyra sits. Not in her old seat. In the one Hana vacated."

        athought "I don't know if that's meaningful. I think it is."

        "She sits in Hana's chair. Her hands are flat on the table. Still."

        l "She'll never call me Mira again."

        a "No."

        l "Good."

        athought "Good."

        athought "She means it. That's the thing."

        athought "Mira Chen died at this table tonight, and Lyra is glad."

        $ scene_mark(_current_scene_id, "lyra_confessed_to_hana")
        $ rel_bump("Lyra", trust=1)
        $ npc_remember("Hana", "learned_lyra_was_echelon", tone="silent_grief")
        $ flag("mira_chen_cover_compromised", True)

        jump .band_crisis

    # --- BRANCH: HOLD COVER ---
    label .lyra_hold_cover:

        a "You can't tell her. Not like this. Not tonight."

        l "Why not?"

        a "Because you're spiraling. And she deserves the truth from someone steady, not someone bleeding."

        "Lyra looks at him. For a moment, the old Echelon analyst surfaces — the one who weighed variables, calculated outcomes, filed the correct form."

        l "You're right."

        athought "She hates that I'm right."

        l "Mira Chen would smile. Mira Chen would drink her tea and say goodnight and check on the blanket rotation."

        l "So that's what I'll do."

        "She picks up the cold cup. Drinks. The performance resumes — but the mechanism is visible now."

        athought "She smiles at someone passing by. The smile is perfect."

        athought "I'm the only one in the room who can see the gears turning behind it."

        "Later. The corridor outside her bunk."

        l "Goodnight, Aeron."

        a "Goodnight, Lyra."

        athought "She closes the door. I stand in the corridor."

        athought "I can hear it through the wall. The click of the Band interface."

        athought "She's checking her Band. Not reading data — just activating and deactivating the display. Over and over."

        athought "The rhythm is compulsive. Mechanical. The pattern of someone gripping the thing that made them."

        athought "Click. Glow. Dark. Click. Glow. Dark."

        athought "I want to knock. I don't."

        athought "Some spirals need to hit bottom before they teach you anything."

        $ scene_mark(_current_scene_id, "lyra_held_cover_hana")
        $ flag("lyra_band_crisis_peak", True)
        $ npc_remember("Hana", "still_trusts_mira_chen", tone="warm")

        jump .band_crisis

    # --- BAND COMPULSION PEAK ---
    label .band_crisis:

        # Regardless of choice, this is where Lyra's Band-checking reaches its crisis point.

        # VISUAL: Lyra alone. Band pulsing on her wrist. Her fingers tracing the edge.
        # CAMERA: Close on the Band. The light reflected in her eyes.

        athought "That night I dream about forms."

        athought "Rows of entries. Family units. Names I never read because the form didn't ask for names."

        athought "Status: Relocated. Status: Relocated. Status: Relocated."

        athought "In the dream, every entry has Hana's face."

        "Morning."

        "Lyra is at breakfast before anyone else. Her sleeves are pulled down to her knuckles."

        athought "The Band is hidden. Completely covered."

        athought "First time I've seen her do that."

        athought "Either she's protecting the cover or she can't stand looking at it."

        athought "I don't ask which."

        if scene_has(_current_scene_id, "lyra_confessed_to_hana"):
            "Across the room, Hana eats alone. She doesn't look up when Lyra passes."
            athought "There's a seat between them now. Measured. Permanent."
            athought "Lyra chose this. I think it's the first honest thing Mira Chen ever did."
        else:
            "Across the room, Hana waves. Lyra waves back."
            athought "The performance is seamless."
            athought "Under her sleeve, the Band pulses. I can see the faint glow through the fabric."
            athought "She hasn't stopped checking."

        # --- SCENE CLOSE ---

        #stop ambient fadeout 2.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ flag("lyra_sector7_confronted", True)
        $ scene_mark(_current_scene_id, "completed")

        return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s05a_woman_from_sector_7_emp
# cann.chapter: Act III, Phase I — Proving Ground (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Act III Phase I. During community-building period at Phoenix Base.
#   - After Breath of Faith (s03), before Orders and Prayers (s06).
# cann.what_happened:
#   - Lyra, operating as "Mira Chen," encounters Hana Vasik at a community meal.
#   - Hana's daughter Maren (age 8 at filing) was "relocated" via Sector 7 sweep — the sweep
#     Lyra logged coordinates for when she was Echelon.
#   - Hana doesn't recognize Lyra/Mira. But Lyra recognizes the face from File 7-Delta-1138.
#   - Hana's kindness (tea, gratitude, mentioning her daughter wanted a Band) becomes unbearable irony.
#   - Player choice: Lyra confesses partially or holds cover.
#   - Confess path: Lyra tells Hana she worked for Echelon in Sector 7. Hana walks away in silence.
#   - Hold cover path: Lyra maintains the Mira Chen persona. Band-checking spirals to crisis.
#   - Band Compulsion Peak: regardless of choice, Lyra's relationship with her Band reaches breaking point.
# cann.aeron_state:
#   - Peripheral. Observant. He reads Lyra's tells but doesn't override her agency.
#   - His role is to hold space, not to decide for her.
# cann.path_tracking:
#   - EMP baseline. Confess path: trust+1 for Lyra, mira_chen_cover_compromised flag.
#   - Hold cover path: lyra_band_crisis_peak flag. OB-lean choice in EMP context.
#   - Both paths: lyra_sector7_confronted flag set.
# cann.thematic_flags:
#   - Motifs: Forms (dehumanizing language), "relocated" (euphemism as violence), Band (identity/chain).
#   - Mira Chen as fiction — the cover name chosen FROM the sector she helped destroy.
#   - Hana's present tense ("She is wonderful") vs the file's past tense ("Status: Relocated").
#   - The Band edge visible under the sleeve — the thing Hana's daughter admired is the thing Lyra can't face.
#   - "Every day I smile and hand her food, I'm writing 'relocated' on her daughter's life."
# cann.character_moments:
#   - Lyra: The analyst confronting the human cost of analysis. File 7-Delta-1138 has a mother.
#   - Hana: Kindness as inadvertent cruelty. She is the wound Lyra cannot bandage.
#   - Aeron: Reading Lyra's tells — the Band-checking, the thumb on the wrist, the fixed smile.
#     He doesn't intervene. He waits. That's its own kind of care.
# cann.block_status:
#   - VARIANT (EMP). Confess/hold cover branch affects Lyra's arc going forward.
# cann.requires_followup:
#   - Confess path: Hana's silence should echo. She doesn't forgive. She doesn't accuse. She withdraws.
#   - Hold cover path: Band-checking escalation pays off in later Lyra crisis scene.
#   - "Mira Chen" cover may be compromised if confess path taken — affects operational security.
#   - The Band compulsion peak should be referenced when Lyra eventually confronts her identity.
