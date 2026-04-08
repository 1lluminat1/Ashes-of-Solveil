# =======================================================
# EMERGENCE MENU — Timed Hidden Third Option Screen
# File: game/screens/emergence_menu.rpy
# =======================================================
# This screen replaces the standard choice menu at specific
# moments where a hidden third option should fade in after
# the player waits without clicking.
#
# Usage:
#   call screen emergence_menu(
#       option_a="Step forward",
#       option_b="Step back",
#       option_c="Sit down at the rail.",
#       wait_seconds=12.0,
#       prompt="A man stands at the rail."
#   )
#   $ result = _return
# =======================================================

transform emergence_fade_in:
    alpha 0.0
    pause 0.5
    linear 2.0 alpha 1.0

screen emergence_menu(option_a, option_b, option_c, wait_seconds=12.0, prompt=None):
    modal True

    # Track when the menu was shown
    default emergence_timer_done = False

    # Timer that fires once after wait_seconds
    timer wait_seconds action SetScreenVariable("emergence_timer_done", True) repeat False

    frame:
        style_prefix "choice"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 10

            if prompt:
                text prompt style "choice_prompt"

            textbutton option_a:
                action Return("a")

            textbutton option_b:
                action Return("b")

            # The hidden third option — only appears after the timer
            if emergence_timer_done:
                textbutton option_c at emergence_fade_in:
                    action Return("c")
