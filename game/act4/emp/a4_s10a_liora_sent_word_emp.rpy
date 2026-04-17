# =======================================================
# ACT 4 - Scene 10a: Liora Sent Word (Empathy Path)
# File: a4_s10a_liora_sent_word_emp.rpy
# Type: SELENE CODA — post-s10 reveal beat
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s10a_liora_sent_word_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s10a_liora_sent_word_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 85mm. This is a small scene. One room, two people, one piece of
    #         paper. The camera holds mostly in two-shot with occasional pushes
    #         into Selene's hands or Aeron's face. No crossing the line. No
    #         coverage gymnastics. The scene is a handoff, not a dialogue
    #         exchange, and the camera knows it.
    # LIGHTING: Late morning. Different from s10 — the annex was pre-dawn.
    #           This is the day Aeron has walked into. The light is hard and
    #           plain. They are not in the annex. They are in a corridor
    #           alcove two turns off the war room. Selene brought him here
    #           after the morning brief. She did not say what it was.
    # SFX: Base ambient, daytime. The brief has just ended. Distant voices
    #      from the war room corridor. Selene's hand on the folded paper is
    #      the only sound inside the alcove for the first beat.
    # FACE: Selene — composed, but holding something she only finished
    #       metabolizing an hour before Aeron walked into the annex. The
    #       thing she delivers in this scene is a thing she has been
    #       carrying for less than a day. Aeron — still holding the water
    #       cup from s10. The cup is the prop of his unfinished state. He
    #       has not put it down. Selene pulled him from the brief without
    #       explanation. He is braced.
    # BLOCKING: A narrow alcove off a secondary corridor. One shelf, one
    #           bench, no chairs. They stand. Selene does not sit in this
    #           scene. Neither does Aeron. The scene is the length of a
    #           handoff, not the length of a conversation. They stand
    #           through the whole thing.

    # scene bg_corridor_alcove_morning_emp with dissolve
    # play ambient "sfx/ambient/base_corridor_day.ogg" fadein 2.0

    # ========== PHASE 1 — THE ALCOVE ==========

    # CAMERA: 85mm two-shot, the alcove entrance framed
    #         between them. Selene enters first and turns
    #         to face him before he is fully inside. She
    #         does not move into the alcove further than
    #         she has to. The alcove is shallow.
    # LIGHTING: the corridor light from the open end of
    #           the alcove. Hard daylight. No warmth. The
    #           scene is not intimate the way s10 was
    #           intimate — it is surgical. Selene chose a
    #           place where neither of them could mistake
    #           this for a continuation of the annex.

    "The morning brief ends at oh-nine-thirty. Selene runs it, the way she said she would. Aeron sits in the secondary chair, the way she said he would. The water cup from the annex is on the floor beside his chair the entire brief. He does not drink from it once. He does not put it down somewhere else either."

    "At the close of the brief, Selene does not dismiss him with the others. She lifts one hand — the smallest gesture, a half-inch — and the gesture is a request for him to stay."

    "He stays."

    "The room empties. Zira looks at him on the way out. She does not speak. Tessa does not look at him at all; her attention is already on her board in her head. Lyra's look is the look of someone who knows the day is not finished for him yet. Noelle's look is the look of someone who has seen this shape before and is choosing not to name it."

    "Selene does not speak until the door closes."

    sel "Walk with me."

    "He walks with her. The cup goes with him, because he has not decided yet what to do with it."

    "They do not go toward her quarters. They do not go toward his. They turn right at the first junction and take a secondary corridor Aeron has passed a hundred times without entering. Two turns later there is an alcove — shallow, maybe six feet deep, one shelf on the back wall with some folded tarpaulin on it, one bench along the side, no chairs, no table, no pretense of a working space."

    "Selene steps into the alcove. She turns. She does not sit on the bench. She is not going to sit in this scene."

    athought "I know this shape. This is the shape of a sentence she has already decided to deliver and has not decided how."

    # ========== PHASE 2 — THE PAPER ==========

    # CAMERA: push in on Selene's inside coat pocket. Her
    #         hand goes to it and stops. She does not
    #         retrieve the paper yet. The push is the
    #         scene's first real camera move. The hand is
    #         in frame, the coat is in frame, Aeron is out
    #         of focus behind her hand. The paper is the
    #         next object in the scene that exists.
    # LIGHTING: the alcove is backlit from the corridor
    #           end. Selene's face is half-shadowed. She
    #           stands slightly turned — not fully facing
    #           him, not fully facing away. The half-turn
    #           is the shape of someone delivering news
    #           she has not rehearsed.

    sel "I received a message yesterday evening. Nineteen-forty-two hours, through a relay chain I have not used since the Stillwater year."

    "Her hand goes to her inside coat pocket. It stops there. She does not pull the paper out yet. The hand is a fist around the paper through the coat lining."

    sel "The relay chain was Liora's. Not the Ghostline. Older. A route she kept going for the pre-Phoenix courier work. I have not heard traffic on that route in nine years."

    "She looks at him for the first time since they entered the alcove."

    sel "Liora was killed in the Orrery. You know that. You were there when Zira surfaced the confirmation."

    a "I was there."

    sel "What you do not know — what I did not know until yesterday evening — is that Liora sent a final packet before she went in. She keyed it to a delayed relay. The relay sat on the packet for the full mourning window and the routing delay and the confirmation cascade, and then it fired. It fired yesterday evening. The packet arrived on my handset at nineteen-forty-two."

    sel "I did not open it until twenty-three-ten. I needed the hours between."

    athought "She is telling me the timing because the timing is part of the sentence. She is telling me she had the paper for three hours and twenty-eight minutes before she let herself read it."

    sel "I read it at twenty-three-ten. I read it four times between twenty-three-ten and midnight. I did not sleep after. I came to the annex with you at oh-four-fifty because I had already decided that the annex scene was the scene I owed you first. This scene is the scene I owe you second."

    sel "They are different scenes. I could not give them to you in the same hour. I am giving you the second one now."

    "She pulls her hand out of the coat pocket. The paper is a single folded sheet, the kind of thin durable courier stock that is used once and burned after. It is folded in thirds. It is unsealed — she has unfolded it and refolded it."

    sel "Before I give you this paper, I have to tell you what it says. I am not going to let you read it cold. The words on the paper are small and precise and if you read them cold you will read past them without understanding what they mean."

    sel "I am going to tell you what Liora told me. Then I am going to give you the paper. Then we are going to stand here for however long you need to stand here."

    # ========== PHASE 3 — THE SENTENCE ==========

    # CAMERA: single. Selene's face, three-quarters. The
    #         paper is still in her hand, not yet offered.
    #         Aeron is off-camera for this entire phase.
    #         The camera does not cut to him once. His
    #         presence is audible — the breath, the shift
    #         of weight, the cup moving in his hand — but
    #         he is not in the frame. The sentence is
    #         Selene's to deliver. The camera honors that.
    # LIGHTING: unchanged. Her face half-shadowed, the
    #           paper held at waist height. The hard
    #           corridor light.

    sel "In the annex this morning I told you that Kael had a wife named Rava and a daughter named Soren. I told you that the last time I saw Rava was six days before Stillwater, at a laundry collective in the Foundry Wards, and that she was carrying Soren on her hip. I told you that after Stillwater I lost the line on both of them. I told you I had understood for nine years that they did not survive the collapse of Kael's cell and the sweep that followed. I told you I had been carrying that understanding the way a person carries a stone in a boot — not every day, but every day that I ran."

    sel "What Liora's packet says is that the understanding was wrong in one half and right in the other half."

    "A pause. She looks down at the paper. She does not read from it. She has memorized the sentence."

    sel "Rava is dead. That half is right. Rava did not die in the immediate collapse of Kael's cell. She survived Stillwater by four days and then she did what I think I would have done in her position — she left. She took Soren and she went to ground in an Unders community in Sector 10. She raised Soren there for two years. Liora ran supplies through that community — quietly, off the Phoenix books — and she kept an eye on both of them without telling me because Rava had asked her not to tell me. Rava's reason was that she did not want Soren raised inside a war, and I was the war in a uniform."

    sel "I am not going to defend myself against that reason. The reason was correct."

    sel "Rava was killed two years later. In a sweep. In Sector 10."

    "A beat."

    sel "It was Operation 391. Your operation. You led the sweep."

    "The silence inside the alcove becomes a different kind of silence. The cup in Aeron's hand is audible for the first time — a faint ceramic tick as his grip shifts."

    sel "You did not know who she was. You did not know Kael had a wife. You did not know Kael was alive to have had a wife. The sweep was orders. You were twenty-four and you were running a perimeter clearance and you did what the order said to do. Liora's packet is explicit that she is not naming this as your fault. She wrote — I am quoting — *the name of the man who led the sweep is a man who did not know what he was doing to his own bloodline, and the not-knowing is a mercy the packet does not take away from him.* That is Liora's sentence. Not mine."

    sel "The second half of the understanding — the half that was wrong."

    "She looks up from the paper. She is looking at him again. The camera is still on her face. He is still off-frame."

    sel "Soren was not in the room when Rava was killed. She had been hidden at a neighbor's three alleys over. The neighbor was an older woman, part of the Unders community, not armed. The sweep did not reach that alley. When it was over, Liora's courier network was already moving — Liora had a protocol for extracting children from sectors that had been swept, and the protocol fired within the hour. A courier took Soren out of Sector 10 that night. Liora moved her to an Outlands safe house six days later."

    sel "Soren has been in the Outlands since 383 AC. She is eleven years old. She has been raised by a small community Liora trusted. She knows her father's name. She knows her mother's name. She knows her uncle's name."

    sel "Your niece is alive, Aeron. Liora sent the packet to tell me she is alive."

    # ========== PHASE 4 — THE RECEIVING ==========

    # CAMERA: slow push onto Aeron for the first time in
    #         the scene. He does not react the way a
    #         person reacts to good news. He reacts the
    #         way a person reacts to a sentence that has
    #         four separate weights in it and only one of
    #         them is good.
    # LIGHTING: unchanged.

    "Aeron does not move."

    "The cup in his hand does not move."

    "His face does not move."

    athought "Rava is dead. I killed Rava. I did not know I was killing Rava. I killed her in a sweep I ran two years into my command career, in a sector I had been given as a clearance objective, and the order was the order and the sweep was the sweep and the woman in the third house on the left of the second alley was my brother's wife."

    athought "My brother's wife had a daughter. The daughter is eleven. The daughter is alive."

    athought "Kael has a daughter."

    athought "Kael has a daughter and I took her mother from her."

    "He does not speak for a count of fourteen."

    "Selene does not speak either. She is not going to fill the silence. The silence is the honest response to the sentence she just delivered, and if she interrupts it she is interrupting Aeron doing the only thing he can do with the sentence, which is to sit inside it."

    "At the count of fourteen, Aeron's left hand — not the cup hand, the other one — lifts to his mouth and stops there. He does not put his hand over his mouth. He stops the motion halfway, the way a person stops a motion when he realizes there is no gesture that would help."

    "He lowers the hand."

    a "Selene."

    sel "I am here."

    a "Say the last sentence again. I heard it. I want to hear it again."

    sel "Your niece is alive. Her name is Soren. She is eleven years old. She is in the Outlands. Liora has been protecting her for seven years without telling me. Liora sent me the packet because she knew she was going to die in the Orrery and she had decided — the last decision she made before going in — that I needed to know, and through me, that you needed to know."

    sel "She is alive, Aeron."

    a "Okay."

    "He says it the way a person says okay when the word is the only word he trusts his mouth with."

    a "Okay."

    # ========== PHASE 5 — THE HANDOFF ==========

    # CAMERA: two-shot. The paper is the prop that
    #         anchors the frame. Selene's hand offers it
    #         across the alcove. Aeron's free hand — the
    #         not-cup hand — takes it. The takeover is
    #         slower than it needs to be. The paper is
    #         the scene's gravity now.
    # LIGHTING: unchanged.

    "Selene unfolds the paper halfway and folds it back. She is not going to read it to him. She is going to hand it to him. The unfolding and refolding is the small gesture of a person who needs her hand to remember it is a hand before she uses it for the thing it has to do."

    "She extends the paper."

    sel "Take it. Read it here. Read it once and do not read it again today. Tonight you can read it as many times as you need. For now, read it once. The words on the paper are Liora's words and they are going to hit you differently than my summary did. That is correct and that is supposed to happen."

    "Aeron takes the paper."

    "He reads it."

    "The camera does not show us the paper. The camera holds on his face. His face does one thing — a small tightening at the jaw, the kind of tightening that happens when a sentence on paper is smaller and more precise than a sentence spoken — and then it holds the new shape for the duration of the read."

    "He folds the paper in thirds again. He does not give it back. He holds it in the cup hand, under his thumb, the cup and the paper in the same hand now."

    a "Liora wrote 'the child has been told her uncle's name. She has not been told her uncle's face. If the two are ever placed in the same room, the placement should be a meeting she controls, not a meeting he expects.' Is that the sentence you were warning me about."

    sel "That is the sentence."

    a "Soren gets to decide whether she wants to meet me."

    sel "Soren gets to decide."

    a "Not me. Not you. Not Liora's courier chain. Soren."

    sel "Soren."

    a "Okay."

    "He says it a third time. The third okay is a different register than the first two. The first two were the okay of a man receiving a sentence. The third is the okay of a man accepting a rule."

    # ========== PHASE 6 — THE LEAVING ==========

    # CAMERA: pulls back one small step. Not a retreat —
    #         a release. The alcove gets its full depth
    #         back in the frame. Selene and Aeron are
    #         both inside it, both standing, neither of
    #         them ready to step out yet.
    # LIGHTING: unchanged. The hard corridor light is
    #           the same light it was when they walked
    #           in. The scene is not going to give them
    #           a different light.

    sel "I am not going to tell you what to do with the next hour. I am going to tell you what I did with my equivalent hour last night. I went to the bunk I have not slept in for a week and I did not sleep. I sat on the edge of it and I held the paper in my lap. I did not cry. I did not pray. I was not ready to do either of those things and I did not make myself do them."

    sel "If you need the bunk version of the next hour, go to your quarters. If you need to walk, walk. If you need Lyra, go to Lyra — she is the right person for this if you are in a praying shape, and I know she has not earned a priority over the other three yet, and I am telling you this as information, not as an instruction."

    sel "What I do not want you to do in the next hour is come back to the war room."

    sel "The war room is not where this sentence goes. You do not carry this sentence to a table with a map on it. You do not carry it to the brief. You do not carry it to Zira or to Tessa or to Noelle unless you are ready to say the sentence out loud to one of them, and if you say it to one of them you do not say it to the others today. This is not a distribution."

    sel "This is a compartment."

    sel "I have been carrying the Kael compartment for nine years. You now have a compartment of your own. The rule of compartments is that you carry them alone until you choose who to open them to. I am not going to make the choice for you. I am telling you the rule."

    a "I understand the rule."

    sel "I know."

    "A beat."

    sel "I am going back to the war room in five minutes because the war room does not know what just happened in this alcove and the war room has a full day of work. I am going to run that day. I am going to run it as well as I have ever run a day. I am going to run it with this sentence inside me the way I have been running days with the Kael compartment inside me for nine years, and I am going to be okay at it because running days is the thing I know how to do."

    sel "You do not have to run a day today. I am going to tell the room you are on a personal assignment I gave you this morning, and the room is going to accept that because the room trusts me, and the assignment will be real because the assignment is to carry this sentence through the next twelve hours without doing anything stupid with it."

    sel "That is the assignment."

    a "Copy."

    sel "Aeron."

    a "Yeah."

    sel "One more thing, and then I am going to walk out of this alcove first."

    sel "The sentence on the paper is not the end of the Kael story. It is a turn in the Kael story. I do not know where the turn goes. I do not know if there is a meeting with Soren at the end of the turn. I do not know if Soren wants a meeting, and I am not going to ask her through a courier chain because asking her through a courier chain is the kind of command-move that would make the meeting a meeting I engineered and not a meeting she chose."

    sel "The turn goes where Soren decides it goes. Our job — yours and mine — is to be the kind of people she could choose, if she chooses."

    sel "That is the whole lesson of the annex this morning, applied to this sentence. I am only realizing it now. I did not know I was about to get a demonstration of the lesson within four hours of delivering it."

    a "Shared command."

    sel "Shared command. Applied to a sentence neither of us gets to command."

    "She steps past him — not around him, not through him, past him, shoulder brushing shoulder in the narrow alcove, the brush the small physical fact of the scene — and out into the corridor. She does not look back."

    "Aeron stays in the alcove. The cup is in his right hand. The paper is under his thumb in the same hand. His left hand is at his side, open."

    "The light from the corridor does not change."

    "The scene ends with him still standing in the alcove, not looking at the paper, not looking at the corridor, not looking at the bench, looking at nothing in particular, which is what a person looks at when a sentence has just entered him and has not found a place to sit down."

    # stop ambient fadeout 3.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Selene", trust=1)
    $ flag("selene_delivered_liora_word", True)
    $ flag("aeron_knows_rava_was_stillwater_wife", True)
    $ flag("aeron_knows_he_killed_rava", True)
    $ flag("aeron_knows_soren_alive", True)
    $ flag("liora_final_packet_delivered", True)
    $ npc_remember("Selene", "delivered_liora_packet_to_aeron", tone="shared_compartment")
    $ npc_remember("Aeron", "received_soren_alive_sentence", tone="unplaced_weight")
    $ npc_remember("Aeron", "read_liora_final_packet", tone="compartment_opened")
    $ canon_set("aeron.rava_knowledge", "knows")
    $ canon_set("aeron.soren_knowledge", "knows_alive")
    $ canon_set("aeron.stillwater_sweep_recontextualized", True)
    $ canon_set("selene.kael_compartment_state", "shared_with_aeron")
    $ canon_set("liora.final_packet_delivered", True)
    $ metric("aeron_compartments_held_alone", change=1)
    $ tp_seed("a4.selene.liora_packet")
    $ tp_seed("a5.soren.possible_meeting")
    $ scene_mark(_current_scene_id, "completed")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s10a_liora_sent_word_emp
