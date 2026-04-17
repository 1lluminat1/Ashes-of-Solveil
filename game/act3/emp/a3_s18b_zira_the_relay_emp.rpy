# =======================================================
# ACT 3 - Scene 18b: The Relay (Empathy Path)
# File: a3_s18b_zira_the_relay_emp.rpy
# Type: ZIRA EMOTIONAL BEAT -- post-letter processing
# Fires after a3_s18a (the letter). Zira alone at the relay station.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a3_s18b_zira_the_relay_emp"
$ scene_mark(_current_scene_id, "entered")

label a3_s18b_zira_the_relay_emp:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked. Opens on Zira's hands on the relay console, not her face.
    #         The camera stays on hands and equipment for the first third. When it
    #         finds her face, it holds. No cuts. The intimacy is in the stillness.
    #         Final beat: the camera pulls back to show the whole station -- Zira
    #         small inside the network she built.
    # LIGHTING: Relay station at night. Blue-green terminal glow. One amber desk lamp.
    #           The amber is the only warm thing in the room. It lights her hands.
    # SFX: Loop -- relay station hum. Ghostline carrier signal cycling. Quiet.
    #      One-shots -- console toggle, her breath, chair creak.
    #      No music. The ambient carries it.
    # BLOCKING: Zira alone at the relay console. She has just returned from delivering
    #           the letter to Aeron. The station is hers. No one else comes in.

    # ========= VOICE BASELINE =========
    # EMP cadence. Zira interior. Sharp self-assessment that softens into something
    # she doesn't have vocabulary for yet. zthought carries the scene.
    # Almost no spoken dialogue -- she is alone.

    # --- VISUAL SETUP ---
    # [INT. PHOENIX BASE - RELAY STATION - NIGHT]

    #scene bg_relay_station_night_emp with dissolve
    #play ambient "sfx/ambient/relay_station_hum.ogg" fadein 2.0

    # ========== PHASE 1 -- THE RETURN ==========

    "The relay station is quiet. Zira came back here after she gave him the letter because this is the room where the letter stopped being intelligence and started being personal, and she needs to sit with that transition in the place where it happened."

    "Her console is still running. The Ghostline carrier maps cycle through their patterns -- courier routes, dead drops, the architecture of a network she inherited from ghosts and rebuilt into something that breathes."

    zthought "He sat down."

    zthought "I told him to sit and he didn't. Then he read the letter and his legs decided for him. That is not something I planned for."

    zthought "I plan for most things."

    "She toggles through the relay logs. The dead drop in Sector 4 is flagged in her system as RETRIEVED. The courier mark is catalogued. The chain of custody is clean."

    "The chain of custody does not include the part where a man read his dead mother's handwriting and recognized his own."

    zthought "Not dead. Missing. Presumed dead. Those are different categories and I used to be precise about them."

    zthought "She is alive. The courier mark dates, the paper degradation, the ink -- my analysis puts the letter at sixteen to nineteen years old, but the network pattern it connects to is active. Someone is still running drops through infrastructure she built."

    zthought "Liora Rylan is alive and she has been running a courier network that predates mine, and I found her because I was mapping the roots of my own system and her roots were underneath."

    # ========== PHASE 2 -- THE WEIGHT ==========

    "She leans back in the chair. The amber lamp catches the edge of her jaw. She's not looking at the console anymore."

    zthought "I found his mother."

    zthought "That sentence has a shape I did not expect. I have found people before. I have found dead drops, safe houses, compromised agents, buried supply caches. Finding is what the Ghostline does. Finding is what I do."

    zthought "But I found his mother."

    zthought "The Ghostline -- my network, my couriers, my mapping protocols -- surfaced the woman he has been grieving for most of his life. The woman he sealed behind whatever wall he built when he was too young to build walls and built one anyway."

    "She closes the relay log. Opens it again. Closes it."

    zthought "I don't know if that was a gift or a weapon."

    zthought "I found her for him. I gave him the letter because it was addressed to his father and the handwriting said Marcus and there was no version of this where I kept it. But the finding -- the fact that my network was the mechanism -- that changes something between us and I cannot map the shape of what it changes."

    zthought "If she is alive and he finds her and she is who the letter says she is, then I gave him back a piece of himself he thought was gone."

    zthought "If she is alive and he finds her and she is not who he needs her to be, then I gave him a wound with my network's fingerprints on it."

    # ========== PHASE 3 -- THE NETWORK ==========

    "The Ghostline maps cycle on the console. She watches the patterns without reading them."

    zthought "The courier infrastructure she built -- it's good. Better than good. The stamp methodology, the dead drop placement, the addressing conventions -- she was running a network before the Purge that would have taken me years to design from scratch."

    zthought "I built on top of her work without knowing it. The foundations of my network are her foundations. The routes I thought I discovered were routes she laid down and the Purge buried but didn't kill."

    zthought "I have been standing on her architecture for three years."

    "She pulls up the Sector 4 mapping overlay. The courier routes thread across the display. Her routes in blue-green. Beneath them, in a paler trace, the pre-Purge layer. Liora's layer."

    zthought "Her network kept six thousand names alive. Mine keeps the Ghostline breathing. We are doing the same work separated by a generation and a catastrophe, and I did not know she existed until I found a letter she never sent to a man she loved and left."

    zthought "I love you. I left. Both are true."

    zthought "I don't have that sentence in my vocabulary. I don't leave. I route around. I find the other path. I map the alternative."

    zthought "But I understand the woman who wrote it. And that is the part I didn't expect."

    # ========== PHASE 4 -- THE QUIET ==========

    "She turns off the mapping overlay. The console dims to standby. The amber lamp is the only light left."

    "She sits in the relay station with the hum of the Ghostline and the knowledge that the network she built is rooted in a woman she has never met, and that the man she gave the letter to is sitting somewhere in this base with his mother's handwriting against his chest."

    zthought "I am going to find her."

    zthought "Not for intelligence value. Not for the network. For him."

    zthought "That is not how I make decisions. That is not the calculus I was trained in. The Ghostline runs on operational logic -- every asset, every risk, every route evaluated by what it costs and what it yields."

    zthought "Finding Liora Rylan for Aeron Rylan yields nothing I can put in a briefing."

    zthought "I am going to do it anyway."

    "She reaches for the console. Her fingers hover over the relay controls."

    "She doesn't activate them. Not tonight. Tonight is for sitting with the weight of what she already found."

    "The Ghostline hums. The relay station holds her. The amber lamp stays on."

    #stop ambient fadeout 3.0
    #scene black with fade

    # ========= STATE UPDATES =========
    $ rel_bump("Zira", trust=1)
    $ npc_remember("Zira", "processed_liora_letter_alone", tone="quiet_resolve")
    $ scene_mark(_current_scene_id, "completed")

    call li_lore_check("Zira") from _a3_s18b_lore

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a3_s18b_zira_the_relay_emp
# cann.chapter: Act III, Phase III -- Revelation & Cost (Empathy Path)
# cann.chapter_start: False
# cann.when_in_timeline:
#   - After a3_s18a (the letter). Same night. Zira returns to the relay station alone.
# cann.what_happened:
#   - Zira processes the delivery of Liora's letter to Aeron.
#   - Recognizes that the Ghostline was built on Liora's pre-Purge courier infrastructure.
#   - The key line: "I found her for you. I don't know if that was a gift or a weapon."
#   - Decides to find Liora -- not for intelligence, for Aeron.
# cann.zira_state:
#   - Confronting the personal dimension of her network for the first time.
#   - "I have been standing on her architecture for three years."
#   - The operational calculus cannot hold what she is feeling.
# cann.callbacks:
#   - a3_s18a: the letter delivery. Aeron sitting down. "It was always yours."
#   - Liora's 6000-name network. Zira's Ghostline built on top of it.
#   - "I love you. I left. Both are true." -- Zira understands the sentence she doesn't have.
# cann.requires_followup:
#   - Zira's search for Liora feeds into s20 (Story Keeper) reveal.
