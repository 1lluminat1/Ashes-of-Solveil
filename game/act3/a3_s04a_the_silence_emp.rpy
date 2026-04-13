# =======================================================
# ACT 3 - Scene 04a: The Silence (Empathy Path)
# File: a3_s04a_the_silence_emp.rpy
# Type: TRUE PATH MECHANIC (Silence)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s04a_the_silence_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s04a_the_silence_emp:

    $ show_timeline("DAY 23", "14:00", "Phoenix Base — War Room")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm, locked tripod. Council framing — wide establishing, then rotating close-ups
    #         on each speaker during the menu options. If the timer fires: slow push-in on Aeron,
    #         tightening from medium to close as the silence stretches. Hold his face.
    # LIGHTING: War room amber and tactical green. Displays showing the Sector 4 corridor —
    #           patrol routes overlapping, compression visible. The map is a closing fist.
    # SFX: Loop — war room hum, tactical display cycling. Clock tick layered in during the menu.
    #       One-shots — chair shift, datapad tap, Selene's fingers drumming once.
    # FX/COMP: Tactical display: Sector 4 corridor with red overlay showing Echelon compression.
    #          During menu: subtle timer bar at screen bottom (20 seconds).
    # BLOCKING: Full council around the command table. Selene and Aeron at the head.
    #           Zira standing (always standing). Lyra seated, hands folded. Noelle at her crystal.
    #           Tessa near the door, arms crossed.
    # FACE: Council — engaged, each person leaning toward their own answer.
    #        Aeron (if timer fires) — still. The stillness of someone refusing to speak rather
    #        than someone with nothing to say. Then: clarity. Not borrowed. His.

    # ========= VOICE BASELINE =========
    # EMP cadence. Council scene — multiple voices, each carrying their framework.
    # The four menu options are explicitly labeled as other people's doctrines.
    # The Silence path is Aeron finding his own voice by refusing to borrow one.

    # ========== WAR ROOM — PLANNING COUNCIL ==========

    #scene bg_war_room_emp with dissolve
    #play ambient "sfx/ambient/war_room_planning.ogg" fadein 2.0

    "The Sector 4 corridor glows red on the tactical display. Echelon's response to the convoy interdiction — patrol compression, drone sweeps, checkpoints at every junction."

    "It was their window. Now it's a wall."

    sel "Noelle's pattern analysis confirms it. Echelon has locked down the entire Sector 4 approach. Tighter intervals, lower altitude sweeps, rotating checkpoint positions."

    n "They've also redirected two mobile response units from the northern perimeter. Response time to any incursion in the corridor has dropped from eleven minutes to four."

    z "Four minutes. That's nothing."

    n "That's the point."

    sel "Which brings us to the question."

    "She turns to Aeron. The table turns with her."

    sel "We need to move through that corridor to reach the civilian shelters on the far side. Medical supplies, food, two hundred people waiting for extraction."

    sel "The corridor is the only viable route. Going around adds three days and exposes us to the eastern garrison."

    sel "Aeron. How do we approach this?"

    athought "Six faces. All of them waiting."

    athought "I know what Marcus would say. I know what Kael would say. I know what Selene herself would say if she weren't asking me."

    athought "I know what Noelle's data suggests."

    athought "The question is whether any of those answers are mine."

    # ========== THE CHOICE — TIMED MENU (20 seconds) ==========

    # IMPLEMENTATION NOTE: This uses a timed menu screen. If the player selects
    # an option, the corresponding branch plays normally. If 20 seconds pass
    # without a selection, the timer fires and we jump to the Silence path.
    # The Silence path is a TRUE PATH bonus — all four labeled options are
    # complete, valid continuations. The Silence is a reward for refusal.

    $ _silence_timer_fired = False

    # NOTE: Implementation requires a custom screen (silence_council_menu)
    # that displays four options with a 20-second timer. If the timer expires,
    # it sets _silence_timer_fired = True and returns "silence".

    # call screen silence_council_menu

    # For script purposes, the menu logic:
    menu:
        "The council watches. The tactical display cycles. Twenty seconds."

        # --- MARCUS'S DOCTRINE ---
        "\"We strike hard and fast. Hesitation kills.\" {i}(Marcus's doctrine){/i}":
            $ choice_and_dev(
                _current_scene_id, "_marcus_doctrine", "EMP", factor=0,
                next_scene_label=None,
                note="Borrows Marcus's framework. Valid tactical answer. Not Aeron's voice."
            )
            jump .marcus_path

        # --- KAEL'S PROMISE ---
        "\"We protect everyone or this means nothing.\" {i}(Kael's promise){/i}":
            $ choice_and_dev(
                _current_scene_id, "_kael_promise", "EMP", factor=0,
                next_scene_label=None,
                note="Borrows Kael's framework. Valid moral answer. Not Aeron's voice."
            )
            jump .kael_path

        # --- SELENE'S PRAGMATISM ---
        "\"We calculate acceptable losses and commit.\" {i}(Selene's pragmatism){/i}":
            $ choice_and_dev(
                _current_scene_id, "_selene_pragmatism", "EMP", factor=0,
                next_scene_label=None,
                note="Borrows Selene's framework. Valid strategic answer. Not Aeron's voice."
            )
            jump .selene_path

        # --- NOELLE'S ANALYSIS ---
        "\"We need more data before deciding.\" {i}(Noelle's analysis){/i}":
            $ choice_and_dev(
                _current_scene_id, "_noelle_analysis", "EMP", factor=0,
                next_scene_label=None,
                note="Borrows Noelle's framework. Valid cautious answer. Not Aeron's voice."
            )
            jump .noelle_path

    # NOTE: If the 20-second timer fires without a click, jump to .silence_path
    # The screen implementation should handle: $ _silence_timer_fired = True
    # then jump a3_s04a_the_silence_emp.silence_path

    # ========== BRANCH: MARCUS'S DOCTRINE ==========
    label .marcus_path:

        a "We strike hard and fast. Hesitation kills."

        "The words land clean. Zira nods."

        z "Finally. Someone with a spine."

        sel "Speed favors us if the entry point holds. Noelle, can you map a breach window?"

        n "Narrow. But possible. I can identify a seventeen-minute gap in the eastern checkpoint rotation."

        sel "Then we plan for seventeen minutes. Fast in, fast out."

        athought "It's a good answer. It's the answer my father would have given."
        athought "I don't know if that makes it wrong."

        $ npc_remember("Zira", "aeron_chose_speed_doctrine", tone="approval")

        jump .council_close

    # ========== BRANCH: KAEL'S PROMISE ==========
    label .kael_path:

        a "We protect everyone or this means nothing."

        "Tessa exhales. Lyra sits straighter."

        t "That's the only answer that matters."

        sel "It's the answer that costs the most time. We'd need to clear every checkpoint before moving the civilians."

        l "Then we clear every checkpoint."

        sel "With what reserves? We're already stretched."

        a "We find a way. Two hundred people are counting on us to not do the math that makes them expendable."

        "Selene studies him. Measuring."

        sel "Then we find a way."

        athought "It's a good answer. It's the answer Kael would have given."
        athought "I don't know if that makes it enough."

        $ npc_remember("Tessa", "aeron_prioritized_protection", tone="grateful_trust")

        jump .council_close

    # ========== BRANCH: SELENE'S PRAGMATISM ==========
    label .selene_path:

        a "We calculate acceptable losses and commit."

        "The room shifts. Tessa's jaw tightens. Selene's expression doesn't change."

        sel "Define acceptable."

        a "The corridor has three chokepoints. If we move fast, we lose the stragglers at the rear. Maybe ten, fifteen people. The other hundred and eighty-five make it through."

        n "That aligns with my projections. Eighty-nine percent extraction rate with current resources."

        t "And the other eleven percent?"

        "Silence."

        a "We make it count."

        athought "It's a good answer. It's the answer Selene herself uses when nobody's watching."
        athought "I don't know if that makes it bearable."

        $ npc_remember("Selene", "aeron_mirrored_pragmatism", tone="complicated_recognition")

        jump .council_close

    # ========== BRANCH: NOELLE'S ANALYSIS ==========
    label .noelle_path:

        a "We need more data before deciding."

        "Noelle's stylus pauses. She almost smiles."

        n "Agreed. The current dataset is insufficient for a ninety-percent-confidence recommendation."

        z "We don't have time for more data. Those people are waiting now."

        a "And they'll be waiting dead if we walk into a pattern we don't understand."

        sel "How long?"

        n "Forty-eight hours of additional surveillance gives me a complete rotation model. Seventy-two gives me predictive capability."

        sel "Forty-eight. Not seventy-two. We can't afford the extra day."

        a "Forty-eight it is."

        athought "It's a good answer. It's the answer Noelle gives when the room wants action and she wants certainty."
        athought "I don't know if that makes it mine."

        $ npc_remember("Noelle", "aeron_valued_data_primacy", tone="intellectual_respect")

        jump .council_close

    # ========== TRUE PATH: THE SILENCE ==========
    label .silence_path:

        # This branch fires ONLY if the 20-second timer expires without a click.
        $ tp_silence_used(_current_scene_id)

        "Twenty seconds pass. The tactical display cycles. The room waits."

        "Aeron doesn't speak."

        "Selene's fingers drum once on the table. Zira shifts her weight. Lyra's hands tighten in her lap."

        "Still nothing."

        z "Aeron."

        "He looks at her. Then at Selene. At Noelle. At Lyra. At Tessa."

        "At the display. The corridor. The compression patterns. The wall Echelon built in three days."

        athought "I've spent my whole life speaking in other people's voices."

        a "I've spent my whole life speaking in other people's voices."

        "The room goes still."

        a "My father's doctrine. Kael's idealism. Selene's pragmatism. Noelle's models."

        a "Every answer I've ever given has been borrowed from someone else's framework. Someone else's war."

        sel "Aeron—"

        a "I'm done."

        "He steps forward. Puts both hands on the tactical display. The corridor pulses under his palms."

        a "None of those answers account for what I am. What we have that Echelon doesn't."

        n "Which is?"

        a "Me."

        "Not arrogance. The word lands flat, factual."

        a "I spent three years running Echelon patrols through that corridor. I know the maintenance tunnels, the blind spots, the infrastructure that doesn't appear on any tactical display because it was never classified as strategic."

        a "There's a service network under the corridor — atmospheric processing, water reclamation, cable conduit. It runs parallel to the surface route for the full length."

        sel "It's not on our maps."

        a "It's not on anyone's maps. Echelon built it during the infrastructure expansion and then classified the plans to prevent exactly this kind of use."

        a "But I walked those tunnels. I inspected them quarterly. I know every junction, every access point, every structural weakness."

        "He straightens."

        a "We don't go through the corridor. We go under it. The compression, the drones, the checkpoints — none of it touches us. We move two hundred people through service tunnels that Echelon forgot exist because the man who inspected them is standing on the wrong side of their wall."

        "The room is quiet. Then Zira laughs. Short and sharp."

        z "That's insane. I love it."

        n "The structural integrity of a sub-corridor service network would need verification, but if the access points are viable—"

        a "They're viable. I'll draw the route tonight."

        sel "You're proposing we use your Echelon knowledge against them."

        a "I'm proposing we use the one thing no one else at this table has. The perspective of someone who's been both."

        "Selene looks at him for a long moment. Something shifts in her expression — not surprise, recognition."

        sel "Both."

        a "Echelon trained me. Phoenix chose me. The corridor doesn't have to be a choice between speed and safety. We just have to stop looking at it the way either side taught us to."

        "Selene nods. Once."

        sel "Draw the route. Noelle, structural verification on whatever he gives you. We brief at 0600."

        n "Understood."

        "The council breaks. But Selene stays."

        sel "(quietly) You didn't answer for twenty seconds."

        a "I know."

        sel "You were waiting."

        a "I was listening. To all of them. To myself."

        sel "And?"

        a "My voice sounds different than I expected."

        "She studies him."

        sel "It sounds like yours."

        athought "Like mine."
        athought "For the first time, that doesn't feel like a problem."

        $ flag("silence_path_taken", True)

        jump .scene_end

    # ========== COUNCIL CLOSE (for labeled options) ==========
    label .council_close:

        "The council settles into planning. Details, timelines, contingencies."

        "The machinery of the next operation."

        athought "The answer I gave was good. It was the right answer for the room."
        athought "I'm not sure it was mine."

    # ========== SCENE END ==========
    label .scene_end:

        #stop ambient fadeout 2.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ scene_mark(_current_scene_id, "completed")

        return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s04a_the_silence_emp
