# =======================================================
# ACT 3 - Scene 20b: The Archive (Empathy Path)
# File: a3_s20b_lyra_archive_emp.rpy
# Type: LYRA EMOTIONAL + PLOT BEAT -- after the Story Keeper reveal
# Fires after a3_s20. Lyra finds Aeron searching for his mother's trail.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s20b_lyra_archive_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s20b_lyra_archive_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked. Opens on Aeron's hands at the mapping terminal -- searching.
    #         Lyra enters frame from the left. The camera holds the two-shot but favors
    #         the space between them -- the gap that closes across the scene.
    #         The prayer beat: close on Lyra's mouth. The Old Tongue is sound, not subtitle.
    #         The recognition beat: Lyra's hand on the registry page. Macro on the handwriting.
    # LIGHTING: Mapping station, late. Blue-green terminal glow. When Lyra speaks the prayer,
    #           the amber practical catches her face. The warmth arrives with the words.
    # SFX: Loop -- mapping station ambient. Terminal hum. Quiet.
    #      One-shots -- Lyra's footsteps (soft, deliberate), the old registry page turning.
    # BLOCKING: Aeron at the mapping terminal. Lyra enters. She does not sit -- she stands
    #           beside him. The prayer is standing. The registry recognition is standing.
    #           They are both upright for the whole scene. Neither sits.

    # ========= VOICE BASELINE =========
    # EMP cadence. Lyra's warmth tempered by reverence. She is not here to comfort --
    # she is here to be present, and the presence includes a piece of intelligence
    # she didn't know she was carrying. lthought for her interior.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - MAPPING STATION - LATE NIGHT]

    #scene bg_mapping_station_night_emp with dissolve
    #play ambient "sfx/ambient/mapping_station_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE SEARCH ==========

    "Aeron is at the mapping terminal at 0300. The relay maps are open. He is not mapping courier routes -- he is searching. The cursor moves through pre-Purge records with the focus of a man who has just learned his mother is alive and cannot stop looking for the shape of her in the data."

    "He doesn't hear Lyra come in."

    lthought "He has been here for two hours. I checked the corridor log. He came straight from the briefing with Zira and Noelle and he has not left."

    lthought "He is looking for her. Of course he is. The Story Keeper has a name now and the name is his mother's and he is tracing her through the network like a man following a prayer he just learned the words to."

    "She stands at the edge of the station. She doesn't announce herself."

    l "Aeron."

    "He looks up. His eyes take a moment to adjust from the terminal glow to the person standing in the doorway."

    a "Lyra. It's late."

    l "It is late. You are still here."

    a "I'm following the courier mark from the letter. The same mark Zira found in the Story Keeper network. If I can trace the pattern far enough back, I can find her transit route."

    l "I know what you are doing."

    "She enters the station. Crosses to the terminal. Stands beside him -- not close enough to crowd, close enough that her shoulder is visible in his peripheral vision."

    l "I am not here to tell you to stop."

    a "Good."

    l "I am here to stay."

    # ========== PHASE 2 -- THE PRAYER ==========

    "She is quiet for a long time. The terminal cycles. Aeron searches. Lyra watches the data scroll without reading it -- she is watching him read it, and the watching is the vigil."

    lthought "He is holding the letter inside his jacket. I can see the shape of it against his chest. He has not taken it out. He does not need to take it out. He knows what it says."

    lthought "I know what it means to search for someone the faith told you was gone. I did it for three years with the Anayet texts before I found the wing."

    "She speaks. Not to him. Not exactly."

    l "{i}Vel anai su theran, vel anai su meret.{/i}"

    "The Old Tongue. A single line. The cadence of something older than the Cathedral, older than the registries, older than any system that tried to contain it."

    athought "I don't know the translation. I don't need it. The sound is enough."

    athought "She is praying. Not for the dead -- for the searching. She is blessing the act of looking for someone who might still be alive."

    l "It means: {i}What is sought in love is found in love.{/i} It is what the Anayet mothers said before the Long Walk. It is not a promise. It is a direction."

    a "A direction."

    l "Yes. Toward. Not a guarantee of arrival. Just the facing."

    "The terminal hums. The prayer sits in the room like a stone dropped into still water. The ripples are quiet."

    # ========== PHASE 3 -- THE RECOGNITION ==========

    "Lyra is watching the pre-Purge records scroll. Something catches her eye."

    lthought "Wait."

    "She leans forward. Her hand comes up -- not touching the screen, hovering near it."

    l "Stop. Go back."

    "Aeron stops the scroll. Steps back to the previous record set."

    l "There. The handwriting sample in the courier registration."

    "On the screen: a fragment of a handwriting sample from a pre-Purge courier registration. Part of the dead drop network. The handwriting is small, even, unhurried."

    l "I have seen this hand before."

    a "Where?"

    lthought "The wing. The sealed wing where the Cathedral kept the names they did not want found. The registries I was not supposed to read. The records that survived the Purge because someone hid them in the one place Echelon would not look -- inside the faith's own archive."

    l "In the Cathedral. In the wing where they kept the names."

    "Aeron turns to her. The searching stops."

    a "What wing?"

    l "The sealed wing of the Cathedral archive. The registries from before the Purge. The names of people who were removed from public record -- dissidents, defectors, people who chose to disappear rather than comply."

    l "The Cathedral kept them. Not officially. A group of archivists -- Anayet-trained, some of them -- hid the registries in the sealed wing because the names were sacred to them. Not politically. Theologically. The Anayet tradition holds that a name spoken is a soul preserved."

    l "I found the wing when I was seventeen. I spent two years reading the registries before they caught me and sealed it again."

    a "And the handwriting."

    l "I have seen this hand. This exact hand. In the registry of the Sector 4 displaced -- the families that were moved during the first Purge sweep. The curling 'a.' The high 't.' I remember because the penmanship was beautiful and the content was a list of children who had been separated from their parents."

    "The room is very still."

    l "She was keeping the names, Aeron. Before Zira. Before the Ghostline. Your mother was keeping the names."

    athought "She was keeping the names."

    athought "Liora. In the sealed wing of the Cathedral. Writing the names of children separated from their parents. In the same handwriting that wrote the letter to my father. In the same handwriting I inherited."

    a "Can you find the registry again?"

    l "The wing was resealed. But I remember the location. If the Cathedral archive survived the displacement, and if the sealed wing was not found by Echelon in the interim -- yes. I can find it."

    a "Lyra."

    l "I know."

    "She doesn't need him to say the rest. She already knows what the registry means: a thread. A concrete trail. Liora's handwriting in the Cathedral, connected to the courier network, connected to the Story Keeper."

    # ========== PHASE 4 -- THE STAYING ==========

    l "I will help you search. Not tonight. Tonight, I will stay."

    a "You don't have to."

    l "I know I don't have to."

    lthought "He does not understand yet that the staying is not obligation. It is the same impulse that brought the Anayet mothers to the Long Walk -- the refusal to let someone search alone. The direction is toward. The company is the prayer."

    "She stands beside him at the terminal. She does not touch him. She does not speak the Old Tongue again. She is present in the way that presence is a discipline -- not passive, not active, just there."

    "He goes back to searching. The cursor moves through the records."

    "Lyra watches. The mapping station hums."

    "He searches. She stays."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Lyra", trust=1)
    $ flag("lyra_cathedral_registry_clue", True)
    $ npc_remember("Lyra", "recognized_liora_handwriting_cathedral", tone="reverent_certainty")
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s20b_lyra_archive_emp
# cann.chapter: Act III, Phase III -- Revelation & Cost (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - After a3_s20 (Story Keeper reveal). Same night, 0300. Aeron searching.
# cann.what_happened:
#   - Lyra finds Aeron searching for Liora's trail at the mapping terminal.
#   - She offers an Old Tongue prayer: "What is sought in love is found in love."
#   - Plot clue: Lyra recognizes Liora's handwriting from the sealed Cathedral wing
#     where dissident registries were hidden by Anayet-trained archivists.
#   - Liora was keeping names of displaced children before the Ghostline existed.
#   - Lyra can potentially locate the registry if the Cathedral archive survived.
# cann.callbacks:
#   - a3_s18a: the letter. The handwriting. The curling 'a' and high 't.'
#   - a3_s20: the Story Keeper reveal. The courier mark. The network pattern.
#   - Lyra's Anayet tradition: names spoken are souls preserved.
#   - The sealed wing: Lyra found it at seventeen, read registries for two years.
# cann.requires_followup:
#   - flag("lyra_cathedral_registry_clue") gates future registry search scenes.
#   - The sealed wing location feeds into potential Act 4 Cathedral return.
