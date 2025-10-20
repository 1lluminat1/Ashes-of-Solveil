# act2_activity_06_survival_skills.rpy


# =======================================================
# ACT 2 - Activity 6: Survival Skills (Zira Vulnerability)
# =======================================================


label activity_survival_skills:

    # VISUAL: Safe house. Evening. Day 5. Just Aeron and Zira.
    # LIGHTING: Dim overhead bulb. Shadows deep. Intimate space.
    # SOUND: City hum distant; their breathing; occasional siren far away.

    scene bg_safe_house with fade

    "{i}Day 5. Activity: Survival Skills.{/i}"
    "{i}Zira said I need to learn how to actually survive down here.{/i}"
    "{i}Not just hide. Survive. Blend in. Become invisible.{/i}"

    # VISUAL: Zira sitting cross-legged on floor. Spread of items before her.
    # Clothing, tools, maps, markers. Teaching materials.

    z "Alright, Glass. Time for your education in not being a walking Echelon advertisement."
    z "Sit down. Pay attention. This might keep you alive."

    # VISUAL: Aeron sits across from her. Tired but attentive. Five days of activities wearing on him.
    a "What am I learning today?"
    z "How to be nobody. How to move through the Unders without screaming 'I'm from Aeries, please murder me.'"
    z "Clothing, speech patterns, body language, cultural markers. Everything that separates us from them."

    # VISUAL: She pushes bundle of clothes toward him. Worn. Local. Unders style.
    z "First: you dress like you belong. No clean lines. No military posture in civilian clothes."
    z "Wear this. Look like you've lived here your whole life."

    # VISUAL: He examines clothes. Rough fabric. Stained but functional. Real.
    a "These are... used."
    z "Of course they're used. Nobody down here has new anything."
    z "New clothes mean you stole them or you're Echelon. Both get you killed."
    z "(pushes them) Change. Now. I need to see how you move in them."

    # VISUAL: He changes (off screen). Returns wearing Unders clothing. Feels wrong.
    # LIGHTING: He looks different. Rougher. More real. Less Glass.

    z "(circles him, examining) Better. You look human now instead of weapon-shaped."
    z "But you're still moving wrong. Too precise. Too controlled."
    z "Unders don't move like soldiers. We slouch. We shuffle. We conserve energy."

    # VISUAL: She demonstrates. Her posture shifts. Less confident. More tired. Real.
    z "See? I'm not Zira the rogue anymore. I'm just another worker going home."
    z "Invisible. Forgettable. That's how you survive."

    # VISUAL: Aeron tries to copy. Awkward at first. Too deliberate.
    a "(attempting slouch) Like this?"
    z "No, you look like you're injured. Relax. Let gravity win."
    z "You've been fighting gravity your whole life. Stop fighting. Just exist."

    # VISUAL: He tries again. Better. More natural. She nods approval.
    z "There. That's better. You look tired instead of dangerous."
    z "Tired is good. Tired is normal. Everyone down here is tired."

    # VISUAL: She sits again. Pulls out hand-drawn maps. Territory markers.
    z "Next: territories. The Unders aren't unified. They're fractured into districts, each controlled by different groups."
    z "You need to know who owns what. Where you're safe. Where you're dead."

    # VISUAL: She traces routes on map. Markers. Symbols. Complex web.
    z "Red marks: hostile territory. Stay out unless you want problems."
    z "Green marks: neutral zones. Markets, clinics, public spaces. Safe-ish."
    z "Blue marks: friendly contacts. People I know. Use my name carefully."

    a "How do I know which territory I'm in?"
    z "Graffiti. Tags. Colors. Each group marks their space."
    z "(points to map) See this? Three vertical lines. That's the Rust Collective. Hard people, but fair."
    z "This one? Circle with a dot. The Underlows. Avoid them. They hate Echelon more than most."

    # VISUAL: Aeron studies map. Memorizing. Taking it seriously.
    a "Why are you teaching me this? You could've just given me the map."
    z "Because maps don't teach survival. Experience does."
    z "And I don't have time to save your ass every time you wander into wrong territory."
    z "(slight pause) Also... I need you to survive. For what's coming."

    # VISUAL: Something in her tone. Heavier. More personal. He notices.
    a "What's coming?"
    z "War. Eventually. If we're lucky."
    z "If we're not lucky? Echelon crushes what's left of resistance and we all die anyway."
    z "Either way, I need you ready. Can't have you dying because you didn't know a gang sign."

    # VISUAL: She pulls out small notebook. Worn. Personal. Hesitates before opening.
    z "There's one more thing you need to learn. Language."
    z "Not just words. Hand signals. Code phrases. Ways to communicate without speaking."

    # VISUAL: She demonstrates hand signals. Quick. Precise. Military-esque but different.
    z "This means 'danger.' This means 'move.' This means 'Echelon nearby.'"
    z "These kept resistance alive before the Purge. Some still use them."

    # VISUAL: Aeron copies signals. Muscle memory activating. Learns quickly.
    a "These are... old military signals. Modified."
    z "Smart boy. Yeah, they're adapted from old resistance codes."
    z "My brother taught me these. Before..."
    "{i}She stops. Cuts off. Didn't mean to mention that.{/i}"

    # VISUAL: Aeron notices. Carefully approaches the opening she left.
    a "Brother?"
    z "(tense) Forget I said that."
    a "Zira—"
    z "Drop it, Glass. We're here to teach you survival, not excavate my past."

    # VISUAL: Silence. Heavy. She's guarded now. Walls up. But something's cracking.
    "{i}She's hiding something. Something painful. Something that explains her.{/i}"

    menu:
        "The moment hangs between them. Push or let it go?"
        
        "Press gently—'You mentioned him before. When you saved us. Who was he?'":
            $ zira_trust += 2
            $ zira_loyalty += 1
            $ aeron_empathy += 1
            
            a "(gentle) You mentioned him before. When you saved us that first night. Who was he?"
            z "(jaw tight) I said drop it."
            a "And I'm saying you don't have to carry it alone."
            a "You've saved my life twice. Taught me how to survive. Given me everything."
            a "Let me know who I'm surviving for. Why you're doing this."
            
            # VISUAL: She stares at him. Measuring. Debating. Then something breaks.
            z "(long exhale) ...Kai. His name was Kai."
            
        "Let it go—'Alright. Show me the next signal.'":
            $ zira_trust += 0
            $ zira_loyalty += 0
            
            a "Alright. Show me the next signal."
            
            # VISUAL: She looks at him. Brief surprise. Then nods. Appreciates the space.
            z "Smart. Don't push. I respect that."
            z "(demonstrates signal) This one means—"
            
            # VISUAL: She stops mid-gesture. Looks at notebook. At hand signals.
            # Something in her cracks anyway. Can't keep it in.
            
            z "(quiet) His name was Kai. My brother."
            z "He taught me these signals. Before Echelon killed him."

    # VISUAL: The room temperature drops. Truth laid bare. Painful and raw.
    # SOUND: City hum fades. Just her breathing. Just this moment.

    "{i}Kai. Her brother. Dead.{/i}"
    "{i}Everything she's done suddenly makes sense.{/i}"

    a "(quiet) What happened?"
    z "(stares at notebook) He tried to defect. Like you. Four years ago."
    z "He was Echelon too. Mid-level operative. Nothing special. Just another weapon."
    z "But he had a conscience. Started questioning orders. Seeing what they really were."

    # VISUAL: She traces hand signals in notebook. Memorizing. Remembering.
    z "He came to me. Said he couldn't do it anymore. Needed help getting out."
    z "I was already underground by then. Rogue. Surviving on my own."
    z "I told him I'd help him. Get him out. Find him a new life in the Unders."

    # VISUAL: Her jaw clenches. Painful memory surfacing. She forces it out.
    z "We planned it for weeks. Every detail. Every contingency. I thought we had it perfect."
    z "(bitter laugh) We didn't account for Marcus Rylan."

    # VISUAL: Aeron goes still. Father's name like ice water. Always his father.
    a "Marcus... knew?"
    z "Marcus knows everything. That's his gift. Omniscient bastard."
    z "Kai made it three blocks from Echelon HQ before they caught him."
    z "Not patrol. Not guards. Marcus himself. Waiting."

    # VISUAL: She closes notebook. Hands shaking slightly. Controlled fury.
    z "Marcus gave him a choice. Return to service, or face execution for treason."
    z "Kai chose execution. Said he'd rather die free than live as Glass."
    z "(voice breaking slightly) Marcus shot him personally. Made example of him."
    z "Broadcasted it. 'This is what happens to traitors. This is Echelon's mercy.'"

    # VISUAL: Aeron's stomach drops. Father's cruelty familiar but still devastating.
    a "{i}Father killed her brother. Made it public. Made it terror.{/i}"
    a "{i}Four years ago. I was eighteen. Still Glass. Still obedient.{/i}"
    a "{i}Did I see that broadcast? Did I watch her brother die and feel nothing?{/i}"

    a "I'm sorry. I'm so sorry, Zira."
    z "Don't apologize for your father. You didn't pull the trigger."
    z "(looks at him) But you're him. Same escape attempt. Same conscience emerging."
    z "That's why I'm helping you. You're Kai's second chance."

    # VISUAL: Truth settles. Her motivation crystal clear. Redemption proxy.
    a "I'm not your brother."
    z "I know you're not. But you're close enough."
    z "When I saw you crack—when Glass started breaking—I saw Kai again."
    z "Same look in your eyes. Same realization that the system is rot."
    z "And I thought... maybe this time it works. Maybe this time he gets out."

    # VISUAL: She stands. Paces. Energy needing release. Emotion too strong.
    z "I told myself I wouldn't care. That you were just another asset. Another tool."
    z "But I do care. And that's fucking terrifying."
    z "Because if you die... it's like watching Kai die again."

    # VISUAL: Aeron stands. Approaches carefully. She's coiled tight. Vulnerable and dangerous.
    a "I'm not going to die."
    z "(bitter laugh) That's what Kai said. Right before Marcus put a bullet in his head."
    a "I'm not Kai. And I'm not going to let Marcus win again."
    z "You don't know that. Nobody knows that."
    z "Echelon always wins. That's what they do. They crush hope and call it order."

    # VISUAL: He moves closer. Not touching. Just present. Grounding.
    a "Then we change the pattern. We make Echelon lose."
    a "For Kai. For everyone Marcus killed. For everyone we can still save."
    z "(looks at him, eyes wet but fierce) You really believe that? That we can win?"
    a "I have to. Because if I don't believe it, what's the point of any of this?"

    # VISUAL: She stares at him. Measuring. Then something shifts. Decision made.
    z "(reaches into jacket pocket) I have something for you."
    z "Something I've been carrying for four years. Something Kai wanted me to have."

    # VISUAL: She pulls out device. Small. Technical. Advanced. Hacking tool.
    # LIGHTING: Faint blue glow. Precious. Irreplaceable.

    z "Hacking device. Military-grade. One of a kind. Kai built it himself."
    z "Can bypass Echelon security protocols. Slice through encrypted systems."
    z "He was carrying it when they killed him. I recovered it after... after the execution."

    # VISUAL: She holds it out. Offering. Painful to give away but necessary.
    z "I want you to have it. Use it to do what Kai couldn't."
    z "Burn Echelon from the inside. Make Marcus pay."

    # VISUAL: Aeron takes it carefully. Reverent. Understanding the weight.
    a "Zira, I can't take this. It's—"
    z "It's a tool. And tools are meant to be used, not worshipped."
    z "Kai would want someone to finish his work. Might as well be you."
    z "(firm) Take it. Honor him by destroying the thing that killed him."

    # VISUAL: He closes hand around device. Acceptance and responsibility.
    a "I will. I promise."
    z "Don't promise. Just do it."
    z "(slight pause) And Glass? Don't die. I can't watch that twice."

    # VISUAL: Their eyes meet. Understanding. She's not just helping him. She's saving herself.
    a "I won't die. I'm too stubborn."
    z "(small smile) Good. Stubbornness might be what saves you."
    z "Kai was stubborn too. Just not stubborn enough."

    # VISUAL: She turns away. Wipes eyes quickly. Composing herself. Walls returning.
    z "(back to business) Alright. Enough feelings. Back to survival."
    z "You know the territories. You know the signals. You know why I'm invested."
    z "Now you need to practice. Tomorrow you're going out alone."

    a "Alone?"
    z "Can't hold your hand forever. You need to learn to move through the Unders independently."
    z "I'll track you. Make sure you don't die. But you're on your own."
    z "(slight grin) Try not to get murdered on your first solo trip."

    # VISUAL: Despite everything, he almost laughs. Her humor cutting through weight.
    a "I'll do my best."
    z "Your best better be good enough."

    # VISUAL: She gathers teaching materials. Packs them away. Preparing to leave.
    z "Get some rest. Tomorrow's going to be interesting."
    z "(at door, looks back) And Glass? Thanks. For listening. For... caring."
    z "Most people don't bother asking about the dead. Easier to ignore ghosts."

    a "Kai isn't a ghost. Not while we remember him."
    z "(soft smile) No. I suppose he isn't."
    z "Goodnight, Aeron. Sleep if you can."

    # VISUAL: She leaves. Door closes. He's alone with Kai's device and new understanding.
    "{i}Zira the rogue. Zira the survivor. Zira the sister.{/i}"
    "{i}She's not helping me out of belief or ideology.{/i}"
    "{i}She's helping me because I'm her second chance. Her do-over. Her hope.{/i}"

    # VISUAL: He examines hacking device. Blue glow. Kai's legacy.
    a "{i}Four years ago, Marcus killed her brother for trying to escape.{/i}"
    a "{i}Now I'm trying to escape. And she's making sure I succeed.{/i}"
    a "{i}Kai's second chance. That's a lot of weight to carry.{/i}"
    a "{i}But if it means Zira gets her closure... I'll carry it.{/i}"

    # VISUAL: He stores device carefully. Precious. Irreplaceable. Mission.
    a "{i}For Kai. For Zira. For everyone Marcus destroyed.{/i}"
    a "{i}We're going to burn Echelon down. And Marcus with it.{/i}"
    a "{i}That's not a promise. That's a guarantee.{/i}"

    # TRANSITION: End of activity. Rewards gained. Zira loyalty deepened.

    # REWARDS SUMMARY SCREEN:
    "{b}Activity Complete: Survival Skills{/b}"
    "
    Rewards:
    - Skill Unlocked: 'Unders Disguise' (Reduced detection in Lower Spans)
    - Item Gained: Kai's Hacking Device (Bypass Echelon security)
    - Knowledge Gained: Territory maps, hand signals, cultural markers
    - Relationship Deepened: Zira (Trust +2, Loyalty +1)
    
    Zira's Past Revealed:
    - Her brother Kai tried to defect 4 years ago
    - Marcus Rylan personally executed him
    - Zira helping Aeron = second chance for Kai
    - Kai's hacking device now yours—use it to finish his work
    
    You can now navigate the Unders independently.
    Zira will track you but won't intervene unless necessary.
    Tomorrow: Solo navigation test.
    "

    $ activities_completed += 1
    $ days_remaining -= 1
    $ hacking_device = True
    $ inventory.append("kais_hacking_device")
    $ contacts["zira"]["trust"] = 8
    $ contacts["zira"]["loyalty"] = 10
    $ skill_unders_disguise = True
    $ activity_skills_done = True
    $ zira_backstory_revealed = True
    $ aeron_knows_about_kai = True

    # canon_note: Zira's brother Kai revealed - defector killed by Marcus 4 years ago
    # canon_note: Marcus personally executed Kai, broadcasted it as terror example
    # canon_note: Zira helping Aeron = proxy redemption for Kai's death
    # canon_note: "You're Kai's second chance" - her core motivation exposed
    # canon_note: Kai's hacking device given to Aeron - precious legacy item
    # canon_note: Device bypasses Echelon security - crucial for Act 3 infiltration
    # canon_note: Zira's loyalty now 10/10 - she will die for Aeron if needed (Act 3 Scene 18)
    # canon_note: Hand signals taught - resistance communication system
    # canon_note: Territory maps learned - navigate Unders safely
    # canon_note: "Don't die. I can't watch that twice." - emotional core of relationship
    # canon_note: Aeron was 18 when Kai died - may have seen broadcast, didn't process it
    # canon_note: Zira cried but controlled it - vulnerability shown rarely
    # canon_note: Tomorrow = solo navigation (next scene option)
    # canon_note: This scene cements Zira as family, not just ally

    jump act2_activity_hub