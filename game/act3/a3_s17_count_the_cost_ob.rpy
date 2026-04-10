# =======================================================
# ACT 3 - Scene 17: Count the Cost (Obedience Path)
# File: a3_s17_count_the_cost_ob.rpy
# Path: OB
# Type: TESSA FIRST EROTIC (CONDITIONAL)
# Character Focus: Tessa, Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s17_count_the_cost_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s17_count_the_cost_ob:

    # ========= GATE CHECK =========
    # This scene ONLY fires if player apologized to Tessa in s10.
    # If dismissed, skip entirely.
    if flag("tessa_dismissed_s10"):
        $ scene_mark(_current_scene_id, "skipped")
        return

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked tripod. The steadiest camera on the OB path. No drift.
    #         No handheld. The stability IS Tessa. Opens wide on the medbay corridor --
    #         after hours, dim. Tessa in the doorway of the supply room.
    #         Tightens slowly. By the consent gates: close-ups so still they could be
    #         photographs. The camera doesn't move because neither does she.
    #         This is the quietest scene on the OB path.
    # LIGHTING: Medbay corridor: emergency strip lighting only (amber, low, 15%).
    #           The supply room: a single overhead at minimum -- just enough to see.
    #           Tessa's lamp (the portable one she carries) is present but OFF.
    #           She didn't bring light. She brought herself.
    #           Intimacy: same low amber. No change. The light doesn't perform.
    #           Aftercare: same. Nothing changes. That's the point.
    # SFX: Loop -- medbay night ambient: ventilation, distant drip from a pipe,
    #      the faintest hum of monitoring equipment in the next room.
    #      One-shots -- fabric shift, breath (his, uneven; hers, steady), skin on skin (quiet).
    #      The dominant texture: silence. Not awkward. Inhabited.
    # FX/COMP: Supply room: shelves of medical supplies. Antiseptic smell implied.
    #          A cot pushed against the wall -- the one Tessa naps on during long shifts.
    #          Clean sheets. Her field kit on the shelf. His jacket on the door handle.
    # BLOCKING: Tessa in the supply room. She's not waiting for him -- she's working late.
    #           He finds her. She doesn't ask why he's there. She makes room.
    #           Physical contact is slow. Grounding touch first. Temperature comfort.
    #           She doesn't reach -- she opens space and lets him enter it.
    # CANON: TESSA FIRST EROTIC (OB). The quietest intimacy on the path.
    #        She doesn't try to fix him. Doesn't argue doctrine. Doesn't demand proof.
    #        She just stays. That's her entire methodology.
    #        For the first time on OB, someone holds him without asking anything.
    #        Callbacks: s10 (apology), Tessa's board, the medbay corridor visits.
    # CONSENT: 3-gate framework. Tessa's gates: (A) grounding touch offered,
    #          (B) temperature comfort (his cold hands, her warm ones),
    #          (C) explicit verbal -- "You can leave whenever you need to."
    # FACE: Tessa -- steady. Her steadiness is not performance. It's practice.
    #        Aeron -- the mask thins. Not cracks -- thins. Like paint worn by weather.

    # ========= VOICE BASELINE =========
    # OB Aeron: Quieter than with anyone else. Tessa's silence is contagious.
    #           His clinical cadence softens -- not to warmth, but to something like rest.
    # Tessa: Minimal words. She speaks in actions and short observations.
    #        Her voice is the voice of someone who's been up for eighteen hours
    #        and has stopped performing alertness.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - MEDBAY SUPPLY ROOM - LATE NIGHT]
    # A small room off the main medbay. Shelves. A cot. Medical supplies in labeled bins.
    # The room of someone who takes care of things and people and doesn't distinguish between them.

    #scene bg_medbay_supply_room_night with dissolve
    #play ambient "sfx/ambient/medbay_night_quiet.ogg" fadein 2.0

    # ========== PHASE 1 -- FINDING HER ==========

    athought "0330. I'm in the corridor again."

    athought "The medbay corridor. Third time this week."

    athought "I don't come here for treatment. I come here because the lighting is different. Amber. Low. The only corridor on the base that doesn't feel like an interrogation room."

    athought "And because she's here."

    "The supply room door is ajar. Light from inside -- dim, barely there. The sound of someone sorting. Quiet. Methodical."

    athought "Noelle noticed the pattern. She logged it -- instance seven. Visited Tessa's medbay at 0400 and sat in the corridor for eleven minutes."

    athought "She didn't log tonight. Tonight I don't sit in the corridor."

    "He pushes the door open."

    "Tessa is at the shelving unit. Sorting surgical kits. Her hands move with the automatic precision of repetition -- she could do this blindfolded. Has, probably, during blackouts."

    "She doesn't startle. She glances. Notes him. Returns to sorting."

    t "Can't sleep."

    "Not a question."

    a "No."

    t "There's a cot."

    "She nods toward it. No ceremony. No invitation. Just information."

    athought "There's a cot. As if sleep were that simple."

    athought "For Tessa, maybe it is. She sleeps in three-hour blocks between emergencies. She's made peace with the limitations of rest."

    "He sits on the edge of the cot. The springs don't creak -- she's kept them oiled. The sheets are clean."

    athought "She maintains this space. Even the supply room. Even the place no one sees."

    athought "That's who she is. Maintenance as care."

    "She continues sorting. The quiet between them isn't awkward. It's inhabited."

    t "Your hand."

    athought "She sees it. The tremor."

    a "It's fine."

    t "It's been doing that for three weeks."

    a "You've been watching."

    t "I'm a medic. I watch."

    "She sets down the surgical kit. Wipes her hands on her thighs. Turns to face him."

    t "Let me see."

    # ========== PHASE 2 -- GROUNDING ==========

    "She crosses to the cot. Sits beside him. Close. Their knees touch."

    "She takes his left hand. Holds it in both of hers."

    athought "Her hands are warm. They're always warm. Circulation, she'd say. Good peripheral blood flow."

    athought "But it feels like more than circulation."

    "She turns his hand palm-up. Her thumb traces the tendons. Clinical. She's assessing."

    t "Not neurological. Stress-reactive. The tremor follows your cortisol cycle."

    a "You can tell that from touch."

    t "I can tell that from four years of medical training and three weeks of watching you pretend it isn't happening."

    athought "She doesn't scold. She states. The statement is the scold."

    "Her hands close around his. Warm pressure. Steady."

    t "Breathe."

    a "I'm breathing."

    t "You're ventilating. That's different. Breathe. Slower."

    athought "I try. Four in. Six out. Lyra's rhythm."

    athought "Except right now it's Tessa's instruction. The same count. Different context."

    "His breathing slows. Her hands hold his. The tremor subsides -- not from force, not from discipline. From warmth."

    athought "The tremor stops with Nyra because she gives me structure."

    athought "It stops with Tessa because she gives me permission to have it."

    athought "I don't know which is healthier."

    athought "I know which one feels like rest."

    # ========== PHASE 3 -- CONSENT GATES ==========

    # --- CONSENT GATE A: Grounding touch offered ---

    "She doesn't release his hand. Her thumb continues the slow circles on his wrist."

    t "You've been coming to this corridor."

    a "Yes."

    t "Not for the medbay."

    a "No."

    t "For what?"

    athought "For you. The honest answer."

    athought "I don't say it. But something in my expression does."

    "She reads it. The way she reads vital signs -- quickly, accurately, without commentary."

    t "Okay."

    athought "One word. She says 'okay' and everything in the room shifts."

    t "Your hands are cold."

    "She brings his hand to her collarbone. Holds it there. Her skin is warm through the thin fabric of her scrubs."

    # --- CONSENT GATE B: Temperature comfort ---

    t "Feel that?"

    a "Yes."

    t "That's a resting heart rate. Sixty-two BPM. Normal."

    t "Yours is ninety-four. That's not normal for you."

    a "You know my normal?"

    t "I know everyone's normal. Yours dropped from seventy-one to sixty-eight during the first week after Selene. Then it climbed. It's been climbing since."

    athought "She tracks us. All of us. Not with Noelle's machines -- with her hands, her eyes, the attention she pays because it's the only thing she knows how to give."

    "Her hand lifts to his face. Not reaching -- offering. Her palm open, hovering near his jaw."

    t "This okay?"

    a "Yes."

    "Her palm on his jaw. Warm. Still."

    athought "She doesn't search. Lyra searches. Zira claims. Nyra worships."

    athought "Tessa waits. She puts her hand out and waits for me to lean into it."

    athought "I lean."

    # --- CONSENT GATE C: Explicit exit ---

    t "You can leave whenever you need to. No questions. Door's right there."

    a "I know."

    t "I mean it. No feelings hurt. No grudges. Just the door."

    a "I don't want the door."

    t "What do you want?"

    athought "Rest."

    athought "I want rest."

    athought "Not sleep. Not mission downtime. Not the false ease of doctrine."

    athought "Rest. The kind that requires another person."

    a "This."

    "She nods. No drama. No relief. Just acknowledgment."

    t "Okay. Then stay."

    # ========== PHASE 4 -- INTIMATE SEQUENCE ==========

    # VISUAL: The supply room. Low amber light. Shelves of medical supplies.
    # The cot against the wall. Two people who aren't performing anything.
    # CAMERA: Locked. Still. The stillness is Tessa's gift to the scene.
    # The intimacy is slow. Grounding. Temperature-first -- cold hands warming.
    # No urgency. No demand. No doctrine. Just presence.

    "It starts with temperature. His cold hands finding warmth against her skin. Her steady hands guiding without directing."

    athought "She doesn't rush. She doesn't perform. She moves the way she works -- attentive to each variable, adjusting without being asked."

    "Her forehead against his. Breathing together. Not the forced sync of resonance or the desperate grasp of need."

    "Just breathing. In the same room. At the same time."

    athought "For the first time on this path, no one is asking me to be anything."

    athought "Not a commander. Not a weapon. Not a man who feels or a man who doesn't."

    athought "Just present. Just here."

    t "(whisper) Easy."

    athought "One word. She says it and my shoulders drop two inches."

    athought "I didn't know they were raised."

    # [INTIMATE CONTENT HERE]

    # ========== PHASE 5 -- AFTERCARE ==========

    # VISUAL: After. Same light. Same room. Nothing has changed except them.
    # She holds him. His head against her shoulder. Her arms around him.
    # Not clinging. Not gripping. Holding. The way you hold something
    # that might break but hasn't yet.
    # CAMERA: Wide. Still. Two figures on a cot in a supply room.
    # The most unremarkable composition on the OB path. That's the point.

    "The supply room. Same light. Same hum. Nothing in the room has changed."

    "She holds him."

    "Not desperately. Not possessively. Not devotionally."

    "She holds him the way she holds everything that needs holding -- carefully, completely, without commentary."

    "His head against her shoulder. His breathing is slow. Her arms around him."

    "Silence."

    "Not the silence of things unsaid. The silence of things that don't need saying."

    athought "She doesn't ask if I felt anything."

    athought "She doesn't ask what this means."

    athought "She doesn't ask me to come back or stay away or choose or prove or demonstrate."

    athought "She holds me."

    athought "For the first time on this path, someone just holds me without asking anything."

    athought "I don't know what to do with that."

    athought "I let it happen."

    "Minutes pass. The ambient hum. The distant drip. Her heartbeat against his ear -- sixty-two BPM, steady, unchanged."

    "She doesn't speak first. Neither does he."

    "Eventually, her hand moves to his hair. Not stroking -- resting. Her fingers find a rhythm that isn't rhythm. Just presence with motion."

    athought "The tremor is gone."

    athought "Not suppressed. Not disciplined into stillness."

    athought "Gone. The way pain leaves when the source is removed."

    athought "I don't know what that means."

    athought "I don't examine it."

    "The supply room is quiet. The base turns in its sleep."

    "She holds him. He lets her."

    "That's the scene."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ flag("tessa_first_intimate", True)
    $ rel_bump("Tessa", trust=2, affection=1)
    $ metric("tessa_intimacy_level", set_to=max(metric("tessa_intimacy_level"), 1))
    $ npc_remember("Tessa", "held_him_no_words", tone="quiet_steadiness")
    $ npc_remember("Aeron", "tessa_didnt_ask_anything", tone="unfamiliar_rest")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s17_count_the_cost_ob
