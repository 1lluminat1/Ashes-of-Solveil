init -1 python:
    def _has_any_saves():
        try:
            return bool(renpy.list_saved_games())
        except Exception:
            return False

init python:
    # Width of your left artwork strip in pixels.
    # (Measure it or tweak until it looks right.)
    LEFT_STRIP_W = int(config.screen_width * 0.22)  # e.g. ~22% of 1920 = 422px

    # Center of the remaining area (screen minus left strip).
    # This becomes the x-align for the title block.
    TITLE_ALIGN_X = 0.5 + (LEFT_STRIP_W / float(config.screen_width)) * 0.5
    # algebra note: = (LEFT_STRIP_W + (config.screen_width - LEFT_STRIP_W)/2) / screen_width
    PANEL_W = 560
    PANEL_PAD_X = 48
    PANEL_PAD_Y = 72


# === Custom SAY screen (name top-left; uses your fonts/character colors) ===
transform solveil_say_alpha:
    alpha 0.95

screen say(who, what):
    $ pal = ui_current()
    $ _yoff = 52 if who else 0

    window:
        id "window"
        xalign 0.5
        yalign 0.85
        xmaximum 1700
        yminimum 320
        padding (pal["padding"], pal["padding"])
        background Solid(pal["box_bg"])
        at solveil_say_alpha

        if who:
            text who id "who":
                xpos 0
                ypos 0
                # Name face/size/color come from your Character + gui.name_*.

        text what id "what":
            xpos 0
            ypos _yoff
            # Dialogue/VO styling comes from your say styles (and *thought*_text).

        # Minimal continue indicator (no image dependency)
        text "›":
            xalign 0.98
            yalign 0.95
            size 24
            color pal["highlight"]


# ==========================================
# Solveil — Main Menu (right-aligned, sleek)
# Keeps stock screens.rpy intact.
# ==========================================

# ---- styles (local to this file)
style mm_button is default:
    background None
    hover_background Solid("#FFFFFF1A")   # your translucent hover look
    padding (12, 10)
    hover_sound "audio/ui/hover.mp3"      # <-- plays once when a button gains focus
style mm_button_text is default

init -1 python:
    # Safe palette fallbacks if your gui vars aren't defined yet
    gui_act_bg       = getattr(gui, "act1_bg", "#0A0E14")
    gui_act_text     = getattr(gui, "act1_text", "#C0C5CE")
    gui_act_accent   = getattr(gui, "act1_accent", "#3D4C5F")
    gui_act_highlight= getattr(gui, "act1_highlight", "#5A7A99")
    interface_font   = getattr(gui, "interface_font", "fonts/Exo2-Regular.ttf")
    name_font        = getattr(gui, "name_font", "fonts/Exo2-Medium.ttf")

# Transparent button with subtle hover highlight
init -1:
    style mm_button:
        xsize 420
        yminimum 64
        padding (18, 18)
        left_padding 28
        right_padding 28
        background None
        hover_background Solid(gui_act_accent + "44")      # ~26% tint on hover
        insensitive_background None
        xalign 1.0  # right align inside the column
        yalign 0.5
        focus_mask True

    style mm_button_text:
        font interface_font
        size 26
        color gui_act_text
        hover_color "#EDF1F5"
        outlines [(1, "#00000066", 0, 0)]  # subtle legibility pop
        xalign 0.0
        text_align 0.0
        kerning 0.3

# Optional: slight slide-in for the menu column (kept subtle)
transform mm_slide_in:
    on show:
        alpha 0.0 xoffset 24
        linear 0.25 alpha 1.0 xoffset 0

# Optional: right-side gradient veil to help text contrast over busy BGs
transform right_veil:
    alpha 0.0
    linear 0.25 alpha 1.0


screen main_menu():

    tag menu

    if renpy.loadable("images/ui/main_menu_bg.png"):
        add "images/ui/main_menu_bg.png" fit "cover"
    else:
        add Solid(gui_act_bg)

    add Solid("#00000066")

    # --- Right panel (background + contents)
    frame:
        background Solid("#0F1419CC")
        xalign 1.0
        yalign 0.5
        xsize PANEL_W
        yfill True
        padding (PANEL_PAD_X, PANEL_PAD_Y)
        at right_veil

        vbox:
            spacing 36
            xfill True

            # Title group (centered *inside* the panel)
            vbox:
                xalign 0.5
                spacing 6
                text "ASHES OF SOLVEIL":
                    font name_font
                    size 48
                    color "#EDF1F5"
                    outlines [(2, "#000000AA", 0, 0)]
                    xalign 0.5
                text "A choice-driven narrative":
                    font interface_font
                    size 18
                    color gui_act_highlight
                    xalign 0.5

            null height 40

            # Menu (keep your mm_* styles)
            vbox:
                spacing 12
                style_prefix "mm"
                xalign 0.5     # use 0.0 if you prefer left-aligned buttons
                at (mm_slide_in if not preferences.reduced_motion else None)

                textbutton _("New Game"):
                    action Start()
                    activate_sound "audio/ui/start_click.mp3"   # only this button uses this click sound
                textbutton _("Continue") action Continue() sensitive _has_any_saves()
                textbutton _("Load Game") action ShowMenu("load")
                textbutton _("Settings")  action ShowMenu("preferences")
                if renpy.has_screen("extras"):
                    textbutton _("Extras") action ShowMenu("extras")
                textbutton _("Quit") action Quit(confirm=True)

    # Version (bottom-right)
    text "{size=14}v[gui.version]{/size}":
        xalign 0.985
        yalign 0.98
        color "#8FA6B8"
        outlines [(1, "#00000099", 0, 0)]