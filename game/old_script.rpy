# Okay well Im gonna send you my entire script right now, you tell me:
# # act1.rpy

# label act1:
#     # *** SCENE 0 - PROLOGUE ***
#     # Panoramic view of a scorched earth. Collapsed cities, twisted metal, fires still burning.
#     n "{i}Long ago, the world fractured under the weight of its own ambition.{/i}"
#     n "{i}Cities fell. Nations crumbled. From the ashes rose a single bastion of order: Solveil.{/i}"
#     # Panoramic view of the upper levels of Solveil
#     n "{i}A city-state built skyward on the skeletons of the old world.{/i}"
#     n "{i}At the top: the Aeries—seat of power, privilege, and control. Where the elites rule from spires that pierce the clouds and scrape the heavens.{/i}"
#     # Panoramic view of the middle levels of Solveil
#     n "{i}Below: the Middle Levels. Crucible of labor and law. Backbone of industry. A working class indebted to a system built against them.{/i}"
#     # Panoramic view of the unders
#     n "{i}And beneath it all: the Unders. Forgotten. Forsaken. Swallowed by smog and shadow.{/i}"
#     n "{i}For centuries, the regime known as Echelon has maintained the illusion of peace—order upheld by relics channeled through devices called Aether Bands.{/i}"
#     n "{i}Gifts, some believe. Curses, others say. Only those who submit are chosen. Only those who obey... survive.{/i}"
#     n "{i}But not all bloodlines were lost to time. Not all truths remain buried.{/i}"

#     # *** SCENE 1 - AERON'S BEDROOM ***
#     # VISUAL: Dimly lit bedroom with cool blue tones. Rain streaks down the window. Aeron sits at the edge of his bed, city lights flickering in the distance.
#     a "{i}Rain taps the glass like it's trying to remind me the world is still out there.{/i}"
#     a "{i}I know, just not sure I'm part of it.{/i}"
#     # Close up of Aeron's face reflected in the window, fractured by rain droplets.
#     # SYMBOLIC: fragmented reflection = fractured identity, rejection
#     a "{i}They say a band makes you someone...{/i}"
#     a "{i}...so what does that make me?{/i}"
#     # Aeron stands up, walks to the wall.
#     # There's a locked display case — empty. A label beneath the glass reads "For the Chosen."
#     a "{i}Funny. An empty frame feels heavier than the damn band ever would have.{/i}"
#     # Cut to a dusty photo on his nightstand: Aeron and an older boy — his brother — smiling.
#     # The brother's arm covers the band on his wrist.
#     # CAMERA: hold a few seconds on the photo to linger on faded warmth
#     a "{i}My brother smiled like he belonged.{/i}"
#     a "{i}But even smiles fade when the lights cut out.{/i}"
#     # Aeron opens his wardrobe. Pauses. Pulls out a formal black uniform and lays it on the bed.
#     a "{i}Wear the right clothes. Say the right words. Maybe they'll forget I was ever rejected.{/i}"
#     # He sits back down and looks at the skyline once more.
#     a "{i}Or maybe they never will.{/i}"
#     # Fade out as the screen lingers on Aeron's back, the skyline shining brilliantly before him — alone in a room built for someone else's future.

