# =======================================================
# ACT 4 - Scene 04: Lyra Prays Alone (Obedience Path)
# File: a4_s04_lyra_prays_alone_ob.rpy
# Path: OB
# Type: LYRA STATE BEAT
# Character Focus: Lyra (primary, interior), Aeron (late entry, silent)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s04_lyra_prays_alone_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s04_lyra_prays_alone_ob:
    $ show_timeline("26th of Forge, 390 A.C.", "05:00", "Phoenix Base — Shrine Alcove")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked tripod. The OB lens. No drift. No search.
    #         Opens on the shrine corner: a supply alcove Lyra has turned into prayer space.
    #         Three-quarter on Lyra's back. She kneels on a folded blanket on concrete.
    #         Close-ups: her hands at the buckle -- she has cinched the Band tighter.
    #         Her mouth moving. Old Tongue syllables. The syllables reach the air and stop there.
    #         Mid-shots: the shrine objects. Candle, cloth, the small icon she brought from the cathedral.
    #         The candle is lit. It's the only warm light in the alcove. She keeps it alive.
    #         Late scene: Aeron at the threshold. 50mm. He does not enter immediately.
    #         He enters. He kneels beside her. Two-shot, locked, symmetrical. Equal frame weight.
    #         Final: slow push to her hand at the Band. Still cinched. End on that.
    # LIGHTING: One practical -- the candle, low and orange. Behind them, cold overhead strip
    #           from the corridor bleeding through the doorway. Blue-white.
    #           The two lights do not meet. The candle is a pocket. The overhead is the base.
    #           Lyra is lit half by each. Her face is bisected. She does not move into either.
    # SFX: Loop -- base ambient. Ventilation. Distant bootfall. The morning-shift rhythm.
    #      One-shots -- Lyra's breath. The buckle creaking once when she shifts.
    #      The Old Tongue syllables. Low. Under-voiced.
    #      The door: no hiss here. The alcove is open. Aeron's bootfall is the only announcement.
    # FX/COMP: The shrine: functional items pressed into sacred service. A folded medical cloth
    #          as altar linen. A ration tin holding the candle. The icon leaned against the wall
    #          because there is no shelf. The economy of devotion in a military space.
    # BLOCKING: Lyra kneeling. Knees, folded blanket, concrete. Hands in her lap at start --
    #           moving to the Band at the buckle mid-scene. Not loosening. Checking. Confirming.
    #           She does not rise. She does not turn when Aeron arrives.
    #           He kneels beside her, not behind. Not leading. Parallel. A measured distance --
    #           close enough to give a hand, far enough not to crowd the candle.
    # CANON: LYRA STATE BEAT. The morning after s02's restructuring. She has not slept.
    #        The scene is a failure of prayer and the substitution of body for words.
    #        She does not resolve. She does not decide. She marks her position.
    # FACE: Lyra -- not tearful. Past tears. The composure of a priest whose first tool
    #        has failed and who is still holding the second tool because she has to hold something.
    #        Aeron -- the mask. No speech until the single line at the end. He watches her
    #        the way he watches tactical displays. He also gives her his hand without hesitation.

    # ========= VOICE BASELINE =========
    # Lyra: Almost entirely internal (lthought) until the final line.
    #        Her spoken language in this scene is Old Tongue fragments, half-voiced.
    #        The one Aerenine line she speaks is: "I am here." That is the whole of her dialogue.
    # Aeron: One line. "I know." No interior monologue -- this is her scene.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - SHRINE ALCOVE - MORNING]
    # The morning after the restructuring. Before most of the base wakes.
    # A supply alcove off the medical corridor. Lyra has claimed it. The chaplains'
    # quarters on the upper levels are for priests with appointments. This is for her.

    #scene bg_shrine_alcove_ob_morning with dissolve
    #play ambient "sfx/ambient/base_pre_shift.ogg" fadein 2.0

    # ========== PHASE 1 -- THE POSITION ==========

    "The alcove is six feet deep and four feet wide. It used to hold fracture splints. Lyra moved the splints to the next alcove over and asked permission after."

    "The permission was given by a quartermaster who did not look at her when he said yes. She has noticed, in the last ten days, that fewer people look at her directly. She has not decided yet whether the problem is her or the base."

    "She kneels on a folded blanket. The blanket is grey. The concrete beneath it is colder than the blanket can remediate."

    "The candle is lit. She lit it an hour ago. The flame is steady. That is something."

    lthought "Begin."

    lthought "Begin the way you begin."

    "Her hands fold. Thumbs crossed, palms pressed. The Old Tongue opening -- the one she has said every morning since she was eleven years old."

    l "(under voice, Old Tongue) Aleth'i vorun. Sen'drah ilu veyn."

    lthought "The words come out."

    lthought "That is not the same as the words meaning."

    # ========== PHASE 2 -- THE FAILURE OF THE FIRST TOOL ==========

    "She waits. She waits for the thing that usually happens -- the small settling, the way the first line of the morning prayer usually drops into her like a stone into still water and makes a silence that the rest of the prayer fills."

    "The silence does not come."

    "The words drop. Nothing moves. The surface is already moving. The base ambient is louder than the candle. The ventilation does not hold still for her syllables."

    lthought "Try again."

    l "(under voice, Old Tongue) Aleth'i vorun."

    lthought "The syllables come out of my mouth like paperwork."

    lthought "Not metaphor. Actual paperwork. The intonation of a requisition form."

    lthought "The priest in the Academy said once that when the words become office work it is not the words that have failed. It is the person saying them."

    lthought "He said it gently. I do not think he meant it gently."

    "Her thumbs are white where they cross. She had not noticed the pressure."

    "She shifts. The buckle at her hip creaks. The Band is cinched one notch past the notch she usually uses. She tightened it before she knelt. She had not meant to tighten it. Her hand had done it while she was setting up the candle."

    lthought "The Band is not supposed to punish."

    lthought "It is supposed to hold what you have said you will hold. The cinch is the shape of the promise."

    lthought "A loose Band is not a broken Band. A loose Band is a Band for a day when the promise is light."

    lthought "I am not wearing it tight because the promise is heavy."

    lthought "I am wearing it tight because I need to feel it."

    lthought "That is not the same thing."

    # ========== PHASE 3 -- THE NAME IN HER MOUTH ==========

    "She tries a different opening. The one she has not used since she was a novice. The simplest."

    l "(under voice, Old Tongue) Yen sel adrun."

    lthought "I am before you."

    lthought "That was the first prayer I learned. I used to say it in the cathedral yard with the summer dust on my ankles. I said it because it was the shortest and I wanted to be allowed to go play."

    lthought "It worked then."

    "Her breath makes the candle flame bend once and recover."

    lthought "It is not working now."

    "She does not cry. She is past crying. She has cried in the last week until she began to recognize the crying as the part of the day she was most efficient at, and that recognition killed the crying. She cannot grieve a thing she has begun to manage."

    lthought "Say his name."

    lthought "Not in the prayer. In the place underneath the prayer."

    lthought "Aeron."

    "The name lands in the alcove. The candle does not notice. The ventilation does not notice. Only she notices, and she has been noticing it for months."

    lthought "Not the man in my bed."

    lthought "Not the man on the balcony."

    lthought "Not the one I am still holding -- the one I came here to save because I was the only one who knew the shape of what needed saving."

    lthought "The one I am sitting here now trying to ask the Six to intervene for."

    lthought "I cannot tell anymore whether I am saving him."

    lthought "I cannot tell anymore whether I am helping build him."

    # ========== PHASE 4 -- THE COUNT ==========

    "She lowers her hands from their clasp. Opens them. Looks at the palms as if they are a ledger."

    lthought "The Six do not weigh mercy."

    lthought "That is doctrine. I taught it to novices. The gods do not weigh. They count."

    lthought "A mercy counts as one. A cruelty counts as one. They do not have different densities. They do not have signs. The count is the count."

    lthought "What matters is what you are counting toward."

    "Her hands close again. Not in prayer. In fist."

    lthought "I have been counting for him."

    lthought "Every hour I stay here I am adding my count to his count. Every prayer I say in this alcove I am adding the weight of a priest's presence to what he is building. The Six do not care that my intention is to hold him steady."

    lthought "They count what I contribute."

    lthought "I am contributing."

    "Her jaw tightens once. Releases. She has not permitted herself to complete this thought before. She completes it now because the prayer has refused to distract her from it."

    lthought "If I leave him now, I am releasing him fully to Nyra."

    lthought "Nyra does not count. Nyra multiplies. Nyra's hand on him is not a priest's hand -- it is a lever's hand, and the lever moves and the thing it moves moves farther every day."

    lthought "If I leave, the lever is unopposed."

    lthought "If I stay, I am the sanctification of what he is doing."

    lthought "A priest at his side is not a neutral. A priest at his side is a blessing on the doctrine whether the priest speaks or not. The presence itself is the sermon."

    lthought "I know this."

    lthought "I have taught this."

    lthought "I am doing it."

    # ========== PHASE 5 -- THE SECOND ATTEMPT AT PRAYER ==========

    "She tries once more. She tries the prayer for discernment. It is the prayer you say when you cannot tell which thing you are doing. It is the prayer the cathedral made her say before she took her initial vows."

    l "(under voice, Old Tongue) Sel'anor thrun i vethai."

    lthought "Let my hand be clear."

    "She says it. She waits."

    lthought "My hand is not clear."

    lthought "That is the answer. The prayer does not lie. The prayer asks for the thing and the absence of the thing is the answer."

    "She looks at the candle. The candle is still steady. She has done nothing wrong to the candle. The failure is not in the shrine. The failure is in the mouth saying the words."

    lthought "I could get up."

    lthought "I could walk out of this alcove and past the medical corridor and up the stairs and out the north gate and into the sectors, and I could find Liora, and I could stand next to her refusal, and the count would change."

    lthought "The count would change."

    "Her hand goes to the buckle. Not to loosen. To check. She finds it cinched past comfort. She does not adjust it."

    lthought "Why didn't I leave?"

    lthought "The question does not go away. I have been trying to pray it away for an hour and it is still here."

    lthought "Because I love him."

    lthought "That is the first answer and it is the honest answer and it is the answer I no longer trust."

    lthought "Because I promised."

    lthought "That is the second answer and it is the priest's answer and it is the answer that has begun to sound like paperwork."

    lthought "Because I am afraid."

    lthought "That is the third answer and it is the new one and I have not let it sit in the room with me before."

    lthought "Afraid of which thing."

    lthought "Afraid that if I leave, I will discover that the woman who left was not saving him. She was the last handle of her own door. And when the door closes I will be outside it with nothing left to hold."

    "She does not move. The candle does not move. The alcove is holding still for her the way the prayer did not."

    # ========== PHASE 6 -- THE BODY TAKES OVER ==========

    "She bends forward. Not a bow. A fold. Her forehead toward the concrete, stopped an inch above it by the folded blanket."

    "The Band at her hip presses into her ribcage from the angle. She feels the cinch. She has been feeling it for an hour. She goes on feeling it."

    lthought "I cannot make the words hold."

    lthought "I can hold my body in the shape of the words."

    lthought "That is not nothing."

    lthought "It is not what the prayer is supposed to be."

    "She breathes. The breath is ragged for one cycle and then evens. The evenness is not peace. It is discipline."

    lthought "The priests in the old texts said the body prays when the mouth cannot. They meant it as consolation. I am using it as substitute."

    lthought "The substitute is a smaller thing than the original. I know that. I am using the smaller thing."

    # ========== PHASE 7 -- ARRIVAL ==========

    "Bootfall at the threshold. One set. The cadence she has learned to recognize by the specific hesitation in the second step -- the half-beat where he decides whether to come forward or stand."

    "This morning he comes forward."

    "He does not speak. He does not announce. He steps into the alcove and his shadow crosses the candle once and the flame recovers. He kneels beside her."

    "Not behind. Not in front. Beside. The position of someone who has understood the room."

    "She does not turn to him. She does not look up. Her forehead is still an inch above the blanket. The Band is still cinched."

    lthought "He is here."

    lthought "I did not call him. I did not send for him. He came."

    lthought "He has been doing this for four days now. Arriving at the alcove without being asked. Kneeling without being told to kneel. He does not pray with me. He does not say anything. He kneels."

    lthought "I do not know if he is here because he needs this."

    lthought "I do not know if he is here because he has seen that I need this."

    lthought "I do not know if he is here because it is tactically intelligent to be seen kneeling beside the priest."

    lthought "The three possibilities no longer feel different to me."

    "She reaches for his hand without looking. Her fingers find his palm. She does not grip. She takes."

    "He gives it. His hand is steady. Cooler than hers. He does not close his fingers around hers -- he lets her set the pressure. She sets a pressure and his hand meets it. Exactly meets it. No more. No less."

    lthought "He has gotten very good at this."

    lthought "Whatever this is."

    # ========== PHASE 8 -- THE BODY PRAYS ==========

    "She holds the position. Forehead above the blanket. Hand in his hand. The candle holding its flame. The ventilation carrying on its institutional work."

    "Her mouth does not move. The Old Tongue syllables are not coming. She has given up on asking them to come."

    "But her body is still in the shape."

    lthought "I am here."

    lthought "That is the whole of what I have to offer the Six this morning. Not the words. Not the doctrine. The fact of the body in the alcove, kneeling, with a Band cinched one notch past what it needs to be cinched, with a man beside me whose hand I am holding for reasons I can no longer fully name."

    lthought "I am here."

    lthought "Count that however you count it."

    "The silence extends. The base wakes around them. The morning shift begins to move through the medical corridor. Someone passes the alcove and does not look in. The lack of looking is a kind of privacy that this base has learned to give her. She is grateful for it. She is not sure she should be."

    lthought "The priest in me wants to feel held."

    lthought "The priest in me is not being held. The priest in me is holding."

    lthought "That is what the job is. I know that. I have always known that."

    lthought "The part I did not know -- the part I am learning this morning -- is that sometimes the thing you are holding is heavier than the arms you brought."

    # ========== PHASE 9 -- THE LINE ==========

    "She straightens. Slowly. Her forehead comes up from its near-contact with the blanket. Her hand is still in his. She does not look at him. She looks at the candle."

    "She speaks. In Aerenine, not Old Tongue. The single line she has been able to hold in her mouth since the prayer failed."

    l "I am here."

    "Three words. Quiet. Without emphasis. The statement of a position, not a feeling."

    menu:
        "Aeron does not turn to her. His hand stays in hers."

        "I know.":
            "Two words. The matching quiet."
        "Stay.":
            $ rel_bump("Lyra", affection=1)
            "One word. It is not a command. It is a request from the man's tense."
            lthought "He used the tense again. The one that costs him."
        "(Tighten his hand on hers, say nothing.)":
            $ rel_bump("Lyra", trust=1)
            "His fingers close a fraction. Not gripping. Acknowledging."
            lthought "He answered without speaking. The pressure is the sentence."

    "That is all. The two sentences sit in the alcove together. They do not arrange themselves into a dialogue. They are two pieces of acknowledgment from two people who are kneeling next to each other and do not fully know whether they are kneeling for the same thing."

    # ========== PHASE 10 -- THE NON-RESOLUTION ==========

    "She does not let go of his hand. She does not retighten her grip either. The pressure stays exactly where she set it."

    "She does not loosen the Band."

    lthought "I could loosen it now."

    lthought "He is here. The arrival could be the occasion. The body could relax by one notch and I could call the relaxation faith."

    lthought "I am not going to."

    lthought "The Band stays cinched because the thing it is cinched against has not changed. He is here this morning. That is the morning. It is not the answer."

    "Her free hand stays in her lap. She does not move it to the buckle to check. She has checked enough. She knows the buckle is where she put it."

    lthought "The prayer failed to produce words."

    lthought "The prayer did not fail to produce a position."

    lthought "A position is not nothing. A position is not everything. A position is what I have today."

    # ========== PHASE 11 -- HOLD ==========

    "They kneel. The candle holds. The base moves through its morning around them. Neither of them moves to end the scene."

    "Her thumb passes once across the back of his hand. Not a caress. An acknowledgment. The kind of gesture a person makes to confirm that the other person is still in the same coordinates."

    "His thumb does not reciprocate. He does not move his hand. He lets her gesture happen against his skin and does not answer it with a gesture of his own."

    lthought "He is not withholding."

    lthought "He is also not giving."

    lthought "He is here. The here is the whole transaction. I am going to have to decide in some other week whether the here is enough."

    "The candle draws down by a small measure. Wax runs once on the ration-tin rim and cools there."

    lthought "I am counting."

    lthought "I do not know yet what I am counting toward."

    lthought "I am counting anyway."

    # ========== PHASE 12 -- THE END THAT DOES NOT END ==========

    "She does not release his hand. He does not release hers. The scene ends the way the scene began: with the Band cinched, the candle lit, the prayer unfinished, and one more body in the alcove than there was at the start."

    "The final shot holds on her hand at her hip. Her thumb rests against the buckle. The buckle is tight. Her thumb does not move."

    "Fade, slow."

    #stop ambient fadeout 2.5
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Lyra", trust=0, conflict=1)
    $ tp_seed("a4.ob.lyra.rationalization_begins")
    $ canon_set("ob.lyra.band_cinched", True)
    $ flag("ob_lyra_prayer_failed_a4", True)
    $ flag("ob_lyra_body_substitutes_for_words", True)
    $ npc_remember("Lyra", "prayer_became_paperwork", tone="devotion_as_rationalization")
    $ npc_remember("Lyra", "band_cinched_past_comfort", tone="discipline_as_substitute")
    $ npc_remember("Aeron", "knelt_beside_her_without_speaking", tone="presence_without_content")
    $ metric("lyra_ob_rationalization_index", add=1)
    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s04_lyra_prays_alone_ob
