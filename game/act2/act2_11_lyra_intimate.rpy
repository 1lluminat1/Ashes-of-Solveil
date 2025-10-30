# act2_lyra_intimate.rpy
# =======================================================
# ACT 2 - Lyra Intimate Scene
# Helpers-only: no raw dict writes; flags via mark_flag(); 
# romance via unlock_romance(); relationship via rel();
# activities completion via check_scene_flag().
# =======================================================

# Alias so either label name works
label act2_lyra_intimate_scene:
    jump act2_lyra_intimate


label act2_lyra_intimate:
    
    # Mark scene as started/unlocked (flagged, not raw dict)
    $ mark_flag("Lyra", "lewd_scene_unlocked")
    
    # VISUAL: Safe house. Evening deepening into night. Just them.
    # LIGHTING: Single dim light. Shadows soft. Intimate.
    # SOUND: City distant. Their breathing. Heartbeats. Silence alive.
    
    scene bg_safe_house_night with fade
    
    "{i}Night falls. The small space feels smaller. Closer. Like the world narrowed to just this room. Just us.{/i}"
    
    # VISUAL: They sit together. Shoulders touching. Warmth spreading.
    l "(quiet) Thank you for staying."
    a "Of course. Where else would I go?"
    l "I don't know. Just... thank you."
    
    # VISUAL: Silence. Comfortable. Charged. Something building.
    "{i}Silence between us but it's not empty. It's full of everything we haven't said. Everything we've been too scared to say.{/i}"
    
    l "I keep thinking about the rooftop. After the confession. How we held each other."
    a "Me too."
    l "I felt... safe. For the first time since all of this started. Maybe the first time ever."
    a "Even while everything was falling apart?"
    l "Especially then. Because you were there. Because I wasn't breaking alone."
    
    # VISUAL: She turns toward him. Eye contact. Vulnerable. Open.
    l "I don't want to be alone tonight. Not in my head. Not with the nightmares. Not with... everything."
    a "You're not alone. You haven't been alone since we left."
    l "I know. But tonight I need... I need more than just proximity. I need..."
    
    # VISUAL: She trails off. Can't quite say it. Scared of rejection. Of vulnerability.
    "{i}She can't finish. Too scared. Too vulnerable. But I understand. I feel it too.{/i}"
    
    a "I need it too. Whatever it is. I need it too."
    
    # VISUAL: Relief washes over her. Permission granted. Mutual need acknowledged.
    l "(breathes) Okay. Good. I thought maybe I was imagining it."
    a "You're not imagining anything. I feel it. All of it."
    
    # VISUAL: Slow movement. Her hand reaches for his. Fingers intertwine. Electric.
    "{i}Her hand finds mine. Fingers slide between fingers. Warmth. Connection. Simple touch feeling like everything.{/i}"
    
    l "Your hands are shaking."
    a "So are yours."
    l "(small laugh) We're both terrified."
    a "Yeah. But not of each other."
    l "No. Not of each other. Of this. Of what it means. Of what happens if we let ourselves feel it."
    
    # VISUAL: He squeezes her hand gently. Grounding. Reassuring.
    a "Then we feel it. Together. Like everything else we've survived."
    l "Together. Yeah."
    
    # VISUAL: She shifts closer. Head resting on his shoulder. Breathing syncing.
    "{i}She leans into me. Head on my shoulder. Her breath warm against my neck. My arm moves around her. Automatic. Natural. Right.{/i}"
    
    l "(whispers) This isn't performance. Right? This isn't just... survival instinct. Proximity. Desperation."
    a "No. This is real. As real as anything I've felt."
    l "How do you know?"
    a "Because Glass never felt this. Glass never felt anything. This is different. This is human."
    
    # VISUAL: She looks up at him. Faces close. Breath mingling. Moment suspended.
    l "I see you, Aeron. Not Glass. Not the weapon. Not the killer. Just... you. The person underneath everything."
    a "And I see you. Not the perfect soldier. Not Echelon's proof. Just Lyra. Broken and beautiful and real."
    
    # VISUAL: Moment stretches. Everything slows. Choice approaching.
    a "{i}The space between us shrinks. Inches. Then less. Her eyes asking permission. Mine giving it.{/i}"
    
    # VISUAL: Kiss. Gentle at first. Testing. Then deeper. Need pouring through.
    a "{i}Lips meet. Soft. Tentative. Then certain. Her hand in my hair. Mine on her waist. Everything else falling away. Just this. Just us. Just now.{/i}"
    
    # VISUAL: They break apart. Breathing hard. Foreheads touching. Grounding.
    l "(breathless) That was..."
    a "(equally breathless) Yeah."
    l "Should we...?"
    a "Only if you want to. No pressure. No expectations. Just... what feels right."
    
    # VISUAL: She nods. Decision made. Mutual. Consensual. Wanted.
    l "I want to. I need to feel something other than fear and guilt and rage."
    l "I need to feel human. With you. Please."
    
    # VISUAL: He cups her face. Gentle. Reverent. Seeing her completely.
    a "Then let's feel human together."
    
    # VISUAL: Second kiss. Deeper. More urgent. Hands exploring. Not frantic. Purposeful.
    a "{i}We kiss again. Deeper now. Hands moving. Hers sliding under my shirt. Mine tracing her spine. Not desperate. Not rushed. Savoring. Learning. Discovering.{/i}"
    
    l "(between kisses) Bed. Should we...?"
    a "Yeah. More comfortable."
    
    # VISUAL: They move to makeshift bed. Concrete floor with blankets. Not much but theirs.
    # VISUAL: Lying down together. Side by side. Touching. Exploring. Slow build.
    
    "{i}The makeshift bed. Blankets on concrete. Not comfortable but doesn't matter. She's pressed against me. That's all that matters.{/i}"
    
    # VISUAL: Hands roaming. Shirts loosening. Skin touching skin. Intimate but tender.
    l "(whispers) I haven't done this in... I don't even remember. Before Echelon maybe."
    a "Me neither. Glass didn't have time for this. For connection. For feeling."
    l "Then we're both relearning. Together."
    a "Together. Always together."
    
    # VISUAL: Kisses trailing. Neck. Collarbone. Gentle exploration. Building slowly.
    "{i}Her lips on my neck. My hands tracing her sides. Learning curves. Finding what makes her gasp. What makes her sigh. Slow discovery.{/i}"
    
    l "(gasps) There. Right there."
    a "(continues) Like this?"
    l "(nods, breathless) Exactly like that."
    
    # VISUAL: Clothes loosening more. Not removed completely yet. Building tension.
    "{i}Shirts loosening. Her hands on my chest. Mine on her back. Skin warm. Breath hot. Hearts racing. Everything heightening.{/i}"
    
    l "Aeron."
    a "Yeah?"
    l "Don't stop. Whatever this is. Don't stop."
    a "I won't. I promise. I'm here. All of me. For all of you."
    
    # VISUAL: Intensity building. Breathing harder. Movements more urgent. Still tender.
    "{i}Building. Hands more urgent. Kisses deeper. Her leg wrapping over mine. Bodies pressing closer. Heat rising. Everything narrowing to just sensation. Just us. Just this moment.{/i}"
    
    l "(breathless) I need... I need more."
    a "Tell me. Tell me what you need."
    l "You. All of you. No walls. No Glass. No perfect soldier. Just us. Real and broken and here."
    a "Then you have me. All of me. Everything I am."
    
    # VISUAL: Final barriers falling. Emotional and physical. Completely present. Completely vulnerable.
    "{i}Shirts gone. Hands everywhere. Learning. Discovering. Giving. Taking. She gasps my name. I breathe hers. Everything else gone. Just this. Just us. Just now.{/i}"
    
    # VISUAL: Moment peaks. Everything aligned. Trust complete. Vulnerability total.
    l "(whispers against my lips) I trust you. Completely. With everything."
    a "And I trust you. Always. Forever."
    
    # =======================================================
    # FADE TO BLACK - User writes explicit portion manually if desired
    # =======================================================
    
    scene black with fade
    
    "{i}The world narrows. Sensation overwhelming. Her. Me. Us. Everything else falling away.{/i}"
    "{i}[This is where the scene continues in your own words, if you choose.]{/i}"
    
    # =======================================================
    # TIME SKIP - Morning After
    # =======================================================
    
    scene bg_safe_house_morning with fade
    
    "{i}Morning. Gray light through the window. Warm despite concrete floor. Because of her.{/i}"
    
    # VISUAL: Aftermath. Bodies tangled. Blankets askew. Peaceful. Safe.
    # VISUAL: Aeron wakes first. Lyra still sleeping against him. Vulnerable. Beautiful.
    
    "{i}She's still asleep. Pressed against me. Hair messy. Face peaceful. No nightmares last night. For either of us.{/i}"
    
    # VISUAL: Her hand over his heart. His arm around her. Natural. Right.
    a "{i}Her hand over my heart. Like she's checking it still beats. Making sure I'm still here. Still real. Still hers.{/i}"
    
    # VISUAL: She stirs. Wakes. Remembers. Small smile.
    l "(sleepy) Morning."
    a "Morning."
    l "Last night was..."
    a "Yeah."
    l "(small laugh) We're good at finishing each other's sentences now."
    a "Seems that way."
    
    # VISUAL: She doesn't pull away. Stays close. Comfortable. No regret visible.
    l "Do you regret it?"
    a "No. Do you?"
    l "No. I feel... lighter. Like I'm carrying less weight somehow."
    a "Me too. Like some of the ghosts got quieter."
    l "Not all of them. But some. That's progress."
    
    # VISUAL: They lie there. Comfortable silence. No rush to move.
    "{i}We stay tangled together. No rush. No urgency. Just presence. Just being. Just human.{/i}"
    
    l "What does this mean? For us?"
    a "I don't know. But I know it's real. And I know I want more of it."
    l "More of this? Or more of... us?"
    a "Both. All of it. Whatever you're willing to give."
    
    # VISUAL: She kisses him. Soft. Sweet. Morning intimacy different from night passion.
    l "Then you have it. All of it. I'm yours if you're mine."
    a "I'm yours. Completely."
    
    # VISUAL: Final moment of peace before reality intrudes.
    "{i}Morning light. Her in my arms. This moment perfect and temporary and precious. Everything else can wait. Just for now. Just for this moment.{/i}"
    
    l "(finally sits up) We should probably get moving. Things to do. Survival and all that."
    a "Probably. But I'm not in a hurry."
    l "(laughs) Neither am I. But Zira will show up eventually and I'd rather be dressed when she does."
    a "Fair point."
    
    # VISUAL: Getting dressed. Casual intimacy. No shame. No awkwardness.
    "{i}We dress. No rush. No shame. Casual touches. Small smiles. Everything different now. Better different.{/i}"
    
    # Update relationship status via helpers only
    $ mark_flag("Lyra", "lewd_scene_completed")
    $ unlock_romance("Lyra")
    $ rel("Lyra", trust=1, affection=2)
    
    l "Thank you. For last night. For this morning. For all of it."
    a "Thank you for trusting me. For seeing me. For being here."
    l "Always. We're in this together. Remember?"
    a "Always together. Yeah. I remember."
    
    # VISUAL: One more kiss. Then back to reality. Changed but stronger.
    "{i}One more kiss. Then reality returns. But we're different now. Connected deeper. Stronger together. Ready for whatever comes next.{/i}"
    
    # Check if all activities complete (helpers-only, via scene_flags)
    python:
        tasks = ["work","weapons","intel","medical","reputation","survival","past"]
        activities_done = all(check_scene_flag("act2_activity", f"{t}_done") for t in tasks)

    if activities_done:
        "{i}Seven days. Seven tasks. All complete. And now this. Time to see if Selene responds.{/i}"
        jump act2_06_the_message
    else:
        "{i}Still tasks to complete. But last night changed something. Made it all feel possible somehow.{/i}"
        jump act2_activity_hub

    # canon_note: Lyra intimate scene - deeply earned, emotionally vulnerable, physically close
    # canon_note: Requires trust 7+ and affection 5+ to unlock
    # canon_note: Player choice to engage or skip - respects agency
    # canon_note: Builds slowly - emotional connection before physical
    # canon_note: Fade-to-black structure - user can add explicit portion manually if desired
    # canon_note: Morning after shows depth - no regret, comfortable intimacy, relationship deepened
    # canon_note: Romance path activated - changes future interactions
    # canon_note: Trust +1, Affection +2 after scene
    # canon_note: Shows humanization - both learning to feel again after being weapons
    # canon_note: "Together. Always together." - reinforces core relationship theme
    # canon_note: Physical intimacy earned through emotional vulnerability built across Act 1 and Act 2
    # canon_note: No performance - genuine connection between broken people learning to be human

    return