#     # *** SCENE 2 - HALLWAY TO THE GALA ***
#     # Aeron walks alone down a long, opulent hallway. Polished marble, golden inlays. Echelon banners hang from high ceilings.
#     a "{i}The hallway stretches like a runway, every polished tile a reminder of who I'm supposed to be.{/i}"
#     # Elite couples and uniformed officials line the walls in small clusters. They glance up as he passes. Eyes follow, lips murmur. But no one speaks aloud.
#     # CAMERA: slow dolly as Aeron walks, with elite faces briefly catching light then fading back into shadow
#     a "{i}Their eyes scrape like razors. Every glance a silent accusation... or pity.{/i}"
#     # Camera pans low behind Aeron’s feet. His polished shoes echo through the silent corridor.
#     n "{i}His footsteps carry down the long hall, swallowed by the hum of distant music.{/i}"
#     a "{i}They know who I am. They just wish I wasn't.{/i}"
#     # Camera pans to Aerons enclosed fist and empty, bandless wrist.
#     a "{i}No band, no worth. That's all they see.{/i}"
#     # A butler steps aside to let him pass. Gives a stiff nod. Eyes averted.
#     a "{i}Even the staff—obedient in public, disgusted in private.{/i}"
#     # Portraits of past leaders line the walls
#     n "{i}Portraits line the walls: generations of Aeries elites immortalized in paint and gold.{/i}"
#     # Camera settles on a portrait of Marcus, Aeron's father.
#     # VISUAL: Dramatic lighting casts Aeron’s shadow across the portrait — half eclipsed
#     a "{i}My father, the great General Rylan—carved like a saint.{/i}"
#     a "{i}And me? A mistake walking past their perfect world.{/i}"
#     # Doors at the end of the hallway glow faintly from the gala light. Two guards stand motionless on each side of the entrance.
#     n "{i}At the end of the corridor, twin doors glow with warm light.{/i}"
#     # Aeron stops before the towering doors. Two guards posted on either side don't meet his gaze.
#     a "{i}I could turn around. Slip into the shadows.{/i}"
#     a "{i}Would anyone stop me? Would anyone care?{/i}"
#     # He takes a breath, steels himself.
#     a "{i}No. Not tonight.{/i}"
#     # Doors creak open slowly, golden light spilling into the hallway.
#     # Fade into the Gala scene...

#     # *** SCENE 3 - THE GALA ***
#     define e1 = Character("Elite 1", color="#000000")
#     define e2 = Character("Elite 2", color="#000000")
#     define e3 = Character("Elite 3", color="#000000")
#     define ye1 = Character("Young Elite 1", color="#000000")
#     define ye2 = Character("Young Elite 2", color="#000000")
#     define ye3 = Character("Young Elite 3", color="#000000")
#     # Lavish lighting glows gold on marble floors. Strings play softly beneath the hum of champagne flutes and elite murmurs.
#     # Aeron, hands in pocket, steps out from the gala doors.
#     n "{i}The ballroom pulses with artificial warmth—golden chandeliers, velvet drapery, and the sickly-sweet scent of programmed luxury.{/i}"
#     a "{i}All this gold, all this glass—just to hide the rot underneath.{/i}"
#     # A server greets him at the door and offers him a glass of wine
#     a "{i}Nothing but fake smiles and fake wine.{/i}"
#     # A drone glides overhead, projecting live footage of the event to a screen. Aeron catches his own face on the display.
#     a "{i}Even here, no escape from surveilance.{/i}"
#     a "{i}Can't even hate it anymore, just tired of being a caged animal on display.{/i}"
#     # Camera catches a group of elites, whispering and looking at Aeron
#     # MURMUR FX: low, unintelligible whispers layered under soft music
#     e1 "...That's General Rylan's boy. Unbranded—what a waste."
#     e2 "Just another reject. Should have been thrown in the Unders like the rest."
#     e3 "Another disgrace to the Rylan name."
#     # Aeron steps forward
#     a "Funny, I didn't realize ghosts made such lively conversation... Problem?"
#     with hpunch
#     e2 "Of course not, Aeron! Merely... surprised to see you here."
#     a "{i}Sick on stolen power. They flaunt those bands but they're nothing without them.{/i}"
#     a "Surprised to see me breathing, you mean?"
#     with hpunch
#     e1 "Of course not! You're Marcus Rylan's son — your presence honors Echelon."
#     a "Save it."
#     # Aeron brushes past them without looking back, glass still in hand
#     # Murmurs ripple as Marcus Rylan enters from the other side of the room, surrounded by high-ranking officials.
#     n "General Marcus Rylan steps into the light—tall, adorned in ceremonial armor, flanked by Enforcers and sycophants alike."
#     # Aeron watches his father, but they do not interact.
#     a "{i}The gravity shifts when he enters. No applause—just silence and fear dressed in admiration.{/i}"
#     a "{i}He doesn't even look at me.{/i}"
#     a "{i}He doesn't need to. His shadow does enough of the talking.{/i}"
#     # Aeron turns away, catches a glimpse of Lyra across the ballroom in conversation with a Councilwoman.
#     n "Lyra stands poised, her posture sharp, eyes cold. Even in this setting, she cuts through the noise."
#     a "{i}They dress her up like a trophy, parade her like proof that the system works...{/i}"
#     n "Her eyes flick toward Aeron—only for a second—but something unspoken passes between them."
#     a "{i}...but I see it. The steel beneath the silk.{/i}"
#     # A small group of younger elites (around Aerons age) whisper nearby
#     ye1 "I heard he wasn't even compatible."
#     ye2 "Yeah, some kind of defect. Or curse. Maybe both."
#     ye3 "Honestly, it's sad. Pretending like he still belongs."
#     ye2 "I feel bad for his father... two failures and no heir to his legacy."
#     a "{i}I used to flinch at their words. Now it's just background noise in a broken song.{/i}"
#     # Aeron's grip tightens on the glass. A faint crack. A droplet of blood.
#     a "{i}The stem creaks under pressure—fragile, like the image crafted for me.{/i}"
#     a "{i}They sip their wine and laugh like the world hasn’t already ended.{/i}"
#     a "{i}And I’m just supposed to smile back—pretend I didn’t see the cracks first.{/i}"
#     n "{i}He walks away, the crack in the glass echoing louder than any whisper.{/i}"
#     # Aeron sets down the glass of wine and makes his way to the balcony...