# cann.chapter: Act IV, Chapter II — Shared Authority (Phase II) — CODA
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Same morning as a4_s10. Approximately oh-nine-forty, immediately after
#     the morning brief that Selene ran per the a4_s10 close. Selene pulls
#     Aeron from the post-brief dismissal and walks him to a narrow alcove
#     in a secondary corridor two turns off the war room. The scene is
#     roughly ten to fifteen minutes long in story time.
# cann.what_happened:
#   - Selene delivers Liora's final packet. The packet reached her the
#     previous evening at nineteen-forty-two hours via an older relay route
#     Liora had kept going for pre-Phoenix courier work. Selene read the
#     packet at twenty-three-ten and sat with it for the remainder of the
#     night. She delivered the a4_s10 thesis scene first, on purpose, before
#     delivering this coda. The two scenes are intentionally sequenced.
#   - The packet's content, as summarized by Selene and then handed to
#     Aeron as a single folded sheet of thin courier stock:
#       1. Rava survived Stillwater by four days, then left the Phoenix
#          base with Soren and went to ground in an Unders community in
#          Sector 10. Liora ran supplies through the community and
#          maintained oversight without telling Selene because Rava had
#          asked her not to. Rava's reason: she did not want Soren raised
#          inside a war, and Selene was the war in a uniform.
#       2. Rava was killed two years later in a sweep. The sweep was
#          Operation 391. Aeron led the sweep. Aeron did not know who
#          Rava was. Liora's packet is explicit that the not-knowing is a
#          mercy the packet does not take away from him.
#       3. Soren was not in the room when Rava was killed. She had been
#          hidden at a neighbor's three alleys over. Liora's courier
#          network extracted her within the hour of the sweep ending and
#          moved her to an Outlands safe house six days later. Soren has
#          been in the Outlands since 383 AC, raised by a small community
#          Liora trusted. She is eleven years old in the scene's present.
#          She knows her father's, mother's, and uncle's names.
#   - The packet's instruction clause, quoted verbatim in Aeron's voice in
#     Phase 5: "the child has been told her uncle's name. She has not been
#     told her uncle's face. If the two are ever placed in the same room,
#     the placement should be a meeting she controls, not a meeting he
#     expects." This instruction governs the Act V meeting scene.
#   - Aeron's response is not catharsis. The scene is explicit that the
#     sentence enters him and does not find a place to sit down. He says
#     "okay" three times. The third okay is the okay of a man accepting a
#     rule — specifically, the rule that Soren gets to decide.
#   - Selene frames the next twelve hours as a compartment Aeron has to
#     carry alone until he chooses who to open it to. She tells him the
#     war room is not where the sentence goes. She tells him his
#     assignment for the day is to carry the sentence without doing
#     anything stupid with it.
#   - Selene leaves the alcove first. Aeron remains inside it at scene
#     close, cup and paper in the same hand, looking at nothing in
#     particular.
# cann.aeron_state:
#   - Still carrying the water cup from a4_s10. The cup has now been
#     joined by Liora's folded packet. Both in his right hand, the paper
#     under his thumb. The cup-and-paper composite prop is the physical
#     form of two unplaced weights.
#   - Internal state at close: "shared compartment, not yet opened." He
#     has not decided who to tell. He has not decided whether to tell
#     anyone today. The compartment is the assignment.
#   - He now knows: (a) Kael had a wife named Rava, (b) Rava was killed
#     in his own sweep in Sector 10, (c) he did not know who she was at
#     the time, (d) Kael has a daughter named Soren, (e) Soren is alive,
#     (f) Soren is in the Outlands, (g) Soren gets to decide whether she
#     wants a meeting.
# cann.selene_state:
#   - This is the second scene of her day in which she has opened the
#     Kael compartment. The first (a4_s10) transmitted the shared command
#     lesson via the Kael story. This one transmits the update to the
#     Kael story that she herself received the previous night.
#   - She explicitly names, in Phase 6, that she is realizing in the
#     moment that the annex lesson ("shared command, ontology before
#     workflow") applies to the Soren situation. The scene is the first
#     real-time demonstration of the lesson, applied to a sentence
#     neither she nor Aeron gets to command.
#   - She does not cry in this scene. The scene is cold — hard light,
#     standing only, narrow alcove, clipped register. The coldness is
#     intentional and load-bearing. The warm scene is a4_s10. This is
#     the scene that follows it and has to be different.
# cann.path_tracking:
#   - EMP path only. Linear. No branching, no player choice. Coda to the
#     a4_s10 thesis scene.
#   - rel_bump Selene +1 trust. She has now transmitted the second half
#     of the Kael compartment, which she has been carrying for less than
#     a day and which she did not have to share.
#   - flag selene_delivered_liora_word True. This flag gates Act V
#     niece-meeting logic on the EMP path.
#   - flag aeron_knows_rava_was_stillwater_wife True. This flag governs
#     any Act IV Phase III beat where Rava could be referenced.
#   - flag aeron_knows_he_killed_rava True. This flag governs any beat
#     where Aeron's Operation 391 history is re-examined.
#   - flag aeron_knows_soren_alive True. This flag governs any beat
#     where Soren could be referenced.
#   - flag liora_final_packet_delivered True. This closes the Liora
#     posthumous-intelligence thread on the EMP path.
#   - canon_set aeron.rava_knowledge "knows".
#   - canon_set aeron.soren_knowledge "knows_alive".
#   - canon_set aeron.stillwater_sweep_recontextualized True. Any later
#     scene that references Operation 391 must read against this flag.
#   - canon_set selene.kael_compartment_state "shared_with_aeron".
#   - canon_set liora.final_packet_delivered True.
#   - metric aeron_compartments_held_alone incremented by 1.
#   - tp_seed a4.selene.liora_packet.
#   - tp_seed a5.soren.possible_meeting. This seed is the entry point
#     for the Act V meeting scene logic.
# cann.thematic_flags:
#   - The compartment rule: "You carry them alone until you choose who to
#     open them to." Selene's explicit formulation. Load-bearing for any
#     later scene where Aeron is deciding which LI (if any) to tell.
#   - The annex lesson applied in real time: shared command as an
#     ontology, applied to a sentence neither Selene nor Aeron gets to
#     command. This is the scene's thesis — and it is a thesis that only
#     lands because a4_s10 delivered the abstract form four hours earlier.
#   - Soren's agency: Soren decides whether she wants a meeting. The
#     scene does not let Aeron, Selene, or Liora's chain override that.
#     This rule governs the Act V scene.
#   - The mercy clause: Liora's line about the not-knowing being a mercy
#     the packet does not take away from Aeron. This is not absolution.
#     It is a refusal to demand absolution be either granted or withheld.
# cann.character_moments:
#   - Selene: first time in Act IV she has stood for an entire scene. No
#     chair, no table, no sitting. The standing is the physical form of
#     a scene that is too sharp to be held seated.
#   - Selene: she tells Aeron the exact timestamps at which she received
#     the packet, read it, and decided how to deliver it. The precision
#     is the gesture of a person who knows that precision is the only
#     honesty she has to offer right now.
#   - Aeron: three okays. Each one a different register. The scene does
#     its emotional work through the register of that single word.
#   - Aeron: left hand lifts to mouth and stops halfway. This is the
#     scene's only visible gesture from Aeron. It is the gesture of a
#     person who realizes there is no gesture that would help.
#   - Aeron: reads the packet once and folds it back. Does not give it
#     back. Carries cup and paper in the same hand at scene close.
# cann.callbacks:
#   - a4_s10_what_selene_meant_emp: the thesis scene. This scene is its
#     direct coda. The two are structurally one delivery split across
#     two rooms and two registers.
#   - a1_s23_the_sweep: Operation 391 in Sector 10. This is where Rava
#     was killed. The scene now canonically reinterprets that earlier
#     scene. Any replay of a1_s23 after this flag fires should read
#     against it.
#   - a1_s20_lower_spans: the child-between-pipes encounter. The child
#     is canonically Soren at age 4. This scene does not reference a1_s20
#     by name — the reference is load-bearing for the Act V meeting
#     scene, not for this one. This scene establishes the knowledge
#     that will make the a1_s20 gate activate in Act V.
#   - a3 Liora EMP climax: Liora's death in the Orrery is referenced in
#     Phase 2 as the event that keyed the delayed relay. The exact scene
#     ID should be confirmed in a later pass.
# cann.block_status:
#   - MINOR SCENE, LOAD-BEARING. Linear. EMP path only. Coda to a4_s10
#     and precondition for Act V meeting-scene logic on the EMP path.
# cann.requires_followup:
#   - The a1_s20 Lower Spans encounter must retroactively be treated as
#     the Soren-recognition gate. See game/act5/notes_niece_meeting_scene.md.
#   - The Act V meeting scene has not been written. The outline lives in
#     game/act5/notes_niece_meeting_scene.md. Any reference to Soren
#     between this scene and the Act V meeting must respect Liora's
#     instruction: the meeting, if it happens, is Soren's to control.
#   - The paper prop (Liora's folded packet) is now in Aeron's possession.
#     Future scenes may reference it. The cup from a4_s10 is in the same
#     hand. Any later scene where Aeron puts down one but not the other,
#     or both, or neither, is a canonical choice that carries weight.
#   - "Compartment" is now a named concept in Selene's vocabulary and in
#     the game's internal language. Future scenes where Aeron holds a
#     sentence alone before sharing it should use the word.
#   - The OB path equivalent of this scene does not exist and will not
#     exist. On OB, Liora is alive, holds the Soren information herself,
#     and delivers the meeting (if at all) in Act V. The OB path does
#     not need a coda to a4_s10 because a4_s10 is an EMP-only scene.
# =========================================================
