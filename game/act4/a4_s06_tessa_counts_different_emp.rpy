# =======================================================
# ACT 4 - Scene 06: The Board (Empathy Path)
# File: a4_s06_tessa_counts_different_emp.rpy
# Type: TESSA STATE BEAT — evolved ritual, Aeron peripheral
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a4_s06_tessa_counts_different_emp"
$ scene_mark(_current_scene_id, "entered")

label a4_s06_tessa_counts_different_emp:
    $ show_timeline("26th of Forge, 390 A.C.", "05:30", "Phoenix Secondary Base — Medbay")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: Opens from Aeron's POV in the doorway. Shoulder-high, held back,
    #         voyeur framing that knows it is voyeur and respects it. First full
    #         view of the board across the secondary base's main medical wall.
    #         Macro on the marker tip when she lifts it. Macro on the letters
    #         forming — K for Kesa, J for Joren. The camera does not cut to
    #         Tessa's face during the writing. Face only after both names are
    #         down and the marker is capped.
    #         Closing beat: two-shot, both of them in frame, the board taking up
    #         most of the wall behind them. The two new names visible on both
    #         columns' new bottoms — dead side only. The camera holds.
    # LIGHTING: Main medical area, night shift. Work lights along the ceiling at
    #           half-power. A single clip lamp on the upper edge of the board
    #           that Tessa has installed herself — the same lamp from
    #           a3_int_tessa_the_board_emp, transported with the board across
    #           the displacement. The lamp is her light, not the building's.
    # SFX: Main medical area at night. Ventilation. A distant IV pump. Joran Tev
    #      sleeping on the cot across the room (callback to a4_s05a — he is still
    #      there). The squeak of the marker. Her breath. Aeron's breath, kept
    #      back at the door so he does not break her concentration. No music.
    #      One held string only at the last beat, very low.
    # FX/COMP: THE BOARD.
    #          Physical description: a large whiteboard mounted on a rolling
    #          frame. Original board from the first Phoenix base (a2_s14, a2_s16).
    #          Transported through the displacement after the Act 2 raid. Carries
    #          a faint shadow-pattern of the letters of former entries — the
    #          whiteboard has been erased enough times that the cleanest areas
    #          remember the old text as a ghost.
    #          Two columns. LIVING on the left. DEAD on the right. The header
    #          letters are Tessa's hand — the living header in her normal marker,
    #          the dead header in a slightly darker marker she uses only for
    #          headers because the distinction is a rule she set herself years ago.
    #          LIORA RYLAN appears on both columns. Both from Act III. Still there.
    #          Both entries are dated.
    #          The LIVING column is longer than the DEAD column. This has always
    #          been the board's shape. It is still the board's shape tonight.
    #          Below the LIORA RYLAN entry on the dead column, there is clean
    #          space for two new names.
    #          The marker lives on a small shelf just below the bottom edge of
    #          the board frame. Black fine-tip. One cap. No backup marker.
    # BLOCKING: Aeron enters the main medical area from the corridor. Tessa is at
    #           the board, back to the door. He stops in the doorway and watches.
    #           She does not turn. She knows he is there. She adds the names
    #           without acknowledging him. After the marker is capped, she turns.
    #           He enters. They stand side by side at the board for the closing.
    # FACE: Tessa — composed in the chosen way. The composure is a decision and
    #       she is aware of the decision. Aeron — quiet, reverent, the aftermath
    #       of sleep still visible in his face. He had five hours on the cot.

    # ========= VOICE BASELINE =========
    # EMP cadence. The scene is very quiet. Short sentences. The silences are
    # load-bearing, more than in any other scene in this run. Tessa's voice is
    # calibrated to the version of her from the board interlude — structural,
    # plain, the sentences with the "plain as teeth" edge but pulled back from
    # that sharpness into a quieter register. Aeron has almost no lines. The
    # scene is hers and he is entering it on her terms.

    # scene bg_medical_main_night with dissolve
    # play ambient "sfx/ambient/medbay_night_low.ogg" fadein 2.0

    # ========== PHASE 1 — THE DOORWAY ==========

    # CAMERA: opens from Aeron's POV in the doorway. Shoulder-
    #         high, held back. The frame is the width of the
    #         door and the room beyond: Tessa at the board
    #         with her back to us, the board filling the wall
    #         behind her, Joran Tev still asleep on the cot
    #         from a4_s05a in the middle distance. The camera
    #         knows this is voyeur framing and respects the
    #         distance by holding at the threshold — it does
    #         not enter the room when he does not.
    # LIGHTING: main medical night shift. Work lights at half-
    #           power across the ceiling. Tessa's clip lamp on
    #           the board is the brightest surface in the frame
    #           and it is HER lamp, transported with the board
    #           through the displacement. The lamp is the scene's
    #           claim that this is her space, not the building's.

    "Aeron wakes on the medbay cot at oh-five-thirty. The chair beside him is empty. Tessa's jacket is not on the back of it — she took it with her when she stood up, sometime after the sun came in, because Tessa does not leave evidence of a vigil when the vigil is over."

    "He does not wake her out of his sleep by looking for her. He wakes into the realization that she is no longer in the chair and that this is the correct shape for the morning."

    athought "Five hours. Maybe six. The monitor clip is off my finger. She took it off without waking me."

    athought "I have not slept five hours in one stretch since before the execution. That is a neutral fact. I am writing it down in my head as a neutral fact because if I let it be more than a neutral fact right now, I will not be able to stand up."

    "He stands up."

    "He puts his boots back on. His jacket is folded on the end of the cot — she folded it, too."

    "He does not go to the war room. He goes to find Tessa, because the scene they had in this medbay last night has a coda and both of them know it."

    "He does not have to look far."

    "She is in the main medical area, two corridors over, where the board lives."

    # ========== PHASE 2 — THE BOARD ==========

    # CAMERA: push from the doorway POV toward the board itself.
    #         Not a full dolly — a measured push that lands at
    #         medium-wide on the board with Tessa's silhouette
    #         in the near foreground. LIORA RYLAN is visible
    #         on both columns. The older entries from previous
    #         bases form a ghost pattern on the cleanest areas
    #         of the whiteboard surface — former names that
    #         have been erased enough times that they remain
    #         as residue. The camera lets the ghost be visible
    #         without calling attention to it.
    # FX/COMP: the ghost-pattern of erased former entries is
    #          the scene's most important visual texture. Every
    #          name on this board has been carried through two
    #          bases. The residue is the inheritance Tessa's
    #          hands have been making.

    "He stops in the doorway."

    "He does not enter."

    "The board is the first thing the door frame gives him. It takes up most of the opposite wall — rolling frame, tall as a person, wide as his arm-span. The ghost of old text in the white plastic. Tessa's clip lamp at the top. The header letters in her hand."

    "LIVING on the left. DEAD on the right."

    "The living column is long. It runs in columns of small capitals most of the way down the whiteboard. Names he knows. Names he does not. Phoenix fighters. Civilians. The woman from the Sector 9 camp who survived the mercy-death triage by being on the other side of the assessment that night. Joran Tev, the name transferred up to the living column some time in the last twelve hours because Tessa went and confirmed his stabilization at the shift change."

    "The dead column is shorter but not by as much as it used to be."

    "LIORA RYLAN is on both columns."

    "He has not seen the board since before the displacement. He knew the board had held through the move. He did not know the name was still on it twice. He knew it would be. That is a different thing."

    athought "She kept it."

    athought "She kept it on both sides through the displacement and the rebuild. Of course she did. Tessa would not have erased it any more than she would erase a diagnosis. The board is not a scoreboard. The board is a ledger."

    "And below LIORA RYLAN on the dead column, there is clean space."

    "Two name-widths of clean space, waiting."

    "Tessa is standing in front of the board. She has the marker in her right hand. The cap is in her left. She has not uncapped it yet."

    "She is looking at the clean space."

    "He does not enter. He stays at the door. He is not intruding on the ritual — he is bearing witness from the threshold because the threshold is the correct place to bear witness from and he has learned in the last twelve hours to pay attention to correct places."

    # ========== PHASE 3 — THE NAMES ==========

    # CAMERA: two macro inserts in sequence. (1) The marker tip
    #         lifting from the shelf below the board frame —
    #         black fine-tip, her fingers finding the cap,
    #         uncapping in one motion. (2) The letters forming
    #         on the whiteboard: K, E, S, A — then M, A, R, I, N.
    #         Then the second name. Hold each macro for the
    #         duration of the name. The camera does not cut to
    #         Tessa's face during the writing. Her face is not
    #         earned yet. After both names are down and the
    #         marker is recapped, cut to her face for the first
    #         time in the scene — single, profile, no push.
    # SFX: the squeak of the marker is the scene's primary
    #      sound event. Clean, dry, deliberate. The uncap and
    #      the recap are both audible. Between the two names,
    #      her breath holds once. The mix catches the hold.
    # FACE: Tessa — the composure is the decision-face. She has
    #        decided to write the names in this register and
    #        she is executing the decision. Not grieving. Not
    #        performing. Working.

    "She uncaps the marker."

    "The small plastic click is louder in the main medical area than it should be, the way the clasp click was louder in Lyra's quarters two nights ago."

    "She lifts the marker to the board."

    "She writes the first name."

    "K. E. S. A. space. M. A. R. I. N."

    "Her hand does not shake. The letters are the shape her hand makes them in, which is the same shape her hand has been making letters in for every name on this board for three years. She does not write slower for the new ones. She does not write faster."

    "She finishes KESA MARIN and the marker hovers for a fraction of a second at the final letter — not a hesitation, a punctuation. A small deliberate pause that used to be the place where she said the name aloud three times."

    "She does not say it aloud."

    "Her lips do not move."

    "She moves down one line."

    "She writes the second name."

    "J. O. R. E. N. space. H. A. L. E."

    "Same hand. Same speed. The final letter is the same punctuation-pause. The same silence."

    "She caps the marker."

    "Small plastic click."

    "She sets the marker on the shelf below the bottom edge of the board."

    "She does not step back."

    "Aeron does not breathe for a second. Not because he is shocked — because breathing would have been the wrong punctuation for the moment the cap went on. He will catch up on the breath in another second. The board has the rhythm of the room right now."

    "He takes the breath."

    # ========== PHASE 4 — THE THRESHOLD ==========

    # CAMERA: reverse on Aeron at the doorway, still held back.
    #         She turns. The turn is not for him — it is the
    #         natural move of a woman who has finished with the
    #         board and is now choosing whether to give him
    #         permission to enter. The permission is granted by
    #         her eyes. He crosses the threshold. The camera
    #         tracks him entering on the reverse, then cuts to
    #         the wide of both of them at the board.
    # BLOCKING: they stand side by side at the board, equal
    #           distance, neither in front of the other. The
    #           composition is a side-by-side of two witnesses.
    #           No physical contact. The space between their
    #           shoulders is the scene's measured quantity.

    "Tessa speaks without turning."

    t "You can come in, Aeron."

    "He comes in. He crosses the floor slowly. He stops two steps behind her — not close enough to crowd, close enough to see the names the way she is seeing them."

    "He reads both of them. KESA MARIN. JOREN HALE. The letters are ink-black and new against the whiteboard's ghost text. The rest of the dead column's entries have a faint softening from erasure attempts the board did not fully accept. The new names are sharper than the old."

    "He does not say the names aloud."

    "Neither does she."

    athought "She is waiting. She wants me to notice something and she wants me to notice it without her telling me what to notice."

    athought "I am going to do the work."

    "He looks at her hand. The marker is on the shelf. Her hand is at her side. Her thumb is at her own palm — not the Lyra gesture, a different one, the absent gesture of a woman who is holding a rule in her head."

    "He looks at her mouth. Her lips are parted but not shaping a word."

    athought "She did not say them."

    athought "She wrote them and she did not say them aloud."

    a "You did not say them."

    "She turns to him."

    t "I did. In my head."

    a "You used to say them aloud."

    t "I used to. I have stopped. Not all at once — it has been drifting for about six days. Tonight was the first time I wrote two names in one sitting without saying either of them out loud, and I noticed I had not done it and I decided not to fix it."

    "She turns back to the board."

    t "The rule was to say them three times."

    a "Your mother's rule."

    t "My mother's rule. She gave it to me when I was seven. The winter my father did not come back. She told me the rule was for the dead — I believed that for nineteen years. Then I figured out the rule was for me. The point of saying them aloud was not to prove to the universe that the dead were real. The point was to prove to the living that the living were still here."

    t "I said them aloud because I was the one who needed the sound in the room."

    t "I needed the sound in the room because silence scared me. Silence used to scare me because silence was the shape of the winter my father did not come back. Silence was the absence that had killed him, or so I thought when I was seven, and the rule was the thing I put in silence's way."

    "She is looking at the two new names. Not at Aeron."

    t "I have been saying names into rooms for three years. And the rooms have gotten quieter in spite of me."

    t "That is not a complaint. It is an observation about a ritual I am a long way into."

    # ========== PHASE 5 — THE EVOLUTION ==========

    t "The board has changed. Or I have."

    a "Is that good?"

    "It is the only question he has. He does not have a follow-up ready. He is not trying to lead her to a conclusion. He is asking for the reading."

    t "I do not know yet."

    t "I will tell you when I have added more names and it is still quiet and the quiet is still holding."

    t "I can tell you what it might be. I can tell you what I am afraid it might be. I can tell you what I hope it is."

    a "Tell me all three."

    "She is quiet for a long moment. Not because she does not have the answers — because she is arranging them in the order she trusts."

    t "What it might be is: the silence is no longer dangerous to me. It might be that I do not need the sound in the room because I am no longer performing the rule for my seven-year-old self. The seven-year-old has grown up. The grown-up knows that the silence is not the winter her father did not come back. The grown-up is okay with silence."

    t "What I am afraid it might be is: I have stopped feeling the names. That is the thing I am afraid of, always. That the ritual is the thing that keeps the names real to me and that when the ritual changes, the reality goes with it. I have watched medics in the field stop using their rituals. I have watched what happens to the medics afterward. They do not stop being able to work. They stop being able to grieve, and then they stop being able to work, and there is a gap between the two that nobody catches them inside of."

    t "I am trying not to fall into that gap."

    t "And what I hope it is — what I hope — is that I have company now. That the names are being held by more people than just me. That the sound I used to have to make into the room is a sound the room is starting to hold for me. And that the silence is the shape the holding has."

    "She looks at him."

    t "I am going to know which of the three it is by morning. I always do."

    athought "She does. Tessa always does. I am not going to argue with her about that. I have watched her do the work of knowing things by morning for three years."

    athought "I am going to be very careful about what I say next, because the scene does not belong to me and I do not want to put the wrong shape into it."

    # ========== PHASE 6 — THE SILENT BORROWING ==========

    # CAMERA: hold the side-by-side wide. Aeron is learning the
    #         rule-of-three silently. His mouth moves over the
    #         names without voicing them — the same silent
    #         shaping Tessa did in a4_s05a when she ran the rule
    #         on his sleeping body. The scene does not call
    #         attention to the inversion; the camera catches
    #         it as a natural act. Do not push in to confirm
    #         that he is doing it. Trust the wide.
    # FACE: Aeron — the borrowing. This is the first time in
    #        the series he has used her rule, and he is using
    #        it without asking permission because the permission
    #        was already given when she taught it to him
    #        without teaching him. The face is reverent.

    "He does not say the names aloud."

    "He says them in his head instead."

    "Three times. Tessa's rule. The rule for the living."

    athought "Kesa Marin."

    athought "Joren Hale."

    athought "Kesa Marin."

    athought "Joren Hale."

    athought "Kesa Marin. Joren Hale."

    athought "That is the rule. I am using her rule. I am not going to tell her I am using it because telling her would turn the borrowing into a performance and the whole point is that I am not performing anything — I am joining a room that she is holding."

    athought "Presence. That is what Lyra said two nights ago. That is what Tessa said into a corridor last night. Both of them said the same word without either of them being in the room with the other one."

    athought "I am standing in a medical area with two new names on the dead column of a board that has been moved across a displacement. My mother is on both columns. The woman who is holding the chalk for my grief is holding it silently now. And I am inside a ritual I did not invent and did not ask to join and that is being extended to me anyway by a person who is not going to announce the extension because the announcing would cheapen it."

    athought "I am going to pay attention to this the rest of my life."

    "He looks at Tessa."

    "Tessa is looking at the two new names."

    "She feels him looking. She does not turn her head."

    t "You said them."

    "It is not a question."

    a "In my head."

    t "I know."

    a "How did you know?"

    t "Because the silence changed shape. There is a difference between the silence of one person not speaking and the silence of two people not speaking at the same names. It is very small and I can feel it."

    "Then, quieter:"

    t "Thank you for not saying them out loud."

    t "That matters in a way I cannot explain to anyone who has not spent three years counting."

    a "Tessa—"

    t "Do not make me explain it."

    a "I was not going to."

    "They stand in front of the board for a long time after that."

    "The clip lamp is on. The main medical area hums. Joran Tev is still asleep on the cot in the other room — the fighter who came home because Lyra called the ridge flank. The board holds his name on the living column. Tessa transferred it up from the unassigned row at the shift change sometime before dawn."

    "The living column is long."

    "The dead column is long."

    "They are both longer than they used to be."

    "Aeron and Tessa do not move."

    # ========== PHASE 7 — THE CLOSE ==========

    # CAMERA: the scene's final shot is the two-shot wide —
    #         both of them in frame, the board filling the wall
    #         behind them, LIORA RYLAN visible on both columns,
    #         the two new names visible on the dead side. Hold.
    #         The camera does not move. When the held string
    #         fades in, the shot does not react. Fade on the
    #         wide. The board is the last image.
    # SFX: the one held low string enters here per the opening
    #      block. Very low. Under everything else. It does not
    #      resolve before the fade. The string is her rule
    #      given a musical form for exactly long enough to
    #      register that it has a musical form, and then gone.

    "Eventually Tessa reaches up."

    "She puts her hand on the board. Flat palm. Just below the header letters of the dead column."

    "Not on the new names. Just on the column."

    "A small private benediction he is not going to translate into a sentence."

    t "I am going to be here for a little longer. I will come find you in the briefing room after the eight-hundred brief."

    a "Okay."

    t "Go do the chapter."

    a "Okay."

    "He does not leave immediately. He stands beside her for one more breath."

    "Then he turns toward the door."

    "At the doorway he stops, looks back once. Tessa's hand is still on the board. Her back is to him. The light from the clip lamp is catching one side of her hair and the rest of the room is in soft pre-morning."

    "He leaves."

    "The scene holds on Tessa at the board for three beats after the door closes behind him."

    "Her hand comes down from the column."

    "Her lips shape the two names without sound. One full time. Then she caps the imaginary repetition in her head where the rule still lives, and where, for tonight, the rule is enough."

    "Fade."

    # stop ambient fadeout 3.5
    # scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Tessa", trust=1)
    $ canon_set("tessa.board_ritual_silent_phase", True)
    $ canon_set("phoenix_kia.kesa_marin_on_board", True)
    $ canon_set("phoenix_kia.joren_hale_on_board", True)
    $ npc_remember("Tessa", "first_board_scene_with_aeron_silent", tone="shared_ritual")
    $ npc_remember("Aeron", "joined_tessas_silence_at_the_board", tone="witnessed_joining")
    $ flag("aeron_adopted_tessa_rule_silently", True)
    $ tp_seed("a4.tessa_board_silence")
    $ metric("tessa_board_dead_column", delta=2)
    $ scene_mark(_current_scene_id, "completed")

    return


