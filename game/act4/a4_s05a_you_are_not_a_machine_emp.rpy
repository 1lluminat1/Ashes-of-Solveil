# =======================================================
# ACT 4 - Scene 05a: You Are Not a Machine (Empathy Path)
# File: a4_s05a_you_are_not_a_machine_emp.rpy
# Type: TESSA INTIMACY BEAT — forced rest
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s05a_you_are_not_a_machine_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s05a_you_are_not_a_machine_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Three acts of blocking.
    #         (1) Corridor: handheld, tight. Aeron walking. Tessa steps into frame
    #             from the edge — she does not enter the shot, the shot finds her
    #             because she has stopped moving. Over-the-shoulder through the
    #             argument. When she puts her hand on his forearm, the camera finds
    #             the hand and holds.
    #         (2) Medbay: 50mm, still. Tessa's hands are the subject. Aeron is mostly
    #             off-frame — the medbay exists around her hands. A single close-up
    #             on his face when she says the "using endurance as self-harm" line.
    #         (3) Cot: wide. The two of them in the frame, the medbay quiet around
    #             them. Tessa in a chair beside the cot. Aeron asleep. The camera
    #             does not move for the closing beat.
    # LIGHTING: Corridor — standard secondary-base overhead, cold. Medbay treatment
    #           station — overhead surgical strip above the exam table, amber
    #           practicals in the periphery. Cot area — only the practicals. Amber
    #           and low. The dimmer the scene gets, the steadier Tessa becomes.
    # SFX: Corridor — base ambient, distant voices, footsteps. Medbay — ventilation,
    #      generator hum, antiseptic spray, fabric rustle. Cot area — a single IV
    #      line ticking at the edge of hearing. Her breath. His breath slowing as
    #      he drops into sleep. No music in the first two phases; one held low string
    #      at the closing beat, under her naming of him three times.
    # FX/COMP: The scrape on his forearm — dirty, not deep, something he has not
    #          noticed. The vitals read-out on the small monitor beside the cot
    #          showing his heart rate settling over the course of the third phase.
    # BLOCKING: Corridor standoff. Medbay treatment (him seated, her standing, her
    #           hands on his arm). Cot (him lying down, her in the chair).
    # FACE: Tessa — gentle with serrated edges. The clinical mask is present and
    #       the mask is serving as armor, not as distance. Aeron — degraded.
    #       Visible tremor. The dissociation of someone who has not stopped moving
    #       because stopping is the worst option. Relief when he lets her overrule
    #       him. He does not know it is relief until it is already on his face.

    # ========= VOICE BASELINE =========
    # EMP cadence. Tessa drives the entire scene. Her medical register is a mask
    # she takes on and off deliberately — mask on for the overrule, mask off for
    # the honesty, mask ambiguous at the close. Aeron speaks less than she does.
    # He has one line of real protest and one line of real truth. Everything else
    # from him is him being tended to and not stopping her.

    # scene bg_secondary_base_corridor_night with dissolve
    # play ambient "sfx/ambient/base_corridor_low.ogg" fadein 2.0

    # ========== PHASE 1 — THE CORRIDOR ==========

    # CAMERA: handheld tight on Aeron walking. The shot has been
    #         with him since Phase 1 — or implied to have been,
    #         the camera is already at his walking pace. When
    #         Tessa steps out of the medbay doorway, the camera
    #         does NOT cut to her arrival. It finds her because
    #         she has stopped moving and her stillness pulls
    #         focus from the moving background. Stay in the
    #         handheld for the entire corridor argument. Over-
    #         the-shoulder bias when she speaks, reverse on him
    #         when he answers. When her hand lands on his
    #         forearm, rack focus to the hand. Hold the rack.
    # FACE: Aeron — visible tremor in the left hand before Tessa
    #        arrives. The face is degraded in a way the opening
    #        block names: dissociation of someone who has not
    #        stopped moving because stopping is the worst option.
    #        The camera reads the tremor first, the face second.

    "Thirty-eight hours."

    "He has not counted them, because counting them would make him think about stopping, and thinking about stopping is the thing he is not doing tonight."

    "Between the Act IV opener and the council scene and the Marcus adaptation intel and Lyra and Noelle's models and the cipher alcove after the Sector 7 interdiction and the second briefing Selene has waiting for him in twenty minutes — between all of those things, Aeron has not slept."

    "He is walking the south corridor from the cipher alcove toward the war room."

    "His hand has a tremor he cannot quite file as purely physical."

    "Tessa steps out of the medbay door ahead of him. Not in front of him, to the side — so that he can see her stop and decide what she is doing."

    "She does not decide for long."

    "She crosses the corridor in three steps and puts her hand on his forearm."

    "Not tentatively. Not as a check. The way a person stops a door that is about to close on something fragile."

    t "Medbay. Now."

    "He does not stop walking — his body is still aimed at the war room."

    "Her hand does not move."

    "He stops."

    a "Selene is waiting. There is a planning session in twenty minutes."

    t "Selene will wait."

    a "She is holding the room for me."

    t "She will keep holding it. Her commanders do not bleed on her floors."

    athought "Her hand is not cold. It is not the professional touch from the medbay. It is the grip of someone who has decided the corridor is the only part of the building where this argument gets to happen and that the argument is going to happen now or not at all."

    a "Tessa — this is not your call."

    "It is the wrong thing to say."

    "He knows it is the wrong thing to say before it finishes leaving his mouth, and the wrongness is what makes her answer sharper than anything she has ever said to him."

    t "Your body is not a resource to be spent."

    "Her voice is very level."

    t "I am tired of being the only person in this building who remembers that."

    t "Medbay. Now. I am not asking."

    "The corridor is quiet around them. The south corridor is quiet at this hour anyway — the third-shift rotation is in the mess and everyone else is at their posts. There is no audience. There is only the hand on his forearm and the sentence she just said."

    athought "She is not making a medical call right now."

    athought "She is making a command-level intervention from inside a relationship she does not usually make command-level interventions from."

    athought "That is not anger. Anger would be easier to push past."

    athought "That is the look of someone who has been counting and is watching a name move from one side of her ledger to the other in real time."

    athought "I am the name on her ledger."

    "He stops. All the way."

    a "Okay."

    t "Okay?"

    a "Okay. Medbay."

    "Her hand does not leave his forearm. She lets him see the decision register — because Tessa does everything with attention, including watching people choose to be attended to."

    "Then she turns. Her hand slides from his forearm to his elbow and she walks him the thirty meters back to the medbay with the gentle non-negotiable grip of a medic moving a patient who is not going to be moved by any other means."

    # ========== PHASE 2 — THE SCRAPE HE DID NOT NOTICE ==========

    # CAMERA: LOCATION SHIFT — corridor to medbay treatment bench.
    #         50mm, still. The handheld is gone. Tessa's hands
    #         are the subject of the new composition; they
    #         enter each frame first and Aeron enters second as
    #         the object of their care. Cover the cleaning of
    #         the scrape in inserts — the three-inch dirty
    #         abrasion he has not noticed, the antiseptic, the
    #         fresh bandage, the eyes-check, the pulse, the BP
    #         reading at 9 points up. The medbay exists around
    #         her hands. When the scene widens, it widens to
    #         include her face, never his.
    # LIGHTING: medbay treatment station. Overhead surgical
    #           strip directly above the exam table at 5600K,
    #           hard. Amber practicals in the periphery at
    #           2800K. The two temperatures are present at the
    #           same time and Tessa moves between them as she
    #           works. The scene will get dimmer as it goes on.



    # scene bg_medbay_night_low_light with dissolve
    # play ambient "sfx/ambient/medbay_quiet_night.ogg" fadein 1.5

    "The medbay at this hour is in its low-light mode. The overhead surgical strips are off at the main treatment station; only the amber practicals are up. One other cot has a sleeping fighter on it — Joran Tev, recovering from the shoulder wound from Sector 7, the wound that had not existed in Plan A."

    athought "Joran Tev is alive because Lyra called the ridge flank."

    athought "Every room I walk into is going to have the names in it now."

    "Tessa steers him to the treatment bench. Not the exam chair — the bench, the one she used for his Brand-scar night. The one that makes the scene feel like it has happened here before."

    "She pulls on gloves. Latex snap."

    "He watches her do it."

    athought "The gloves are the tell. She is putting the mask on because she needs the mask to say the next part."

    t "Sleeve."

    a "Tessa, nothing is—"

    t "Sleeve, Aeron."

    "He pushes his left sleeve up past the elbow. The old Brand scar is there — the geometry she traced last time. She does not trace it now. She is not here for that tonight."

    "She is here for the thing on the outside of the forearm he has not noticed."

    "A scrape. Three inches long, not deep, dirty. The kind of injury that happens when you move an equipment case in a hurry and the case has a raw edge you did not see."

    "He looks at it."

    athought "I do not know where that came from."

    "He looks at it longer."

    athought "I still do not know where that came from."

    t "When did you last look at your own arms?"

    a "I—"

    t "That is not a rhetorical question. When did you last look at them. Not run a diagnostic. Not log into medbay. When did you last stand in front of a mirror and look at your own forearms?"

    a "I do not know."

    t "Right."

    "She cleans the scrape. Antiseptic on gauze. The particular pressure of someone who knows exactly how much it stings and does not apologize for it."

    athought "It stings. Of course it stings. I did not notice a three-inch dirty scrape on my dominant forearm because I have been running on a fuel that does not include the part of the nervous system that notices things like that."

    athought "I do not want to think about what fuel it is."

    "She checks his eyes. Small penlight. Not because she thinks there is a concussion — because she is cataloguing."

    "She takes his pulse from the wrist. Holds it for thirty seconds. Frowns."

    "Takes his blood pressure. The cuff inflates and he can feel how much of his pulse is the cuff and how much of it is him and the numbers do not feel related to each other."

    "She reads the numbers. She does not say the numbers out loud."

    "She is very quiet."

    # ========== PHASE 3 — THE NAMING ==========

    # CAMERA: the scene's one close-up on Aeron's face. Tight
    #         single, held for the "using endurance as self-harm"
    #         line and his answer. The first time in the scene
    #         the camera leaves Tessa's hands. The close is
    #         earned by her diagnosis — she has named the thing
    #         and the frame catches him receiving the name.
    #         After his one line of truth ("I cannot stop
    #         moving. If I stop, I think about her"), cut back
    #         to her hands for the rest of the phase.
    # FACE: Aeron — the dissociation cracks. Not dramatically.
    #        The jaw softens by a degree. The eyes find her
    #        eyes for the first time in the scene. The moment
    #        of surrender is in the eye-find, not in the words.

    "She pulls the glove off her right hand. Not both — one. The left glove stays on because the left glove is still holding the cuff."

    "Her bare right hand goes to his forearm. Just above the scrape. The warm place. The pulse point."

    t "I am going to say something I have been deciding whether to say for six days."

    a "Tessa—"

    t "You are using endurance as self-harm."

    "The sentence lands in the room before either of them moves."

    t "I have seen this in patients before. The ones who come out of long combat rotations and do not know how to stop moving. They keep their heart rates elevated because the elevated rate is the only shape of their body they recognize. They forget to eat. They forget to drink. They get scrapes they do not notice because the signal-to-noise ratio of their pain system is running at combat levels twenty hours a day."

    t "That is where you are."

    t "I did not want to say it out loud until I was sure. I am sure now. I am sure because your pulse is one hundred and four resting, your blood pressure is up nine points from your last recorded baseline, and you walked into the medbay with a three-inch dirty scrape on your dominant forearm that is at least six hours old and you did not know it was there."

    t "Six days ago I was watching you. Now I am telling you."

    "He is looking at her hand on his forearm instead of her face. It is a thing he does when he is being seen too precisely — he finds a detail to put his eyes on so that his face is still under his own command."

    t "Look at me, Aeron."

    "He looks at her."

    t "You are doing it on purpose."

    "It is not an accusation. It is a diagnosis. The voice is the voice she uses with patients whose pain has a shape they are unwilling to name."

    athought "She is right. I have known she is right for about four hours. The part of me that noticed I was going to collapse before the next briefing was the same part of me that decided not to tell anyone, because telling anyone would have meant stopping, and stopping was the unacceptable outcome."

    athought "Stopping is the unacceptable outcome because if I stop, I am going to think about my mother. I am going to think about the platform. I am going to think about Kesa Marin and Joren Hale. I am going to think about the three-second pause on the extract route where I almost moved my hand."

    athought "I am going to have a body again."

    athought "The body is not the place I want to be."

    "He says the only true sentence he has available."

    a "I cannot stop moving."

    a "If I stop, I think about her."

    "He does not specify her. He does not need to. Tessa's face does not move, which is how Tessa's face moves."

    t "I know."

    t "That is why I am here. To be the thing that stops you before your body stops you first."

    t "Your body is going to win that fight without me. I am not here to ask if you can stop. I am here to make it so that you get to stop inside of a room that knows why stopping is hard."

    "She lets go of his wrist."

    "Not abruptly. She lifts her hand away the way she lifts an instrument off a tray when the instrument's part of the procedure is over."

    "Then she puts her hand on his face."

    "The touch is not medical. It is not the Brand-scar trace. It is the palm of a woman who has been paying attention cupped against the jaw of a man who has not been paying attention to himself. Her thumb at his cheekbone. Her fingers at the line where his jaw meets his ear."

    "He closes his eyes."

    "He did not decide to. The closing was not a performance. His body closed his eyes because his body has been waiting for a reason to close them and her hand was the reason."

    t "Cot. Now. I am going to finish dressing the scrape and then I am going to sit in the chair and you are going to sleep."

    a "Tessa—"

    t "That is the end of the sentence. There is no clause. I am not asking you to report back in the morning. I am not asking for a target duration. I am telling you the next shape of your evening. Cot. Sleep."

    "She removes her hand from his face."

    "He opens his eyes to find her already reaching for the bandage."

    # ========== PHASE 4 — THE COT ==========

    # CAMERA: wide. Third visual register of the scene. Two-shot
    #         of Aeron lying on the cot and Tessa in the chair
    #         beside him. The medbay is quiet around them. Do
    #         not move the camera for the duration of the
    #         settling beat. Hold the wide as the scene narrows
    #         its own sound — the ventilation, the generator,
    #         the IV tick at the edge of hearing, his breath
    #         slowing. The vitals monitor is visible in the
    #         frame but not the subject of the frame. Let the
    #         heart rate number settle across the held shot.
    # LIGHTING: medbay has dimmed. Only the amber practicals
    #           remain. The surgical strip is off. The dimmer
    #           the scene gets, the steadier Tessa becomes
    #           (per opening block). The amber-only framing
    #           signals that she is now operating under her
    #           own light, not the medbay's.

    "She bandages the scrape. Three turns of gauze. Tape. She does not narrate the dressing this time — the gesture is so familiar now it is almost a private language."

    "She stands up."

    t "Boots off."

    a "Tessa."

    t "Boots off. You are not sleeping in boots in my medbay."

    "He unlaces his boots. It takes longer than it should. His hands are tired in a way that has not been tired since a month before he left the Academy — the kind of tired that makes a lace an elaborate mechanical problem."

    "Tessa watches him do it. She does not help. Not because she is being cruel — because she is letting him keep the last piece of authority in the scene that is his to keep."

    "Boots off. Jacket off — she takes it from him and lays it over the back of the chair."

    "She points at the cot."

    "He lies down."

    "The cot is rougher than the one in his own quarters. The blanket is Phoenix standard issue. There is a thin pillow. None of it is the point."

    "The point is that the moment his head touches the pillow, something in the back of his shoulders that he did not know was clenched releases all the way down the base of his spine."

    athought "Oh."

    athought "I have been holding that for thirty-eight hours."

    athought "That is what thirty-eight hours feels like."

    "Tessa moves a chair to the side of the cot. She does not make a production of it. She sits down with a medical datapad in her lap and the amber light from the practicals is on the side of her face and she does not look at him directly because direct looking would make this a scene about being watched, and it is not a scene about being watched."

    "It is a scene about being held without touch."

    "She has his vitals monitor clipped to his finger — he does not remember her clipping it on. The small device makes a tiny measured tick every few seconds. His heart rate is on the screen and it is slowly coming down."

    "One hundred and four."

    "One hundred and two."

    "Ninety-eight."

    "Ninety-four."

    "Ninety-one."

    athought "I am going to fall asleep in about two minutes."

    athought "I have not said thank you."

    a "Tessa."

    t "You do not have to say it."

    a "I want to."

    t "Then say it in the morning. The part of you that can say it right now is the part of you that has been running the scene. I want the part of you that wakes up. That part will say it better."

    a "Okay."

    t "Sleep, Aeron."

    "His eyes close."

    "He is asleep before his next breath finishes."

    # ========== PHASE 5 — THE THREE TIMES ==========

    # CAMERA: slow push from the wide two-shot to a medium
    #         single on Tessa. She is applying her mother's
    #         rule (from a2_int_tessa_torins_name) silently to
    #         his sleeping body — the first callback to the
    #         rule in Act 4 and the rule's first application
    #         to a living person. The camera has to be close
    #         enough to see her mouth form the three iterations
    #         of his name without voicing them. She does not
    #         say them aloud. Her mouth does. The silent
    #         shaping is the scene's moral center.
    # FACE: Tessa — steadier than she has been anywhere in the
    #        series. The rule is doing its work and she is
    #        letting it. No tears. No visible strain. The face
    #        of a woman running an inherited discipline on
    #        someone she has decided to keep.
    # SFX: the held low string from the opening block enters
    #      here. Barely there. Under her mouth. Fade out on
    #      the cut to black.

    "Tessa watches him for a long time."

    "She has done this before — watched patients cross the threshold from too-awake into actual sleep. There is a particular quality to the breath that changes when the body lets go. She has been cataloguing it for years because she is a medic, and cataloguing is what she does instead of grieving in the moment."

    "She catalogues his breath now."

    "Eighty-seven beats per minute. Respiration dropping. Muscle tone in the jaw finally gone."

    "Her hands are folded in her lap. The left is still half-gloved — she takes the glove off now that no one is watching. Both hands bare."

    "She sits with her hands folded in her lap and her eyes on the heart rate monitor and she does not move."

    tthought "I was sharper in the corridor than I meant to be."

    tthought "I was not actually sharper than I meant to be. I was exactly as sharp as I meant to be. I am lying to myself a little because lying to myself about it makes it easier to hold."

    tthought "The sharpness was the only language he was going to hear at the speed he was moving. Gentle would have bounced off. I have been gentle with him for six days and he has been running a heart rate of one hundred and four and collecting scrapes he does not notice. Gentle stops being gentle when gentle lets someone hurt themselves."

    tthought "I am allowed to pick the register."

    tthought "That is the lesson I have been practicing with myself since the board scene. Liora on both sides. Expand the definition of living. Expand the definition of care."

    tthought "The board is in the main medical area right now. It has two new names on it from the Sector 7 operation. I added them this afternoon. I did not say them out loud. I have not said any of the last four names out loud."

    tthought "My mother's rule was to say them three times. I have been saying them silently because the silence is working differently now."

    tthought "It is working because I have company for them. The living column is longer, and the living column has him in it."

    tthought "Which means I have one more name to practice on tonight. The one I did not write on the board because you do not write living people on the board until they are dead, and the point of the rule is that the saying keeps them alive."

    tthought "I am going to try it here."

    tthought "I have never done this part silently before. The silent version is an experiment I am running in a room where the patient is asleep and will not know I ran it."

    tthought "Aeron."

    tthought "Aeron."

    tthought "Aeron."

    tthought "Say it three times and you are still here."

    tthought "You are still here."

    tthought "My mother gave me the rule when I was seven. I do not think she ever imagined I would use it on someone who was not dead yet. I do not think I ever imagined I would use it on someone whose heart rate I was watching decelerate on a monitor at four in the morning in a base nobody was supposed to still be running."

    tthought "Here we are."

    tthought "He is still here."

    tthought "I am not going to leave the chair until the sun comes up."

    "She does not leave the chair."

    "The medbay hums. Joran Tev is asleep in the other cot. Aeron's breathing finds a slow steady cadence. Tessa's hands are folded in her lap and her eyes are on the heart rate monitor and the amber light from the practicals is on the side of her face and she does not move."

    "The camera holds the wide shot for a long beat."

    "Then it fades."

    # stop ambient fadeout 3.5
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Tessa", trust=1, affection=1)
    $ flag("tessa_overruled_aeron_rest", True)
    $ flag("aeron_slept_medbay_cot", True)
    $ npc_remember("Tessa", "overruled_aeron_for_rest", tone="loving_command")
    $ npc_remember("Tessa", "said_his_name_three_times_silent", tone="rule_inherited_differently")
    $ npc_remember("Aeron", "tessa_hand_on_face_in_medbay", tone="given_permission_to_stop")
    $ canon_set("aeron.rest_debt_cleared_once_by_tessa", True)
    $ metric("aeron_endurance_self_harm", set_to=0)
    $ tp_seed("a4.tessa_care_as_command")
    $ scene_mark(_current_scene_id, "completed")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s05a_you_are_not_a_machine_emp
