# act1_13_the_message.rpy


# ======================================================
# ACT 1 - Scene 13: The Message
# ======================================================


label act1_the_message:

    # VISUAL: Aeron's apartment after Lyra leaves; door closed, room dim.
    # LIGHTING: Blue-grey ambient; terminal glow from desk.
    # SOUND: Ventilation hum; distant city drone; rain starting outside.

    "{i}The door seals behind her. The room exhales.{/i}"
    a "{i}She came back. Twice now.{/i}"
    a "{i}Glass recognizes glass. Maybe that's all we need.{/i}"
    a "{i}Maybe breaking together is better than shattering alone.{/i}"

    # VISUAL: He moves to the desk; exhaustion visible in his movements.
    "{i}He moves to the desk. The weight of the night settles.{/i}"

    # NEW: Marcus's mission order arrives
    # VISUAL: Terminal screen flickers—high-priority notification pulse.
    # SOUND: Urgent chime; command-level alert.
    "{i}The terminal chimes. Urgent. Command priority.{/i}"
    "{i}Marcus's seal. Another mission.{/i}"

    # VISUAL: Aeron hesitates; hand hovers over the interface.
    a "{i}Of course. Glass doesn't get to rest.{/i}"
    a "{i}Operation 391.{/i}"

    # ACTION: Player choice—open it or ignore it.
    menu:
        "The notification blinks. Insistent. Command priority."
        "Open the message.":
            $ aeron_opened_order = True
            "{i}He taps the screen. Marcus's orders unfold.{/i}"
            
        "Hesitate.":
            $ aeron_opened_order = False
            "{i}His hand hovers. For a moment, he considers walking away.{/i}"
            a "{i}Glass hesitating. Again.{/i}"
            "{i}But the chime repeats. Command priority. Disobedience isn't an option.{/i}"
            "{i}He opens it.{/i}"
            $ aeron_opened_order = True
    # -------------------------------------------------------------------------

    # VISUAL: Mission order renders on screen—official formatting, Marcus's signature.
    # SOUND: Soft hum as text appears.
    
    "{i}OPERATION DIRECTIVE - PRIORITY ALPHA{/i}"
    "{i}CLASSIFICATION: SECTOR STABILIZATION{/i}"
    "{i}AUTHORIZATION: HIGH MARSHAL MARCUS RYLAN{/i}"

    # VISUAL: Aeron reads; his expression darkens with each line.
    a "{i}(reading) 'Sector 10 - Lower Spans. Comprehensive sweep operation.'{/i}"
    a "{i}'Intelligence indicates organized resistance activity. Rebel communication networks confirmed.'{/i}"
    a "{i}'Objective: Eliminate all hostile elements. Secure sector infrastructure. Zero tolerance protocol.'{/i}"

    # VISUAL: His finger stops scrolling.
    "{i}Zero tolerance. No survivors. Total sweep.{/i}"
    
    a "{i}'Deployment: 06:00 hours. Full tactical complement. Authorization to use lethal force on all targets.'{/i}"
    a "{i}'Estimated resistance: 200-500 individuals.'{/i}"
    a "{i}'Expected civilian collateral: Acceptable within mission parameters.'{/i}"

    # VISUAL: Close-up on his face; jaw tight; something breaking.
    a "{i}Acceptable collateral.{/i}"
    a "{i}200 to 500 people. Reduced to numbers. To metrics.{/i}"
    a "{i}Operation 391. The count continues.{/i}"

    # NEW: Glass realization
    a "{i}This is what Glass does. This is what I've become.{/i}"
    a "{i}390 operations of obeying. Of not asking. Of being useful.{/i}"
    a "{i}And now 391. Another sector. Another sweep. Another—{/i}"

    # VISUAL: Second notification—different tone, unmarked sender.
    # SOUND: Different chime; lower, urgent but not official.
    "{i}A second chime cuts through his thoughts. Different tone.{/i}"
    "{i}Unmarked sender. Encrypted.{/i}"

    # VISUAL: Aeron's eyes flick to the new notification; suspicion and curiosity.
    a "{i}Unmarked means encrypted. Encrypted means trouble.{/i}"
    a "{i}Or answers.{/i}"

    # ACTION: Player choice—open it or focus on Marcus's order.
    menu:
        "Two messages. One from Father. One from... unknown."
        "Open the unmarked message.":
            $ aeron_opened_zira_message = True
            "{i}He swipes Marcus's order aside. The encrypted message decrypts.{/i}"
            a "{i}What are you...?{/i}"
            
        "Ignore it and read Marcus's order again.":
            $ aeron_opened_zira_message = False
            "{i}He tries to focus on the mission parameters.{/i}"
            a "{i}Orders first. Distractions later.{/i}"
            # SOUND: The unmarked message chimes again. Insistent.
            "{i}But the chime repeats. Again. Again.{/i}"
            a "{i}Persistent bastard.{/i}"
            "{i}He opens it.{/i}"
            $ aeron_opened_zira_message = True
    # -------------------------------------------------------------------------

    # VISUAL: Text renders on screen—plain, no signature, deliberate spacing.
    # SOUND: Faint static crackle as text appears line by line.

    "{cps=30}SECTOR 10. LOWER SPANS.{/cps}"
    "{cps=30}NORTHEAST EDGE. GRID SIX-TWO.{/cps}"
    "{cps=30}TONIGHT. COME ALONE.{/cps}"
    "{cps=30}THEY'RE WATCHING YOU.{/cps}"
    "{cps=30}I CAN SHOW YOU WHY.{/cps}"
    "{cps=30}THE TRUTH IS IN THE SHADOWS.{/cps}"

    # VISUAL: Message deletes itself—lines dissolve from bottom to top.
    # SOUND: Digital distortion; screen flickers, then clears.
    "{i}The text dissolves. Gone before he can screenshot it.{/i}"

    a "{i}Self-deleting. Professional.{/i}"
    a "{i}Or paranoid.{/i}"

    # NEW: Connection to Marcus's order
    # VISUAL: He looks between the two screens—Marcus's official order, the ghost of Zira's message.
    "{i}His eyes move between the two messages.{/i}"
    
    a "{i}Sector 10. Same coordinates.{/i}"
    a "{i}Father orders me to sweep it at dawn.{/i}"
    a "{i}Someone else wants me there tonight.{/i}"
    a "{i}Before the sweep. Before the killing starts.{/i}"

    # NEW: Glass perspective
    a "{i}Glass obeys orders. Glass doesn't question.{/i}"
    a "{i}But Glass is cracking.{/i}"
    a "{i}And something about this... feels deliberate.{/i}"

    # VISUAL: He leans back; considers the empty screen.
    "{i}No trace. No evidence. No proof it ever existed except memory.{/i}"
    a "Who the hell are you?"
    a "{i}And why do you want me to see Sector 10 before I destroy it?{/i}"

    # VISUAL: Rain intensifies outside; droplets streak the window in the background.
    "{i}Rain taps the glass. The city hums below.{/i}"

    # ACTION: Player choice—investigate or stay.
    menu:
        "The coordinates burn in his memory. Sector 10. Tonight or tomorrow."
        "Go to the Lower Spans now.":
            $ aeron_goes_early = True
            a "{i}If someone's watching me, I'd rather meet them on my terms.{/i}"
            a "{i}Before dawn. Before the sweep. Before Glass follows orders again.{/i}"
            "{i}He grabs his coat. Marcus's mission order stays on screen, unanswered.{/i}"
            a "{i}Glass hesitates. Glass questions. Glass disobeys.{/i}"
            a "{i}Maybe the cracks are spreading faster than I thought.{/i}"
            
        "Wait and think it through.":
            $ aeron_goes_early = False
            a "{i}Rushing into traps is how people disappear.{/i}"
            "{i}He sits. Thinks. The rain fills the silence.{/i}"
            # NEW: Kael photo deliberation with Glass
            # VISUAL: He looks at Kael's photo on the desk.
            a "{i}What would you do, Kael? Walk into the dark or wait for dawn?{/i}"
            a "{i}'Don't let Father turn you into a weapon,' you said.{/i}"
            a "{i}But staying here, following orders... that's exactly what Glass does.{/i}"
            "{i}He grabs his coat.{/i}"
            a "{i}Maybe it's time to stop being Glass.{/i}"

    # VISUAL: Door opens; corridor light spills in; Aeron's silhouette in the frame.
    "{i}The hallway is empty. Cameras blink red in the corners.{/i}"
    a "{i}They're always watching. Question is—who else is?{/i}"

    # VISUAL: He steps into the corridor; door seals behind him.
    # SOUND: Pneumatic hiss; lock engaging; footsteps on marble.

    "{i}The elevator descends into the dark.{/i}"
    a "{i}Operation 391 starts at dawn. But tonight...{/i}"
    a "{i}Tonight, Glass decides to see what it's really cutting.{/i}"

    # TRANSITION: Fade to Lower Spans (act1_14_lower_spans begins).
    
    # canon_note: Marcus's order is for "the sweep" - Sector 10, 200-500 targets
    # canon_note: Zira's message uses EXACT same coordinates as Marcus's sweep
    # canon_note: Timing is critical - Zira wants him there BEFORE the sweep
    # canon_note: "Show you why" - implies Zira knows what the sweep is really about
    # canon_note: Glass hesitating/questioning/disobeying = cracks spreading
    # canon_note: First time Aeron deliberately defies orders (going early)
    # canon_note: "See what Glass is really cutting" - investigating his own mission
    # canon_note: Sets up moral crisis in sweep scene - he'll know what he's destroying

    return