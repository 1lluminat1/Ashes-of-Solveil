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

    # ---------------------------------------------------------------
    # SOLVEIL CALENDAR
    # ---------------------------------------------------------------
    # Six months of 60 days each (360-day year):
    #   Ember → Rain → Kiln → Cipher → Silence → Forge
    #
    # The game begins on the 3rd of Forge, 390 AC and runs through
    # late Forge. Act 5's finale crosses into Year 391 AC — the
    # first of Ember. The number 391 echoes Operation 391, the
    # Sector 10 sweep that started Aeron's fracture.
    #
    # "DAY X" in scene calls maps to (X + 2)th of Forge, 390 AC.
    # DAY 58 = 60th of Forge (last day of 390 AC).
    # DAY 59+ = 1st of Ember, 391 AC (the new year).
    # ---------------------------------------------------------------

    SOLVEIL_MONTHS = ["Ember", "Rain", "Kiln", "Cipher", "Silence", "Forge"]
    SOLVEIL_DAYS_PER_MONTH = 60
    SOLVEIL_GAME_START_MONTH = 5  # Forge (0-indexed)
    SOLVEIL_GAME_START_DAY = 3    # 3rd of Forge
    SOLVEIL_GAME_START_YEAR = 390

    def _ordinal(n):
        """Return ordinal suffix for a number: 1st, 2nd, 3rd, 4th..."""
        if 11 <= (n % 100) <= 13:
            return str(n) + "th"
        return str(n) + {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

    def _solveil_date(game_day):
        """Convert a relative game day (DAY 1 = first day of Act 1) to
        a Solveil calendar date string.

        Returns: '5th of Forge, 390 AC' or '1st of Ember, 391 AC'
        """
        if not game_day or game_day < 1:
            return ""
        # Calendar day within the starting month
        cal_day = SOLVEIL_GAME_START_DAY + game_day - 1
        month_idx = SOLVEIL_GAME_START_MONTH
        year = SOLVEIL_GAME_START_YEAR

        # Overflow into subsequent months/years
        while cal_day > SOLVEIL_DAYS_PER_MONTH:
            cal_day -= SOLVEIL_DAYS_PER_MONTH
            month_idx += 1
            if month_idx >= len(SOLVEIL_MONTHS):
                month_idx = 0
                year += 1

        month_name = SOLVEIL_MONTHS[month_idx]
        return _ordinal(cal_day) + " of " + month_name + ", " + str(year) + " AC"

    def _parse_day_number(date_str):
        """Extract the day number from 'DAY X' format. Returns 0 if not matched."""
        import re
        m = re.match(r"DAY\s+(\d+)", str(date_str))
        return int(m.group(1)) if m else 0

    # ---------------------------------------------------------------
    # HELPERS
    # ---------------------------------------------------------------

    def show_timeline(date="", time="", location=""):
        """Show the standard timeline card and wait for it to finish.

        Call at the top of a scene label (after scene_mark entered):
            $ show_timeline("DAY 3", "04:17", "Phoenix Secondary Base")

        The 'DAY X' format is auto-converted to the Solveil calendar:
            DAY 3 → '5th of Forge, 390 AC'

        You can also pass a pre-formatted string or an integer day number.
        """
        # Auto-convert DAY X to Solveil calendar
        if isinstance(date, int):
            date = _solveil_date(date)
        elif isinstance(date, str) and date.upper().startswith("DAY "):
            day_num = _parse_day_number(date)
            if day_num > 0:
                date = _solveil_date(day_num)

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