# cann.chapter: Act III, Phase I — Proving Ground
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Three days after Shared Ground (a3_s04). Echelon has adapted. Sector 4 corridor locked down.
#   - Full council planning session for the next operation — civilian extraction.
# cann.what_happened:
#   - Council meeting. Sector 4 corridor compressed by Echelon response. 200 civilians need extraction.
#   - Selene puts the question to Aeron: how do we approach this?
#   - Four labeled options, each explicitly tagged as someone else's framework:
#       1. Marcus's doctrine ("Strike hard and fast. Hesitation kills.")
#       2. Kael's promise ("Protect everyone or this means nothing.")
#       3. Selene's pragmatism ("Calculate acceptable losses and commit.")
#       4. Noelle's analysis ("We need more data before deciding.")
#   - All four produce valid, complete scene continuations (2-3 dialogue exchanges each).
#   - TRUE PATH: If the player lets 20 seconds pass without clicking, the Silence fires.
#   - Silence path: Aeron refuses borrowed voices. "I've spent my whole life speaking in other
#     people's voices. I'm done." Proposes using his unique Echelon knowledge — sub-corridor
#     service tunnels that don't appear on any tactical map — to bypass the corridor entirely.
#   - The key insight: he is the one person who has been BOTH Echelon and rebellion.
# cann.aeron_state:
#   - Each labeled option: competent but borrowed. "I don't know if that makes it mine."
#   - Silence path: breakthrough. His own voice. "The perspective of someone who's been both."
# cann.path_tracking:
#   - Marcus path: npc_remember Zira (approval). factor=0 (no EMP/OB weight — neutral borrow).
#   - Kael path: npc_remember Tessa (grateful). factor=0.
#   - Selene path: npc_remember Selene (complicated recognition). factor=0.
#   - Noelle path: npc_remember Noelle (intellectual respect). factor=0.
#   - Silence path: tp_silence_used() fires. flag("silence_path_taken").
#     Major True Path moment — Aeron finds his own voice.
# cann.thematic_flags:
#   - "I've spent my whole life speaking in other people's voices. I'm done." — Scene thesis.
#   - The Silence as refusal and discovery simultaneously.
#   - "The perspective of someone who's been both" — Aeron's unique value articulated.
#   - Borrowed frameworks: Marcus (force), Kael (protection), Selene (pragmatism), Noelle (data).
#     All valid. None are Aeron's.
#   - Sub-corridor proposal: literal metaphor — going under the surface, finding paths
#     that exist because of his history, not despite it.
# cann.character_moments:
#   - Aeron: The silence IS the answer. Refusing to speak in borrowed voices IS finding his own.
#   - Selene: "It sounds like yours." — She recognizes what just happened.
#   - Zira: "That's insane. I love it." — Respects audacity regardless of source.
#   - Noelle: Immediately shifts to structural verification — the proposal is actionable.
#   - Tessa/Lyra: React warmly to Kael's promise if chosen; present but not central in Silence.
# cann.block_status:
#   - TRUE PATH MECHANIC (Silence). Four valid branches + one hidden bonus.
# cann.requires_followup:
#   - Silence path: sub-corridor extraction becomes a key operation scene.
#   - Labeled paths: each produces a viable but conventionally planned operation.
#   - "My voice sounds different than I expected" — identity integration continues.
#   - Echelon infrastructure knowledge as recurring tactical asset through Act 3.
