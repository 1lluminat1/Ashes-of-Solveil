# =======================================================
# ACT 4 - Scene 05: Zira Cannot Leave (Obedience Path)
# File: a4_s05_zira_cannot_leave_ob.rpy
# Path: OB
# Type: ZIRA STATE BEAT (solo)
# Character Focus: Zira (alone, entire scene)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s05_zira_cannot_leave_ob"
$ scene_mark(_current_scene_id, "entered")

label a4_s05_zira_cannot_leave_ob:
    $ show_timeline("DAY 44", "23:00", "Phoenix Base — Zira's Workshop")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked. No handheld. No drift. This is a woman holding still.
    #         Open wide on the workshop: benches, tool boards, the low orange of a soldering
    #         station on standby. Zira is seated on her work stool. The go-bag is on the bench
    #         in front of her. Frame: three-quarter from her left, bag in foreground, her face
    #         in mid-ground. The bag has equal compositional weight to her.
    #         Mid-scene: tight on her hands. Hands that have been still for an hour.
    #         Insert: the bag contents as she removes items. Locked top-down. Clinical.
    #         Insert: the pressed flower. Same top-down. The camera does not editorialize.
    #         Late: wide again. She is at the bench working on a small tool repair. The bag
    #         is in the corner on the floor. The flower is on the bench surface.
    #         Final shot: her hands, steady, at the repair. Hold. Fade.
    # LIGHTING: Workshop. One overhead halogen over the bench, warm-white. The rest of the
    #           room is dim -- the bench is the only fully lit surface. The bag sits inside
    #           the halogen circle. The corner where she will put the bag is outside it.
    #           Orange standby from the soldering station at frame edge. Small. Steady.
    # SFX: Loop -- workshop ambient. The low hum of a ventilation fan.
    #      One-shots -- zipper of the bag. Paper rustle (waxed sheets). A single metallic
    #      click when she sets the pressed-flower packet down. Her breath, twice, slow.
    #      Later: the small clean sounds of a tool repair. A screw backing out. Oil on cloth.
    #      No music.
    # FX/COMP: The workshop is organized the way Zira organizes things -- not neat, but
    #          coherent. Every tool has a location she could find in the dark. The chaos is
    #          all on the surface and none of it is real.
    #          The go-bag: compact, canvas, the Ghostline logo stitched inside the flap.
    #          It is not a bugout bag. It is a travel bag. That matters.
    # BLOCKING: Zira seated the whole scene until the final beat, when she stands once to
    #           move the bag and then sits again for the repair.
    #           Her stool does not swivel. She has placed it where she needs it.
    #           She does not pace. Zira does not pace.
    # CANON: ZIRA STATE BEAT. Solo. No other characters. No dialogue with anyone.
    #        The scene is about a decision that was already made months ago and is now
    #        being inspected. The inspection is the drama.
    #        The pressed flower is the first time it has appeared in canon. Do not over-explain.
    # FACE: Zira -- unreadable to anyone else. Completely readable to herself for the first
    #        time in months. The expression of a woman who has run out of the particular lie
    #        she was most comfortable telling.

    # ========= VOICE BASELINE =========
    # Entire scene is zthought. There is no spoken dialogue.
    # Zira's interior voice: direct, technical, unsparing. She uses Ghostline vocabulary
    # naturally -- nodes, signal, relay, load -- because that is how her mind works.
    # She does not perform her feelings. She catalogues them the way she catalogues wire.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - ZIRA'S WORKSHOP - LATE NIGHT]
    # Late. The base has gone quiet except for the night rotation in ops.
    # Zira's workshop is down the service corridor, past the generator room.
    # She likes the location because the generator masks her soldering frequencies.

    #scene bg_zira_workshop_ob_night with dissolve
    #play ambient "sfx/ambient/workshop_generator_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE BAG ==========

    "The bag has been on the bench for fifty-seven minutes. She knows because she checked the chrono once at the start, to see how long she had been sitting there, and then decided not to check it again. She has checked it twice anyway. It has been fifty-seven minutes."

    "She is staring at the bag."

    zthought "Inspect the object."

    zthought "That is the training. That is the thing the Ghostline taught me before it became mine -- before you build a node, you inspect the object. You do not assume you know what is in the box. You open the box."

    "The bag is a Ghostline-issue courier bag. She has three of them. This one is older. The canvas is softer at the corners where it has been folded and unfolded for a decade. The Ghostline logo stitched inside the flap is the early mark, before the revision."

    zthought "I packed this bag at twenty-one hundred."

    zthought "I chose it specifically. Not the newer ones. Not the tactical pack. The courier. The bag I have been carrying to meets for ten years. The bag that looks like what I look like. The bag nobody questions."

    zthought "I knew what I was doing at twenty-one hundred. I did not know what I was doing at twenty-one fifteen. And I have been sitting in the gap between those two Zira's ever since."

    "Her hands are in her lap. They are not moving. Her hands are the most still part of her. This is significant -- Zira's hands are almost always moving, even when the rest of her is still."

    # ========== PHASE 2 -- THE INVENTORY ==========

    "She reaches. Pulls the zipper. The sound is louder than it should be in the quiet workshop. She flinches, slightly, and then is angry at herself for flinching."

    zthought "The generator is masking any audio that leaves this room."

    zthought "I know that. I set the room up to make that true."

    zthought "I flinched anyway."

    "She opens the bag. The contents arrange themselves the way she packed them. She packed them fast. She was not performing for herself while packing -- her hands did it, and her mind did something else, and the result is an inventory that looks like a confession."

    zthought "List."

    "She lists. Aloud, in her head, the way she lists wire gauges."

    zthought "One. Two changes of clothing, base Phoenix issue, nothing that identifies as Ghostline."

    zthought "Two. The small encryption kit. The one I built in Sector 7 before I came to this base. It still works. It still can't be traced to Phoenix infrastructure."

    zthought "Three. Three forged IDs, none of which are the current generation. All of which are still good for the checkpoints that do not update weekly."

    zthought "Four. Cash. Not a lot. Enough for four days of movement and one bribe."

    zthought "Five. A data spike with the Ghostline contingency payload -- the handoff instructions for my successor, in case I am dead. Not in case I leave. In case I am dead."

    "Her hand pauses at the fifth item. She has packed the death protocol."

    zthought "That is interesting."

    zthought "If I were leaving on a trip, I would not pack the death protocol. I would not carry the thing that hands off my life's work to the next operator. That lives in the wall safe behind the bench. It does not live in a travel bag."

    zthought "I packed it."

    zthought "I did not notice I packed it until just now."

    zthought "That is not a bag for a trip. That is a bag for someone who is not coming back."

    "She sits with that. The generator hum fills the space the thought leaves behind."

    # ========== PHASE 3 -- THE DOOR ==========

    "She turns her head. Looks at the door."

    "The door to the workshop is a standard pressure hatch. It opens inward. It is unlocked right now. She has never locked it in the months she has been here. The lock exists. She has never used it."

    zthought "The door is unlocked because I do not want to give the impression that I have anything to hide."

    zthought "That is a narrative I told myself. I believed it until about thirty seconds ago."

    zthought "The door is unlocked because if I lock it, I will have committed. The lock is a small act that implies a larger act. I have been refusing the small act so that I do not have to notice the larger one."

    "Her eyes trace the path from the stool to the door. It is nine steps. She has measured it, not deliberately -- you measure the paths through a room you work in. She knows the paths through this workshop the way a pianist knows a keyboard."

    zthought "Nine steps. Two seconds if I do not pick up the bag. Three and a half seconds if I do."

    zthought "I could time the exit. I have timed it. I timed it twice in the last hour without deciding to time it. The numbers were waiting in my head when I asked for them."

    zthought "I am examining the door."

    zthought "I am examining the bag."

    zthought "I am also examining the fact that I am examining both and not moving."

    # ========== PHASE 4 -- THE DECISION MONTHS AGO ==========

    "She leans back on the stool. The stool creaks once, low. She puts her palms flat on the bench on either side of the bag. The bench is cool under her hands. Her hands are not yet as still as they were but they are close."

    zthought "Walk it back."

    zthought "When did I decide to stay."

    "Her mind goes to it without effort. She knows the hour. She has known the hour for months and has been pretending the decision was ambient, that it accumulated, that there was no moment. There was a moment."

    zthought "It was the night of the funeral."

    zthought "I was in the corridor outside the war room. I had the same bag on my shoulder. A different copy of the same bag. I was thirty feet from the north gate. The north gate was open. I had clearance."

    zthought "I stopped."

    zthought "I told myself I stopped because I had one more thing to check. I went to the war room to check it. The war room was empty. He was not there. I had invented a task to give myself the excuse to stop walking."

    zthought "And when I got to the empty war room and the task dissolved under examination, I did not turn around and go back to the gate. I went to my quarters. I unpacked."

    zthought "That was the decision. That was the hour. Thirty feet from the north gate."

    zthought "I have been telling myself I am here because I understand how power works and I can modulate him better than anyone else. I have been telling myself I am here because the Ghostline's integration with Phoenix requires my physical presence. I have been telling myself I am here because Zira does not run."

    zthought "I have been telling myself three truths to keep the fourth truth from forming."

    # ========== PHASE 5 -- THE FOURTH TRUTH ==========

    "Her hands close on the bench edge. She feels the bench, the grain of the old wood she sanded herself, the one knot she left because the knot is a good visual reference for when she is aligning small components."

    zthought "The fourth truth."

    zthought "I stayed because I could not bear to watch him become this from a distance."

    zthought "That is the sentence I have been refusing."

    "Her jaw works once. Sets."

    zthought "Not out of love. Out of proximity addiction. Out of the specific horror of being the person who saw it coming and was not in the room when it happened."

    zthought "If I leave, I will spend the rest of my life watching the news out of Solveil from wherever I run to, and every headline will be a small knife, and every intercepted signal will be me asking whether I could have moved a piece differently if I had been in the room."

    zthought "That is not love. I want to be clear with myself about that. I loved him once. I may love him still -- the operator's definition of love, which is the willingness to bet your own life against the continuation of a thing. But that is not why I am sitting here."

    zthought "I am sitting here because the distance of the outside would be worse than the distance of the inside."

    zthought "Inside, at least, I can see him. Inside, at least, the horror is current data. Outside, the horror would be old data, and old data is worse than current data, and the worse thing is that I would be looking for it in every channel I still have access to because I would not be able to stop."

    # ========== PHASE 6 -- THE FIFTH TRUTH ==========

    "She lets that sit. The workshop hums. Somewhere two corridors over, a night-shift tech drops a tool and curses. She does not hear the words. She hears the tonal shape. She notes it and discards it."

    zthought "Keep going. You started the inspection. Finish it."

    zthought "The fifth truth."

    zthought "I stayed because being near it is the closest I can come to controlling it."

    zthought "That is the Ghostline's oldest mistake, and I know it, and I am making it anyway. The operator who can't stop being in the room because the room is where the levers are. The hand that keeps adjusting the dial because the dial is in reach. The fact that the dial is adjusting something you do not want to adjust does not stop the hand."

    zthought "Proximity is how I tell myself I have power over this."

    zthought "I do not have power over it. I have influence. Influence is what you call the small fraction of power that you keep telling yourself is larger."

    zthought "But the influence is real. I am not lying about that to myself. If I leave, the influence goes to zero. That is not a metaphor. It is an equation."

    zthought "And if the influence goes to zero, the only thing I will have done is save myself."

    # ========== PHASE 7 -- THE SIXTH TRUTH ==========

    "Her breath goes out once, long. She does not allow it to be a sigh. Zira's breath is instrumental, not expressive."

    zthought "The sixth truth."

    zthought "I stayed because I am not better than him and proximity is how I prove it to myself."

    "This is the one she has been walking around all hour. She writes the sentence in her mind without punctuation because the punctuation would soften it."

    zthought "If I left, I would be claiming moral distance."

    zthought "I would be the operator who saw where it was going and walked. I would be the one with the clean hands. And Aeron -- the Aeron that is becoming whatever he is becoming -- would get to be the story I tell about the thing I refused to participate in."

    zthought "I do not have clean hands."

    zthought "I have cleaner hands than most people in this base. I have cleaner hands than Nyra, probably. I do not have clean hands. I have deleted footage. I have built infrastructure that I knew would be used for targeting. I have decided, multiple times, that a specific action was worth a specific cost, and I have signed off on the cost with the cost's name visible on the invoice."

    zthought "If I leave, I will start telling myself a story that erases that. The distance will do the erasing. It will happen even if I try not to let it happen -- memory is a compression algorithm, and compression favors the narrator."

    zthought "If I stay, I have to look at it."

    zthought "I have to look at every day of it. I have to be the person who saw what he became and was in the room when he became it and kept building the networks that he used while he was becoming it."

    zthought "That is not a nobler choice. It is not a better choice. It is the choice I am making because the other choice is a lie I would start telling immediately."

    zthought "Proximity is how I prove to myself that I am not better than him."

    zthought "I need that proof. I do not fully understand why I need it. But I am not going to pretend I don't."

    # ========== PHASE 8 -- THE BAG, INSPECTED ==========

    "She looks at the bag again. The bag is now an object she understands. She packed it. She knows why she packed it. The packing was honest work -- her hands were telling her something, and the something has now reached the front of her mind."

    zthought "The bag is not for leaving."

    zthought "The bag is the question 'would you leave.'"

    zthought "I packed it to ask the question. I have now answered the question."

    zthought "The answer is no."

    "Her hands have stopped gripping the bench. They rest flat. The stillness is no longer the stillness of hesitation. It is the stillness of a decision that does not need any further movement to confirm itself."

    zthought "Now. Empty the bag."

    # ========== PHASE 9 -- THE REMOVAL ==========

    "She pulls items out one by one. She does not move fast. Each item goes back to its place on the shelf or in the wall safe behind her."

    zthought "Clothes -- hamper."

    zthought "Encryption kit -- third drawer, left side, under the oscilloscope case."

    zthought "IDs -- the safe."

    zthought "Cash -- the safe."

    zthought "Data spike with the contingency payload -- the safe."

    "Each item returns to the room with a small precise sound. The workshop absorbs the sounds the way it absorbs everything she does. The workshop is on her side. It always has been."

    "When the bag is almost empty, her hand finds the last object at the bottom -- a flat packet of waxed paper she had tucked in before she closed the zipper an hour ago. She did not put it there deliberately. Or she did, and the deliberation was the kind you only recognize afterward."

    # ========== PHASE 10 -- THE FLOWER ==========

    "She lifts it out. Two squares of waxed paper, pressed together, a small square of something flat between them. She sets the packet on the bench."

    "She opens it."

    "Between the two sheets is a pressed flower. A small one. Six petals, faded blue, the kind of blue that means the flower was dark when it was alive and has lost half of itself to time. The pressing is clean -- whoever pressed it knew what they were doing."

    "She knows what she is doing. She pressed it herself."

    zthought "I am not going to explain this to anyone."

    zthought "Not even to the inside of my own head right now. This is not the night for that. The flower has a story. The story belongs to a Zira who is not fully in this room, and I am not going to drag that Zira into the current transaction."

    zthought "It is enough to say I have been carrying it. It is enough to say that in the moment of packing for departure, my hand reached for it and put it in the bag, because whatever else departure would have meant, it would have meant taking this with me."

    "She looks at the flower. The halogen over the bench turns the waxed paper translucent. The faded blue is almost grey in this light."

    zthought "It is not going back in the bag."

    zthought "The bag is changing purpose. The things for the old purpose have been returned to their places. This is not a thing for any of my places. It is a thing that was going to go with me on a journey I am not taking."

    zthought "It stays on the bench."

    "She sets the packet on the bench a hand's width from the vise. Not in any particular formal location. The spot where you put something you are going to look at later without performing the looking."

    # ========== PHASE 11 -- THE BAG IN THE CORNER ==========

    "She stands. The stool creaks once. Her legs are stiff from the hour of stillness and she waits a beat for them to remember themselves."

    "She picks up the bag. It is lighter now -- almost empty. The Ghostline logo inside the flap is visible at the angle she is holding it."

    "She walks to the corner of the workshop. There is a space between the far bench and the wall where she keeps things that are not in rotation. Spare components. An old rig she has not decided whether to cannibalize. A folded tarp."

    "She sets the bag down in the corner. Not folded. Not closed. Open at the top, the way you leave a bag when you are going to get rid of it later, not when you are going to use it."

    zthought "This bag is not for a trip."

    zthought "This bag is for a fire."

    zthought "Not tonight. Not necessarily soon. But when the end of this comes -- and the end of this is coming, I do not have illusions about that -- this bag is what I burn. Along with some other things I will decide about later."

    zthought "A courier bag full of the operator's identifying material, thrown in a furnace. That is not a leaving bag. That is the last housekeeping of someone who understood that staying meant staying to the end."

    "She looks at the bag for one beat in its new position. Then she turns back to the bench."

    # ========== PHASE 12 -- THE REPAIR ==========

    "The bench has a small tool on it. She put it there yesterday. It is a precision driver with a stripped tip -- the kind of micro-repair she usually does last thing before she calls it a night, because the focus it requires is the kind of focus that sets her down for sleep."

    "She sits. She picks up the driver. She turns the halogen one degree to improve the angle."

    "She gets to work."

    zthought "Hands are steady."

    zthought "That is the answer the body gives when the mind has decided. The mind decided months ago and has been arguing with itself ever since. The argument is over. The hands are reporting the result."

    zthought "I did not choose him again tonight."

    zthought "I want to be precise about that. I did not renew a vow. I did not decide that he is worth this. I did not forgive anything. I did not make peace with Nyra, and I am not going to."

    zthought "I chose to stop pretending I have a choice."

    zthought "The choice was made at the north gate. Everything since has been latency. Tonight I shut down the latency."

    # ========== PHASE 13 -- THE STEADY HANDS ==========

    "The driver's stripped tip responds to her file. She works it down to a new flat. The work is small and clean and requires exactly the fraction of her attention that is not currently holding the decision."

    "The rest of her attention watches the decision. Does not second-guess it. Watches it the way you watch a node you have just brought online -- making sure it stabilizes, making sure the baseline holds, ready to intervene if anything flutters."

    "Nothing flutters."

    zthought "I stayed because I could not bear the distance."

    zthought "I stayed because proximity is a lever I still believe in even when I know the lever is small."

    zthought "I stayed because I am not better than him and I need the proof."

    zthought "Those are the three reasons. They are not the reasons I told anyone. They are not the reasons I will tell anyone. They are the reasons I can live with as long as I am willing to keep looking at them."

    zthought "I am willing to keep looking at them."

    zthought "Tonight was the looking."

    "Her file passes the tip twice more. The metal takes the new edge. She tests it against a cloth. The cloth does not snag. The tip is clean."

    zthought "Tomorrow is operations."

    zthought "Tomorrow I will run relay for whatever he and Nyra have decided overnight. Tomorrow I will not flinch when Nyra calls me by my function instead of my name. Tomorrow I will look him in the face when he gives me an assignment and I will not search him for the man he used to be, because searching is what the Zira I was an hour ago did, and the searching was slowing down the work."

    zthought "The work is the thing."

    zthought "That is the Ghostline answer to everything. It is an answer now too."

    # ========== PHASE 14 -- THE FLOWER ON THE BENCH ==========

    "Her eyes pass over the waxed-paper packet once. She does not pick it up. She does not move it. She does not put it back in a drawer or a safe or a pocket. It stays where she set it -- a hand's width from the vise, in the halogen circle, visible."

    zthought "The flower stays on the bench."

    zthought "I am not going to file it. I am not going to hide it again. The filing was the lie I have been telling myself for years about what I was carrying and why. The unfiling is the small honest act I can do tonight without it costing the operation anything."

    zthought "If someone comes in here tomorrow and sees it and asks, I will not explain it. That will be my whole answer. I will not explain it."

    zthought "If no one asks, the flower stays on the bench until I decide what to do with it. And I may not decide for a long time. That is acceptable. Not every object in a workshop has to be in service."

    "She returns to the driver. The work continues."

    # ========== PHASE 15 -- HOLD ==========

    "The halogen hums. The generator hums. The night shift in ops is running its rotation somewhere three corridors away. The workshop is at equilibrium."

    "Zira works."

    "She is not calm. Calm is not the word. She is at the specific pitch of focus that she gets to when the decision underneath the work has been made and the body no longer has to wrestle with it. Everything she is doing is on top of a base she has now confirmed."

    zthought "I packed a bag."

    zthought "I unpacked a bag."

    zthought "I moved a bag to the corner for a different purpose."

    zthought "I took one thing out that I am not putting away."

    zthought "I went back to work."

    zthought "That is the shape of tonight."

    zthought "It is not a story that will mean anything to anyone but me. It is not a story I will tell even to myself again after I get up from this stool. But it is the shape of the thing, and the shape is now fixed, and I am going to live inside the shape."

    "Her hands are steady."

    "The camera holds on them."

    "The halogen holds the small warm circle of the bench and the bag in the corner is outside the circle and the flower is on the bench and the driver's new tip catches the light once."

    "Fade, slow."

    #stop ambient fadeout 2.5
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Zira", trust=0, conflict=2)
    $ tp_seed("a4.ob.zira.unchose_leaving")
    $ canon_set("ob.zira.bag_for_fire_not_flight", True)
    $ canon_set("ob.zira.pressed_flower_on_bench", True)
    $ flag("ob_zira_north_gate_memory_surfaced", True)
    $ flag("ob_zira_stopped_pretending_she_has_a_choice", True)
    $ npc_remember("Zira", "packed_and_unpacked_the_bag", tone="decision_confirmed_not_made")
    $ npc_remember("Zira", "three_reasons_she_cannot_say_aloud", tone="proximity_addiction_proof_of_not_better")
    $ npc_remember("Zira", "pressed_flower_left_visible", tone="small_honest_act")
    $ metric("zira_ob_commitment_clarity", add=2)
    $ scene_mark(_current_scene_id, "exited")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a4_s05_zira_cannot_leave_ob
