# ===================================================
# ACT 1 - Scene 0: Tutorial
# File: act1_00_tutorial.rpy
# ===================================================


label tutorial:
    # VISUAL: It is highly recommended to display this warning over a simple black screen
    # or a stark, silent environment to emphasize its importance.
    scene black
    
    $ renpy.call_screen("tutorial_screen", text="{b}DISCLAIMER AND CONTENT WARNING\n\nThis game is a work of fiction.\nAny resemblance to real persons, living or dead, or real-world events, is purely coincidental.\nAll characters depicted in this story are over the age of 18.\nPlease note: This narrative explores mature themes and contains graphic depictions of suicidal ideation, mental health crises, and trauma.\n\n{u}Player discretion is strongly advised.{/u}{/b}", cps=42)

    return