# ================================================================
# TIMELINE TITLE CARD — date / time / location at scene transitions
# File: game/ui/timeline_card.rpy
# ----------------------------------------------------------------
# Shows a typed-out overlay at the start of scenes where time has
# passed since the previous scene. Fits the Solveil institutional
# aesthetic: monospaced date/time, thin-weight location, cold
# palette with path-tinted overlay.
#
# Usage in scene files:
#     $ show_timeline("DAY 3", "04:17", "Phoenix Secondary Base")
#
# The card types out with {cps=20}, holds for ~1.8s, then fades.
# Total screen time ~2.8s. Skippable via click.
#
# Echelon interlude variant:
#     $ show_timeline_echelon("E_INT_203", "Aeries Command Spire")
#
# Act title cards use centered text and are handled separately in
# each act's opening scene — not through this system.
# ================================================================


# ----------------------------------------------------------------
# TRANSFORMS
# ----------------------------------------------------------------

transform _timeline_fadein:
    alpha 0.0
    linear 0.3 alpha 1.0

transform _timeline_fadeout:
    linear 0.5 alpha 0.0


# ----------------------------------------------------------------
# MAIN TIMELINE SCREEN
# ----------------------------------------------------------------

screen scene_timeline(date="", time="", location=""):
    # Full-screen overlay. Click-to-dismiss is handled by the
    # helper function's renpy.pause(), not by screen actions.
    modal False
    zorder 200
    layer "master"

    # Background: act palette dark + path tint
    add Solid("#0A0E14")
    add Solid(ui_overlay_color())

    # Content: centered, vertically mid-screen
    vbox:
        xalign 0.5
        yalign 0.48
        spacing 12

        # DATE  ·  TIME (monospaced, letterspaced, muted)
        if date and time:
            text ("{cps=20}" + date + "  \u00b7  " + time + "{/cps}"):
                font gui.system_font
                size 20
                color "#8FA6B8"
                kerning 2.0
                text_align 0.5
                xalign 0.5
        elif date:
            text ("{cps=20}" + date + "{/cps}"):
                font gui.system_font
                size 20
                color "#8FA6B8"
                kerning 2.0
                text_align 0.5
                xalign 0.5

        # LOCATION (thin weight, slightly larger, lighter color)
        if location:
            text ("{cps=20}" + location + "{/cps}"):
                font gui.thin_font
                size 26
                color "#C0C5CE"
                text_align 0.5
                xalign 0.5

    # Fade animation is handled by the helper function's pause timing.
    # Screen shows immediately; helper hides after 2.8s.


# ----------------------------------------------------------------
# ECHELON INTERLUDE VARIANT
# ----------------------------------------------------------------

screen scene_timeline_echelon(designation="", location=""):
    modal False
    zorder 200
    layer "master"

    add Solid("#0A0E14")
    # Red tint for Echelon
    add Solid("#FF436508")

    vbox:
        xalign 0.5
        yalign 0.48
        spacing 12

        # ECHELON // INTERNAL header
        text "{cps=20}ECHELON  //  INTERNAL{/cps}":
            font gui.system_font
            size 18
            color "#FF4365"
            kerning 3.0
            text_align 0.5
            xalign 0.5

        # Designation (e.g., E_INT_203)
        if designation:
            text ("{cps=20}" + designation + "{/cps}"):
                font gui.system_font
                size 20
                color "#8FA6B8"
                kerning 2.0
                text_align 0.5
                xalign 0.5

        # Location
        if location:
            text ("{cps=20}" + location + "{/cps}"):
                font gui.thin_font
                size 24
                color "#C0C5CE"
                text_align 0.5
                xalign 0.5

    # Fade animation is handled by the helper function's pause timing.
    # Screen shows immediately; helper hides after 2.8s.


# ----------------------------------------------------------------
# HELPER FUNCTIONS
# ----------------------------------------------------------------

init python:

    def show_timeline(date="", time="", location=""):
        """Show the standard timeline card and wait for it to finish.

        Call at the top of a scene label (after scene_mark entered):
            $ show_timeline("DAY 3", "04:17", "Phoenix Secondary Base")

        The card types out, holds, then fades. Total ~2.8s. The
        player can click to skip. After this call returns, the scene
        continues normally.
        """
        renpy.show_screen("scene_timeline", date=date, time=time, location=location)
        renpy.pause(2.8, hard=False)  # click-to-skip
        renpy.hide_screen("scene_timeline")

    def show_timeline_echelon(designation="", location=""):
        """Show the Echelon interlude variant of the timeline card.

        Call at the top of Echelon interlude scenes:
            $ show_timeline_echelon("E_INT_203", "Aeries Command Spire")
        """
        renpy.show_screen("scene_timeline_echelon", designation=designation, location=location)
        renpy.pause(2.8, hard=False)
        renpy.hide_screen("scene_timeline_echelon")
