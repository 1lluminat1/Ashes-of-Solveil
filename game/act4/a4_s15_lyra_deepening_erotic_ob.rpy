# =======================================================
# ACT 4 - Scene 15: Lyra Deepening Erotic (Obedience Path)
# File: a4_s15_lyra_deepening_erotic_ob.rpy
# Path: OB
# Type: LYRA EROTIC DEEPENING (OB)
# Character Focus: Lyra, Aeron
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s15_lyra_deepening_erotic_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s15_lyra_deepening_erotic_ob:


    # Gallery — unlock this scene in the character replay grid.
    $ gallery_unlock("a4_s15_lyra_deepening_erotic_ob")
    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm locked. OB register. Opens on the corridor outside Aeron's quarters.
    #         Lyra approaching from frame-left, measured pace. She has not come here
    #         unannounced since a3_s13. The camera tracks her only as far as the door
    #         and then locks. Door cycles. She enters. Interior: same geometry as
    #         a3_s13 (lamp still displaced to the corner, cot with hospital corners,
    #         desk squared). The room has become more institutional, not less.
    #         Two-shot, symmetrical, locked for the first conversation. Close-ups only
    #         on the buckle when she unbuckles the Band. Mid-shot when she sets it on
    #         the bedside table. The setting-down is a shot in itself.
    #         Consent gates: alternating close singles. Her eyes not searching tonight.
    #         His not recessed. Something has changed in both of them -- not softened.
    #         The fabric between them is thinner.
    #         Intimacy: the camera stays clinical. The compositions echo a3_s02 and
    #         a3_s13 but the light is different. Aftercare: wide two-shot, Lyra sitting
    #         up at the edge of the cot, re-buckling. He is on the cot behind her, not
    #         reaching. She is not looking at him. The final exchange happens with her
    #         back to him. She leaves through the door she entered. The camera stays
    #         in the quarters after she is gone. Holds on the empty half of the cot.
    # LIGHTING: The lamp in the far corner (moved in a3_s13, still moved). 3200K amber,
    #           reach shorter than in a3_s02, the amber barely touching the cot.
    #           Cold 5000K overhead. Blue-white city-glow through the reinforced window.
    #           During intimacy: blue dominant, amber almost absent. The setting
    #           continues a3_s13's palette, but the absence of the amber is more total.
    #           Aftercare: overhead off, lamp off. Only the city glow. The room is nearly
    #           dark. The Band re-buckling happens by touch, not sight.
    # SFX: Loop -- quarters ambient. Ventilation. Distant base machinery.
    #      One-shots -- door hiss, fabric, buckle-leather (the Band coming off),
    #       the set-down on the bedside table (ceramic-on-wood contact, single beat),
    #       breathing out of sync (her slightly faster, his slightly slower),
    #       the re-buckle (same leather, different cadence -- slower, deliberate).
    # FX/COMP: The bedside table is metal. The Band setting-down sound is specific.
    #          When she re-buckles it, the camera notes the ring mark left on the metal.
    #          She does not wipe the mark. It stays.
    # BLOCKING: Lyra enters. Aeron is at the desk, not the window (different from a3_s13).
    #           He turns when she enters. He does not rise. She crosses to him. They
    #           speak the first exchange with him seated, her standing. Then he stands.
    #           The consent gate happens in the two-shot, both standing, near the cot.
    #           The unbuckling: she steps back by one pace to do it. Her hands are
    #           steady. She sets the Band on the bedside table. The set-down is clean.
    #           Then she turns back to him. The consent choice is made.
    #           Intimacy marker follows the consent gate.
    #           Aftercare: cot. Lyra sitting up, legs over the side, back to him.
    #           She reaches for the Band on the bedside table. Re-buckles it by feel.
    #           She does not turn to say her closing line. She speaks with her back to him.
    #           She stands. She walks to the door. The door cycles. She is gone.
    #           Camera holds on the quarters after her departure. Aeron does not move.
    # CANON: LYRA EROTIC DEEPENING (OB). The most devastating version of her devotion.
    #        The physical companion to "being in the room with it" from a4_s14.
    #        She chooses to come. She chooses the unbuckling. She re-buckles before leaving.
    #        She does not stay the night. The not-staying is the scene's thesis.
    #        Aftercare is cold because the devotion is rationalization made flesh.
    #        The consent is explicit. The emotional register is dread, power, compulsion.
    # CONSENT: 3-gate framework. OB-mode choices. Three options all lead to intimate marker.
    #          The third (the "scared of what we are making") is shortest, quietest, most
    #          mournful. All three are valid. None are healing.
    # FACE: Lyra -- composed in the way she was composed in the muster bay. Priest-grade
    #        composure. The composure a professional wears over a decision she has made
    #        before arriving. She is not broken tonight. She is clear.
    #        Aeron -- more present than he has been in months. This is dangerous. His
    #        presence is selective. He can give her presence tonight because presence
    #        is tactically useful to the shape of the thing they are making together.
    #        Neither of them would say the sentence that way.

    # ========= VOICE BASELINE =========
    # Lyra: Lthought throughout, but less than a4_s04 and a4_s14. She has done the
    #        interior work in those scenes. Tonight she acts. The spoken lines carry
    #        more weight than the interior.
    # Aeron: Economic. He speaks more in this scene than in a4_s14 because Lyra is
    #        giving him something and the giving requires a ledger of acknowledgments.
    #        His spoken register is quieter than in earlier OB scenes. Not softer --
    #        quieter. He is aware that volume would be wrong in this room tonight.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - AERON'S QUARTERS - NIGHT]
    # Same night as a4_s14. After the muster bay. After the rest of Lyra's day --
    # whatever administrative work she did with the count of one departure blessing
    # sitting under her ribs. She has been deciding since the afternoon whether to
    # come here. She decided in the last forty minutes. She did not pack. She did not
    # prepare. She walked.

    #scene bg_aeron_quarters_ob_night with dissolve
    #play ambient "sfx/ambient/quarters_cold_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE ARRIVAL ==========

    "The corridor outside Aeron's quarters is empty. It is late enough that night watch is the only traffic on this level. Her boots on the deck plating are the only sound."

    lthought "I am walking toward a decision I have already made."

    lthought "The walking is the last place the decision can be reversed. In the muster bay this morning I named the position and then I held the position and then I did my afternoon work with the position held. Now I am making the body do what the position requires."

    lthought "The body has to do something. If the body does nothing then the mouth's doctrine is only a sentence. If the body does something then the doctrine is a practice."

    lthought "A practice is what the priests in the old texts call it when you have committed to a theology with your calendar instead of your tongue."

    "She stops at his door. The door is not coded to her. She has to signal. She raises her hand to the panel and pauses for one breath before she presses it."

    lthought "The breath is mine."

    "She presses."

    # ========== PHASE 2 -- HE OPENS ==========

    "The door cycles. Aeron is at the desk. He was working. The tablet is still in his hand. He turns his head when she enters -- not his body. Just the head. The tablet stays up."

    "She crosses the threshold. The door cycles shut behind her."

    "He sets the tablet down on the desk. Face-down. Screen off. The action is deliberate. He is saying with his hands that the document is not going to be read while she is in the room."

    a "You came."

    "Two words. He is not asking. He is acknowledging."

    l "I came."

    "She moves farther in. Stops three paces from the desk. The overhead light catches her vestments, the clean line of the collar, the curve of the Band at her hip."

    lthought "He is looking at the Band."

    lthought "He has not asked about the notch. He has not remarked that I have not loosened it in three days. He is noticing. That is all."

    "He rises from the desk. Slowly. The precision of his movements has a register she did not have a name for until today -- when he asked her 'is this all right' in the muster bay and she heard the Marcus cadence in it. That same register is in his standing up now."

    lthought "He is using the cadence of a man who knows exactly what the room requires and is going to supply exactly that, no more, no less."

    lthought "I am the room tonight. He is reading me and supplying."

    lthought "I know this. I am going to participate in it anyway. That is the whole shape of the position I am holding."

    # ========== PHASE 3 -- THE OPENING LINE ==========

    "She does not wait for him to speak next. She speaks. She has prepared this sentence -- not the wording, but the thing it is for. The wording comes as she opens her mouth."

    l "I came because I do not want you to think I am the kind of woman who blesses you in public and leaves you alone in private."

    "She says it evenly. No heat. No plea. The statement of a position, the way she said 'I am here' in the shrine alcove."

    "Aeron registers the sentence. His face does not change by much. But there is a small adjustment around the eyes -- a slow-drawer moment, the kind she recognized in the muster bay earlier today."

    lthought "That sentence just went into the drawer."

    lthought "He will take it out. I do not know when."

    a "You do not owe me this."

    "Quiet. Said without defense. Not pushing her away. Naming an accounting question so that her answer is on the record."

    lthought "He is giving me the off-ramp for the second time today."

    lthought "This morning it was 'you could refuse.' Tonight it is 'you do not owe me this.' They are the same sentence said twice. He is making sure, in both directions, that I am not here because I think I have to be."

    lthought "He is more honest tonight than he has been in a month."

    lthought "The honesty is also a tactic. I do not know how much of it is which."

    lthought "I am going to answer both the honesty and the tactic with the same answer, because the answer is the same."

    l "I am not coming because I owe it."

    "She steps one pace closer. Still out of arm's reach. The distance is a choice."

    l "I am coming because my body is the last place I can pray honestly."

    "The sentence sits in the room. She did not rehearse it. It came from the same interior place as the 'go, and come back' this morning -- the place where her theology is making itself in real time out of materials she did not plan to use."

    lthought "I said it out loud."

    lthought "I have been circling that sentence for two weeks. The sentence is accurate. The sentence is also indicting."

    lthought "A priest whose mouth has stopped working has to find another organ to pray with. That is orthodox. The old texts call it the body-prayer. The body-prayer is supposed to be an emergency substitute. I am turning it into a weekly practice."

    lthought "I am not going to call it weekly. Not yet. I am going to call it tonight and see what tomorrow makes me call it."

    # ========== PHASE 4 -- HE RECEIVES ==========

    "Aeron does not respond immediately. When he does, his voice is lower than it was before she came in. He has dropped the register a half-step."

    a "Lyra."

    "Just her name. No sentence attached. The name delivered as acknowledgment -- the way a person acknowledges that they have heard and understood a sentence they were not expecting and do not yet have language for."

    lthought "He said my name the way he used to say it on the balcony."

    lthought "He did not. That is me hearing what I want to hear. He said my name the way he says my name in Act 4. The two cadences are not the same and the part of me that wants them to be the same is the part of me that came here tonight."

    lthought "I am going to let the wanting and the knowing coexist. That is the whole condition I am in. That is the whole scene."

    "She takes the second step. Now she is within arm's reach. She does not reach. Neither does he. The distance is two feet and the two feet are a held line."

    # ========== PHASE 5 -- THE UNBUCKLING ==========

    "She steps back by one pace."

    "The step back is not retreat. It is the amount of room her hands need to work. She lowers her gaze to her own hip. Her fingers find the buckle."

    lthought "I have not unbuckled it in Act 4."

    lthought "Not in the alcove. Not in the muster bay. Not in any of the four days Aeron has knelt beside me without speaking."

    lthought "I am unbuckling it now."

    "Her thumb finds the tongue of the buckle. Lifts. The leather slides free of the ring. The cinch releases by one notch, then by the rest. The Band comes open."

    lthought "The Band at my hip is falling away from me."

    lthought "I can feel the space where it was. The ribcage remembers. The cinched-past-comfort notch has left a small impression in the fabric of my vestment underneath. I am going to feel that impression for an hour."

    "Her hand holds the Band loose. She steps sideways to the bedside table. The bedside table is metal -- a slab of base-issue utility furniture. She sets the Band down on it."

    lthought "The set-down is the part that matters."

    "The ceramic-on-wood sound of a thing being placed with deliberation. One beat. The Band sits on the metal. Its leather curved. Its buckle catching the blue window-light."

    lthought "I did not unbuckle it as a gift tonight. That is important. In the EMP path -- the path my life is not on -- I would have said his name. His real name. And the giving would have been sacrament."

    lthought "This is not sacrament. This is surrender."

    lthought "I am not giving him the Band. I am taking it off because I cannot bring the Band into the thing I am about to do without the Band becoming the witness to the thing. The Band is a witness I do not want in this room tonight. So I am setting it aside. Not because it is too holy for this. Because it is too honest."

    lthought "The Band on the metal table is going to see what I do from across the room and I am going to put it back on before I leave."

    lthought "That is the shape of the scene."

    "She turns back to Aeron. The Band is now behind her, on the table, at the edge of her peripheral vision."

    # ========== PHASE 6 -- THE DECLARATION ==========

    "He has not moved since she stepped back to unbuckle. His eyes are on her. Not on the Band -- on her face. He has been giving her the privacy of his attention for the last forty seconds without moving a muscle."

    lthought "He has gotten very good at being watched at."

    lthought "He was not good at this on the balcony. He was good at looking at me and then looking away. Now he has learned to let me be looked at without my feeling like an object of study. He is doing that deliberately. I know he is doing it deliberately. The knowledge does not ruin the doing."

    "She speaks. The sentence she prepared on the walk."

    l "I am not a vessel tonight."

    "She lets it sit for one beat."

    l "I am a woman who is still trying to recognize you."

    "The word 'recognize' lands in the room. The priest's word. The theological word -- the word the liturgy uses when it says the Six recognize the worthy. She has used it deliberately. She is refusing to let the word stay in its theological frame. She is bringing it down to a woman and a man in a quarters."

    lthought "Recognition is what the old prayer asks the Six to do. 'Let my face be known to you.' I have said that prayer since I was a novice. Tonight I am saying it to Aeron instead of the Six."

    lthought "The substitution is either heresy or the most honest prayer I have ever made. I am not going to decide which one it is tonight. Tonight I am going to do the substitution and see which one it turns out to be in the morning."

    # ========== PHASE 7 -- CONSENT GATE (THREE OPTIONS) ==========

    "He closes the last of the distance. His hand rises -- not to take her, to ask. The hand is between them, palm half-open, at the level of her sternum. The gesture is the same offered-hand as in the muster bay this morning."

    a "Tell me what you need."

    "Quiet. Not a demand. A setting of terms. He is asking her to name the condition she is requesting him under."

    lthought "He is asking the consent question in the language of the muster bay. Same register. Same precision. Same refusal to assume."

    lthought "I have three things I could say. I can feel all three of them in my mouth at once."

    menu:
        "His hand is between us. The Band is on the table behind me. The room is waiting for the sentence I am going to choose."

        "Stay. Recognize me.":
            $ choice_and_dev(
                _current_scene_id, "_recognize", "OB", factor=1,
                next_scene_label=None,
                note="OB: direct request for recognition. The priest's word brought to the bed."
            )
            jump .path_recognize

        "I don't know if I can be recognized right now.":
            $ choice_and_dev(
                _current_scene_id, "_unrecognized", "OB", factor=0,
                next_scene_label=None,
                note="OB: the honest doubt. She comes anyway. She names the doubt as the condition."
            )
            jump .path_unrecognized

        "I want you here but I am scared of what we are making together.":
            $ choice_and_dev(
                _current_scene_id, "_afraid", "OB", factor=0,
                next_scene_label=None,
                note="OB: shortest, quietest, most mournful. She names the fear out loud."
            )
            jump .path_afraid

    # ========== PHASE 8A -- PATH: RECOGNIZE ==========
    label .path_recognize:

        l "Stay."

        "A pause. One breath. The word she has said to him in this room twice before, in a3_s02 and a3_s13. Tonight it is the third time. The third time is different. Tonight she is the one saying it to him in his quarters; tonight it is the one who is requesting, not the one who is permitting."

        l "Recognize me."

        lthought "I said it. The priest's word. I took it out of the cathedral and I put it on this cot."

        "Aeron's hand is still between them. He closes it gently around her hand -- her hand that is still at her side, palm half-open. His fingers find hers and do not squeeze. He matches her pressure the way he did in the alcove. But this time he also turns her palm up in his."

        "The gesture is a reading. He is looking at her hand as if he is going to find the thing she asked him to find in the lines of it."

        a "I will try."

        "Not a promise. Not a guarantee. A declaration of effort. He is not going to lie to her about what he can give. She has asked for something larger than he has been able to give for weeks. He is not going to refuse. He is going to try."

        lthought "Try. He said try."

        lthought "Try is what he has been doing since the first time I came to this room on the night of Selene's funeral. Try is the word that has been underneath every one of our scenes together. Try is the honest word and it is not the same as the word I asked for. I asked for recognize. He heard the ask and answered with try."

        lthought "I am going to take 'try' as the answer. Try is the version of this that does not require him to lie to me. I would rather have try than a performance of recognition."

        lthought "That is the smallest positive thing I can say about my position."

        "She closes the last of the distance. Her forehead touches his. Her free hand rises to his jaw. Her fingers are cold."

        l "Thank you for trying."

        a "Do not thank me yet."

        "A small warning. He is telling her not to mistake the attempt for the result. She hears it."

        l "I know."

        "She kisses him."

        $ flag("ob_lyra_deepening_recognize", True)
        jump .intimate_marker

    # ========== PHASE 8B -- PATH: UNRECOGNIZED ==========
    label .path_unrecognized:

        l "I don't know if I can be recognized right now."

        "Flat. Not quite broken. The honest version of the sentence she could have said instead."

        lthought "I gave him the shape of my doubt. I did not lie about what I am holding in my mouth tonight."

        "Aeron does not pull back. His hand is still extended. He takes the weight of what she just said with the slow-drawer look -- not acceptance, not rejection, a filing of the information."

        a "Then I will not try to recognize you."

        "A beat."

        a "I will be in the room with you."

        lthought "He used my sentence."

        lthought "He used the sentence I said in the muster bay this morning. 'Being in the room with it.' He has been carrying the sentence since I said it. He has pulled it out of the slow drawer already. That is fast for him."

        lthought "He is offering me the thing I told him I was offering him. He is mirroring it. That is either the deepest intimacy we have had in months or the most precise tactical adjustment he has ever made on my behalf."

        lthought "I think -- and the thinking is uncertain -- that tonight it is both."

        "She steps into him. Her forehead to his. Her breathing uneven for the first time tonight."

        l "Be in the room with me."

        a "I am."

        "She kisses him. The kiss is slower than the kiss on the balcony. The kiss of two people who are not sure what they are doing and have agreed to do it together anyway."

        $ flag("ob_lyra_deepening_unrecognized", True)
        jump .intimate_marker

    # ========== PHASE 8C -- PATH: AFRAID ==========
    label .path_afraid:

        l "I want you here."

        "She stops. Her breath catches once. She makes it keep going."

        l "But I am scared of what we are making together."

        "The smallest sentence of the three. Quiet. Almost unvoiced. The sentence she has been keeping away from him for two weeks because saying it aloud would require her to look at it."

        lthought "I said it."

        lthought "I did not say it the way the other two would have said it. The Stay-and-Recognize Lyra would have said it as a request. The I-Don't-Know Lyra would have said it as an admission. I said it as a fear."

        lthought "Fear is the one the priest trained me not to bring into a room. The old texts say fear is what the devoted leave at the threshold. You do not carry your fear into a sacred space. You carry your devotion in and your fear out."

        lthought "I am not at a threshold. I am already inside the room. The fear is in the room with me."

        "Aeron's hand has not dropped. His voice has not risen."

        a "I know."

        "Two words. The same two words he said in the shrine alcove when she said 'I am here.' The echo is deliberate. He is telling her with the repetition that this exchange is the same exchange they had this morning in a different room. The echo is also a kindness -- the smallest, quietest kindness he knows how to give."

        lthought "He said 'I know.'"

        lthought "He did not say 'I am scared too.' He did not say 'do not be scared.' He did not say 'I will protect you from what we are making.' He said I know."

        lthought "That is the honest answer. That is also the answer that does not comfort me."

        lthought "I came here knowing I would not be comforted. Comfort is not what this scene is for. I am doing a body-prayer in a form that refuses comfort. The refusal is the theology."

        "She steps into him. Not fast. The way a person enters cold water. She puts her face against his collarbone. Her breath against his throat."

        a "(quieter) I am here."

        "The sentence she said. Said back to her. The smallest possible exchange. The baseline they are now maintaining."

        "She turns her face up. She kisses him once. Briefly. A kiss that is more acknowledgment than invitation."

        l "(against his mouth) Tonight."

        "One word. It is enough. It is the whole of what she can offer."

        $ flag("ob_lyra_deepening_afraid", True)
        jump .intimate_marker

    # ========== PHASE 9 -- INTIMATE MARKER ==========
    label .intimate_marker:

        # [INTIMATE CONTENT HERE]
        #
        # OB TONE NOTES FOR THE INTIMATE CONTENT THE USER WILL WRITE:
        # - This is the third Lyra intimacy on the OB path (after a3_s02 and a3_s13).
        # - The register is compulsive, rationalized, honest-but-cold. NOT tender.
        # - Her rhythm is slower than a3_s13. His is measured. They are closer to in-sync
        #   than in a3_s13, which is the devastating part: they have adapted to each other's
        #   disregulation. The new sync is not harmony -- it is mutual adaptation to the gap.
        # - She is doing a body-prayer. She is praying with her body because her mouth
        #   has stopped working. The scene should feel like a liturgy that refuses
        #   its own comfort.
        # - He is present. More present than a3_s13. The presence is selective and
        #   slightly tactical. Neither of them names this.
        # - No tender aftercare touches during. No soft vocalizations. If she says his
        #   name, she says it the way she said 'I am here' -- as the statement of a position.

    # ========== PHASE 10 -- AFTERCARE (COLD) ==========

    # VISUAL: After. The lamp is off. The overhead is off. Only city-glow through the window.
    # Lyra sitting up at the edge of the cot. Legs over the side. Bare feet on the cold deck.
    # Her back to Aeron. He is on the cot behind her. He does not touch her. He does not
    # reach for her. He lets her sit up and be sat up.

    "The window light is the only light. The base is quiet at this hour in the way the base is never quite quiet -- the ventilation goes on. The generator hum goes on. The distant machinery of the regime continues to do its work while Lyra sits on the edge of the cot with her back to the man she has just come to."

    lthought "I am awake."

    lthought "A3-s02 Lyra fell asleep on his chest that first night. A3-s13 Lyra cried against him and then slept. A4 Lyra is sitting up."

    lthought "The sitting up is the difference. The sitting up is the canon marker. I am the woman who sat up after."

    "She does not speak. She does not look at him. Her eyes find the bedside table. The metal slab. The Band lying on it. The curve of the leather catching the blue light."

    lthought "There it is."

    lthought "I have to put it back on before I leave."

    "Her hand reaches for the Band. She does not turn. She lifts it off the metal by feel. The leather is cool. It has been off her hip for -- she does not know how long. The time in the intimate phase has no clock attached to it for her. The body-prayer has no minute-hand."

    lthought "The Band is in my hand again."

    "She brings it to her hip. The fabric of her vestment is disturbed. She finds the loop with her thumb. Threads the Band through. Her fingers know this motion. She has done it tens of thousands of times since she was eleven years old."

    lthought "Re-buckle."

    "The leather through the ring. The tongue seated. She does not cinch it to the a4_s04 notch immediately. She cinches it first to her normal notch -- the day notch, the one she wore before the prayer-alcove morning."

    "Then she tightens it one more."

    lthought "Back to the cinched-past notch."

    lthought "The day notch was not enough tonight. The day notch is not my condition. My condition is the past-comfort notch, and I am going to go back to wearing my condition, because what I just did with my body does not change my condition. It was the body-prayer for the condition. The prayer does not resolve the condition. The prayer is how you stay inside the condition without being destroyed by it."

    "She tightens. The leather creaks once. The sound is audible in the quiet of the quarters."

    "Aeron hears it. He does not comment on it. He does not ask her to loosen it. He does not ask why she is putting it back on before she leaves, which is the question a man who did not understand the scene would ask."

    lthought "He understood the scene."

    lthought "I should have expected him to understand. He has been good at understanding geometry since the muster bay this morning. It is one of the things he has inherited from Marcus. Marcus could see the shape of a room the way a surveyor sees a map."

    lthought "Aeron is seeing the shape of tonight."

    # ========== PHASE 11 -- THE CLOSING LINE ==========

    "She does not turn. She speaks with her back to him. Her hands are still at the buckle, confirming the cinch by touch."

    l "I do not know if I am helping you."

    "She lets the sentence sit. She has the right cadence tonight. The cadence of the shrine alcove. Not fast. Not dramatic. The voice of a priest making a record."

    l "I know I am not abandoning you."

    "One beat."

    l "Tonight that is what I have."

    "The record complete. Three sentences. She has not asked him anything. She has not required him to respond. She has laid down a position the way she laid the Band down on the metal table."

    "Aeron does respond. His voice is quieter than it was before the consent gate. Quieter still than during the intimate phase. The quietness is not weakness. It is the voice of a man who knows that what she just said is load-bearing and that his response is going to carry the weight she has asked it to carry."

    a "Tonight it is enough."

    "Three words. Matched to her three sentences. The response she asked for, in the register she asked for it in."

    "The sentence is hollow."

    "Both of them hear the hollowness."

    lthought "He said 'tonight it is enough' and neither of us believes it."

    lthought "That is what we have tonight. We have the sentence and the shared awareness that the sentence is not true. That is more than we have had in a month. The shared awareness is also the scene. The shared awareness is the thing I came here to make with him."

    lthought "I came to make a thing with him in which neither of us was lying to each other about the shape of it."

    lthought "We have made that thing. It is cold. It is honest. It is a lie that both of us know is a lie and are agreeing to hold together for tonight."

    lthought "That is what the position produces. That is what being in the room with it looks like at the level of the body."

    lthought "I am not going to stay the night."

    # ========== PHASE 12 -- SHE LEAVES ==========

    "She stands. Her hand drops from the buckle. She has not turned to look at him since the Band went back on. She is not going to turn now. The not-turning is also a record."

    lthought "If I turn, I will see his face. If I see his face, I will have to decide whether the face I am seeing is the one from the balcony or the one from tonight. I have already decided that I cannot tell the difference anymore. I am not going to force the question on myself by looking."

    lthought "I am going to walk to the door."

    "She walks to the door. Her vestments are settled. The Band is in place. She is composed the way she was composed when she walked into the muster bay this morning. The composure is the professional layer. Under the composure she is a woman who just came to a man in the dark and is walking out of his quarters without saying another word."

    "At the door, she stops. One hand on the panel. She does not turn."

    l "I will be back."

    "Four words. Not a promise. Not a threat. A scheduling note."

    lthought "I am telling him I will come back. I am also telling myself. The record requires me to name the continuity. If I leave without saying it, the scene becomes a thing I did once and ran from. If I leave saying it, the scene becomes a practice."

    lthought "I am choosing practice."

    lthought "The priests in the histories who stayed -- I am being one of them now. I am not the one who told herself the story and was wrong yet. I may become her. Tonight I am the one who is still saying the sentence and meaning it."

    "Aeron answers. From the cot. She hears his voice but does not see his face."

    a "I will be here."

    "Two words. The smallest possible confirmation of the scheduling note. He is not asking her to stay longer tonight. He is not asking her to come sooner next time. He is confirming the geometry."

    "She presses the door panel."

    "The door cycles."

    "She steps through."

    "The door cycles shut behind her."

    # ========== PHASE 13 -- THE ROOM AFTER ==========

    # VISUAL: Camera holds on the quarters. Aeron on the cot. He does not move.
    # The Band is gone from the bedside table. The metal slab has a faint ring mark
    # where the buckle rested. The mark is small. It will fade. It has not faded yet.

    "The quarters are empty except for him. The cot is disordered on the side where she was. The blanket is pushed aside. The city-glow through the window is steady."

    "Aeron does not rise. He does not turn his head to the door. He looks at the bedside table."

    "There is a ring mark on the metal where the Band rested. The buckle left a shape. The shape is small. It is going to fade within the hour. It has not faded yet."

    athought "She left the mark."

    athought "She did not wipe it."

    athought "The mark is the shape of the buckle of a Band that has been on her hip for every day of the month except for the thirty-eight minutes she spent in this room."

    athought "I am going to leave the mark there. I am not going to touch it. It will fade on its own."

    athought "Tomorrow she will come back. The day after, she will come back. If she keeps coming back, the metal will learn the shape and the ring will stop fading. That is how it works with objects and with pressure."

    athought "I do not know if that will happen."

    athought "I know that what happened tonight was not what she deserved. I know that what happened tonight was what she asked for. I know that those two sentences being both true is the condition we are in."

    athought "Tonight it is enough."

    athought "It is not enough."

    athought "Both of those sentences are true."

    athought "The slow drawer is going to hold them next to each other until something happens that changes which one is load-bearing."

    # ========== PHASE 14 -- HOLD ==========

    "The quarters hold. The window holds. The ring mark on the metal holds for another minute and then begins, imperceptibly, to fade."

    "Fade, slow."

    #stop ambient fadeout 2.5
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Lyra", trust=1, attraction=1)
    $ canon_set("ob.lyra.rebuckle_before_leaving", True)
    $ tp_seed("a4.ob.lyra.recognize_you")
    $ flag("ob_lyra_erotic_deepening_a4", True)
    $ flag("ob_lyra_did_not_stay_the_night", True)
    $ flag("ob_lyra_body_as_prayer_practice", True)
    $ metric("lyra_intimacy_level", set_to=max(metric("lyra_intimacy_level"), 3))
    $ metric("lyra_ob_rationalization_index", add=1)
    $ npc_remember("Lyra", "body_is_the_last_place_she_can_pray_honestly", tone="devotion_as_rationalization_made_flesh")
    $ npc_remember("Lyra", "rebuckled_the_band_before_leaving", tone="ritual_over_rest")
    $ npc_remember("Lyra", "said_i_will_be_back_and_meant_practice", tone="scheduling_the_position")
    $ npc_remember("Aeron", "told_her_tonight_it_is_enough_and_heard_the_hollow", tone="shared_awareness_of_the_lie")
    $ npc_remember("Aeron", "saw_the_ring_mark_on_the_metal", tone="object_witness")
    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s15_lyra_deepening_erotic_ob
