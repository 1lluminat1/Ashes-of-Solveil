# act2_activity_07_confront_past.rpy

# =======================================================
# ACT 2 - Activity 7: Confront the Past
# =======================================================

# NOTE: Legacy dict writes have been removed in favor of the new helper system.
# If you need temporary back-compat, uncomment the legacy scaffold near the top.

define voice = Character("Voice", color="#616161")
define man = Character("Hector's Father", color="#4E342E")


label act2_activity_07_confront_past:

    # --- SCENE START (new helper system) ---
    $ mark_scene("activity7_past", start=True)
    $ log_line("activity7_past", "enter")

    # (Optional legacy scaffold; leave commented unless you need fallback.)
    # $ scenes["activity7_past"] = {
    #     "approached_survivor": False,
    #     "offered_help": False,
    #     "just_listened": False,
    #     "defended_actions": False,
    #     "hector_father_met": False
    # }

    # VISUAL: Safe house. Early morning. Aeron preparing. Different energy.
    # LIGHTING: Cold pre-dawn light. Gray. Heavy.
    # SOUND: City still sleeping. Quiet. Too quiet.

    "{i}Day [current_day]. Time to go back.{/i}"
    
    # VISUAL: Aeron checking fake ID. Kade Voss. But today feels like Aeron Rylan.
    a "{i}Sector 10. The Sweep. Where 600 died and 200 lived. I've been avoiding it, running from it. Time to stop running.{/i}"
    "{i}[ob] Names are doors; some only open from the inside. Today I knock as Aeron, not Glass.{/i}"

    # VISUAL: Lyra awake. Watching him. Concerned.
    l "You don't have to do this."
    a "I do. Zira said Selene would ask, but that's not why."
    l "Then why?"
    a "Because I need to see it. What I did, what Glass did. I need to stand there and face it."
    l "And if it breaks you?"
    a "(quiet) Then it breaks me. But I can't keep carrying it without looking at it."

    # VISUAL: She stands. Moves to him. Hand on his arm.
    l "I'm coming with you."
    a "You don't have to—"
    l "I know. But you shouldn't do this alone. Nobody should face their ghosts alone."
    
    # VISUAL: He looks at her. Grateful. Terrified. Accepting.
    a "...Thank you."
    l "Don't thank me yet. Let's see if we survive this."

    # TRANSITION: Journey to Sector 10. Long walk. Descending levels. Getting darker.
    # VISUAL: Moving through Lower Spans. Deeper. Sector 6, 7, 8... toward 10.
    # LIGHTING: Getting dimmer. More decay. Damage from Purge visible.
    # SOUND: Less life. Fewer people. Echoes. Emptiness.

    scene bg_lower_spans_descent with fade

    "{i}Down through sectors still recovering from the Purge. Sector 8 shows scars—buildings damaged, streets empty, ghosts everywhere. Sector 9 is worse with more destruction and fewer survivors. The Purge hit hard here.{/i}"
    "{i}[ob] The city breathes through cracked ribs; every exhale tastes like old fire.{/i}"

    l "(quiet) It's so empty."
    a "Most fled. The ones who stayed... most died in the Purge."
    l "100,000 people. Just gone."
    a "Not gone. Murdered. By Marcus, by Echelon, by the system we served."

    # VISUAL: Continue descent. Sector 10 ahead. Ruins visible.
    "{i}Sector 10 ahead. Where I swept, where it started, where Glass cracked.{/i}"
    "{i}[ob] Distance shrinks; consequences don’t.{/i}"

    # VISUAL: Enter Sector 10. Devastation. Buildings collapsed. Streets torn. Purge aftermath.
    # LIGHTING: Dark. Oppressive. Few lights working. Rubble everywhere.
    # SOUND: Wind through ruins. Metal creaking. Emptiness screaming.

    scene bg_sector10_ruins with fade

    "{i}Sector 10. Three weeks after the Sweep, two weeks after the Purge. Ruins everywhere—buildings collapsed from orbital strikes, streets torn apart. Nothing living should be here, but I am. Standing in the graveyard I helped create.{/i}"
    "{i}[ob] Buildings remember how to kneel; the street keeps its head bowed.{/i}"

    # VISUAL: Aeron stops. Staring. Memories flooding back. Overwhelming.
    a "{i}This corner. The child I saved stood right here. I logged her as terminated and she ran. She lived for two more weeks before the Purge. Did she survive the Purge or did I just delay her death?{/i}"
    "{i}[emp] Mercy felt like oxygen then; now it burns going down.{/i}"

    l "(hand on his shoulder) Aeron."
    a "(shaking) I walked these streets with orders to kill everyone. And I did. Most of them. 600 people."
    a "Right here on this street I killed... I don't even remember how many. They blur together."
    l "You also saved 200. That matters."
    a "Does it? I saved 200 and then the Purge killed most of them anyway. What's the point of mercy if it just delays death?"

    # VISUAL: Lyra quiet. No answer. Because there isn't one.
    "{i}Silence. Because what can she say? She's right and I'm right and nothing fixes it.{/i}"

    # VISUAL: Continue walking. Deeper into ruins. Looking for something. Someone.
    a "Zira said there's a survivor here. Someone who stayed, someone who remembers."
    l "How do we find them?"
    a "We don't. They find us. If they want to."
    "{i}[ob] In places like this, the ground does introductions.{/i}"

    # VISUAL: Walk through devastation. Each step a memory. Each corner a ghost.
    "{i}The vendor's stall was there. I killed him on direct orders. He begged but I shot anyway. The apartment on the fourth floor held a family of five—I breached it and four died while one child escaped. I logged them as terminated. Every step is blood, every breath is guilt, every moment is drowning.{/i}"

    # VISUAL: Aeron stops. Breathing hard. Panic building. Too much. Too fast.
    a "{i}Can't breathe. Too much, too many ghosts, too much blood.{/i}"

    l "(grabs him) Aeron. Look at me. Breathe."
    a "(gasping) I can't—there's too many—I killed—"
    l "Breathe. In. Out. Focus on my voice. Just my voice."
    
    # VISUAL: She grounds him. Hands on his shoulders. Eye contact. Breathing together.
    "{i}Her voice, her breath, her presence grounding me before I drown completely. In. Out. In. Out. Slowly the panic recedes. Barely, but enough.{/i}"
    "{i}[emp] She lends me a heartbeat until mine remembers its job.{/i}"

    a "(shaking) Thank you."
    l "Don't thank me. Just keep breathing. We'll get through this."
    a "Will we?"
    l "We have to. We came this far and we don't stop now."

    # VISUAL: Voice from the shadows. Male. Older. Cautious.
    voice "You came back."

    # VISUAL: Both turn. Man emerges from ruins. 50s. Scarred. Hollow eyes. Survivor.
    # SOUND: Footsteps on rubble. Slow. Deliberate.

    "{i}A man emerging from shadows, watching us. How long has he been there?{/i}"
    "{i}[ob] He is built from edges—rib, ruin, resolve.{/i}"

    a "Who are you?"
    man "Someone who lived. Barely. Someone who remembers you."
    a "You know me."
    man "Everyone in Sector 10 knew Glass. Hard to forget the man who swept through killing everyone."

    # VISUAL: Tension. Lyra's hand moves toward weapon. Aeron stops her.
    a "I'm not here to fight."
    man "Then why are you here? Nostalgia? Guilt? Curiosity?"
    a "...All of them. And to apologize. For what it's worth."
    man "(bitter laugh) Apologize. To who? The dead don't hear you."

    # VISUAL: Aeron doesn't flinch. Accepts it. Deserves it.
    a "I know. But I'm saying it anyway. I'm sorry for everything, for all of it."
    man "Sorry. That's it? Sorry for killing my son? Sorry for destroying my home? Sorry for being Echelon's perfect weapon?"
    a "Yes. I know it's not enough. Nothing's enough, but it's all I have."

    # VISUAL: Man steps closer. Evaluating. Angry but controlled.
    man "You killed 600 people here in one night. Do you even remember their faces?"
    a "...No. Not all of them. They blur together. And that makes it worse."
    man "At least you're honest. Most killers pretend to remember, pretend each death mattered."
    a "They did matter. Every single one. I just... I couldn't let them matter at the time or I'd have stopped. And stopping meant failing. And failing meant—"
    man "Meant what? Death? Punishment? What was so important you killed 600 people?"
    a "Nothing. There was nothing important enough. I just... followed orders. Like I always did, like Glass always did."

    # VISUAL: Man stares. Long. Hard. Then looks away.
    man "My son's name was Hector. He was 23, worked in mechanics. Good kid who didn't deserve any of this."
    man "You shot him in our apartment on the third floor. He was trying to protect me. You killed him and logged me as terminated."
    man "But you didn't kill me. You saw me hiding and you walked away. Why?"
    "{i}[emp] A name turns a crater into a map; everything in me tilts toward it.{/i}"

    # VISUAL: Aeron remembers. Vaguely. So many apartments. So many faces.
    a "I... I don't remember specifically. But by that point I was cracking. Saving who I could while failing everyone else."
    a "I'm sorry about Hector. I'm sorry you had to watch him die. I'm sorry I didn't save him."
    man "Sorry doesn't bring him back."
    a "No. It doesn't. Nothing does."

    # ACTION: Player choice - how to respond?
    menu:
        "The father stands there. Broken. Angry. Waiting."
        
        "Offer to help him - try to make amends":
            $ mark_flag("activity7_past.offered_help")
            $ rep("unders", +2)
            $ rel("hector_father", trust=+1)
            $ mark_flag("activity7_past.hector_father_met")
            $ log_line("hector_father", "help_needed")

            a "You're right. Sorry isn't enough. So let me help. Whatever you need—food, supplies, rebuilding. Anything."
            man "Help? You think helping now fixes what you destroyed?"
            a "No. But it's better than doing nothing. Better than just walking away again."
            man "Why? Why do you care now? Guilt? Redemption? What?"
            a "All of it. And because Hector deserved better. You deserved better. Everyone here did."
            
            # VISUAL: Man considers. Struggles. Wants to hate him. But exhausted.
            man "...Fine. You want to help? There are survivors scattered through these ruins. About 30 of us left from thousands."
            man "We need medical supplies. Food. Building materials. Basic things to survive."
            man "You bring those and maybe I'll believe you're serious. Maybe."
            a "I'll bring them. I promise."
            "{i}[emp] Promises are brittle until carried; this one sits in my pocket like a tool, not a word.{/i}"
            man "Promises from Glass should mean nothing. But... I'll give you one chance. Don't waste it."
            
        "Just listen - let him speak his pain":
            $ mark_flag("activity7_past.just_listened")
            $ rep("unders", +1)
            $ rel("hector_father", trust=+0)
            $ mark_flag("activity7_past.hector_father_met")
            $ log_line("hector_father", "shared_pain")

            a "I can't fix this. Can't undo it. All I can do is listen. If that helps."
            man "(laughs, hollow) Listen. To what? My pain? My rage? What good does that do?"
            a "Maybe none. But you deserve to be heard. Hector deserves to be remembered by someone who was there."
            
            # VISUAL: Man stares. Then slowly starts talking. Pain pouring out.
            man "He wanted to be an engineer. Build things instead of breaking them. He was good too, talented, had a future."
            man "Then you came. One night with orders for a compliance sweep. Kill everyone."
            man "He tried to fight. Grabbed a pipe thinking he could protect me. Brave and stupid both."
            man "You shot him center mass. Professional. Quick. He didn't suffer long. Small mercy."
            man "Then you saw me hiding, terrified, waiting to die. And you just... left. Walked away, logged me dead, moved on."
            man "I lived. But everything I lived for died that night. Everything."
            "{i}[emp] I make myself a vessel and try not to leak; his story deserves a steady container.{/i}"
            
            # VISUAL: Silence. Heavy. Nothing to say. Just witness his pain.
            a "Thank you for telling me. For letting me know who Hector was. He mattered. He still matters."
            man "To you? Or to your guilt?"
            a "...Both. But mostly to you. He mattered to you and that's what counts."
            
        "Defend your actions - you were following orders":
            $ mark_flag("activity7_past.defended_actions")
            $ rep("unders", -2)
            $ rel("hector_father", trust=-2)
            $ mark_flag("activity7_past.hector_father_met")
            $ log_line("hector_father", "rejected_by_survivor")

            a "I was following orders. I didn't have a choice. If I refused I'd be killed. My family would be killed."
            man "(steps back) Following orders. That's your defense?"
            a "I'm not defending it. I'm explaining—"
            man "You're making excuses. You had a choice. You could have refused, could have defected earlier. You chose not to."
            a "It's not that simple—"
            man "It is that simple. You killed my son because you were ordered to and you followed that order. That's a choice. Your choice."
            man "Don't come here looking for forgiveness while pretending you had no agency. You did. You chose. Live with it."
            
            # VISUAL: Man turns away. Conversation over. Disgusted.
            man "Get out. Don't come back. You're not welcome here."
            "{i}[ob] He leaves a door-shaped absence behind, and it closes on my tongue.{/i}"

            "{i}He walks away and disappears into ruins. I fucked that up completely by defending myself, by explaining, by making excuses—everything Tessa told me not to do.{/i}"

    # VISUAL: Aftermath of conversation. Processing. Heavy.
    if renpy.has_label("_dummy_check"):  # harmless no-op to keep Ren'Py parser happy on empty blocks
        pass
    if renpy.python.py_eval("get_flag('activity7_past.defended_actions')"):
        l "(quiet) That went well."
        a "Don't. I know I fucked up."
        l "Why did you defend it? You know you were wrong."
        a "I don't know. Instinct. Glass instinct to defend the mission and justify the kill."
        a "I'm supposed to be past that but it's still there, still rotting inside me."
        l "Then cut it out before it poisons everything you're trying to build."
    else:
        l "(quiet) That was hard to watch."
        a "Imagine how hard it was to live through. For him, for Hector."
        l "You handled it better than I expected."
        a "Did I? Feels like I just opened wounds that'll never heal."
        l "Maybe. But you faced it. That's more than Glass would have done."

    # VISUAL: Continue through ruins. Alone with thoughts. Ghosts everywhere.
    "{i}Sector 10. Graveyard of my making. Every step is a reminder, every breath is guilt.{/i}"
    "{i}[ob] The wind catalogs what we leave unsaid; the rubble files it under 'too late.'{/i}"

    # VISUAL: Find memorial. Makeshift. Names scratched on metal. Hundreds of names.
    # VISUAL: Wall of the dead. Each name a person. A life. A story ended.

    "{i}A wall with names scratched into metal. Hundreds of names. The dead memorialized by survivors. Hector's name is there, fourth from the top, and hundreds more below.{/i}"

    a "{i}Every single name. People I killed or helped kill. All here.{/i}"
    "{i}[emp] Each letter is a weight; together they’re a gravity that refuses to let me float away from what I’ve done.{/i}"

    l "(reading names) This is... all of them?"
    a "No. These are just the ones they could identify. Bodies recovered, names remembered."
    a "The rest are ash. Scattered, anonymous, forgotten except by those who loved them."

    # VISUAL: Aeron reaches out. Touches wall. Fingers tracing names. Heavy silence.
    "{i}My hand touches the cold metal. Rough scratches forming letters forming names forming lives that ended. Hector. Mara. Jen. David. Kessler. Tomas. On and on and on. Each name a weight, each name a ghost, each name a piece of glass cutting deeper.{/i}"
    "{i}[ob] The wall doesn’t forgive—walls never do. It only agrees to remember.{/i}"

    a "(whispers) I'm sorry. All of you. I'm sorry."
    
    # VISUAL: Lyra beside him. Silent. Present. No words help here.
    l "What do we do now?"
    a "We remember. We carry them. We try to do better."
    l "Is that enough?"
    a "No. But it's all we have."

    # VISUAL: Aeron pulls out small knife. Considers. Then scratches something into wall.
    # CARVING: "I'm sorry. - Glass"

    "{i}I carve words into the metal. Simple, insufficient, but necessary. 'I'm sorry. - Glass.' An admission, an apology, a gravestone for who I was.{/i}"
    "{i}[emp] The blade bites cleaner than truth, but the sting lands where it should.{/i}"

    l "Glass?"
    a "Yeah. Because Aeron didn't do this. Glass did. And Glass is dead. This is his grave too."
    l "Poetic."
    a "True. Glass died in the Purge along with everyone else. What's left is something else. Someone trying to be better."
    l "And if you fail?"
    a "Then at least I tried. That has to count for something."
    "{i}[ob] Names are masks until you bleed through them; this one finally sticks to skin.{/i}"

    # VISUAL: They stand there. Minutes passing. Honoring the dead. Carrying the weight.
    "{i}We stand for minutes or hours. Time loses meaning in graveyards. 600 names I helped create, thousands more from the Purge. All dead, all remembered, all haunting.{/i}"

    # VISUAL: Finally, Aeron turns away. Can't stay here forever.
    a "We should go. Nothing more we can do here."
    l "Are you okay?"
    a "No. But I will be. Eventually. Maybe."
    l "That's honest at least."
    a "Honesty's all I have left. Everything else burned."

    # VISUAL: Walk back through ruins. Changed. Heavier. Clearer.
    "{i}Walking back through ruins. Each step away from ghosts, each step toward something new. Maybe.{/i}"
    "{i}[emp] Step, breathe, carry—rituals for not breaking where the city already has.{/i}"

    # VISUAL: Hector's father watching from distance. Sees them leave. Doesn't approach.
    "{i}Hector's father watches from the shadows. Sees us leave but doesn't stop us, doesn't bless us, just watches. That's enough for now. Maybe forever, but enough.{/i}"

    # TRANSITION: Return to safe house. Evening. Exhausted. Changed.
    scene bg_safe_house with fade

    "{i}Back at the safe house. Evening. Body exhausted, mind more so. But something shifted. Facing ghosts, naming them, remembering them. Doesn't fix anything, doesn't redeem anything, but it's something.{/i}"

    # VISUAL: Lyra watching him. Concerned but understanding.
    l "How are you?"
    a "Heavy. Hollow. But... clear. Does that make sense?"
    l "Yeah. It does."
    a "I faced it. Saw what I did, met someone who lost everything because of me. And I didn't run."
    l "That's progress."
    a "Is it? Feels like I just confirmed what I already knew. That Glass was a monster, that I killed hundreds, that sorry means nothing."
    l "But you went. You faced it. You apologized even knowing it wouldn't help. That's not nothing."
    
    # VISUAL: Aeron quiet. Processing. Accepting. Maybe believing.
    a "Tessa said count the living but I need to count the dead too. Remember them, carry them."
    a "600 from the Sweep. Thousands from the Purge. All dead because of what I started, what I participated in."
    a "I can't forget them. Won't forget them. They deserve to be remembered."
    l "And they will be. By us, by survivors, by history."
    l "But you need to keep living too. Carrying the dead is important but don't let them drown you."
    "{i}[ob] Ledger of a life: debts in bone, payments in breath.{/i}"

    # VISUAL: He looks at her. Grateful. Grounded. Connected.
    a "Thank you for coming with me. For keeping me from drowning."
    l "That's what we do. We keep each other from drowning. Remember?"
    a "Yeah. I remember."

    # Show outcome summary based on choice (reads flags from helpers; works even if UI hides them)
    if renpy.python.py_eval("get_flag('activity7_past.offered_help')"):
        "{i}I offered help and promised supplies. Gave Hector's father a reason to maybe trust me. Maybe. One more thread, one more connection, building toward something slowly.{/i}"
    elif renpy.python.py_eval("get_flag('activity7_past.just_listened')"):
        "{i}I listened and let him speak his pain. Honored Hector's memory by hearing it, by remembering. Small and insufficient, but real. Sometimes that's all you can do.{/i}"
    else:
        "{i}I defended myself and made excuses. Proved I'm still carrying Glass's instincts, his cowardice. I need to do better, be better, before those instincts poison everything.{/i}"

    a "{i}Confronted the past. Faced the ghosts, named the dead, apologized to survivors. Doesn't fix anything, doesn't redeem anything, but it's done. And I'm still here. One more step away from Glass, one more step toward whatever comes next.{/i}"

    # Mark activity complete (new helper)
    $ mark_scene("act2_activity", complete="past")
    $ log_line("activity7_past", "exit")

    # TRANSITION: Back to hub
    jump act2_activity_hub

    # canon_note: Activity 7 complete - confronted past in Sector 10 ruins
    # canon_note: Returned to Sweep site - emotional weight, panic attack, Lyra grounds him
    # canon_note: Met Hector's father - survivor who lost son during Sweep
    # canon_note: Three choices: offer help (+2 rep, future subplot), listen (+1 rep, closure), defend actions (-2 rep, burned bridge)
    # canon_note: Memorial wall - hundreds of names, scratched Glass's apology into it
    # canon_note: "Glass died in the Purge" - symbolic grave for old identity
    # canon_note: 600 from Sweep + thousands from Purge - Aeron acknowledges full scope
    # canon_note: Lyra support crucial - keeps him from drowning in guilt
    # canon_note: If offered help: subplot with Hector's father, bringing supplies to survivors
    # canon_note: Sets up Selene meeting - she'll ask if he confronted past, he can say yes honestly
    # canon_note: Character growth: facing ghosts instead of running, remembering dead while counting living
    # canon_note: Emotional catharsis - doesn't fix anything but creates clarity

    return
