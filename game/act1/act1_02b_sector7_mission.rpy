# act1_02b_sector7_mission.rpy


# ===================================================
# ACT 1 - Scene 2B: Sector 7 Mission
# ===================================================


define unit2 = Character("Unit-2", color="#4A90E2")
define unit3 = Character("Unit-3", color="#4A90E2")

label act1_sector7_mission:

    # FADE IN: Mid Levels, Sector 7 — pre-dawn. Sterile floodlights. Air tastes like metal.
    # VISUAL: Industrial corridor; cold white lighting; steam vents hissing.
    # SOUND: Low mechanical drone; distant city hum; boot steps on metal grating.
    # LIGHTING: Harsh white overhead; deep shadows in corners; clinical atmosphere.
    
    #scene bg_sector7_corridor with fade
    #play sound "sfx/comm_ping.ogg"
    
    a "{i}Orders arrive as light: white, clean, forgiving.{/i}"
    a "{i}Order is mercy.{/i}"  # Doctrine of Worth (mantra 1)
    
    # HUD overlay — mission card "Stabilization Sweep / S7-Δ"
    # Low mechanical drone under everything.
    #play sound "sfx/industrial_drone_loop.ogg"
    
    # COMMS — Marcus (diegetic)
    m "Containment only. Keep it surgical. The Directorate remembers numbers, not noise."
    
    a "{i}Obedience is survival.{/i}"  # mantra 2
    a "{i}389 operations. This is 390.{/i}"
    a "{i}Seven years earning the right to exist.{/i}"
    
    # Staged door breach
    # VISUAL: Heavy door; red security light; breach charge placement.
    # SOUND: Electronic beep; charge arming; team breathing through comms.
    #play sound "sfx/breach_charge.ogg"
    
    a "{i}Door seals behind us. Footfalls count distance. Four signatures. No hostiles flagged.{/i}"
    a "{i}Precision is grace.{/i}"  # mantra 3
    
    # VISUAL: Family inside — two adults shielding a small form; an older teen at a rusted panel.
    # LIGHTING: Emergency light strips; shadows long; faces half-visible.
    # CAMERA: Low angle; Aeron's POV; rifle sight framing.
    a "{i}White steals their colors first. The room learns to hold its breath.{/i}"
    
    # TEAM (off-screen, filtered) — use however you handle squad VO
    # SOUND: Radio static; filtered voices; mechanical breathing.
    unit3 "{i}Clear path.{/i}"
    unit2 "{i}Panel's hot. Unregistered transmitter.{/i}"
    unit3 "{i}Orders?{/i}"
    
    # Aeron's silent signal; suppressed fire
    # VISUAL: Hand signal; team moves; muzzle flashes (suppressed).
    # SOUND: Suppressed bursts — pff-pff-pff; brass hitting floor; bodies falling.
    #stop sound
    #play sound "sfx/suppressed_bursts.ogg"
    
    a "{i}The manual says flinching spreads panic.{/i}"
    
    # SILENCE. Fans hum. Fluorescent buzz returns.
    # VISUAL: Smoke hanging in air; bodies on floor; family photo frame shattered.
    # SOUND: Ventilation system; fluorescent hum; settling debris.
    a "{i}Doubt is rot.{/i}"  # mantra 4
    
    # PROCEDURE / METRICS
    # VISUAL: HUD overlay; vitals flatline; mission timer; efficiency rating.
    # CAMERA: Close on Aeron's visor reflection; emotionless.
    a "{i}Vitals checked. Zero resistance. Logs compiled. Efficiency rating: {b}99.7%{/b}.{/i}"
    #play sound "sfx/hud_confirm.ogg"
    
    # COMMS — Marcus praise
    m "Flawless work, Aeron. Sector Seven will hold its line tonight."
    m "This is what resolve looks like."
    
    a "{i}Worth is proven through service.{/i}"  # mantra 5
    a "{i}He calls it resolve. The corridor calls it quiet.{/i}"
    
    # Micro gesture — glove inspection
    # VISUAL: Close-up; Aeron's hands; removes right glove slowly.
    # LIGHTING: Glove catches light; latex shines.
    a "{i}I peel the glove. No blood. Cleaner than the room deserves. The latex gleams under the light.{/i}"
    
    # MANTRAS - ALL PERFECT, NO GLITCHES:
    # VISUAL: Aeron stands; posture perfect; breathing steady.
    # These mantras flow smoothly - automated, internalized, no hesitation.
    a "{i}Order is mercy.{/i}"
    a "{i}Obedience is survival.{/i}"
    a "{i}Precision is grace.{/i}"
    a "{i}Doubt is rot.{/i}"
    a "{i}Worth is proven through service.{/i}"
    
    # NEW: Small seed of doubt AFTER mantras (not during)
    # VISUAL: Brief pause; something crosses his face, then disappears.
    a "{i}...Mercy.{/i}"
    a "{i}Who taught me that word?{/i}"
    
    # NEW: But suppresses it immediately
    # VISUAL: Jaw tightens; shoulders straighten; mask back in place.
    a "{i}Doesn't matter. The mission's logged.{/i}"
    a "{i}390 operations. The count continues.{/i}"
    
    # Propaganda screens wake in the hall
    # VISUAL: Wall screens flicker to life; white letters on black.
    # LIGHTING: Screen glow illuminates corridor; sterile white light.
    a "{i}Anthems bloom across the wall: STABILITY IS SALVATION. White letters pretending to be light.{/i}"
    
    # Team exfil (off-screen)
    # SOUND: Boot steps; equipment rattling; door mechanisms.
    unit2 "{i}Route green.{/i}"
    unit3 "{i}Uploading bodycam. Metrics clean.{/i}"
    
    # Absence, not remorse
    # VISUAL: Aeron stands still; team moving past him; alone in the corridor.
    a "{i}No pulse of guilt. No sickness. Just breath and static. The city hums the same.{/i}"
    
    # NEW: Mission count emphasis
    a "{i}389 operations before this. This is 390.{/i}"
    a "{i}The number used to mean something. Now it's just... counting.{/i}"
    
    # Walk-out; lights flicker
    # VISUAL: Team exits; Aeron last; looks back at room once.
    # SOUND: Lights flickering; electrical buzz; door sealing.
    #play sound "sfx/lights_flicker.ogg"
    
    a "{i}File the victory. Walk the corridor. Leave the room as clean as the report.{/i}"
    
    # Glass motif
    # VISUAL: Reflection in visor; distorted, empty.
    a "{i}My visor gives me someone else's eyes back.{/i}"
    a "{i}Feel nothing. Ask nothing. Do what you're told.{/i}"

    # NEW: Very subtle doubt (not a break)
    a "{i}Order is mercy.{/i}"
    a "{i}(…){/i}"
    a "{i}...Is this what mercy looks like?{/i}"

    # NEW: Player empathy seed
    menu:
        "It flickers at the edge of thought — a face, a feeling, unwelcome."
        "Bury it.":
            $ adjust_empathy(-1)
            a "{i}Weakness spreads like infection. I cut it out.{/i}"
            a "{i}The mission's logged. Sector's secure. That's all that matters.{/i}"

        "Let it stay.":
            $ adjust_empathy(1)
            a "{i}The child's face stays with me. Just the eyes. That’s all it takes.{/i}"
            a "{i}The report will be clean. But I won’t be.{/i}"
    
    # NEW: But he doesn't dwell - pushes it away
    a "{i}The mission's complete. The sector's secure.{/i}"
    a "{i}That's all that matters.{/i}"
    
    # HOLO-CALL → Marcus
    # VISUAL: Fade to black; hologram shimmer effect.
    # SOUND: Incoming call tone; connection establishing.
    #stop sound
    #play sound "sfx/holocall_incoming.ogg"
    #scene black with fade
    
    a "{i}Incoming request: High Marshal Rylan.{/i}"
    a "{i}Private channel. He never uses private channels.{/i}"
    
    # TRANSITION: Brief Marcus conversation
    # VISUAL: Marcus hologram; military uniform; backdrop of command center.
    # LIGHTING: Blue hologram glow; cold, authoritative.
    
    m "Exemplary work, Aeron. Your metrics were flawless."
    m "99.7% efficiency. Seven years of training produces this."
    m "You are becoming precisely what I intended."
    
    # NEW: Glass reference from Marcus
    m "Glass completes missions. Glass doesn't question."
    m "That's what makes you valuable."
    
    a "{i}That’s what they call me.{/i}"
    a "{i}Sharp. Obedient. Disposable. Transparent.{/i}"

    
    # NEW: Very subtle internal question
    a "{i}...Is this what you intended, Father?{/i}"
    a "{i}Or just what you'll accept?{/i}"
    
    m "Tomorrow night, you'll attend the Sector 7 Gala."
    m "Directive presence. Show them what Echelon excellence looks like."
    m "Rest now. You've earned it."
    
    a "{i}Earned it.{/i}"
    a "{i}Order is mercy.{/i}"
    a "{i}...{/i}"
    a "{i}The words feel automatic. Like breathing.{/i}"
    
    # NEW: But he doesn't dwell
    a "{i}Tomorrow, the gala. Tonight, the report.{/i}"
    a "{i}There’s no rest. Just reports. Then orders. Then more silence.{/i}"
    
    # TRANSITION
    # VISUAL: Fade to black; hold for beat.
    # TEXT OVERLAY: "Morning. The day of the gala."
    #scene black with fade
    centered "{i}Morning. The day of the gala.{/i}"
    
    # canon_note: First appearance of "Glass" identity and mantras
    # canon_note: Mantras work PERFECTLY here - no glitches, no stuttering
    # canon_note: Only small doubt AFTER mantras ("Who taught me that word?")
    # canon_note: Mantras don't actually start breaking until later scenes
    # canon_note: 99.7% efficiency rating is important — Marcus references it later
    # canon_note: This is operation 390 of 389 completed — track this number
    # canon_note: Aeron does NOT break here — just tiniest seed of doubt
    # canon_note: Glove/Glass motif parallels — both shine, both empty
    # canon_note: Family photo in background (shattered) — callback opportunity for later
    # canon_note: Scene should feel clinical, empty, automatic - like he's done this 389 times before
    
    # Jump to morning routine
    return