# cann.chapter: IV -- Violence Normalized
# cann.path_tracking: OB
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Same night as a4_s14 (muster bay blessing). Late night.
#   - After Lyra's afternoon administrative work with the count of the departure
#     blessing under her ribs. She decided in the last forty minutes to come.
# cann.what_happened:
#   - Lyra arrives at Aeron's quarters unannounced for the first time in a4.
#   - Opening line: "I came because I do not want you to think I am the kind of woman
#     who blesses you in public and leaves you alone in private."
#   - He names the off-ramp: "You do not owe me this." (Echoes "you could refuse"
#     from the muster bay this morning. Second time today.)
#   - She answers: "I am not coming because I owe it. I am coming because my body
#     is the last place I can pray honestly."
#   - The unbuckling: she unbuckles the Band and sets it on the metal bedside table.
#     Not as gift (contrast EMP path unbuckling as sacrament). As surrender.
#   - She names the position: "I am not a vessel tonight. I am a woman who is still
#     trying to recognize you."
#   - Consent gate -- three OB-mode options:
#     1. "Stay. Recognize me." -- direct request. He answers "I will try."
#     2. "I don't know if I can be recognized right now." -- honest doubt.
#        He answers using her sentence back: "I will be in the room with you."
#     3. "I want you here but I am scared of what we are making together."
#        -- shortest, quietest, most mournful. He answers "I know."
#   - All three lead to [INTIMATE CONTENT HERE] marker. OB tone notes in-file.
#   - Aftercare: COLD. Lyra sits up, does not stay on him. Back to him.
#     Reaches for the Band. Re-buckles by feel. Cinches to the day notch, then
#     tightens one more to the past-comfort notch.
#   - Closing exchange: "I do not know if I am helping you. I know I am not
#     abandoning you. Tonight that is what I have." / "Tonight it is enough."
#     -- The line is hollow. Both of them hear it.
#   - She does not stay the night. She walks to the door.
#   - Scheduling note at the door: "I will be back." / "I will be here."
#   - Camera holds on the empty quarters after she leaves. Aeron sees the ring
#     mark the Band left on the metal bedside table. He does not wipe it.
# cann.aeron_state:
#   - More present than in a3_s13. The presence is selective and tactically aware
#     of what the room requires. He has already pulled "being in the room with it"
#     out of the slow drawer and offered it back to her.
#   - He hears the hollowness of his own closing line. He says it anyway because
#     it is the answer Lyra asked for in the register she asked for it in.
#   - The ring mark moment: the first tender/devastating interior he has permitted
#     himself in weeks. Object-witness. He leaves the mark. He will not wipe it.
# cann.lyra_state:
#   - Devotion as rationalization made flesh. The physical companion to her muster
#     bay doctrine of "being in the room with it."
#   - The body-prayer as practice -- she knows this is becoming a weekly thing.
#     She is refusing to name it as weekly tonight.
#   - Band re-buckled before leaving -- ritual over rest. The cinched-past-comfort
#     notch is her condition, and the body-prayer does not change the condition.
#   - She does not stay the night. The not-staying is the scene's thesis.
# cann.path_tracking:
#   - rel_bump Lyra trust=1 attraction=1.
#   - canon_set ob.lyra.rebuckle_before_leaving True.
#   - tp_seed a4.ob.lyra.recognize_you.
#   - lyra_intimacy_level = 3 (previously 2 in a3_s13).
# cann.thematic_flags:
#   - The unbuckling as surrender, not sacrament. Explicit contrast to EMP path.
#   - The metal bedside table as the place where the Band rests while she prays
#     with her body. The Band as witness. She sets it aside because it is too
#     honest to bring into the thing she is about to do.
#   - The ring mark on the metal. Object witness. He does not wipe it.
#   - The three consent options -- all valid, none healing. Third is shortest,
#     quietest, most mournful. First is the priest's word (recognize) brought down
#     to the bed. Second is the honest doubt. Third is the fear she has been
#     keeping away from the room.
#   - "I will try" -- Aeron's answer to recognize me. Not a promise. Not a lie.
#   - "I will be in the room with you" -- Aeron using Lyra's sentence back.
#     Mirroring raised to intimacy. Devastating because it is precise.
#   - "I know" -- his answer to the fear. The same two words from a4_s14.
#     The baseline they are maintaining.
# cann.character_moments:
#   - Lyra: opening line, the unbuckling, the vessel sentence, the consent choice,
#     the re-buckling, the three-sentence record, "I will be back."
#   - Aeron: "You do not owe me this," "I will try" / "I will be in the room with
#     you" / "I know," the hollow "Tonight it is enough," the ring mark moment.
# cann.callbacks:
#   - a3_s02_stay_with_me_ob (first intimacy -- falls asleep on his chest).
#   - a3_s13_proof_of_life_ob (deepening -- cried against him, "I felt you. I think.").
#   - a4_s04_lyra_prays_alone_ob (Band cinched past comfort, "I am here").
#   - a4_s14_lyra_sanctifying_violence_ob (being in the room with it, muster bay).
#   - EMP a4_s04 (unbuckling as sacrament with "Anayet" -- explicit contrast).
# cann.block_status:
#   - VARIANT (three consent paths, all lead to marker). Lyra deepening Act 4 OB.
# cann.requires_followup:
#   - The Band re-buckling before leaving is a tracked canon marker.
#     Future Lyra OB scenes register whether she ever stays the night. In OB, she
#     may not. The not-staying is the deterioration signal.
#   - The ring mark on the metal table -- object-witness Aeron noticed. Should
#     recur when he next looks at the bedside table (target: a4 late or a5).
#   - "I will try" -- Aeron's promise to try to recognize her. Tracked variable
#     for whether he makes progress or loses the capacity entirely.
#   - "My body is the last place I can pray honestly" -- the line is the thesis
#     of Lyra's Act 4 arc. Should echo in late Act 4 when the body-prayer either
#     holds or fails.
#   - The lyra_ob_rationalization_index metric now incremented twice in one day
#     (a4_s14 and a4_s15). The climb is steep. Endgame variable.
