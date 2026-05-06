# =======================================================
# ACT 4 - Scene 20c: The Last Transmission (Empathy Path)
# File: a4_s20c_last_transmission_emp.rpy
# Type: ZIRA THESIS BEAT — Renn's last broadcast decrypted
# Matrix: Zira × Aeron. The eleven-year ritual completes.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s20c_last_transmission_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s20c_last_transmission_emp:
    $ show_timeline("4th of Glass, 390 A.C.", "03:14", "Phoenix Secondary Base — Zira's Workshop")

    # Codex stage bumps
    $ codex_reveal("zira", to_stage=4, source="a4_s20c_last_transmission_emp")
    $ codex_reveal("renn_kael", to_stage=4, source="a4_s20c_last_transmission_emp")
    $ codex_unlock("the_choice_at_the_console", source="a4_s20c_last_transmission_emp")
    $ codex_unlock("the_nine_names", source="a4_s20c_last_transmission_emp")
    $ codex_unlock("ghostline_voice_credential", source="a4_s20c_last_transmission_emp")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm. Zira's workshop. The room is smaller than the war
    #         room and smaller than Noelle's workspace and intentionally
    #         lower-ceilinged than either — the ceiling sits maybe
    #         seven feet at its lowest beam. The room is shaped like a
    #         person sitting in a closet. It is hers.
    #         Coverage opens tight on her hands at the cipher terminal.
    #         The hands are the scene's first subject — the same way
    #         Tessa's hands opened her surgical scenes. Zira's hands
    #         carry the eleven years. The terminal in front of her is
    #         a small custom rig: scuffed casing, cable-strain wraps,
    #         a tool-bound cipher-test station nobody else in the
    #         rebellion is allowed to touch.
    #         The two-shot for the listen sequence is Zira and Aeron
    #         seated in the workshop's only two chairs — one her
    #         working chair, one the spare she has had since the base
    #         rebuild and never offered to anyone before tonight.
    #         The chair is going to be Aeron's chair from this scene
    #         forward.
    #         The broadcast plays as audio against held two-shot.
    #         The camera does not cut to the speaker. The camera does
    #         not visualize Renn. The camera holds on Zira's face for
    #         the broadcast's first three minutes. The camera shifts
    #         to two-shot for the final ninety seconds. The camera
    #         does not push in. The push-in would be a directorial
    #         mercy the scene refuses.
    # LIGHTING: Workshop, late late night. Single overhead at half.
    #           The terminal screen glow. The three-core-node
    #           monitoring panel along the back wall — three small
    #           green lights at standard standby pulse. The pressed
    #           flower's oilskin sits in the drawer below the
    #           workstation; the drawer is closed at scene open. The
    #           lighting does not change across the scene. The room
    #           is the room.
    # SFX: Workshop ambient — the low hum of the cipher terminal,
    #      the further hum of Ghostline carrier hiss leaking through
    #      the monitoring panel, the far ambient of the base's
    #      overnight HVAC. The cipher terminal's micro-tone when it
    #      runs a cycle. One-shots: the cipher-completion chime
    #      (small, three-tone, distinct from the cycle tone — the
    #      audience is going to hear this only once); the workshop
    #      door open and close (twice — once when Zira leaves to find
    #      Aeron, once when she returns with him); the soft mechanical
    #      sound of Zira opening the lead-lined drawer beneath the
    #      workstation; the audio of the broadcast itself (the
    #      scene's load-bearing acoustic event); the four seconds of
    #      silence at the end of the broadcast that are the recording
    #      of the silence before Marcus shot Renn.
    #      No music bed. The scene refuses one. The broadcast is the
    #      only music the scene is willing to permit.
    # FACE: Zira — eleven-years face. The face she has been carrying
    #        through every Ghostline scene of the project, now
    #        receiving the thing she has been carrying it for.
    #        The face does not break early. The face holds through
    #        the technical first three minutes. The face begins to
    #        break in the final ninety seconds. The breaking is not
    #        catharsis. The breaking is information arriving.
    #        Aeron — receptive, deep into Act 4 receptive. He has
    #        been the receiver of compartments for two months by this
    #        point — Selene's Soren delivery, Noelle's Verdant
    #        decrypt, the Liora file. He recognizes the shape of
    #        the room when Zira brings him to it. He does not ask
    #        what is happening. He sits where she points. He
    #        listens.
    # BLOCKING: Zira at the cipher terminal for the first phase.
    #           Stands once — a small motion, the chair pushed
    #           back without sound — and walks out of the workshop
    #           to find Aeron. Returns with him. Sits him in the
    #           spare chair. Returns to her own chair. Plays the
    #           broadcast. Reaches for the drawer at the close.
    #           Touches the pressed flower without picking it up.
    #           Says one word at the end. The choreography is
    #           minimal. The minimum is the scene.

    # ========= VOICE BASELINE =========
    # Zira: workshop voice. Plainer than her Ghostline-coded operator
    #        voice. The tech metaphors thin out tonight. The voice that
    #        emerges as the technical voice fails is just hers — quiet,
    #        Unders-cadenced, eleven years patient. zthought interior
    #        carries the eleven years.
    # Aeron: minimal. Maybe four spoken lines across the entire scene.
    #         He says "Yeah" when she finds him, "Okay" when she
    #         points at the chair, the broadcast plays without
    #         interruption, and he says exactly one sentence after
    #         the broadcast ends. The sentence is short.
    # Renn (audio only): the broadcast itself. Renn's voice as
    #        established in canon — calm, technical, patient. The
    #        first three minutes are operational. The final ninety
    #        seconds shift register. Renn does not perform the
    #        shift. The shift is what happens to a man who knows
    #        he has two minutes left and has work to finish.

    # scene bg_zira_workshop_late with dissolve
    # play ambient "sfx/ambient/zira_workshop_terminal.ogg" fadein 2.0

    # ========== PHASE 1 — THE CYCLE ==========

    # CAMERA: 50mm. Open tight on Zira's hands at the
    #         cipher terminal. The hands are working
    #         the same sequence they have worked four
    #         thousand and eighty-three times. The
    #         keystroke pattern is muscle memory; the
    #         eyes are not on the screen. The eyes are
    #         on the corner of the screen where the
    #         progress indicator lives.
    # SFX: cipher cycle tone, low hum, carrier hiss
    #      leak from the monitoring panel.

    "The workshop at oh-three-fourteen. The base is in its deepest second-shift quiet. Zira is at the cipher terminal. Her hands are working the same sequence they have worked, by her own count, four thousand and eighty-three times."

    "She does not count the cycles aloud. She counts them privately, the way some people count rosary beads. The four thousand and eighty-three is the count as of last night's cycle. Tonight will be four thousand and eighty-four. The number is meaningless and the number is exact."

    zthought "Today's fragment came in at twenty-two-fifty-eight via the Sector Three maintenance pull. CAD-internal traffic burst, twelve-second window, returned a thirty-seven-byte block."

    zthought "Thirty-seven bytes."

    zthought "Eleven years and the largest single fragment I have ever pulled in one cycle. The largest before this was nine. Most cycles are zero or one."

    zthought "Thirty-seven."

    "Her fingers complete the load sequence. The fragment's thirty-seven bytes resolve in the test buffer. She tabs to the cipher-test routine. The routine is the routine. She has run the routine, by her own count, four thousand and eighty-three times. Tonight is the four thousand and eighty-fourth."

    zthought "Run."

    "She runs it."

    "The cipher terminal hums. The cycle tone holds. Zira watches the corner of the screen. The watching is the ritual. The ritual is the eleven years."

    zthought "Most nights the routine returns NULL within forty seconds. The longest cycle I've ever recorded was a hundred and sixty-two seconds — three years ago, on an eight-byte fragment that turned out to be padding. Tonight the cycle has been running for —"

    "She glances at the timer. Two minutes seven seconds. Three minutes. Three minutes forty-one. The cycle has not returned NULL. The cycle has not returned anything."

    zthought "It's not going to return NULL."

    zthought "I'm noticing what I'm noticing."

    zthought "I'm not letting myself notice it yet."

    "The cycle continues. Four minutes. Five. Six. The terminal's cycle tone has not faltered. The progress indicator has not changed for three of the last four minutes. The fragment is processing through the cipher's deepest layers — the layers Zira has been able to populate only with placeholder noise for eleven years because she did not have the key bytes to fill them."

    zthought "Tonight the layers aren't noise."

    zthought "I'm still not letting myself notice."

    "Six minutes forty seconds. The progress indicator moves a single pixel. Then another. Then it begins to advance."

    "It advances steadily for the next fifty-one seconds."

    "At seven minutes thirty-one, the cipher-completion chime sounds."

    "Three tones. Distinct from the cycle tone. Zira has heard the cycle tone four thousand and eighty-three times. She has never heard the completion chime. She has imagined what it would sound like. She had it wrong."

    "Her hands stop on the keyboard."

    "The terminal displays a single line at the corner of the screen, in the dim white text the cipher routine uses for completion notices:"

    "*DECRYPTION COMPLETE — 1 FILE — 5:12 AUDIO — RENN_FINAL_BROADCAST.wav*"

    zthought "Eleven years."

    zthought "Tonight."

    "She does not move."

    # ========== PHASE 2 — THE WALK ==========

    # CAMERA: pulls back from the terminal to a wider
    #         shot of the workshop. Zira at the chair.
    #         The terminal display reflected in the
    #         monitoring panel glass behind her. Three
    #         small green lights from the core nodes
    #         pulse at standard standby. The room
    #         feels smaller than it did at scene open.
    # LIGHTING: unchanged.

    "She does not play the file."

    "The reason is in her hands, which have not moved, and in her eyes, which have not left the corner of the screen where the completion notice sits."

    zthought "If I play it now, I play it alone, in this workshop, at oh-three-twenty-three on the fourth of Glass, and the playing is mine and the hearing is mine and the file becomes a thing that lives inside the workshop forever."

    zthought "I do not want it to live inside the workshop alone."

    zthought "I do not want to be the only person in the room when it plays."

    zthought "I have been alone with this for eleven years. I am not going to be alone with it for the playing."

    "She stands."

    "The motion is small. The chair pushes back without sound — Zira's chair has been on her own oiled tracks for years; she does not let it scrape. She stands and looks at the terminal one more time. The completion notice is still there. The file is still there. The file is going to be there in five minutes when she comes back."

    zthought "Aeron is in his quarters. He went to bed at twenty-two-thirty. He has been asleep for four and a half hours. I am going to wake him."

    zthought "I am going to wake him because he is the person I want in the room."

    zthought "I am not going to explain to him why he is the person I want in the room. He will not ask."

    "She walks to the workshop door. Opens it. The corridor outside is the second-shift quiet. She closes the door behind her."

    "The cipher terminal hums alone. The completion notice glows at the corner of the screen. The file waits."

    # ========== PHASE 3 — THE WAKING ==========

    # CAMERA: cut to the corridor outside Aeron's
    #         quarters. Zira at the door. She does
    #         not knock the way one knocks for an
    #         operational summons. She knocks twice —
    #         the soft Ghostrunner knock, the
    #         tap-tap she uses on Ghostline channels
    #         when she is sending a non-urgent ping.
    # LIGHTING: corridor at second-shift dim, the
    #           night-mode amber.

    "She knocks twice. Soft taps. The Ghostrunner ping."

    "The base is small enough that the knock is heard. Aeron has not been sleeping deeply tonight — he never sleeps deeply this late in Act 4, when the count of compartments is still exceeding the count of nights he has had to file them. He hears the knock. He registers the cadence."

    "The cadence is the Ghostrunner ping. The ping is Zira's. The ping is non-urgent."

    "He registers all of that in the first second. He is awake by the second second. He is at the door by the eighth."

    "He opens it. He is dressed in the layered base-night clothes he sleeps in. His hair is at sleep-rotation. He does not look surprised."

    "He looks at her face."

    "He sees what is on her face."

    "He does not ask."

    a "Yeah."

    "One syllable."

    "He pulls a coat from the hook by the door. He follows her without dressing further. He does not lock his quarters behind him. They walk the corridor together to her workshop. They do not talk."

    "She opens the workshop door. Holds it. He goes in first. She follows. She closes the door."

    "She points at the spare chair."

    a "Okay."

    "He sits."

    # ========== PHASE 4 — THE NAMING ==========

    # CAMERA: two-shot. Zira at her terminal chair,
    #         angled. Aeron in the spare chair, angled
    #         to her. The terminal between them, the
    #         completion notice still glowing at the
    #         corner of the screen. The workshop is
    #         the workshop.

    "Zira sits."

    "She does not look at the terminal yet."

    "She looks at her hands on her knees."

    z "Eleven years tonight. Four thousand cycles. The fragment landed twenty minutes ago."

    "She says it plainly. She is not sure who the sentence is for. Aeron hears it as the only context he is going to need. He registers the sentence and waits."

    z "The file is Renn's. He encrypted it in his personal cipher — one we built between us when I was twelve, never operational, never written down. I have been carrying the encrypted block for eleven years. I have been hunting the key bytes for eleven years. Tonight I have them."

    z "The file is five minutes and twelve seconds of audio."

    z "I think it is the broadcast he was running when Marcus shot him."

    z "I have not played it."

    z "I am going to play it now. I am playing it because I have decided I am playing it. I am playing it with you in the room because I am not going to be alone in the room when it plays."

    z "I am not asking you to do anything. You sit there. The audio plays. After it plays, we sit with it. That is the plan."

    a "Okay."

    "Same syllable from before. Same register. He has nothing else to offer; nothing else is needed."

    "She turns to the terminal. She calls up the file. Her hands are steady. The eleven years has trained the hands."

    "She presses play."

    # ========== PHASE 5 — THE TECHNICAL THREE MINUTES ==========

    # CAMERA: holds tight on Zira's face for the
    #         duration of the broadcast's first three
    #         minutes. Aeron is audible through the
    #         broadcast — small breath, a single shift
    #         in the chair at the two-minute mark —
    #         but visually he is out of frame. Zira's
    #         face is the scene. The face is doing the
    #         work the face has not had to do for
    #         eleven years, which is hear Renn speak
    #         and not have it be the same thirty-
    #         seven-second relay-junction recording.
    # SFX: the broadcast plays. Renn's voice. The
    #      voice that has been on Ghostline's three
    #      core nodes as a thirty-seven-second loop
    #      for eleven years. The same voice. Saying
    #      different words. The audience has heard
    #      the loop in pieces across earlier scenes;
    #      tonight the audience hears the voice say
    #      something it has not said before. The
    #      effect is supposed to be vertiginous.

    "The broadcast plays."

    "The first thing on the recording is Renn clearing his throat. A small wet sound. Zira has not heard Renn clear his throat in eleven years."

    "Then his voice, unmistakable — the voice from the relay junction reset. The patience. The tech-voice cadence."

    renn "(via recording) Successor channel. This is Renn at the Sector Twelve-B primary. If you are listening to this it means I did not make it back and the wafer made it to whoever is rebuilding. I am going to walk you through the priority items in the order I would want them rebuilt. I am going to be efficient. The walk is the walk."

    "Zira's hands stay on her knees. Her face does not change. The face is holding."

    renn "(via recording) Priority one. Repeater chains. You will find seven configured chains in the southern sub-mesh. Six are stable. The seventh is the one I rebuilt last week — node Corvid through the bird-feeder factory. The handshake on that one is non-standard. I built it asymmetric to keep it off Echelon's pattern reads. To replicate, you reverse the third-byte flip in the —"

    "He continues. The technical detail runs for ninety seconds. The detail is not the point. The voice is the point — the voice that has been a thirty-seven-second loop for eleven years, saying words it has not said before."

    "Zira's eyes have closed at some point in the ninety seconds. Aeron does not see when."

    "The broadcast continues. Repeater chain configuration. Beacon credential rotation. The geographic distribution Renn wanted for the first ten Ghostline nodes — the same distribution Zira used for the rebuild, eleven years later, because the wafer's partial map carried it. Zira is hearing, for the first time, the reasoning behind the choices she has been making for eleven years. The reasoning is not new to her. She has reverse-engineered it. The reasoning being said *aloud* by the man who wrote it is what is new."

    "Her hands have moved from her knees to the edge of the workstation. Aeron sees the move. He does not comment."

    "The broadcast hits the three-minute thirty-eight mark. Renn's voice shifts — not in pitch, not in tempo, just in *attention.* He has heard something."

    renn "(via recording) Z — I'm hearing them at the perimeter. Two minutes maybe."

    # ========== PHASE 6 — THE FINAL NINETY SECONDS ==========

    # CAMERA: shifts to a held two-shot. Zira and
    #         Aeron in the same frame for the first
    #         time during the broadcast. The shift
    #         is the camera registering that the
    #         scene has changed. Zira does not turn
    #         to Aeron. Aeron does not turn to Zira.
    #         Both of them face the terminal. The
    #         camera holds.
    # SFX: Renn's voice continues. The audience hears
    #      it as the broadcast hears it. No editorial
    #      treatment.

    renn "(via recording) I'm going to hold the post until the broadcast hits the seventeenth cell. After that, the repeater chain takes over. I configured it last week. You didn't know. Sorry — wanted you to have a redundancy you didn't owe me."

    "Zira's eyes are still closed. Aeron's face has the institutional stillness he has carried since the alcove with Selene."

    "The recording's ambient shifts. Some part of Sector 12-B's relay floor is audible behind Renn — small mechanical sounds, distant. Echelon is approaching. The sounds change."

    "Renn breathes once. The breath is on the recording. They hear it."

    renn "(via recording) You asked. I answered. I'd answer the same. Keep the line alive."

    "A pause. The smallest pause."

    renn "(via recording) Out."

    "The recording continues for four seconds after *Out.*"

    "Four seconds of silence. The silence is the recording of the silence before Marcus shot Renn. The silence has no sound except the very faint persistent hiss of the Sector 12-B relay floor and the very distant approach of Echelon at the perimeter. There is no gunshot in the recording. The recording cuts out at four seconds."

    "The cipher terminal returns to ambient hum."

    # ========== PHASE 7 — THE ROOM ==========

    # CAMERA: holds the two-shot. Zira and Aeron in
    #         the same frame. Neither moves.
    # LIGHTING: unchanged.

    "The workshop is the workshop."

    "The cipher terminal hums."

    "The three core node lights pulse at standby."

    "Zira's eyes are still closed."

    "Aeron speaks."

    a "Z."

    "He uses the name Renn used. He chose it deliberately. The choice lands in the room. Zira's eyes open."

    a "I am here for whatever you need from this hour. I am not going to fill it with anything that is not yours to fill."

    "He says it plainly. The line is short. The line is what he has."

    "Zira does not respond immediately. She is not crying. The eleven-year face has not let her cry tonight. The crying is a budget she has not allocated and the lack of allocation is itself the work."

    z "You heard him."

    a "I heard him."

    z "He was good. He was so steady."

    "She is saying it like it surprises her. The surprise is that the eleven-year-built mental reconstruction of Renn is *less* than the recording. The recording is more than the memory. The memory has been thinner than the actual man. She has been carrying a smaller version of him."

    z "He was so much him."

    "She says it twice."

    z "He was so much him."

    "Aeron does not respond. He waits."

    z "I have been carrying half of him. The half I rebuilt from the wafer. Tonight he became more. The more is information. I do not know what to do with the more."

    a "You do not have to do anything with it tonight."

    z "I know."

    "She closes her eyes again. Briefly. Opens them."

    # ========== PHASE 8 — THE NAMES ==========

    z "I want to tell you nine names."

    a "Okay."

    z "Tev. Kessa. Ami. Yves."

    "She pauses after each name. Aeron does not interrupt. The naming is its own pace."

    z "Sera. Linn. Halix. Doss. Brann."

    z "They are the nine I could not save. The nine in Ash-Nine."

    z "Tev was fifteen. Kessa was seventeen. Ami and Yves were eighteen. They were the four young ones at the relay floor when the choice landed. They would have lived if I had pushed the override. I did not push the override. They died at their posts."

    z "Sera and Linn were Kira's parents."

    "She watches Aeron's face for the recognition. The recognition arrives. She does not pause for him to respond. She continues."

    z "Sera and Linn were going to die regardless of the override. So were Halix and Doss and Brann. They were the senior operators. The override would not have reached them in time. Their deaths are a different math. I carry them anyway. The carrying is not interested in the math."

    z "I have been transmitting the nine names through Ghostline's encrypted layer for eleven years. They are the salt for the network's authentication routine. Every burst transmission across Ghostline carries them. The network cannot validate a packet without them. I built remembrance into the protocol. I did it without telling anyone. I am telling you now because tonight is the night I am no longer the only person who knows."

    a "I have been carrying the salt."

    z "Yes. Every time you have used a beacon credential. Every Ghostline-mediated scene of your life since Obsidian Bridge. The salt is the salt. You have been authenticating against the nine names for over a year."

    "A pause."

    z "The credential signature on the chip carries something else."

    z "Renn."

    z "The thirty-seven-second relay-junction recording is the frequency-domain anchor for Ghostline's credential validation. Every chip I have ever issued carries a fragment of his voice as its signature. Validating a credential means matching the fragment against the canonical recording on the three core nodes."

    z "The chip I gave you at the bridge carries his voice."

    z "I gave you my brother's voice as your key to my network. You have been authenticating against him since Act One. He has not been the file. He has been the door."

    "Aeron's left hand lifts halfway and stops. The same halfway gesture from the alcove with Selene. The gesture of a person who realizes there is no gesture that would help."

    "He lowers the hand."

    a "Zira."

    z "I know."

    a "Thank you."

    "He does not elaborate. Thanking her is the small word. The small word is what is available."

    z "You are welcome."

    "She means it. The two-word exchange holds.”

    # ========== PHASE 9 — THE FLOWER ==========

    # CAMERA: Zira's hand reaches toward the lower
    #         drawer beneath the workstation. The
    #         camera follows the hand. The drawer
    #         opens. The oilskin packet is inside.
    #         She unfolds the oilskin. The pressed
    #         winterbloom resolves. Camera tight on
    #         the flower, on her hand at the edge
    #         of it.
    # LIGHTING: unchanged.

    "Zira opens the lower drawer."

    "Aeron has not seen her open the drawer before. He has seen the drawer. He has known the drawer is sealed. The opening is its own disclosure."

    "Inside the drawer: an oilskin packet, folded in fourths. The wafer's lead-lined sub-compartment is to the right of the packet. She does not touch the wafer. She lifts the oilskin out and sets it on the workstation."

    "She unfolds the oilskin. The pressed winterbloom resolves on the cloth. The flower is the flower from a3_s19b — the one Selene gave her, pre-displacement, the one she has not touched."

    "Zira looks at the flower."

    "She rests her hand on the cloth beside the flower. Not on the flower itself. The hand rests for two seconds. Then she moves the hand the half-inch."

    "Her fingers touch the pressed flower for the first time in canon."

    "She does not pick it up. She just touches it. The touch lasts perhaps four seconds. It is the smallest gesture in the scene, and the only one that matters."

    "She does not move the flower from the cloth. She does not return it to the oilskin. She leaves the oilskin open, the flower exposed, the drawer open."

    z "I have been carrying that for two months. I would not let myself touch it. Selene gave it to me before the displacement. She did not say what it was for. I think she knew what it would be for. I think she saw something in me that needed an object that was *from before* and I did not want the object because I did not want there to be a *before* I needed the object for."

    z "There is a before. There is always a before. The before is the night Renn answered."

    z "I am keeping the flower on the bench. The drawer stays open."

    # ========== PHASE 10 — OUT ==========

    # CAMERA: pulls back slowly to a wide on the
    #         workshop. Zira at the workstation, the
    #         flower on the cloth, the drawer open.
    #         Aeron in the spare chair. The cipher
    #         terminal still glows the completion
    #         notice in the corner of the screen.
    #         The three-core-node monitoring panel.
    #         The room is the room.
    # LIGHTING: unchanged. The room has not changed.
    #           The room is different.

    "Zira turns back to the cipher terminal."

    "She does not close the file. She files it in a private archive of her own — a single encrypted store separate from Ghostline's distributed storage. The file is going to live in the workshop with her. It is also going to live, from this hour forward, on a backup she will create tomorrow at one of the three core nodes. She does not tell Aeron about the backup. She has decided already."

    "She closes the cipher-test routine. The completion notice clears from the screen."

    "She types one line into her personal Ghostline operator log. The log is the small private journal she keeps for her own work — the journal nobody else reads. The line is dated 4 Glass 390 oh-three-fifty-six."

    "*Cipher decryption complete. File received. Aeron in the room. Out.*"

    "She has not used the word *Out* in her log before tonight. Her standard sign-off has been *Z. close.* — operational shorthand. Tonight is the first time she has signed off as *Out.*"

    "The word is hers now."

    "She did not earn it. He gave it to her. It is the same word for both reasons."

    "Aeron sees the word resolve on the screen as she types it. He recognizes it. He does not name the recognition aloud."

    z "I am going to close the workshop in five minutes. You can stay in the chair until I do. After that we walk back to the corridor. The hour after this hour is yours."

    a "I will stay."

    "She nods once."

    "Five minutes pass. Neither of them speaks. The workshop ambient hums. The three core nodes pulse at standby. The flower stays on the cloth."

    "At oh-four-oh-one Zira stands. She does not close the drawer. The flower stays on the bench."

    "She walks Aeron to the workshop door. He follows her into the corridor. The door closes behind them. The workshop is empty."

    "The cipher terminal hums alone. The completion notice has cleared. The flower is on the cloth in the open drawer. The wafer is in its lead-lined sub-compartment. Renn's broadcast is in the private archive and is going to be backed up to a core node tomorrow."

    "Out."

    "Fade."

    # stop ambient fadeout 4.0
    # scene black with fade

    # ========= STATE UPDATES =========
    $ flag("last_transmission_complete", True)
    $ flag("zira_renn_letter_decrypted", True)
    $ flag("breach_choice_disclosed_emp", True)
    $ flag("nine_names_disclosed_emp", True)
    $ flag("beacon_chip_renn_voice_disclosed_emp", True)
    $ flag("flower_kept_on_bench_emp", True)
    $ flag("zira_out_signoff_active_emp", True)
    $ flag("marna_disposition_locked_faber", True)
    $ canon_set("zira.renn_letter_decrypted", True)
    $ canon_set("marna.disposition_signed_by_faber", True)
    $ canon_set("zira.choice_disclosed_to_aeron_emp", True)
    $ canon_set("zira.nine_names_disclosed_aloud_emp", True)
    $ canon_set("zira.flower_position_emp", "on_bench_drawer_open")
    $ canon_set("zira.signoff_default_emp", "Out")
    $ canon_set("aeron.knows_choice_at_console", True)
    $ canon_set("aeron.knows_nine_names", True)
    $ canon_set("aeron.knows_beacon_chip_carries_renn", True)
    $ canon_set("aeron.workshop_chair_assigned_emp", True)
    $ canon_set("renn.last_broadcast_received_by_zira", True)
    $ canon_set("renn.last_broadcast_audience_count_emp", 2)
    $ rel_bump("Zira", trust=4, affection=2)
    $ npc_remember("Zira", "decrypted_renn_letter_after_eleven_years", weight=4)
    $ npc_remember("Zira", "played_broadcast_with_aeron_in_room", tone="not_alone_for_the_playing")
    $ npc_remember("Zira", "named_nine_aloud_first_time", tone="memorial_externalized")
    $ npc_remember("Zira", "told_aeron_chip_carries_renn", tone="gift_named")
    $ npc_remember("Zira", "touched_pressed_flower_first_time", tone="from_before_acknowledged")
    $ npc_remember("Zira", "used_out_as_signoff_first_time", tone="word_inherited")
    $ npc_remember("Aeron", "called_her_z_renns_name", tone="vocabulary_received")
    $ npc_remember("Aeron", "received_choice_at_console_disclosure", tone="grief_witnessed_not_solved")
    $ npc_remember("Aeron", "thanked_her_for_credential_disclosure", tone="gift_acknowledged_quietly")
    $ npc_remember("Aeron", "stayed_silent_for_broadcast_duration", tone="held_the_room_the_way_she_asked")
    $ tp_seed("a4.zira.broadcast_received")
    $ tp_seed("a4.zira.choice_witnessed")
    $ tp_seed("a4.aeron.renn_voice_credential_understood")
    $ tp_seed("a4.zira.flower_touched")
    $ tp_seed("a4.zira.out_inherited")
    $ tp_seed("a5.zira.backup_to_core_node_pending")
    $ metric("zira_compartments_externalized", change=4)
    $ scene_mark(_current_scene_id, "completed")
    call li_lore_check("Zira") from _a4_s20c_lore
    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s20c_last_transmission_emp