# cann.chapter: IV -- Violence Normalized
# cann.path_tracking: OB
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Late night after a4_s04 shrine beat. Parallel batch. Zira alone in her workshop.
# cann.what_happened:
#   - Zira has packed a go-bag. It sits on her bench. She stares at it for an hour.
#   - She inventories the contents and notices she packed the Ghostline death protocol --
#     proof the bag was never a travel bag.
#   - She walks back to the decision point: the night of the funeral, thirty feet from
#     the north gate, bag on her shoulder. She stopped. She invented a task. She unpacked.
#   - She names the three truths she has been refusing:
#     (1) She stayed because she could not bear to watch him become this from a distance.
#     (2) She stayed because proximity is the only control she still believes in.
#     (3) She stayed because she is not better than him and proximity is the proof.
#   - She empties the bag. Everything goes back to its place.
#   - Last item: a pressed flower in waxed paper. First canon appearance. Unexplained.
#   - She sets the flower on the bench. Not filed. Not hidden. Visible.
#   - She moves the empty bag to the corner. Not packed for a trip -- kept for a fire.
#   - She returns to the bench and works on a precision driver repair. Hands steady.
#   - Internal thesis: "I did not choose him again. I chose to stop pretending I have a choice."
# cann.aeron_state:
#   - Not in this scene. Does not appear.
# cann.zira_state:
#   - The "unchose leaving" beat. Commitment clarified into a fixed shape.
#   - Not recommitment. Confirmation that the decision was made months ago and
#     has been arguing with itself under the surface until tonight.
#   - The pressed flower is the one personal concession she permits herself.
# cann.path_tracking:
#   - rel_bump Zira trust=0 conflict=2. tp_seed a4.ob.zira.unchose_leaving.
#   - canon_set ob.zira.bag_for_fire_not_flight True.
#   - canon_set ob.zira.pressed_flower_on_bench True.
# cann.thematic_flags:
#   - "Bag for a fire, not a flight" -- the OB register of Zira's endgame housekeeping.
#   - The three truths (proximity addiction / influence over moral distance / proof of
#     not being better) as the Zira OB confession. Never spoken aloud to another character.
#   - The pressed flower: first canon appearance. Kept ambiguous. A thing she has carried.
#   - The north gate memory: the hour the decision was actually made.
# cann.character_moments:
#   - Zira's technical self-diagnosis. Operator language applied to her own interior.
#   - The steady hands at the repair as the body's answer.
#   - The choice to leave the flower visible instead of filing it.
# cann.callbacks:
#   - a3_s20_you_dont_get_to_break_ob: "I chose you before. I'm choosing again."
#     This scene is the private version of that public confrontation. Not recommitment --
#     recognition.
#   - a3_s25_aftermath_ob: "Yeah. We proceed." -- the three-word public answer.
#     This scene is the 500 unspoken lines underneath those three words.
# cann.block_status:
#   - ANCHOR (OB). Solo state beat, no player choice, no branching.
# cann.requires_followup:
#   - The pressed flower on the bench as a tracked object. Future Zira OB scenes can
#     reference whether it is still there, whether she has moved it, whether she has
#     finally explained it.
#   - The bag in the corner as a tracked object. The "for a fire" intent is a late-game
#     marker -- the furnace scene is implicitly set up here.
#   - Zira's three truths as internal baseline. Not for dialogue. Internal only.