# cann.chapter: IV -- Violence Normalized
# cann.path_tracking: OB
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Morning after a4_s02 restructuring. Parallel batch with zira state beat.
#   - Lyra has not slept. Before the morning shift has fully begun.
# cann.what_happened:
#   - Lyra in the shrine alcove she has claimed in the medical corridor.
#   - She cannot make the Old Tongue prayers hold. The syllables come out like paperwork.
#   - She catalogues her own position: priest at his side sanctifies his doctrine.
#   - "The Six do not weigh mercy. They count it. What am I counting toward."
#   - She arrives at the question: why didn't I leave? She names three answers:
#     love (no longer trusted), promise (sounds like paperwork), fear (new and honest).
#   - Body substitutes for prayer. She holds the shape she cannot fill with words.
#   - Aeron arrives without being asked. Kneels beside her. Does not speak.
#   - She reaches for his hand without looking. He gives it at exactly her pressure.
#   - She finally speaks one line: "I am here." He says: "I know." That is the dialogue.
#   - Non-resolution: the Band stays cinched past comfort. She does not loosen it.
# cann.aeron_state:
#   - Functionally silent. One line. He is learning to mirror her without feeling her.
#   - Three possible reasons for his presence -- she can no longer distinguish them.
# cann.lyra_state:
#   - Rationalization begins. Prayer as office work. Discipline substituting for faith.
#   - The Band cinched past comfort is the physical register of the rationalization.
# cann.path_tracking:
#   - rel_bump Lyra trust=0 conflict=1. tp_seed a4.ob.lyra.rationalization_begins.
#   - canon_set ob.lyra.band_cinched True.
# cann.thematic_flags:
#   - The prayer-as-paperwork image anchors her Act 4 deterioration.
#   - The Band as physical discipline substituting for absent faith.
#   - "Count that however you count it" -- the priest's language of ledgers.
#   - The two-shot kneeling with no contact beyond the held hand.
# cann.character_moments:
#   - Lyra: the three-answer inventory for why she stayed.
#   - The body substitute: position when the words fail.
#   - Aeron: presence without content. He arrives and kneels and does not give.
# cann.callbacks:
#   - a3_s13_proof_of_life_ob: "I felt you. I think." -- the qualifier growing.
#   - a3_s24_liora_ob: Liora walked. Lyra is the one who stayed.
#   - a4_s02 restructuring: the prior night that made this morning necessary.
# cann.block_status:
#   - ANCHOR (OB). State beat, no player choice.
# cann.requires_followup:
#   - The Band notch as a tracked canon marker. Future scenes register whether
#     Lyra ever loosens it. On OB, she does not.
#   - The prayer-as-paperwork image should recur when Lyra next attempts devotion.
#   - "I am here" / "I know" -- the sparsest possible exchange. The baseline they
#     are now maintaining. Future scenes can erode even this.
