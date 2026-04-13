# =======================================================
# ACT 3 - Scene 01: Ashes in Formation (Obedience Path)
# File: a3_s01_ashes_in_formation_ob.rpy
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s01_ashes_in_formation_ob"
$ scene_mark(_current_scene_id, "entered")

label a3_s01_ashes_in_formation_ob:

    $ show_timeline("DAY 22", "08:00", "Phoenix Base — Assembly Hall")

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm lens (OB detachment), locked tripod for funeral, handheld for war room.
    #         Wide establishing shots emphasize isolation. Close-ups catch micro-expressions.
    #         Slow, deliberate push on the empty chair at the end.
    # LIGHTING: Memorial chamber: cold 5600K through reinforced glass, harsh overhead strips.
    #           No warmth. Clinical. The casket lit like evidence.
    #           War room: blue-green tactical displays, cold steel reflections, no practicals.
    # SFX: Loop - base hum (cold variant), ventilation drone, distant machinery.
    #      One-shots - footsteps on concrete, door hiss, chair scrape (blade-like at end).
    # FX/COMP: Breath visible in cold air, display reflections on faces, casket shadow.
    # BLOCKING: Memorial: Aeron at podium, four LIs in front row (Lyra, Zira, Tessa, Noelle).
    #           43 rebels behind them. The witnesses don't look at each other.
    #           War room: Same four around table. Selene's chair empty at head.
    # CANON: This is the OB Act 3 opener. Aeron executed Selene; four LIs witnessed and stayed.
    #        The funeral is a collective lie. This scene binds them through complicity, not love.
    # FACE: Faces visible but guarded. Masks, not intimacy.

    # ========= VOICE BASELINE =========
    # OB cadence: Formal, clinical, minimal contractions. Short declarative sentences.
    # Aeron is detached but self-aware. He knows this is monstrous. He chooses efficiency.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - MEMORIAL CHAMBER - DAY]
    # Cold light through reinforced glass. The rebellion's makeshift memorial space -
    # concrete walls, salvaged flowers, a projection frame cycling through images of the dead.
    # Today there's only one image: Selene Ward.
    # The casket is closed.
    # In the front row: Lyra, Zira, Tessa, Noelle. They know.

    #scene bg_memorial_chamber_day with dissolve
    #play ambient "sfx/ambient/base_hum_cold.ogg" fadein 2.0
    #play music "music/ob_funeral_drone.ogg" fadein 3.0

    # --- OPENING: THE FORMATION ---

    athought "Forty-seven people stand in rows. I counted them as they entered."

    athought "Forty-three of them believe the story we're about to tell."

    athought "Four of them were there when it happened."

    # VISUAL: The memorial chamber. Rows of rebels in salvaged uniforms. At the front:
    # Lyra (pale, rigid), Zira (jaw tight), Tessa (hands clasped too hard), Noelle (watching).
    # They don't look at each other. They don't look at Aeron. The casket is sealed.

    #show memorial_formation with dissolve

    athought "They expect me to speak. I've prepared remarks. Twelve sentences. Efficient. Consistent with the story we agreed to tell."

    athought "The casket is closed. Head wounds don't permit open ceremonies."

    athought "Lyra chose the flowers. Zira secured the corridor feeds. Tessa cleaned the body. Noelle wrote the incident report."

    athought "We're all guilty. That's what holds us together now."

    # --- THE EULOGY (THE LIE THEY TELL TOGETHER) ---

    a "Commander Selene Ward served this cause for nineteen years."

    athought "My voice doesn't waver. I've practiced this."

    athought "In the front row, Lyra's hands are folded in her lap. The same hands that didn't stop me. She's praying, I think. I don't know to whom."

    a "She built the courier network that kept us alive. She unified cells that had given up on unity. She made decisions no one else would make, and she carried the weight of every one."

    # VISUAL: The faces in the crowd. Most weep openly. In the front row, no one cries.
    # They've already spent those tears - or they've none left.

    #show memorial_crowd_grief with dissolve

    athought "Zira stares straight ahead. She hasn't spoken to me since it happened. But she hasn't left, either. She deleted the corridor footage herself."

    a "Three days ago, during the Sector 9 evacuation, Commander Ward intercepted a round meant for a civilian courier. She completed the operation. Then she died."

    athought "The lie hangs in the air. No one in the front row flinches."

    athought "Tessa washed Selene's blood from my hands. She didn't say a word. When I asked why she was helping, she said: 'Because someone has to keep you human.'"

    athought "I don't know what she meant. I don't know if she still believes it."

    a "Her sacrifice preserved forty-seven lives. This cell. This mission. The war continues because she chose to end."

    athought "Noelle is the only one looking at me. Her expression is clinical. Cataloging. She's studying how I deliver the lie, measuring my composure, noting the places where my voice should break and doesn't."

    athought "Later, she'll tell me my performance was 'statistically convincing.' I don't know if that's a compliment or a warning."

    a "We honor her by continuing. Dismissed."

    # --- AFTERMATH: THE WEIGHT ---

    # VISUAL: The formation breaks. Most of the rebels file out, grief-stricken but unsuspecting.
    # The front row doesn't move. They wait until the room empties. Then they wait longer.

    #stop music fadeout 2.0

    athought "The others file out. Forty-three people who believe their commander died a hero."

    athought "Four people remain. They don't move until the last footsteps fade."

    # VISUAL: The memorial chamber, nearly empty. Aeron at the podium. Lyra, Zira, Tessa, Noelle
    # in the front row. No one speaks. The silence is heavier than the eulogy.

    #show memorial_empty_frontrow with dissolve

    athought "The silence stretches. I should say something. Acknowledge what we've done. What we're doing."

    athought "I don't."

    # VISUAL: Zira is the first to move. She stands, adjusts her jacket, walks toward the door.
    # She pauses beside Aeron but doesn't look at him.

    z "The story holds. For now."

    athought "She doesn't wait for a response. The door hisses shut behind her."

    # VISUAL: Tessa rises next. She looks at Aeron - really looks - and for a moment
    # something flickers in her expression. Pain. Or pity.

    t "I need to check on the wounded."

    athought "She doesn't have wounded. She has already finished her rounds. But I don't stop her."

    # VISUAL: Noelle stands. She tilts her head, studying Aeron like a specimen.

    n "Your micro-expressions during the third sentence suggested rehearsal rather than recall. Consider varying your pause lengths next time."

    athought "She leaves. I don't know if that was advice or accusation."

    # VISUAL: Only Lyra remains. She hasn't moved. Her hands are still folded. Her eyes are closed.

    #show lyra memorial_alone with dissolve

    athought "Lyra sits motionless. Her lips move without sound - the shape of words I can't hear."

    a "Lyra."

    athought "She opens her eyes. She looks at me. And for a moment, I see something that might be the last ember of the woman who loved me before I became this."

    l "I keep waiting to feel something."

    a "And?"

    l "Nothing. Just... silence."

    athought "She stands. She doesn't touch me. She doesn't look at the casket."

    l "I chose this. I chose you. I need to understand why."

    a "When you do, tell me."

    athought "She leaves. The door closes. I'm alone with the casket."

    # --- TRANSITION: WAR ROOM ---

    #scene black with fade
    #pause 1.0

    # [INT. PHOENIX BASE - WAR ROOM - LATER]
    # Cold steel table. Tactical displays. The chair at the head - Selene's chair - sits empty.
    # The four witnesses are already seated. No one has taken the head chair.

    #scene bg_warroom_ob with dissolve
    #play ambient "sfx/ambient/warroom_hum.ogg" fadein 2.0

    athought "The war room. The same table. The same displays. The same people who watched me pull the trigger."

    athought "Selene's chair sits empty at the head. None of them have touched it."

    # VISUAL: Around the table: Lyra (rigid), Zira (coiled), Tessa (withdrawn), Noelle (observing).
    # They don't look at each other. They look at the displays, at the table, at anything but the empty chair.

    #show warroom_group_ob with dissolve

    athought "We haven't spoken about it. Not directly. We've spoken around it - logistics, schedules, supply routes. The shape of the absence without the name."

    z "Three supply routes compromised. Zero fallback positions. Someone needs to make a call."

    athought "Her voice is flat. Professional. As if this is any other briefing."

    athought "As if she didn't watch me execute our commanding officer three days ago."

    t "We just buried her, Zira."

    z "We just buried a story. The rebellion needs to keep moving."

    athought "Tessa flinches. Lyra doesn't react. Noelle takes a note."

    l "Moving without a plan is how we lose more people."

    z "Sitting here pretending we haven't already lost is how we lose ourselves."

    athought "They look at me. All of them. Waiting."

    athought "They watched me kill her. They chose to stay. Now they're waiting to see what that choice cost them."

    # --- CHOICE: COMMAND RESPONSE ---

    menu:
        "Four faces. Four witnesses. Four people waiting to see who I'm now."

        "Take command.":
            $ choice_and_dev(
                _current_scene_id, "_take_command", "OB", factor=1,
                next_scene_label=None,
                note="Immediate pragmatism. Zira responds to decisive command."
            )
            jump .take_command

        "Acknowledge what binds us.":
            $ choice_and_dev(
                _current_scene_id, "_acknowledge_guilt", "OB", factor=1,
                next_scene_label=None,
                note="Naming complicity explicitly. Lyra and Tessa respond to honesty."
            )
            jump .acknowledge_guilt

        "Say nothing. Let the silence speak.":
            $ choice_and_dev(
                _current_scene_id, "_embrace_silence", "OB", factor=1,
                next_scene_label=None,
                note="Weaponized silence as test. Noelle respects the clean experiment."
            )
            jump .embrace_silence

    # --- BRANCH: TAKE COMMAND ---
    label .take_command:

        a "Enough."

        athought "The word cuts through the noise. They stop."

        athought "This is what they chose. This is what they stayed for. Someone who would make the call. Someone who wouldn't hesitate."

        a "Zira. Pull the eastern route. Redirect through the maintenance tunnels in Sector 7. Lyra, you've point on the next supply run. Tessa, I want casualty projections by 1800. Noelle, find me every patrol pattern deviation in the last seventy-two hours."

        athought "They stare at me. The same eyes that watched me pull the trigger."

        a "We don't have time to question what we've done. We've time to make it mean something. Move."

        athought "Zira is the first to nod. Of course she's. She understands pragmatism. She deleted the footage."

        z "...understood."

        athought "The others follow. One by one. They rise. They move. They do what I tell them."

        athought "That's what they chose. That's why they're still here."

        $ rel_bump("Zira", respect=1)
        $ flag("ob_immediate_command", True)

        jump .scene_close

    # --- BRANCH: ACKNOWLEDGE GUILT ---
    label .acknowledge_guilt:

        a "We all saw what happened."

        athought "The words land like a blade dropped on stone. No one moves."

        a "We all chose to stay. We all chose this story. Whatever comes next, we carry it together."

        athought "Lyra's jaw tightens. Tessa's hands flatten against the table. Zira exhales slowly. Noelle tilts her head, cataloging."

        l "Is that supposed to make it easier?"

        a "No. It's supposed to make it true."

        athought "Silence. Then Tessa speaks, her voice barely above a whisper."

        t "She would have done the same thing. If it had been you standing in her way."

        athought "I don't know if that's absolution or accusation. I don't ask."

        a "Eastern route is compromised. Sector 7 reroute. Assignments as discussed. We move in six hours."

        athought "They rise. They don't look at each other. But something has shifted - the silence between us is no longer avoidance."

        athought "It's agreement."

        $ rel_bump("Lyra", trust=1)
        $ rel_bump("Tessa", trust=1)

        jump .scene_close

    # --- BRANCH: EMBRACE SILENCE ---
    label .embrace_silence:

        athought "I don't speak. I watch them. They watch me. The silence stretches until it becomes its own kind of answer."

        athought "We all know what we did. We all know why we're here. Words would only diminish it."

        n "Interesting."

        athought "Noelle breaks the silence. Her voice is clinical, detached."

        n "You're testing whether we'll speak first. Whether the guilt will fracture our cohesion before the mission does."

        a "And?"

        n "It won't. We've already made our calculation. Speaking now would only introduce inefficiency."

        athought "Zira snorts. It isn't quite a laugh."

        z "She isn't wrong. Eastern route, Sector 7, move in six. Do we need to keep pretending this is a discussion?"

        a "No."

        athought "They rise. They move. The silence follows them out."

        athought "Noelle pauses at the door."

        n "For what it's worth: your silence was more effective than any justification would have been."

        athought "She leaves. I don't know if that was a compliment."

        $ rel_bump("Noelle", respect=1)

        jump .scene_close

    # --- CONVERGENCE: THE CHAIR ---
    label .scene_close:

        # VISUAL: Aeron alone in the war room. The displays hum. Selene's chair remains empty.
        # CAMERA: Slow push toward the chair as he approaches it.

        athought "The room is quiet now. The displays cycle through data I've already memorized. Supply lines. Patrol routes. Casualty estimates."

        athought "Selene's chair sits at the head of the table. Empty. Waiting."

        athought "Four people watched me kill her. Four people chose to stay. Four people are now bound to me by something stronger than loyalty."

        athought "Complicity."

        athought "I should feel something about that. Guilt. Gratitude. Horror."

        athought "I feel efficiency."

        athought "Selene would have called that a warning sign. I call it necessary."

        # VISUAL: Aeron turns to look at Selene's chair. Slowly, deliberately, he pulls it back. He sits.
        # CAMERA: Low angle looking up at him in the chair. Coronation by crime.

        athought "I pull out Selene's chair. The metal scrapes against the floor - a sound like a blade drawn from its sheath."

        athought "I sit."

        athought "The chair is cold. The war room is silent. The displays cycle through casualty projections and supply routes."

        athought "Four witnesses. One chair. One story we tell together."

        # --- FADE OUT ---

        #stop ambient fadeout 2.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ flag("selene_killed_by_aeron", True)
        $ flag("lis_witnessed_murder", True)
        $ flag("aeron_took_command_chair", True)
        $ scene_mark(_current_scene_id, "completed")

        return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s01_ashes_in_formation_ob