#     # *** SCENE 4 - THE BALCONY ***
#     # Aeron steps outside; neon-lit Solveil skyline stretches beyond the railing.
#     # Aeron lights a cigarette; inhales, exhales a plume of smoke.
#     a "{i}They look down at the Unders like they're another species, but we're all human.{/i}"
#     a "{i}Makes me sick...{/i}"
#     # Sound of heels approaching
#     # Lyra appears in the doorway, formal uniform partially unbuttoned, cigarette in mouth.
#     # Lyra steps forward and joins Aeron at the railing.
#     l "Got a light for an old colleague?"
#     a "(wryly) Didn't think Echelon's golden girl smoked."
#     l "(smirks) If you know a better way to deal with all this, I'm all ears."
#     # Lyra leans in as Aeron lights her cigarette, eyes never leaving his.
#     # Lyra inhales, then exhales a cloud of smoke; the smoke changing colors against the neon-lit backdrop.
#     n "{i}They sit in silence for a moment, gazing out at the congested skyline.{/i}"
#     # Lyra faces Aeron, still leaning on the railing with one arm.
#     l "Didn't peg you for the melancholic rooftop type."
#     a "Didn't peg you for the rooftop type either."
#     a "Figured you'd be in there charming every politician with two brain cells."
#     l "(laughs softly) Please. I'd rather jump off this balcony."
#     a "(cracks a slight smile) Careful—someone might call that sedition. They'd be lost without you."
#     l "Let them. I've lived this life since I could crawl. Doesn't mean I'm blind."
#     # Aeron turns to face Lyra, his tone more serious now.
#     a "So what do you see, then?"
#     l "(studies him) I see a room full of people drunk on power they don't understand..."
#     l "...who'll do anything for a regime that thrives on brutality and suppression..."
#     l "...and one person standing out here..."
#     l "...pretending he doesn't want to burn it all down."
#     a "{i}She says it like it's obvious. Like she sees right through me.{/i}"
#     # Pause. Aeron watches her closely as he exhales another cloud of smoke.
#     a "You think you know me?"
#     l "I hear what they say about you. I know the truth is far from the rumors."
#     a "I'm used to it. They've been whispering since I was twelve."
#     l "Let them whisper. They're scared of what they don't understand—scared of you."
#     a "They're scared of my father."
#     a "I'm just a rumor. Forgotten. Useless heir to the Rylan line."
#     a "{i}Even the name Rylan feels foreign now. Heavy. Hollow.{/i}"
#     # (beat)
#     a "Why are you really out here?"
#     l "Because in a room full of luxury, you're the only one not pretending."
#     n "{i}They smoke in silence for a beat.{/i}"
#     a "How long are you back from assignment?"
#     l "Not long. You know how it is—high value, high surveillance."
#     l "They only let me breathe when they want something."
#     a "And what do they want from you tonight?"
#     l "To parade me. To remind everyone I belong to them."
#     a "They think everything belongs to them..."
#     a "...that anything the sun touches is in their grasp..."
#     a "...but in the darkness the truth shows..."
#     a "...a society built on lies. Built on stolen power."
#     a "You don't belong to anyone."
#     n "{i}For a moment, she doesn't speak. His words echo louder than the city below.{/i}"
#     # Lyra turns slightly toward him, visibly moved but trying to hide it.
#     l "(softly) Always so serious."
#     l "And here I thought I was the dramatic one."
#     a "{i}But she doesn't pull away.{/i}"
#     n "{i}The air between them feels heavier now. Something has shifted.{/i}"
#     a "{i}For once, the silence doesn't feel empty.{/i}"
#     # Camera pans back, two faint sparks of light in the dark—their cigarettes.
#     # Fade to black.

