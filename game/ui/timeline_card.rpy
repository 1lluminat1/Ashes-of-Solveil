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
    # The game spans 383-391 AC (8 years). Each act takes place in
    # a different year with time skips between them:
    #
    #   Act 1: Late Forge, 383 AC  (Aeron age 23 — Echelon service)
    #   Act 2: Early Ember, 385 AC (age 25 — post-defection)
    #   Act 3: Mid Cipher, 388 AC  (age 28 — rebellion deepens)
    #   Act 4: Mid Forge, 390 AC   (age 30 — shared authority / violence)
    #   Act 5: Late Forge → Ember, 390-391 AC (age 31 — the fall)
    #
    # Within each act, "DAY X" is relative to that act's start.
    # The helper auto-detects the current act from _current_scene_id.
    #
    # 391 AC = Year of Echelon's fall = Aeron's 391st mission number.
    # Zira reveals the parallel in Act 5's prep scene.
    # ---------------------------------------------------------------

    SOLVEIL_MONTHS = ["Ember", "Rain", "Kiln", "Cipher", "Silence", "Forge"]
    SOLVEIL_DAYS_PER_MONTH = 60

    # Per-act calendar origin: (start_month_index, start_day, year)
    # "DAY 1" in each act maps to start_day of the specified month/year.
    ACT_CALENDAR = {
        1: (5, 42, 383),   # Act 1: 42nd of Forge, 383 AC
        2: (0, 8, 385),    # Act 2: 8th of Ember, 385 AC
        3: (3, 15, 388),   # Act 3: 15th of Cipher, 388 AC
        4: (5, 25, 390),   # Act 4: 25th of Forge, 390 AC
        5: (5, 52, 390),   # Act 5: 52nd of Forge, 390 AC → overflows to 391 Ember
    }

    def _ordinal(n):
        """Return ordinal suffix for a number: 1st, 2nd, 3rd, 4th..."""
        if 11 <= (n % 100) <= 13:
            return str(n) + "th"
        return str(n) + {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

    def _get_current_act():
        """Detect the current act number from _current_scene_id."""
        sid = str(getattr(renpy.store, '_current_scene_id', ''))
        if sid.startswith('a1_'): return 1
        if sid.startswith('a2_'): return 2
        if sid.startswith('a3_'): return 3
        if sid.startswith('a4_'): return 4
        if sid.startswith('a5_'): return 5
        return 1  # fallback

    def _solveil_date(game_day):
        """Convert a relative game day (DAY X within the current act) to
        a Solveil calendar date string.

        Uses _current_scene_id to determine which act we're in,
        then offsets from that act's calendar origin.

        Returns: '44th of Forge, 383 AC' etc.
        """
        if not game_day or game_day < 1:
            return ""

        act = _get_current_act()
        month_idx, start_day, year = ACT_CALENDAR.get(act, ACT_CALENDAR[1])

        cal_day = start_day + game_day - 1

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