# cann.chapter: Act IV — Shared Authority — ZIRA THESIS BEAT
# cann.chapter_start: False
# cann.path_tracking: EMP
# cann.when_in_timeline:
#   - 4 Glass 390 AC. Oh-three-fourteen to oh-four-oh-one. Forty-seven
#     minutes. Late late night. Approximately twelve hours after
#     a4_s20b (Verdant Decrypt EMP). Aeron has been asleep for four
#     and a half hours when Zira knocks.
#   - Eleven years and one month after the Breach. Four thousand and
#     eighty-fourth cipher cycle Zira has run on Renn's encrypted file.
#     The first cycle that did not return NULL.
# cann.what_happened:
#   - Zira at the cipher terminal, running her nightly ritual on Renn's
#     encrypted block. The fragment from a CAD-internal traffic burst
#     pulled at twenty-two-fifty-eight via Sector Three maintenance is
#     thirty-seven bytes — the largest single fragment ever pulled in
#     a single cycle. The cipher cycle runs for seven minutes thirty-
#     one seconds. The completion chime sounds. The decryption is
#     done.
#   - The decrypted file: RENN_FINAL_BROADCAST.wav, five minutes
#     twelve seconds. Renn's last broadcast. The thing he was
#     transmitting when Marcus shot him.
#   - Zira does not play the file alone. She walks to Aeron's
#     quarters at oh-three-thirty-something, knocks the soft
#     Ghostrunner ping, brings him to the workshop. He follows
#     without questions. She names the eleven years, the four
#     thousand cycles, the file.
#   - The broadcast plays. First three minutes: Renn's working
#     session, technical successor instructions. Repeater chains,
#     beacon credentials, the geographic distribution Renn wanted
#     for Ghostline's first ten nodes (the same distribution Zira
#     used for the rebuild — she has been hearing the reasoning
#     behind her own choices for the first time).
#   - Final block: Renn aware of the breach proximity. Discloses the
#     repeater chain redundancy ("I configured it last week. You
#     didn't know."). Then five compressed sentences that carry the
#     entire validation: "You asked. I answered. I'd answer the
#     same. Keep the line alive. Out." The compression is the load.
#     The conversation Zira has been imagining for eleven years was
#     longer than the actual broadcast. The not-getting-to-the-rest
#     is its own grief.
#   - Four seconds of silence in the recording after Out. The
#     silence is the recording of the silence before Marcus shot
#     Renn. No gunshot in the file.
#   - Aeron speaks once after the broadcast: "Z." He uses the name
#     Renn used. Then: "I am here for whatever you need from this
#     hour. I am not going to fill it with anything that is not
#     yours to fill."
#   - Zira: "He was so much him." Said twice. The eleven-year-built
#     mental reconstruction of Renn was thinner than the actual
#     recording. The recording is more than the memory. The
#     memory has been carrying half of him.
#   - Zira names the nine. Aloud for the first time. Tev (15),
#     Kessa (17), Ami (18), Yves (18) — the four young at the
#     relay floor. Sera, Linn, Halix, Doss, Brann — the five
#     senior. Names Sera and Linn as Kira's parents.
#   - Zira discloses the cryptographic salt mechanic: the nine
#     names are Ghostline's authentication salt. Aeron has been
#     carrying them in his beacon credential since Obsidian
#     Bridge. The network cannot validate without them.
#   - Zira discloses the Beacon Chip's voice carrier: Renn's
#     thirty-seven-second relay-junction recording is the
#     frequency-domain anchor for credential validation. Aeron
#     has been authenticating against Renn's voice since Act I.
#     "I gave you my brother's voice as your key to my network."
#   - Aeron's only other line: "Thank you." Zira: "You are
#     welcome." The two-word exchange holds.
#   - Zira opens the lower drawer. Unfolds the oilskin. Touches
#     the pressed winterbloom for the first time in canon. Does
#     not pick it up. Leaves it on the cloth. Drawer stays open.
#     "I am keeping the flower on the bench."
#   - Zira files the broadcast in private archive. Plans backup
#     to a core node tomorrow (does not tell Aeron). Types her
#     personal log entry: "Cipher decryption complete. File
#     received. Aeron in the room. Out." First use of *Out* as
#     sign-off in her vocabulary.
#   - Five minutes of silence in the workshop. Aeron stays in
#     the chair until Zira stands. They walk to the corridor
#     together. Workshop door closes. Workshop empty. Cipher
#     terminal humming alone. Flower on the cloth in the open
#     drawer.
# cann.zira_state:
#   - Eleven years of decryption work completes. The hunt that
#     has structured every Ghostline maintenance cycle for over
#     a decade ends tonight.
#   - The Choice at the Console is externalized to Aeron for the
#     first time. The eleven-year carry is no longer alone.
#   - The nine names are spoken aloud. The salt is named.
#   - The Beacon Chip's voice carrier is disclosed. The gift is
#     acknowledged.
#   - The pressed flower is touched. Drawer stays open. Flower
#     stays on the bench. Sentimental keeping is canon.
#   - *Out* is inherited from Renn as her personal sign-off. The
#     word is hers from this scene forward. EMP only.
#   - The grief is not lighter. The grief is witnessed. The
#     carrying is no longer alone.
# cann.aeron_state:
#   - Receives the broadcast in silence. Does not interrupt. Does
#     not solve. Does not console.
#   - Says "Yeah" at his quarters door, "Okay" when she points
#     at the chair, "Z" after the broadcast (using Renn's name
#     for her), "I am here for whatever you need from this hour.
#     I am not going to fill it with anything that is not yours
#     to fill," "Zira" (in response to her chip disclosure),
#     "Thank you," "I will stay." Approximately seven spoken
#     interventions across forty-seven minutes. Most of the
#     scene is silence-as-presence.
#   - Now knows: the Choice at the Console; the nine names; the
#     Beacon Chip's cryptographic anchor; the meaning of the
#     thirty-seven-second recording on the three core nodes.
#   - Has been assigned the spare chair in the workshop. The
#     chair is now his.
#   - The hand-on-console gesture (a meter from her, present,
#     not touching) translates here as the half-lifted hand that
#     stops halfway. He does not need to touch. The not-touching
#     is the work.
# cann.path_tracking:
#   - EMP path only. The OB equivalent (a4_s20c_last_transmission_ob,
#     pending) plays the structurally inverted scene: Zira decrypts
#     alone, plays the broadcast alone, files it alone, does not
#     touch the flower, does not name the nine to anyone, does not
#     adopt *Out* as sign-off. The disclosure is internal-only
#     because OB Aeron has not earned the broadcast.
# cann.thematic_flags:
#   - The Choice at the Console as canonical reframe of the Breach.
#     The "override misfired" framing is replaced. Zira asked.
#     Renn agreed. The math was right. The math killed Renn. The
#     grief structure is partnership-in-cost, not survivor's-guilt-
#     of-accident. Future Zira/Renn references should respect this
#     reframe.
#   - The nine names as cryptographic salt. Ghostline's
#     authentication system canonically requires the nine to be
#     transmitted with every packet. Future Ghostline references
#     should respect that the network's deepest layer is a
#     memorial.
#   - The Beacon Chip carries Renn's voice. The chip Aeron has
#     been carrying since the Bridge contains a frequency-matched
#     fragment of Renn's thirty-seven-second recording. Future
#     beacon-chip references should respect this.
#   - "Out" as Zira's inherited sign-off. The word is now hers.
#     Future Zira-closes-a-transmission scenes can use it. EMP
#     only. OB Zira's sign-off remains operational-standard.
#   - The pressed flower touched once and kept on the bench is
#     canon. Drawer stays open in EMP. Future workshop scenes
#     should respect the staging.
#   - "He was so much him." The recording-vs-memory disjunction
#     is canon. Zira's eleven-year mental reconstruction of Renn
#     was thinner than the actual recording. The recording is
#     additive grief — more of him to carry, not less.
#   - Renn's vocabulary for Zira: *Z* and *kid.* Never Zero. Zero
#     is not canon; it was author-process trivia.
#   - The Aeron-spare-chair-in-Zira's-workshop is canon. From
#     this scene forward, Aeron has a chair in her room. Future
#     Zira-workshop scenes should respect the assignment.
# cann.character_moments:
#   - Zira: four thousand and eighty-three prior cycles named
#     aloud as confirmation of the eleven-year ritual.
#   - Zira: walks to Aeron's quarters because she will not be
#     alone in the room when the broadcast plays. The decision
#     is the scene's first deliberate choice.
#   - Zira: knocks the Ghostrunner ping (soft tap-tap, non-
#     urgent). Aeron recognizes the cadence in seconds.
#   - Zira: "He was so much him." Said twice. The most compressed
#     Zira line in the scene.
#   - Zira: names the nine in order. The naming is the scene's
#     load-bearing public ritual.
#   - Zira: discloses the chip carries Renn. "I gave you my
#     brother's voice as your key to my network."
#   - Zira: touches the pressed flower for the first time. Does
#     not pick it up. Leaves it on the cloth. Drawer stays open.
#   - Zira: types *Out* in her personal log. First use as
#     sign-off in her vocabulary.
#   - Aeron: "Yeah" at the door. Single syllable. The scene's
#     first Aeron line.
#   - Aeron: uses Renn's name "Z" for Zira after the broadcast.
#     The choice is deliberate. The choice is acknowledgment.
#   - Aeron: "I am here for whatever you need from this hour. I
#     am not going to fill it with anything that is not yours
#     to fill." The Aeron-listening-doctrine articulated for the
#     first time in scene.
#   - Aeron: half-lifted hand that stops halfway after Zira's
#     chip disclosure. The presence-without-touch gesture from
#     a4_s09 returns here in its purest form.
#   - Aeron: "Thank you." Compressed acknowledgment.
# cann.callbacks:
#   - a1_s21_zira_first_contact: the Beacon Chip's first
#     appearance. Retroactively recontextualized — what Zira
#     gave Aeron at the Bridge was Renn's voice as credential.
#   - a1_s26_obsidian_bridge: the credential transfer. Aeron has
#     been carrying Renn since this scene.
#   - a2_s06 (Hand Off the Wire) and onwards: every Ghostline-
#     mediated Aeron scene retroactively becomes Aeron
#     authenticating against Renn's voice. The ambient weight
#     of the entire EMP Aeron-Ghostline relationship gets re-
#     read after this disclosure.
#   - a2_s10 (Static Faith): Zira's first direct naming of
#     Renn's execution. This scene is the long completion of
#     that disclosure.
#   - a2_s17 (Building Something): the thirty-seven-second
#     recording as kept memorial. Now contextualized as the
#     credential anchor.
#   - a2_int_01 (Signal Check): the exit plan, Aeron added to
#     non-negotiable list. The eleven-year carry was already
#     shaping the commitment.
#   - a3_s19b (Before the Weight, OB) — pressed flower
#     introduction. The flower is canon-locked here as Selene's
#     gift, pre-displacement. This scene is the EMP touch-and-
#     keep.
#   - a4_s09a (Noelle Defection Coda): structural twin in pass
#     architecture. Both scenes are eleven-year compartments
#     opening in solitary workshops. Noelle's compartment is
#     hidden trauma uncovered. Zira's compartment is named
#     trauma deepened. The two scenes pair as the project's
#     mirrored late-Act-IV grief beats.
#   - a4_s10a (Selene's Liora packet to Aeron): the scene
#     structurally rhymes — single delivery of a long-carried
#     compartment. Selene to Aeron : Zira to Aeron :: Liora to
#     Selene : Renn to Zira.
#   - canon_notes_zira.md: the full sec 2 (Choice at the
#     Console), sec 3 (Last Transmission), sec 4 (Nine Names),
#     sec 5 (Beacon Chip Carries Renn), sec 8 (Three Core
#     Nodes), sec 9 (Pressed Flower Extended), sec 10 (Out
#     sign-off) — all canon delivered here per spec.
# cann.block_status:
#   - MAJOR SCENE, LOAD-BEARING. Linear. EMP path only. Zira's
#     thesis beat. Foundational for: every subsequent EMP
#     Ghostline scene (Aeron now knows the credential anchor),
#     every subsequent Zira-Renn reference (Choice is now
#     canonized), every subsequent Kira scene (Sera and Linn
#     are now named in the salt), every subsequent workshop
#     scene (Aeron has a chair, the flower is on the bench, the
#     drawer is open).
# cann.requires_followup:
#   - The backup to a core node Zira plans for the next day is
#     unwritten. Author at discretion whether to dramatize.
#   - The Selene-knew-the-flower-was-for-this-purpose subtext
#     is open territory. Zira speculates Selene saw something
#     in her that needed an object. A future Zira-Selene
#     scene (impossible — Selene is dead by Act 4 EMP given the
#     chronology; Selene died in Act 2 OB; on EMP she is alive,
#     so a Selene reaction to the flower-touch is open authoring
#     territory if Aeron tells her).
#   - Whether Zira ever plays the broadcast for other LIs is
#     open. Default: she does not. The audience is Aeron. The
#     broadcast lives between Aeron and Zira from this scene
#     forward. Selene, Lyra, Tessa, Noelle, Kira do not hear
#     it by default. Author at discretion if a later scene
#     wants Zira to share with another character.
#   - Kira does not learn about the salt by default. If a future
#     scene wants Kira to learn that her parents' names are
#     embedded in Ghostline's authentication routine, that is
#     significant Act 5 material and is open authoring
#     territory.
#   - The Aeron-spare-chair-in-Zira's-workshop is now a fixture
#     in the room. Future workshop scenes should respect that
#     the chair has its place.
#   - *Out* propagates to Zira's Ghostline traffic from this
#     scene forward. Future Zira sign-offs in EMP scenes
#     default to *Out.*
#   - The flower stays on the bench. Drawer stays open. If a
#     future workshop scene closes the drawer, that closure is
#     a canonical inflection point and should be authored
#     deliberately.
# =========================================================