#     # *** SCENE 5: AERON'S BEDROOM – AFTER THE GALA ***
#     n "{i}Later that night...{/i}"
#     # VISUAL: Aeron's room bathed in shadows. City lights flicker through the tall window.
#     a "{i}She didn’t even say goodbye.{/i}"
#     a "{i}Just vanished... like smoke from a dying flame.{/i}"
#     a "{i}But I saw it—in her eyes tonight...{/i}"
#     a "{i}Not duty. Not protocol. Something real.{/i}"
#     a "{i}Maybe I’m not the only one tired of pretending.{/i}"
#     # Aeron sits at his desk. An envelope bearing the sigil of Echelon rests beside a flickering terminal.
#     n "{i}On the desk: a sealed mission order. Echelon’s crest stamped in crimson wax.{/i}"
#     a "{i}Another dance. Another performance in their twisted theater.{/i}"
#     # Aeron looks down at his wrist—bare, unmarked.
#     a "{i}Smile for the mask I never asked to wear.{/i}"
#     # He opens the envelope. Pulls out a thin sheet. Reads silently.
#     a "{i}\"Rebel activity detected in Sector Ten. Suspects traced to northeastern Unders.\"{/i}"
#     a "{i}\"Investigate and prove your worth, son.\" –Marcus.{/i}"
#     a "{i}Same commands. Same cycle.{/i}"
#     a "{i}Day after day, mission after mission... and nothing changes.{/i}"
#     # Aeron walks to the window, gazing down at the Unders glowing far below.
#     a "{i}The definition of insanity... repeating the same thing, expecting something different.{/i}"
#     a "{i}Am I insane?{/i}"
#     a "{i}Will anything ever change?{/i}"
#     a "{i}I live like a ghost—clinging to the hope that it’ll all be worth it someday.{/i}"
#     a "{i}But there’s no end in sight.{/i}"
#     a "{i}It used to be better...{/i}"
#     a "{i}Before I became... whatever this is.{/i}"

#     # *** SCENE 5.1 -FLASHBACK: AERON & LYRA, AGE 11 – THE HILL OUTSIDE THE CITY ***
#     # VISUAL: Gentle golden hour glow over a grassy hill. 
#     # Wind brushes through wildflowers. Aeron (age 11) and Lyra (age 11) sit overlooking the sprawl of Solveil from a distance. 
#     # They wear academy uniforms, slightly scuffed from sneaking out.
#     n "{i}Years ago... before the branding, before the silence, before the weight of names and legacies...{/i}"
#     n "{i}...there was this hill. Just outside the security perimeter, far enough for trouble, close enough to still matter.{/i}"
#     a "{i}We weren't supposed to be there. But rules never meant much to Lyra.{/i}"
#     # Young Lyra tosses a rock down the slope. Young Aeron mimics her.
#     l "If you could fly anywhere—right now, no tech, no band—just wings... where would you go?"
#     a "Anywhere but here."
#     l "Lame answer. Try again."
#     a "...Somewhere with real trees. Not these synthetic plastic ones."
#     l "(grins) So you're a nature boy, huh?"
#     a "Better than being stuck in a glass tower pretending everything's perfect."
#     l "Then we’ll run away someday. You and me."
#     a "You serious?"
#     l "(nods) Dead serious."
#     a "{i}Back then, it felt real. Like we could just... run. Leave the city behind. No father. No duty. Just two stupid kids chasing wind.{/i}"
#     # Lyra stands and offers her hand to Aeron.
#     l "Promise me—if the world ever turns to shit, we'll still find a place like this. Just ours."
#     a "(softly) I promise."
#     # Their hands clasp—two children grasping something bigger than they understand.
#     n "{i}For a moment, the city didn’t exist. Just us, and the sound of the wind.{/i}"
#     n "{i}I should’ve held on tighter to that moment.{/i}"
#     # Fade to white, leading into next flashback.
#     a "{i}But then, on that day... it all turned to shit...{/i}"

