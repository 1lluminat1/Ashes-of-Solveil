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
    # The game spans 383-391 AC (8 years). Each act takes place in
    # a different year with time skips between them:
    #
    #   Act 1: Late Forge, 383 AC  (story start — Echelon service)
    #   Act 2: Early Ember, 385 AC (post-defection — six months later)
    #   Act 3: Mid Cipher, 388 AC  (rebellion deepens — 3 years on)
    #   Act 4: Mid Forge, 390 AC   (the Aegis stutters)
    #   Act 5: Late Forge → Ember, 390-391 AC (Fall of Echelon)
    #
    # Within each act, "DAY X" is relative to that act's start.
    # The helper auto-detects the current act from _current_scene_id.
    #
    # 391 AC = Year of Echelon's fall = Aeron's 391st mission number.
    # Zira reveals the parallel in Act 5's prep scene.
    # ---------------------------------------------------------------

    SOLVEIL_MONTHS = ["Ember", "Rain", "Kiln", "Cipher", "Silence", "Forge"]
    SOLVEIL_DAYS_PER_MONTH = 60

    # Per-act calendar origin:
    #   (start_month_index, start_day_of_month, year, first_game_day_in_act)
    #
    # IMPORTANT: "DAY X" in the scripts is a CUMULATIVE day number that
    # carries across acts (Act 1 ends DAY 7, Act 2 starts DAY 8, Act 3
    # starts DAY 22, Act 4 starts DAY 43). Inside the story-world, multi-
    # year time skips happen between acts; the day numbers do NOT reflect
    # those gaps — the calendar origin per act handles that.
    #
    # Mapping: each act's first cumulative DAY maps to the listed
    # (month, day_of_month, year). Subsequent scene days offset forward
    # from there.
    ACT_CALENDAR = {
        1: (5, 42, 383,  1),   # DAY 1  = 42nd of Forge,   383 AC (story start)
        2: (0,  8, 385,  8),   # DAY 8  = 8th  of Ember,   385 AC (post-defection)
        3: (3, 15, 388, 22),   # DAY 22 = 15th of Cipher,  388 AC (rebellion deepens)
        4: (5, 25, 390, 43),   # DAY 43 = 25th of Forge,   390 AC (Aegis stutters)
        5: (5, 52, 390, 56),   # DAY 56 = 52nd of Forge,   390 AC → overflows into 391 (Fall)
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

    def _solveil_date_parts(game_day):
        """Convert a cumulative game day (DAY X from the script) to
        a (date_text, year_text) tuple, e.g. ('25th of Forge', '390 A.C.').

        Uses _current_scene_id to determine which act we're in, looks up
        that act's calendar origin, then offsets relative to the act's
        first cumulative day. Day numbers carry across acts; the per-act
        origin handles the story-world year jumps.
        """
        if not game_day or game_day < 1:
            return "", ""

        act = _get_current_act()
        month_idx, start_day, year, first_day = ACT_CALENDAR.get(act, ACT_CALENDAR[1])

        # Offset from the act's first cumulative day, not from DAY 1.
        cal_day = start_day + (game_day - first_day)

        # Forward overflow into subsequent months/years
        while cal_day > SOLVEIL_DAYS_PER_MONTH:
            cal_day -= SOLVEIL_DAYS_PER_MONTH
            month_idx += 1
            if month_idx >= len(SOLVEIL_MONTHS):
                month_idx = 0
                year += 1

        # Backward underflow (defensive — for a stray scene below the
        # act's declared first day; shouldn't happen in normal play).
        while cal_day < 1:
            cal_day += SOLVEIL_DAYS_PER_MONTH
            month_idx -= 1
            if month_idx < 0:
                month_idx = len(SOLVEIL_MONTHS) - 1
                year -= 1

        month_name = SOLVEIL_MONTHS[month_idx]
        date_text = _ordinal(cal_day) + " of " + month_name
        year_text = str(year) + " A.C."
        return date_text, year_text

    def _solveil_date(game_day):
        """Backward-compat: returns the full date string with year embedded.

        Prefer _solveil_date_parts() for new code — it returns the year
        separately so the timeline card can render it on its own line.
        """
        date_text, year_text = _solveil_date_parts(game_day)
        if not date_text:
            return ""
        return date_text + ", " + year_text

    def _parse_day_number(date_str):
        """Extract the day number from 'DAY X' format. Returns 0 if not matched."""
        import re
        m = re.match(r"DAY\s+(\d+)", str(date_str))
        return int(m.group(1)) if m else 0

    def _split_year_from_date(date_str):
        """Extract a 'NNN A.C.' year from a preformatted date string.

        Returns (date_without_year, year_text). If no year is found,
        returns (date_str, ''). Used for hand-authored dates like
        '368 AC' (a1_s01_branding) or '5th of Ember, 390 AC'.
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
    # HELPERS
    # ---------------------------------------------------------------

    def show_timeline(date="", time="", location=""):
        """Show the standard timeline card and wait for it to finish.

        Call at the top of a scene label (after scene_mark entered):
            $ show_timeline("DAY 3", "04:17", "Phoenix Secondary Base")

        The 'DAY X' format is auto-converted to the Solveil calendar.
        The year is split out and rendered on its own prominent line:

            390 A.C.
            5th of Forge  ·  04:17
            Phoenix Secondary Base

        You can also pass a pre-formatted string ('368 AC',
        '5th of Ember, 390 AC') or an integer day number — the year is
        extracted from any of these forms and shown on the year line.
        """
        year = ""

        # Auto-convert DAY X (or int) to Solveil calendar parts
        if isinstance(date, int):
            date, year = _solveil_date_parts(date)
        elif isinstance(date, str) and date.upper().startswith("DAY "):
            day_num = _parse_day_number(date)
            if day_num > 0:
                date, year = _solveil_date_parts(day_num)
        elif isinstance(date, str):
            # Hand-authored date like '368 AC' or '5th of Ember, 390 AC'.
            # Pull the year onto its own line if present.
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
