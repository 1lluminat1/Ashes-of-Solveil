# =======================================================
# ACT 3 - Scene 08: Perfect Execution (Obedience Path)
# File: a3_s08_perfect_execution_ob.rpy
# Path: OB
# Type: OPERATION + NARRATOR AWARENESS
# Character Focus: Aeron, Nyra (co-command), Zira (aftermath)
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s08_perfect_execution_ob"
$ scene_mark(_current_scene_id, "entered")

# ny (Nyra) is defined centrally in ui_solveil.rpy

label a3_s08_perfect_execution_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 40mm locked during planning. Switch to 50mm handheld during the operation --
    #         but steadier than combat should be. The steadiness IS the horror.
    #         Mirrored two-shots of Aeron and Nyra throughout. Same posture. Same timing.
    #         Wide aftermath shot: bodies, silence, Nyra's soldiers already policing the scene.
    # LIGHTING: Planning room: tactical blue. Operation: sodium orange from sector infrastructure,
    #           muzzle flash, then darkness. Aftermath: grey pre-dawn. Clinical.
    # SFX: Loop -- operation: suppressed gunfire, boots on concrete, radio clicks.
    #      Aftermath: wind, distant city hum, body bags being zipped.
    #      One-shots -- each kill is a single sound: pop, thud, silence. Clean.
    # FX/COMP: Tactical overlay during planning. Kill zone geometry.
    #          Operation: smoke, muzzle flash, precision movement.
    #          Aftermath: Echelon bodies in rows. Nyra's soldiers working. No urgency.
    # BLOCKING: Planning: Aeron and Nyra at the tactical table, mirrored posture.
    #           Operation: split-screen movement. Two teams, one mind.
    #           Aftermath: Aeron standing over the kill zone. Zira behind him.
    # CANON: First joint operation. Sector 4 strike. Fourteen Echelon dead. Zero Phoenix.
    #        This is OB Aeron at his most capable and his most disturbing.
    # FACE: Aeron: mask throughout. Nyra: calm. Zira: unsettled. The dead: unseen.

    # ========= VOICE BASELINE =========
    # OB Aeron: Operational. Clipped. No wasted words during the op. Reflective after.
    # Nyra: Mirror of Aeron's cadence. They finish each other's tactical sentences.
    # Zira: Present for aftermath. Disturbed by how clean it was.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - TACTICAL ROOM - 0300]
    # Then: [EXT. SECTOR FOUR - ECHELON SUPPLY DEPOT - 0430]
    # Then: [EXT. SECTOR FOUR - AFTERMATH - 0500]

    #scene bg_tactical_room_ob with dissolve
    #play ambient "sfx/ambient/base_hum_cold.ogg" fadein 1.5

    # --- PLANNING ---

    "0300. The tactical room is lit by the blue glow of the planning display. Two figures stand on opposite sides of the table."

    "Mirror images. Same posture. Same angle of attention."

    #show nyra tactical_standing with dissolve

    athought "Sector Four supply depot. Echelon resupply point for their eastern corridor patrols. Twelve to sixteen personnel. Light armor. Predictable rotation."

    athought "Nyra identified it. I confirmed it. Together we built the operational plan in forty minutes."

    athought "It should have taken four hours."

    ny "Two teams. Alpha enters from the western access. Bravo holds the eastern chokepoint. Suppressive fire pins them against the loading bay wall."

    a "Crossfire angle from the second-floor landing. Elevation advantage neutralizes their cover."

    ny "Timing window: ninety seconds from first contact to full suppression. After that, their communication relay activates and we lose the element of surprise."

    a "Ninety seconds is generous. Your soldiers can do it in sixty."

    "Something flickers across her face. Not quite a smile."

    ny "Seventy. I account for human error."

    a "Fair."

    athought "She accounts for human error. She does not account for her own."

    athought "Neither do I."

    # --- THE OPERATION ---

    #scene bg_sector4_depot_night with dissolve
    #play ambient "sfx/ambient/urban_night_tense.ogg" fadein 2.0

    "0430. Sector Four."

    "The supply depot sits in a concrete hollow between two derelict residential blocks. Emergency lighting casts sodium orange across the loading bays. Four Echelon guards on external rotation. The rest inside."

    athought "Alpha team in position. Bravo holding the chokepoint."

    athought "Nyra's voice in my earpiece, steady as a metronome."

    ny "Alpha, confirm position."

    a "Alpha confirmed. Visual on four external. Two at the south bay, two walking perimeter."

    ny "Bravo confirmed. Eastern chokepoint sealed. No exits."

    athought "Sealed. No exits."

    athought "Fourteen people inside a box they do not know is closing."

    a "Execute on my mark."

    "Three seconds."

    a "Mark."

    #play sound "sfx/suppressed_gunfire_burst.ogg"

    "The first two guards drop before the sound reaches the walls. Suppressed fire. Center mass. They fold like paper."

    "The perimeter guards turn. Too slow. Nyra's Bravo team has already closed the eastern access. The first guard's weapon rises halfway before two rounds find his chest."

    "The fourth runs. Three steps. A single shot from the second-floor landing. He falls mid-stride."

    athought "Four down. Eight seconds."

    "The interior responds. Shouts. Weapons cycling. The loading bay door rolls open and three Echelon soldiers push out into what they think is defensible cover."

    "It is not."

    "Crossfire from Alpha and the landing position catches them in a geometry they cannot escape. Three seconds of concentrated fire. Then silence."

    athought "Seven down. Nineteen seconds."

    "The remaining personnel inside attempt to barricade. Nyra's Bravo team breaches the eastern service entrance -- the one Echelon sealed with a padlock and forgot about."

    "The breach is surgical. Room by room. Each doorway cleared in sequence. No hesitation. No wasted ammunition."

    #play sound "sfx/door_breach_clean.ogg"

    athought "I can hear it through the comms. The rhythm of it. Door. Clear. Move. Door. Clear. Move."

    athought "Like a heartbeat."

    "The last Echelon operative is cornered in the supply manager's office. He has a sidearm. He raises it."

    "Two rounds. Center mass. He sits down against the wall like someone who is very tired."

    ny "All clear. Fourteen hostiles neutralized."

    a "Phoenix casualties?"

    ny "Zero."

    athought "Zero."

    athought "Fourteen dead. Zero lost. Seventy-one seconds."

    # --- AFTERMATH ---

    #scene bg_sector4_depot_dawn with dissolve
    #play ambient "sfx/ambient/wind_urban_quiet.ogg" fadein 2.0

    "0500. The pre-dawn grey turns the depot into a photograph. Monochrome. Still."

    "Nyra's soldiers move through the kill zone with professional efficiency. Weapons collected. Ammunition secured. Supplies catalogued."

    "The bodies are arranged in rows. Not out of respect -- out of inventory."

    athought "Fourteen Echelon soldiers. Supply depot personnel. Not frontline. Logistics, maintenance, two communications officers."

    athought "They died in seventy-one seconds."

    athought "They died cleanly."

    "Zira arrives with the Ghostline relay team. She stops at the depot entrance. Surveys the scene."

    #show zira depot_entrance with dissolve

    "Her eyes move across the rows. The collected weapons. The soldiers working without urgency. The absence of chaos."

    z "How many?"

    a "Fourteen."

    z "Ours?"

    a "Zero."

    "She looks at the kill zone. The geometry of it. The precision."

    z "That was too clean."

    a "Clean is efficient."

    ny "Clean is mercy."

    "Nyra approaches from the eastern access. No blood on her. No disorder."

    ny "Every second of confusion is a second of suffering. We gave them seventy-one seconds. Most of them never knew what was happening."

    z "That isn't mercy. That's extermination."

    ny "The distinction is academic. The outcome is identical. The only variable is the suffering of the target."

    ny "Would you prefer we had given them time to be afraid?"

    "Zira has no answer. She turns to the relay equipment and begins working."

    athought "Zira sees the horror in the precision."

    athought "She is correct."

    athought "But the precision is why no one on our side is dead."

    # --- NARRATOR AWARENESS ---

    athought "Operation successful. Echelon losses: fourteen combatants. Phoenix losses: zero."

    menu:
        "The depot is quiet. The bodies are in rows. The numbers are clean."

        "Fourteen people are dead because of my plan.":
            $ choice_and_dev(
                _current_scene_id, "_weight_of_command", "EMP", factor=1,
                next_scene_label=None,
                note="Acknowledges the human cost. Cross-path moment -- EMP impulse on OB path."
            )
            jump .weight

        "Clean execution. Optimal outcome.":
            $ choice_and_dev(
                _current_scene_id, "_optimal", "OB", factor=1,
                next_scene_label=None,
                note="Full OB framing. The numbers are the truth."
            )
            jump .optimal

        "Those are the only two ways this system knows how to count." if tp_narrator_available():
            $ tp_narrator_acknowledged(_current_scene_id)
            jump .narrator_awareness

    # --- BRANCH: WEIGHT ---
    label .weight:

        athought "Fourteen people are dead because of my plan."

        athought "Supply clerks. A communications officer who was probably twenty-three. A maintenance tech whose tools are still laid out on the workbench."

        athought "They had rotations and routines and probably complained about the food."

        athought "And I drew a line on a map that ended them."

        "He walks through the depot. Past the rows. Past the collected weapons."

        athought "Clean execution."

        athought "I can hold both of those things. The precision and the cost. I can hold them."

        athought "But I notice which one I thought of first."

        jump .post_choice

    # --- BRANCH: OPTIMAL ---
    label .optimal:

        athought "Clean execution. Optimal outcome."

        athought "Fourteen Echelon operatives neutralized. Supply chain disrupted for an estimated nine days. Ammunition and provisions secured for Phoenix operations."

        athought "Zero casualties on our side. Two minor injuries -- a twisted ankle during the breach, a bruised elbow from cover transition."

        athought "By every metric that matters, this was perfect."

        "He reviews the supply manifest Noelle will need. Ammunition counts. Ration types. Medical supplies."

        athought "Perfect."

        athought "The word sits easily. That is new."

        jump .post_choice

    # --- BRANCH: NARRATOR AWARENESS ---
    label .narrator_awareness:

        athought "Fourteen dead. Zero lost. The math is clean."

        athought "But that is Marcus's math. And the grief is Kael's."

        athought "Neither of them is standing here. I am."

        athought "What is missing is the thing the system cannot count: the moment before the last guard raised his sidearm. The half-second where he might have surrendered."

        athought "We did not give him that half-second."

        athought "And I am the plan."

        jump .post_choice

    # --- POST-CHOICE ---
    label .post_choice:

        # VISUAL: Dawn breaking over the depot. Nyra's soldiers finishing their work.

        "The sky lightens. The depot operation is complete. Nyra's soldiers load the last of the secured supplies onto the transport."

        "Nyra appears beside Aeron. Close. Not touching."

        ny "The first of many, Commander."

        a "Yes."

        ny "Your planning was precise. Your execution was disciplined. The operation reflects the quality of its architect."

        athought "Its architect."

        athought "She means it as praise."

        athought "I accept it."

        "The transport rolls out. The depot stands empty. In nine hours, Echelon will discover what happened here."

        "They will find fourteen bodies in rows. Weapons accounted for. Supplies missing."

        "They will find no evidence of who did this. No spent casings that don't match their own inventory. No DNA. No trail."

        "Clean."

        athought "Seventy-one seconds."

        athought "We are getting better at this."

        athought "The question I do not ask: better at what?"

        # --- END ---

        #stop ambient fadeout 2.0
        #scene black with fade

        # ========= STATE UPDATES =========
        $ scene_mark(_current_scene_id, "completed")
        $ canon_set("sector4_strike_success")
        $ npc_remember("Nyra", "perfect_execution", tone="mirrored_command")
        $ npc_remember("Zira", "perfect_execution", tone="disturbed_by_precision")

        return

# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s08_perfect_execution_ob
# cann.chapter: Act III, Phase I -- Consolidation
# cann.chapter_start: False
# cann.when_in_timeline: Days after "Terms of Order." First joint Aeron/Nyra operation.
# cann.what_happened:
#   - Sector 4 supply depot strike. Co-planned by Aeron and Nyra in 40 minutes.
#   - Execution: 71 seconds. 14 Echelon dead. Zero Phoenix casualties.
#   - Surgical precision. Two teams, mirrored command, no wasted motion.
#   - Zira: "That was too clean." Nyra: "Clean is mercy."
#   - Player choice: acknowledge the human cost (EMP cross-path), accept the optimal
#     outcome (OB), or see past both frames (Narrator Awareness / True Path).
#   - TP beat: "That's Marcus's math. And the grief is Kael's. Neither of them is standing here."
# cann.aeron_state:
#   - OB peak capability. Clipped operational language. Mirrored with Nyra.
#   - Post-op reflection depends on choice: weight, satisfaction, or awareness.
#   - "We are getting better at this. The question I do not ask: better at what?"
# cann.path_tracking:
#   - Weight of command: choice_and_dev EMP factor=1 (cross-path moment)
#   - Optimal: choice_and_dev OB factor=1
#   - Narrator Awareness: tp_narrator_acknowledged (if available)
#   - All paths: canon_set("sector4_strike_success")
# cann.thematic_flags:
#   - The operation's beauty IS the horror. Flawless violence.
#   - Aeron and Nyra as mirrored command -- same posture, same timing, one mind.
#   - "Clean is mercy" -- Nyra's doctrine. Reduces suffering by reducing time.
#   - Zira's discomfort: "Too clean." She recognizes Echelon methodology.
#   - The supply manager sitting down "like someone who is very tired" -- death domesticated.
#   - Bodies in rows "not out of respect -- out of inventory."
#   - TP narrator beat references Marcus (father/control) and Kael (friend/grief) --
#     the two poles Aeron cannot synthesize without True Path awareness.
# cann.character_moments:
#   - Nyra: "Seventy. I account for human error." Mirrored command. "The first of many."
#   - Zira: "That was too clean." / "That isn't mercy. That's extermination."
#   - Aeron: "We are getting better at this." The satisfaction is the tell.
# cann.block_status:
#   - ANCHOR (always plays). Choice affects internal framing, not plot.
# cann.requires_followup:
#   - Echelon Interlude 3 (OB) -- how Echelon interprets this operation.
#   - "Tessa Friction" -- Tessa reacts to what Aeron is becoming.
#   - Counter-strike -- Echelon responds with targeted assassination attempt.