# cann.chapter: Act III, Chapter I - Complicity (Obedience Path)
# cann.chapter_start: True
# cann.when_in_timeline:
#   - Act III opener, three days after Selene execution. Her funeral.
# cann.what_happened:
#   - Aeron delivers a rehearsed eulogy to 47 rebels. 43 believe the lie. 4 were there.
#   - The four LIs (Lyra, Zira, Tessa, Noelle) each contributed to the cover-up.
#   - After the funeral, they gather in the war room. No one has taken Selene's chair.
#   - Player choice: take command (Zira respect), acknowledge guilt (Lyra/Tessa trust), or silence (Noelle respect).
#   - All paths end with Aeron sitting in Selene's chair. Coronation by crime.
# cann.aeron_state:
#   - OB detachment - clinical, efficient, self-aware but unmoved.
#   - He knows this is monstrous. He chooses utility over conscience.
# cann.path_tracking:
#   - OB baseline. All three choices are OB-coded; variance is which LI responds.
#   - Take command: rel_bump Zira respect+1, flag ob_immediate_command.
#   - Acknowledge guilt: rel_bump Lyra trust+1, Tessa trust+1.
#   - Embrace silence: rel_bump Noelle respect+1.
# cann.thematic_flags:
#   - The funeral is a lie they're telling TOGETHER. Collective authorship of the narrative.
#   - Their bond is no longer shared ideals - it's shared crime. Complicity > loyalty.
#   - The inside/outside of the lie: 43 believers, 4 witnesses.
#   - "I feel efficiency." / "Selene would have called that a warning sign. I call it necessary."
# cann.character_moments:
#   - Lyra: Numb. Praying to no one. "I keep waiting to feel something. Nothing. Just silence."
#   - Zira: Professional. Deleted the footage. "The story holds. For now."
#   - Tessa: Conflicted. "Because someone has to keep you human." May have failed.
#   - Noelle: Clinical. Cataloging. "Your performance was statistically convincing."
# cann.block_status:
#   - ANCHOR (OB Act 3 opener); requires followup scene load.
# cann.requires_followup:
#   - Next scenes: Nyra introduction, OB council restructure, complicity deepening beats.
#   - Lyra's numbness needs bridge to later fierce conviction.
#   - Tessa's "keep you human" needs payoff.
#   - The four-witness complicity binds them for rest of OB route.