# cann.chapter: Act III, Phase II -- Deepening (Obedience Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - After Noelle's contradiction logs and the Zira confrontation.
#   - Late night. Aeron's third visit to the medbay corridor.
# cann.what_happened:
#   - CONDITIONAL: Only fires if player apologized in s10. Skip if dismissed.
#   - Aeron comes to the medbay corridor at 0330. Third time this week.
#   - Finds Tessa sorting surgical kits. She doesn't ask why he's there.
#   - She sees the tremor. Takes his hand. Clinical assessment becomes grounding.
#   - "Not neurological. Stress-reactive." She's been watching for three weeks.
#   - Consent gates: (A) grounding touch offered, (B) temperature comfort
#     (his cold hands, her warm skin), (C) "You can leave whenever you need to."
#   - The quietest scene on OB. No urgency, no demand, no doctrine.
#   - Aftercare: SILENCE. She holds him. No words. No questions.
#     "For the first time on this path, someone just holds me without asking anything."
#   - The tremor is gone. Not suppressed -- removed. The source addressed, not the symptom.
# cann.aeron_state:
#   - OB quieter than with anyone else. Tessa's silence is contagious.
#   - "I don't know which is healthier. I know which one feels like rest."
#   - The comparison: Nyra stops the tremor through structure, Tessa through permission.
#   - Post-intimate: "I don't examine it." Deliberate non-analysis. OB vulnerability.
# cann.path_tracking:
#   - flag("tessa_first_intimate"). rel_bump("Tessa", trust=2, affection=1).
#   - trust=2 because Tessa is the only LI who earns the higher trust bump on OB.
#     She earns it by NOT asking for anything.
#   - If dismissed in s10: scene_mark("skipped"), return. No state changes.
# cann.thematic_flags:
#   - Silence as intimacy: the aftercare has NO dialogue. Unique on the path.
#   - The four LI comparison: Lyra searches, Zira claims, Nyra worships, Tessa waits.
#     "She puts her hand out and waits for me to lean into it."
#   - The tremor diagnostic: stress-reactive vs. neurological. Tessa treats the source.
#     Nyra treats the symptom (through structure). The comparison is the theme.
#   - Medbay corridor as recurring space: Noelle logged it. Aeron keeps coming back.
#     The corridor as the one warm-lit space on the base.
#   - "That's the scene." -- meta-acknowledgment. The simplicity IS the statement.
# cann.character_moments:
#   - Tessa: Minimal words. Maximum presence. "Easy." -- one word that drops his shoulders.
#     She doesn't try to fix him. She creates conditions for rest.
#   - Aeron: "For the first time on this path, someone just holds me without asking anything."
#     The OB revelation: being held without conditions is unfamiliar.
#   - The cot springs: she kept them oiled. Maintenance as care. That's Tessa.
# cann.block_status:
#   - CONDITIONAL VARIANT. Requires s10 apology. If dismissed: skipped.
#   - The skip itself is meaningful: if you drove her away, this rest doesn't exist.
# cann.requires_followup:
#   - Does Aeron return to the medbay corridor more or less after this?
#   - Tessa's silence as counterweight to Nyra's doctrine: conscious choice or instinct?
#   - The tremor: does it return? Does he seek Tessa or Nyra when it does?
#   - The s10 gate: players who dismissed Tessa should feel the absence.
#   - "That's the scene" as potential callback: simplicity as thesis.