# =========================================================
# CANONICAL NOTES
# =========================================================
# cann.scene_id: a4_s06_tessa_counts_different_emp
# cann.chapter: Act IV, Chapter I — Shared Authority
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Morning after a4_s05a. Oh-five-thirty. Aeron wakes on the medbay cot.
#     Tessa has already left the chair but is in the main medical area at the
#     board. Aeron finds her there before the eight-hundred briefing with Selene.
# cann.what_happened:
#   - Aeron wakes on the cot — his first five-hour sleep since before the Liora
#     execution. The chair beside him is empty. His jacket is folded at the foot
#     of the cot (Tessa).
#   - He goes to find Tessa. She is at the board in the main medical area,
#     marker in one hand, cap in the other. The board is set up as before
#     (displacement-transferred original): LIVING column on the left, DEAD
#     column on the right. LIORA RYLAN on both. Joran Tev transferred up to the
#     living column at the shift change. Below LIORA RYLAN on the dead column:
#     clean space for two new names.
#   - Aeron stops in the doorway. He does not enter. He watches her add the
#     names: KESA MARIN, JOREN HALE. She writes without saying either name
#     aloud. She caps the marker. She sets it on the shelf below the board.
#   - She tells him he can come in. He does. They stand in front of the board.
#     He notices she did not say the names. He asks about it.
#   - Tessa explains the evolution: her mother's rule was to say them three
#     times, and she has been saying them aloud for three years. In the last
#     six days the habit has been drifting into silence. Tonight is the first
#     time she has written two names in one sitting without saying either of
#     them aloud, and she noticed the silence and chose not to fix it.
#   - She names the mechanism: the rule was never about proving the dead were
#     real. The rule was about proving the living were still here. She needed
#     the sound in the room because the silence used to scare her.
#   - She gives three readings of what the change might mean:
#       (1) Good: the silence is no longer dangerous to her — the seven-year-old
#           has grown up.
#       (2) Bad: she has stopped feeling the names — the gap medics fall into
#           where grief stops working and then work stops working.
#       (3) Hoped: she has company now, and the names are being held by more
#           people than just her, and the silence is the shape the holding has.
#     She says she will know which by morning. She always does.
#   - Aeron says the two names silently in his head, three times, Tessa's rule
#     applied to her board in her medical area. He does not tell her he is
#     doing it. Tessa knows anyway — she can feel the silence change shape when
#     a second person is not speaking at the same names. She thanks him for not
#     saying them out loud.
#   - They stand at the board for a long time after that. She puts her flat
#     palm on the board just below the dead column header — a private
#     benediction. She tells him to go do the chapter and that she will come
#     find him after the eight-hundred brief. He leaves.
#   - After he is gone, the camera holds on Tessa. Her lips shape the two names
#     once without sound. The scene fades.
# cann.aeron_state:
#   - Peripheral. The scene does not belong to him and he knows it. He is
#     learning to witness a grief practice that is not his own and to participate
#     in it by the rules of the person whose practice it is.
#   - The silent three-times rule, which he borrowed from Tessa in the cipher
#     alcove in a4_s05, is now being performed in her physical presence for the
#     first time. He does not announce it. This is the character beat — the
#     refusal to announce it.
#   - "Presence is enough" is now an active pattern he is tracking across both
#     Lyra and Tessa. The scene explicitly notes his awareness of the pattern.
# cann.tessa_state:
#   - The Act IV evolution of her ritual is now external and visible to another
#     character for the first time. Aeron is the first person to see her use
#     the board without speaking.
#   - She is deliberately unresolved about whether the silence is good, bad, or
#     the thing she is hoping for. The scene refuses to close on a verdict. The
#     refusal is the character moment.
#   - Her ability to feel the difference between one-person silence and
#     two-person silence is the scene's quiet thesis. Her ritual is porous now.
#     It can hold a second person without her having to invite them by name.
#   - The flat palm on the column below the header is a private gesture the
#     scene does not translate. This is intentional. Future Tessa beats may
#     explicate or deepen it.
# cann.path_tracking:
#   - EMP path. Linear. No player choice.
#   - rel_bump Tessa +1 trust.
#   - canon_set tessa.board_ritual_silent_phase True — the board is now in a
#     silent phase of its evolution. Any later Tessa board beat must read against
#     this state.
#   - canon_set phoenix_kia.kesa_marin_on_board True and
#     canon_set phoenix_kia.joren_hale_on_board True — the names are now
#     physically on the board, in addition to being canon_set in a4_s05.
#   - flag aeron_adopted_tessa_rule_silently True — the first time Aeron has
#     formally adopted an LI's ritual. He will carry this into later Act IV
#     scenes whether or not the game surfaces it.
#   - tp_seed a4.tessa_board_silence — True Path seed. Aeron joining Tessa's
#     practice silently is a Silence-family True Path beat (mirrors a3_s04a
#     "The Silence" — the refusal of borrowed voices is structurally related
#     to joining a practice without announcing it).
#   - metric tessa_board_dead_column incremented by 2. This metric may be
#     visible on Tessa's board in later scenes and should accrue with future
#     Phoenix KIA.
# cann.thematic_flags:
#   - Evolution of grief discipline. The rule of three goes silent. The ritual
#     does not die, it changes shape. Tessa is being explicit that rituals can
#     change and the changing is not failure.
#   - Porous ritual. Tessa's practice can now be shared without being performed
#     for. The scene distinguishes between sharing a practice (silent joining)
#     and performing it for an audience (saying names aloud into a room to
#     prove they are real).
#   - The board as physical object. The displacement-transferred original. The
#     ghost text in the whiteboard. LIORA RYLAN on both columns still. This is
#     the first time in Act IV the board is shown on-camera.
#   - Silence as a shape the holding has. Tessa's hoped reading, unresolved at
#     scene close. The hope is a commitment Aeron has participated in.
#   - Presence as the Act IV through-line. Lyra and Tessa both name it without
#     coordinating. Aeron is tracking the convergence. The scene makes the
#     convergence explicit in Aeron's internal monologue.
# cann.character_moments:
#   - Tessa: writing two names without saying them aloud. The moment of noticing
#     she has not said them and choosing not to fix it. The three readings of
#     what the silence might mean, arranged in the order she trusts. The flat
#     palm on the column. The shaping of the names without sound after Aeron
#     leaves. She does not turn to him when she says "thank you for not saying
#     them out loud" — the thanks is in the silence's shape, not in her face.
#   - Aeron: staying in the doorway until she invites him in. Reading both
#     names without saying them. Saying them silently in his head, three times,
#     on her rule, in her space. The refusal to announce the borrowing. "I am
#     going to pay attention to this the rest of my life."
# cann.callbacks:
#   - a2_int_tessa_torins_name: the origin of the rule. Her mother, the winter
#     her father did not come back, the rule for the counter. This scene is
#     the second major evolution of that rule (first: a3_int_tessa_the_board_emp
#     when Liora went on both columns).
#   - a3_int_tessa_the_board_emp: LIORA RYLAN on both sides. The board is shown
#     here with both entries still present — the canon is maintained through the
#     displacement. The present scene is the pre-dawn interlude's mirror with
#     Aeron in the room.
#   - a3_s20a_scar_and_steady_emp: the hands steady after. Tessa's hands are
#     steady for the writing. The scene trusts that established physiology.
#   - a4_s05_delegation_test_emp: the source of Kesa Marin and Joren Hale as
#     Phoenix KIA, and the source of Aeron's adoption of the rule of three.
#     The cipher alcove scene where Aeron first said the names silently is the
#     mechanical precedent the current scene completes.
#   - a4_s05a_you_are_not_a_machine_emp: the silent three-times naming Tessa
#     used on Aeron's sleeping body. The two scenes are a matched pair — she
#     performed the rule silently on him last night; he performs it silently on
#     her dead tonight. Neither of them announces the parallel. The structure
#     is the point.
#   - a4_s04_lyra_unbuckled_emp: "presence is enough" as cross-LI vocabulary.
#     Aeron tracks the pattern explicitly in this scene's internal monologue.
#   - a3_s04a_the_silence_emp: the True Path refusal of borrowed voices. The
#     current scene extends that Silence register into a grief practice — the
#     same structural move (refuse to perform, join the silence) applied to a
#     different object. tp_seed references this lineage.
# cann.block_status:
#   - LINEAR. No branching, no choice. EMP path only.
# cann.requires_followup:
#   - Tessa's three readings are explicitly unresolved. A later Act IV scene
#     should return to the board and deliver or refuse the verdict.
#   - The silent-ritual state is now canon. Any later Tessa scene that shows
#     her saying a name aloud at the board must treat it as meaningful — she
#     has not said one aloud since six days before this scene.
#   - Aeron has now silently joined an LI's grief practice. The parallel move
#     for other LIs may be available in later Act IV beats (Lyra's Anayet,
#     Zira's trust-interdependence, Noelle's analysis-commitment).
#   - The tp_seed a4.tessa_board_silence should be checked at the Act IV close
#     to determine whether Aeron has continued to silently observe her practice
#     across the intervening scenes. The True Path bonus is contingent on
#     maintained silent participation, not one-off adoption.
