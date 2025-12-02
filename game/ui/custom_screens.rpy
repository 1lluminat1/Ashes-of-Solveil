
init python:
    import re

    _TAG_RE = re.compile(r"\{.*?\}")  # strips {b} {/b} etc.

    def _plain_length(marked_text):
        try:
            s = str(marked_text)
        except Exception:
            s = marked_text
        s = _TAG_RE.sub("", s)
        return len(s)

    def typing_seconds(marked_text, cps):
        cps = max(1, int(cps or 30))
        return _plain_length(marked_text) / float(cps)

# ---- blink animation for the hint (skipped if Reduced Motion is on)
init:
    transform blink_hint:
        alpha 0.0
        linear 0.6 alpha 1.0
        linear 0.6 alpha 0.0
        repeat

# === Choice menu with optional prompt, no image assets required ===

screen choice(items):
    $ pal = ui_current()
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 22

        # Show prompt if provided by the script (first string in `menu:`).
        if hasattr(items, "prompt") and items.prompt:
            text items.prompt style "choice_prompt_text" xalign 0.5 color pal["text"]

        for i in items:
            button:
                xsize 820
                yminimum 60
                padding (18, 14)
                background Solid(pal["choice_idle"])
                hover_background Solid(pal["choice_hover"])
                action i.action

                text i.caption style "choice_button_text" xalign 0.5

style choice_prompt_text is default:
    font gui.interface_font
    size 26
    outlines [(2, "#0006", 0, 0)]
    text_align 0.5

# === Tutorial / Disclaimer modal (centered, no scrollbar) ===
# Usage:
#   $ renpy.call_screen("tutorial_screen", text="...{b}warning{/b}...", cps=42)

screen tutorial_screen(text, cps=30):
    modal True
    tag tutorial

    # internal state
    default reveal_immediate = False
    default reveal_done = False

    # darken bg
    add Solid("#00000080")

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 1280
        padding (36, 36)
        background Frame("#0F1419CC", 12, 12)

        vbox:
            spacing 28
            xalign 0.5

            # centered content with typewriter
            text text:
                xalign 0.5
                text_align 0.5
                line_spacing 10
                size 22
                slow True
                slow_cps (9999 if reveal_immediate else cps)

            # Show the continue hint ONLY after reveal is complete.
            if reveal_done:
                if preferences.reduced_motion:
                    text "Click, Enter, or Space to continue":
                        xalign 0.5
                        size 18
                        color "#8FA6B8"
                else:
                    text "Click, Enter, or Space to continue":
                        xalign 0.5
                        size 18
                        color "#8FA6B8"
                        at blink_hint

    # Finish timing: when the natural type time elapses, allow dismiss.
    if not reveal_done and not reveal_immediate:
        timer typing_seconds(text, cps) action SetScreenVariable("reveal_done", True)

    # If the user has requested instant reveal, flip done shortly after.
    if reveal_immediate and not reveal_done:
        timer 0.05 action SetScreenVariable("reveal_done", True)

    # Full-screen invisible button to capture clicks and do the right thing.
    button:
        xfill True
        yfill True
        background None
        hover_background None
        focus_mask None
        action If(reveal_done, Return(True), SetScreenVariable("reveal_immediate", True))

    # Keyboard equivalents
    key "K_RETURN"    action If(reveal_done, Return(True), SetScreenVariable("reveal_immediate", True))
    key "K_KP_ENTER"  action If(reveal_done, Return(True), SetScreenVariable("reveal_immediate", True))
    key "K_SPACE"     action If(reveal_done, Return(True), SetScreenVariable("reveal_immediate", True))
    key "mouseup_1"   action If(reveal_done, Return(True), SetScreenVariable("reveal_immediate", True))

    # Block ways to skip/dismiss
    key "mouseup_3" action NullAction()    # right click does nothing
    key "K_ESCAPE"  action NullAction()    # ESC does nothing
    key "skip"      action NullAction()    # Skip key does nothing