# cann.chapter: Act IV, Chapter I — Shared Authority
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Immediately after a4_s05 (Delegation). Same night — late into it. Aeron is
#     moving from the cipher alcove back toward the war room for a Selene briefing.
#     38 hours since his last sleep. Tessa intercepts him in the south corridor.
# cann.what_happened:
#   - Corridor: Tessa physically stops Aeron with a hand on his forearm. Tells him
#     medbay, now. He protests that Selene is waiting. She refuses — "Her
#     commanders do not bleed on her floors." He tries "This is not your call."
#     She answers with the scene's cutting line: "Your body is not a resource to
#     be spent. I am tired of being the only person in this building who remembers
#     that. Medbay. Now. I am not asking." He stops.
#   - Medbay: She takes him to the treatment bench (the same one from
#     a3_s20a_scar_and_steady_emp). Finds a three-inch dirty scrape on his forearm
#     he has not noticed. Cleans it. Checks his eyes, pulse, blood pressure. His
#     resting heart rate is 104. BP is up 9 points from baseline.
#   - She names the pattern: "You are using endurance as self-harm. I have seen
#     this in patients before. The ones who come out of long combat rotations
#     and do not know how to stop moving."
#   - He says the one true sentence he has: "I cannot stop moving. If I stop, I
#     think about her." (Unspecified her. Unnecessary to specify.)
#   - She answers: "That is why I am here. To be the thing that stops you before
#     your body stops you first."
#   - She puts her palm on his face — not medical, not erotic, the gesture of a
#     woman who has been paying attention. He closes his eyes without deciding to.
#   - Cot: She takes him to a cot in the medbay. Boots off. Jacket off. He lies
#     down. His back releases in a way that tells him how long he has been holding
#     it. He tries to say thank you. She defers it to morning. He sleeps within
#     one breath.
#   - Tessa's internal beat: she acknowledges that she was exactly as sharp as she
#     meant to be in the corridor. She has been expanding her definition of care
#     since the board scene (a3_int_tessa_the_board_emp) and the sharpness is
#     part of that expansion. She then performs her mother's three-times rule
#     silently on Aeron — the first time she has used the rule on a living person.
#     "Say it three times and you are still here. You are still here."
#   - She does not leave the chair beside the cot. She stays until sunrise.
# cann.aeron_state:
#   - Broken-open, grieving, running on dissociated endurance. His tremor, his
#     unnoticed scrape, his failure to see his own arms. These are the scene's
#     body-level evidence that the delegation scene cost him more than he has
#     admitted and that Liora's death is still the thing he is running from.
#   - The scene is the first time in Act IV he lets someone overrule him on
#     bodily limits. This is a canonical first. Future rest scenes should read
#     against it.
#   - "I cannot stop moving. If I stop, I think about her." — first explicit
#     statement of the endurance-as-avoidance pattern. Aeron has said versions
#     of this to no one until tonight.
# cann.tessa_state:
#   - Tessa's register is the scene's whole lesson. She moves between gentle-with-
#     serrated-edges and clinical mask and bare hand on face. The mask is not
#     distance — it is the armor she puts on to give herself permission to say
#     the harder thing.
#   - Her internal monologue reveals the Act IV evolution of her practice. She
#     is using the rule of three on living people now, silently, as a private
#     act of care. This is the mechanical seed for a4_s06 (the silent board beat).
#   - She stays in the chair until dawn. No monologue about it — the staying is
#     the statement.
# cann.path_tracking:
#   - EMP path. Linear. No player choice. Relationship-gated entry.
#   - rel_bump Tessa +1 trust, +1 affection.
#   - flag tessa_overruled_aeron_rest True. flag aeron_slept_medbay_cot True.
#   - canon_set aeron.rest_debt_cleared_once_by_tessa — this is a one-time
#     canonical state. Future overwork beats may re-open the debt.
#   - metric aeron_endurance_self_harm reset to 0. The metric should accrue in
#     subsequent scenes if Aeron slides back into the pattern.
#   - tp_seed a4.tessa_care_as_command — Tessa's authority inside the
#     relationship as a distinct kind of shared authority from the operational
#     kind. This is the Act IV Tessa thesis in compressed form.
# cann.thematic_flags:
#   - Care as command authority. Love as the thing with the right to overrule.
#     This is a distinct mode of shared authority from the Selene-delegation
#     mode in a4_s05. The chapter is teaching Aeron multiple shapes of shared
#     authority and this is one of them.
#   - Endurance as self-harm: diagnosis made explicit. The avoidance pattern is
#     named. Aeron cannot claim ignorance in future scenes.
#   - The rule of three silently applied to a living person. First instance.
#     Sets up a4_s06.
#   - The medbay treatment bench as a recurring intimate space for Aeron and
#     Tessa — same bench as a3_s13. The location carries memory.
# cann.character_moments:
#   - Tessa: the corridor hand on the forearm. The sharpness chosen deliberately.
#     The moment she removes one glove and puts her bare hand on his face. The
#     silent three-times naming. Sitting in the chair until dawn.
#   - Aeron: the three-inch scrape he did not notice (the scene's body-level
#     indictment). The unlacing of his own boots as a failing mechanical problem.
#     The closing of his eyes without deciding to. The release at his spine when
#     he lies down. "I cannot stop moving. If I stop, I think about her."
#   - The structural character moment: Aeron lets himself be commanded inside a
#     register that is not operational. He has been commanded operationally
#     before (Selene does it in a4_s05). This is the first time in Act IV he
#     accepts intimate command authority.
# cann.callbacks:
#   - a2_int_tessa_torins_name: her mother's rule — say it three times and you
#     are still here. The rule was for the counter. Here the rule is applied to
#     a living person for the first time.
#   - a3_int_tessa_hands_remember_emp: her steadiness after. The scene trusts
#     that established baseline.
#   - a3_int_tessa_the_board_emp: Liora on both sides of the board. Tessa's
#     explicit Act IV thesis about expanding the definition of living. This
#     scene is an enactment of that thesis on a patient who is not dead.
#   - a3_s20a_scar_and_steady_emp: the same treatment bench, the Brand scar, the
#     same hands. The scene does not repeat intimacy from that night — it adds
#     the next register of the same relationship.
#   - a4_s05_delegation_test_emp: Joran Tev is asleep in the adjacent cot. The
#     Phoenix fighter who would have died in Plan A. Aeron notes it internally.
#   - a4_s04_lyra_unbuckled_emp: "presence is enough" as cross-LI language.
#     This scene reinforces that Tessa's vocabulary and Lyra's vocabulary are
#     converging on the same word without coordination. Aeron noted the echo in
#     the Lyra scene; Tessa's "the thing that stops you" is its twin.
# cann.block_status:
#   - LINEAR. No branching, no choice. EMP path only. Relationship-gated entry.
# cann.requires_followup:
#   - The silent rule-of-three used here on Aeron's sleeping body is the exact
#     mechanical seed for a4_s06 (the silent board scene). The two scenes are
#     written as a matched pair.
#   - aeron_endurance_self_harm metric is reset but not removed. Future Act IV
#     scenes can re-increment it if Aeron slides.
#   - The medbay cot is canonically a place Aeron has slept once. Any later
#     reference to him sleeping in medbay should carry this scene's weight.
#   - "Your body is not a resource to be spent" is a load-bearing Tessa line.
#     Callback candidate for later Act IV scenes involving overwork, grief,
#     or operational cost.
