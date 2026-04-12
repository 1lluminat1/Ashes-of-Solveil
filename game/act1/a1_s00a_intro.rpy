# ===================================================
# ACT 1 - Scene 1: Intro
# File: act1_00a_intro.rpy
# ===================================================


label a1_s00a_intro:

    # Seed the Codex silently on first mention.
    # Clicking any of the inline {a=codex:...} links below opens the
    # full entry; hovering highlights the term with a soft glow.
    $ codex_mention("solveil_tiers", source="a1_s00a_intro")
    $ codex_mention("bands",         source="a1_s00a_intro")

    # VISUAL: Cold white top-light over a pristine skyline above the clouds (Aeries).
    # The view should feel sterile, geometric, and silent—false perfection.

    "The world ended in ash, and someone built upward to forget it."
    "{a=codex:solveil_tiers}Solveil{/a}—order stacked into the sky."

    # VISUAL: Transition downward through the tiers—Aeries → Middle Levels.
    # AERIES should feel suffocating perfection: symmetry, glass, no wind.

    "At the peak: the {a=codex:solveil_tiers}Aeries{/a}. Glass without dust. Silence without peace."

    # VISUAL: Middle Levels—dense, industrial, humming with surveillance and motion.

    "Below that: the Middle Levels churn—industry, schedule, and the hum of being watched."
    "A restless machine, paying for the view above."

    # VISUAL: Unders—neon haze, dripping water, faint human sounds; light returns from within.
    # Should contrast sharply with the silence of the upper tiers.

    "And beneath it all: The **{a=codex:solveil_tiers}Unders{/a}**. The forgotten heart."
    "Here, light survives by learning to breathe."

    # VISUAL: Composite wide shot of the entire city—Aeries to Unders, unified vertical frame.
    # The palette should shift from white → steel → blue → amber.

    "Echelon keeps the peace with pageantry and power—relics tamed into {a=codex:bands}Aether Bands{/a}."
    "Some call them gifts. Others, shackles. Obedience makes the difference."

    # VISUAL: Fade to black; single ember glows. 
    # Color shift from cold white to faint orange—symbol of hidden humanity.

    "Not everything stayed buried..."

    # canon_note: Keep narration under ~140 words. 
    # Aeries = top-down white light (control); Unders = internal warm light (humanity).
    # Save explicit Verdant/Ethereal bloodline reveal for later scenes.
    
    return
