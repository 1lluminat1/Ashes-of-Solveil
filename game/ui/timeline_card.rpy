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

screen scene_timeline(date="", time="", location="", year=""):
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
        spacing 14

        # YEAR (top line — prominent, warm amber, wide kerning)
        # The year is the single most important framing element:
        # the story spans 383–391 A.C., and players need to feel
        # the time skips between acts. Always show on its own line.
        if year:
            text ("{cps=20}" + year + "{/cps}"):
                font gui.system_font
                size 24
                color "#D4B886"
                kerning 5.0
                text_align 0.5
                xalign 0.5

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
        elif time:
            text ("{cps=20}" + time + "{/cps}"):
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
    # AC = "After Consolidation" (the founding of Solveil at 1 AC).
    # See Notion: 12_Solveil_Timeline_AC-AE_Enriched_Canon[LORE].
    #
    # Six months of 60 days each (360-day year):
    #   Ember → Rain → Kiln → Cipher → Silence → Forge
    #
    # The game spans 383-391 A.C. across four acts, with multi-year
    # time skips between them:
    #
    #   Act 1: Late Forge,   383 A.C.       (story start — Echelon service)
    #   Act 2: Early Ember,  385 A.C.       (post-defection — two years later)
    #   Act 3: Mid Cipher,   388 A.C.       (rebellion deepens — three years on)
    #   Act 4: Late Forge,   390 A.C.       (the Aegis stutters — two years on)
    #   Act 5: Late Forge → Ember, 390-391  (Fall of Echelon — not yet written)
    #
    # SCENE CONVENTION:
    # Scene files call show_timeline with the literal in-fiction date
    # string, e.g.
    #
    #   $ show_timeline("25th of Forge, 390 A.C.", "10:00", "War Room")
    #
    # The card renders the year on its own prominent line, the date
    # and time on a second line, and the location on a third. There
    # is no "day counter" — each scene file says the date directly.
    #
    # ACT_CALENDAR below exists only as documentation of the canonical
    # start-of-act dates, and as a reference the legacy _solveil_date*
    # helpers need for the deprecated DAY-N format (kept for backward
    # compat only; all live scenes use literal date strings).
    # ---------------------------------------------------------------

    SOLVEIL_MONTHS = ["Ember", "Rain", "Kiln", "Cipher", "Silence", "Forge"]
    SOLVEIL_DAYS_PER_MONTH = 60

    # Canonical start-of-act calendar anchor (doc/reference).
    # Tuple: (start_month_index, start_day_of_month, year)
    ACT_CALENDAR = {
        1: (5, 42, 383),   # Act 1 opens: 42nd of Forge,  383 A.C.
        2: (0,  8, 385),   # Act 2 opens: 8th  of Ember,  385 A.C.
        3: (3, 15, 388),   # Act 3 opens: 15th of Cipher, 388 A.C.
        4: (5, 25, 390),   # Act 4 opens: 25th of Forge,  390 A.C.
        5: (5, 52, 390),   # Act 5 opens: 52nd of Forge,  390 A.C. (not yet written)
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

    def _split_year_from_date(date_str):
        """Extract a 'NNN A.C.' year from a literal date string.

        Returns (date_without_year, year_text). If no year is found,
        returns (date_str, ''). This is how live scene files feed the
        card: the scene passes a literal like '25th of Forge, 390 A.C.'
        and this helper splits the year off so the card can render it
        on its own prominent top line.

        Also handles the legacy short form used by the a1_s01_branding
        prologue ('368 AC'), where there is no day-of-month component.
        """
        import re
        if not date_str:
            return "", ""
        # Match optional comma + whitespace + year + optional A.C./AC suffix
        m = re.search(r",?\s*(\d{3,4})\s*A\.?\s*C\.?\s*$", str(date_str), re.IGNORECASE)
        if not m:
            return date_str, ""
        year_text = m.group(1) + " A.C."
        date_without_year = date_str[:m.start()].rstrip(", ").strip()
        return date_without_year, year_text

    # ---------------------------------------------------------------
    # LEGACY DAY-N HELPERS — DEPRECATED
    # ---------------------------------------------------------------
    # These remain only so any old `show_timeline("DAY 5", ...)` call
    # that slips through keeps working. Live scene files no longer use
    # the DAY-N format — they pass literal in-fiction date strings
    # directly (see _split_year_from_date above).
    # ---------------------------------------------------------------

    def _get_current_act():
        """Detect the current act number from _current_scene_id (legacy)."""
        sid = str(getattr(renpy.store, '_current_scene_id', ''))
        if sid.startswith('a1_'): return 1
        if sid.startswith('a2_'): return 2
        if sid.startswith('a3_'): return 3
        if sid.startswith('a4_'): return 4
        if sid.startswith('a5_'): return 5
        return 1

    def _solveil_date_parts(game_day):
        """Legacy helper: convert a 1-indexed within-act day to
        (date_text, year_text). Kept for backward compat only.
        """
        if not game_day or game_day < 1:
            return "", ""
        act = _get_current_act()
        month_idx, start_day, year = ACT_CALENDAR.get(act, ACT_CALENDAR[1])
        cal_day = start_day + (game_day - 1)
        while cal_day > SOLVEIL_DAYS_PER_MONTH:
            cal_day -= SOLVEIL_DAYS_PER_MONTH
            month_idx += 1
            if month_idx >= len(SOLVEIL_MONTHS):
                month_idx = 0
                year += 1
        return _ordinal(cal_day) + " of " + SOLVEIL_MONTHS[month_idx], str(year) + " A.C."

    def _solveil_date(game_day):
        """Legacy helper: full date string with year embedded."""
        d, y = _solveil_date_parts(game_day)
        return d + ", " + y if d else ""

    def _parse_day_number(date_str):
        """Legacy helper: extract the day number from 'DAY X' format."""
        import re
        m = re.match(r"DAY\s+(\d+)", str(date_str))
        return int(m.group(1)) if m else 0

    # ---------------------------------------------------------------
    # HELPERS
    # ---------------------------------------------------------------

    def show_timeline(date="", time="", location=""):
        """Show the standard timeline card and wait for it to finish.

        Call at the top of a scene label (after scene_mark entered):
            $ show_timeline("25th of Forge, 390 A.C.", "10:00", "Phoenix Base — War Room")

        The year is automatically split off from the date string and
        rendered on its own prominent top line:

            390 A.C.
            25th of Forge  ·  10:00
            Phoenix Base — War Room

        Legacy DAY-N format is still accepted for backward compatibility
        but live scenes all use literal in-fiction date strings.
        """
        year = ""

        if isinstance(date, int):
            # Legacy: integer game day
            date, year = _solveil_date_parts(date)
        elif isinstance(date, str) and date.upper().startswith("DAY "):
            # Legacy: "DAY N" format — auto-convert via per-act calendar
            day_num = _parse_day_number(date)
            if day_num > 0:
                date, year = _solveil_date_parts(day_num)
        elif isinstance(date, str):
            # Live path: literal in-fiction date string like
            # "25th of Forge, 390 A.C." or "368 AC" — split the year off.
            date, year = _split_year_from_date(date)

        renpy.show_screen("scene_timeline", date=date, time=time, location=location, year=year)
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