#     # *** SCENE 5.2 AERONS BRANDING RITUAL FLASHBACK ***
#     define c1 = Character("Cleric 1", color="#000000")
#     define c2 = Character("Cleric 2", color="#000000")
#     define c3 = Character("Cleric 3", color="#000000")
#     define c4 = Character("Cleric 4", color="#000000")
#     # *** SCENE 5.5 – FLASHBACK: THE BRANDING CEREMONY ***
#     # VISUAL: A golden chamber deep within the Aeries. Ancient relic suspended midair. Aeron lies on a ceremonial table, robed in white. Marcus watches from the shadows.
#     # The chamber is circular, walls adorned with golden engravings of past Echelon champions.
#     # Incense smoke curls through shafts of white light filtering from the domed ceiling.
#     # Four clerics stand at cardinal positions. Each holds a staff embedded with a fragment of the original Relic.
#     # Aeron lies on a stone altar veined with glowing circuitry. His ceremonial gown shimmers with gold thread.
#     a "{i}This is it...{/i}"
#     a "{i}The day I've trained for since I could walk.{/i}"
#     a "{i}Finally, the Rylan legacy will pass to me.{/i}"
#     c1 "We gather under the Eye of Ascension. One of the blood. One of the line."
#     c2 "Let the relic judge his soul. Let the flame carve its path."
#     c3 "Let him bear the mark of the Risen."
#     c4 "May his vessel carry the burden of command."
#     c1 "Echelon blesses you, child of lineage."
#     # A cleric steps forward, presenting a radiant silver band on a silk pillow.
#     # The band is placed onto Aeron's wrist. Another cleric raises the relic staff.
#     # VISUAL: The relic pulses. Tendrils of lightning shoot out, striking the band.
#     n "{i}The relic hums — low at first, then rising like a scream swallowed by silence.{/i}"
#     n "{i}A tendril of light lashes from its core, striking the band. Sparks dance across Aeron's skin.{/i}"
#     a "{i}It burns—no, it *sears*. But I hold still. This is what I trained for.{/i}"
#     n "{i}Etchings burn across Aeron’s skin—symbols of power, crawling like fire beneath the flesh.{/i}"
#     # But then things turn.
#     n "{i}The light pulses again. Too bright. The air thickens. The stone beneath him trembles.{/i}"
#     a "AHHH—GOD—!!"
#     n "{i}Symbols race across his body like molten veins. His back arches. His voice breaks.{/i}"
#     # Aeron begins to scream.
#     a "AHHHH—AGHH—FUCK—!!"
#     # The marks spread rapidly, covering his entire body, before violently receding and vanishing.
#     # The band glows blinding white... then shatters into dust.
#     # Clerics recoil in stunned silence. The relic dims.
#     n "{i}One of the clerics drops their staff. The relic stutters — its light spasms, flickers, dies...{/i}"
#     n "{i}Then, silence. The band explodes in a white-hot burst, leaving only dust.{/i}"
#     c2 "(gasps) The band... rejected him..."
#     c3 "No, it's impossible..."
#     c4 "It’s never failed before—"
#     m "Enough."
#     # Marcus steps forward. Calm. Commanding.
#     m "Fate has chosen differently. The band did not fail... it responded."
#     m "My son has a greater purpose than any of you can comprehend."
#     m "The relic has spoken. Not in rejection—but in revelation."
#     m "My son is not forged like others. He is... chosen."
#     m "(quietly, to himself) The prophecy... it wasn't a myth after all."
#     # FADE TO: Aeron’s present-day silhouette against the window.
#     a "{i}That day... my fate was sealed.{/i}"
#     a "{i}My father called it destiny. Said the relic had spoken.{/i}"
#     a "{i}Maybe he was right. Or maybe he only saw what he wanted to see.{/i}"
#     a "{i}Because ever since that day... I stopped thinking for myself.{/i}"
#     a "{i}I lived to fulfill someone else's vision—his vision.{/i}"
#     a "{i}But maybe it's time I write my own path.{/i}"
#     a "{i}Forge something real... on my own terms.{/i}"
#     a "{i}And find out what fate really has in store for me.{/i}"

#     # *** SCENE 5.3 – BALCONY, AERON’S BREAKING POINT ***
#     # VISUAL: Aeron’s room, later that night. The city glows cold blue through the window. 
#     # A single photo of his brother sits on the desk. The envelope from Marcus still open. 
#     # Quiet. Just the low hum of the city outside.
#     # Aeron sits at the desk, staring at the photo.
#     a "{i}You always smiled like you belonged...{/i}"
#     a "{i}Even with the band burning your skin, you smiled.{/i}"
#     a "{i}And then one day you just… stopped smiling.{/i}"
#     # Camera moves closer on the photo — Aeron’s brother, arm over his shoulder, the band just visible.
#     a "{i}I used to hate you for leaving me here.{/i}"
#     a "{i}Now... I think I understand why you did it.{/i}"
#     # Aeron stands, takes the photo, sets it down gently.
#     a "{i}I don’t even know if I’m angry anymore. Just tired.{/i}"
#     a "{i}Tired of pretending this all means something.{/i}"
#     # He walks to the balcony door. Opens it. Wind drifts in, cold and metallic.
#     n "{i}He steps outside. The city sprawls below, endless and uncaring.{/i}"
#     # Aeron lights a cigarette. Hands shake. Smoke drifts upward.
#     a "{i}One more smoke... my last smoke.{/i}"
#     # He exhales, stares at the edge of the railing.
#     a "{i}Maybe if I step over, it’ll finally be quiet.{/i}"
#     a "{i}No more missions. No more ghosts whispering my name.{/i}"
#     a "{i}No more failure.{/i}"
#     # Camera pans low — his foot on the railing, hands gripping cold metal.
#     n "{i}The wind tugs at his coat. Below, the city roars like a living thing.{/i}"
#     # --- PLAYER CHOICE ---
#     menu:
#         "Step forward":
#             a "{i}Just one more step...{/i}"
#         "Step back":
#             a "{i}I can't keep living like this...{/i}"
#     # Regardless of choice, knock interrupts.
#     # A sharp double knock at the door. Startling. Cigarette trembles between his fingers.
#     n "{i}A knock at the door. Sharp. Sudden. Like fate itself rapping against the walls.{/i}"
#     a "{i}...Lyra?{/i}"  # (optional mutter under his breath)
#     # Aeron steps back down from the railing, still shaken.
#     n "{i}For a moment, the city noise fades. The only sound is his heart, hammering in his chest.{/i}"
#     # Fade to black or transition to Lyra’s entrance scene.

#     # *** SCENE 5.4 – LYRA’S VISIT ***
#     # After the balcony scene where Aeron almost stepped off:
#     # Knock at the door. Cigarette trembles in his fingers.
#     #play sound "knock.ogg"
#     n "{i}A knock at the door. Sharp. Sudden. Like fate itself rapping against the walls.{/i}"
#     a "{i}...Lyra?{/i}"
#     # He steps off the railing, still shaken. Opens the door.
#     l "You look like hell."
#     a "(forces a half-smile) You should see the other guy."
#     l "(arches a brow) Not funny."
#     # Lyra steps in without waiting for permission, eyes scanning the room.
#     # The photo of Aeron’s brother sits on the desk, the envelope open.
#     n "{i}Her gaze lingers on the photo, then on his empty wrist. She doesn’t comment.{/i}"
#     l "I thought you’d be asleep. Or at least pretending."
#     a "Sleep’s a luxury these days."
#     # Lyra sits on the edge of his desk, cigarette still between her fingers.
#     l "I needed to get out of that gala. All those smiles felt like knives."
#     # Aeron lights her cigarette for her again. Their fingers brush.
#     a "(quietly) Thanks for knocking."
#     l "(studies him) You’re shaking."
#     a "Cold air. Nothing more."
#     # Small pause — tension.
#     l "You don’t have to keep doing this, you know."
#     a "Doing what?"
#     l "Carrying everything alone. Pretending you’re made of stone."
#     a "{i}Her words land heavier than she knows.{/i}"
#     a "(looks away) Stones don’t crack. People do."
#     l "(softly) You’re not your father, Aeron."
#     n "{i}For a long moment they say nothing. The city hums beyond the window, neon bleeding across the room.{/i}"
#     # Choice — Let her in or not:
#     menu:
#         "Let Lyra stay":
#             a "(after a beat) Sit, then."
#             l "(sits on the edge of his bed) Better."
#             a "I’m not sure what’s better about it."
#             l "You’re still here. That’s better."
#             n "{i}She says it like a fact. Not a question.{/i}"
#         "Tell her to leave":
#             a "It’s late. You shouldn’t be here."
#             l "(hurt, but hides it) Right. Forget I knocked."
#             n "{i}She turns for the door but hesitates, eyes lingering on him one last time.{/i}"
#             l "You’re still here. That’s something."
#             n "{i}The door clicks shut behind her. Silence fills the room again.{/i}"
#     # Regardless of choice, Aeron ends alone again, shaken but alive.

#     # *** SCENE 6 – THE UNDERS (LATE NIGHT WALK) ***
#     n "{i}Later that night...{/i}"
#     # VISUAL: Aeron in a hooded coat, descending into the Unders via an old elevator or stairwell. 
#     # Flickering neon signs, dripping pipes, the smell of ozone and oil.
#     a "{i}I couldn’t sleep. Not after tonight.{/i}"
#     a "{i}The air down here tastes different—like metal and rainwater, like something still alive.{/i}"
#     # He passes a market stall — vendors selling scrap tech, food cooked over open flames.
#     n "{i}The Unders pulse with a different kind of life. No marble, no velvet. Just rust, steam, and survival.{/i}"
#     a "{i}They call this place forgotten, but I think it’s the only part of Solveil still awake.{/i}"
#     # Children dart past, laughing, barefoot. A man sharpens a blade under a flickering sign. 
#     # An Enforcer drone buzzes overhead but doesn’t stop.
#     a "{i}Even down here, their eyes are everywhere. But the people don’t bow. They keep moving.{/i}"
#     # Aeron stops by a rail overlooking a lower level. Smoke rises in lazy curls.
#     a "{i}No spires. No chandeliers. Just humanity, raw and unpolished.{/i}"
#     # A woman approaches — worn clothes, eyes tired but kind.
#     woman "Looking for a good time, stranger? Warm bed, no questions asked."
#     menu:
#         "Accept her offer":
#             a "{i}Her voice is soft. Tired. Everything I thought I wanted...{/i}"
#             a "{i}But even as I nod, I already feel cold inside.{/i}"
#             # Fade out – do not show the act.
#             n "{i}Later, Aeron sits on the edge of a narrow cot, shirt half-buttoned, cigarette trembling between his fingers.{/i}"
#             a "{i}Connection isn’t something you can buy.{/i}"
#             a "{i}I don’t even remember her name.{/i}"
#         "Refuse politely":
#             a "(shakes his head) Not tonight."
#             woman "(shrugs) Your loss."
#             a "{i}Her footsteps fade back into the crowd. I feel lonelier than before.{/i}"
#     # Aeron keeps walking, the Unders stretching ahead.
#     a "{i}This place feels like a mirror. Everyone down here is running from something.{/i}"
#     a "{i}Me too.{/i}"
#     # He stops at a flickering sign, looking up at the rusted beams above.
#     a "{i}Maybe the Unders aren’t forgotten. Maybe they’re just waiting—for someone to remember them.{/i}"
#     # Fade out, setting up next plot beat.
#     return
