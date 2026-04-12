# ================================================================
# SOLVEIL SHELL UI
# File: game/ui/solveil_shell.rpy
# ----------------------------------------------------------------
# Gathers the pieces of the player-facing shell that weren't in
# the baseline Ren'Py screens layer:
#
#   - characters_screen       (LI relationship summary, read-only)
#   - tp_interstice_screen    (90s True Path activation vignette)
#   - solveil_navigation      (override of default navigation — adds
#                              Codex + Characters buttons)
#   - solveil_main_nav_hooks  (Codex + Characters in main menu)
#   - global keymap           (C = codex browser, V = characters)
#
# Depends on:
#   - game/ui/ui_solveil.rpy            (palette, path_accent, chars)
#   - game/codex/codex_system.rpy       (codex_browser screen)
#   - game/systems/true_path.rpy        (tp_active, tp_depth)
#   - game/solveil_state_system.rpy     (STATE, empathy helpers)
# ================================================================


# ================================================================
# 1) GLOBAL KEYMAP
# ----------------------------------------------------------------
# C / F2 → Codex browser
# V / F3 → Characters screen
# These are routed through config.keymap so they work anywhere the
# game is accepting input (not during menus/rollback etc.).
# ================================================================
init -1 python:
    def _solveil_in_game():
        """True when we're inside a running scene, not on the main/menu screens."""
        try:
            # `main_menu` is a Ren'Py global; True while sitting on the menu.
            if renpy.store.main_menu:
                return False
        except Exception:
            pass
        # Also block while another modal menu owns input.
        try:
            if renpy.get_screen("main_menu") is not None:
                return False
        except Exception:
            pass
        return True

    def _solveil_open_codex():
        # Route through ShowMenu so the tag-menu screen flows through
        # Ren'Py's menu stack (respects save/load/history behavior).
        if not _solveil_in_game():
            return
        if not renpy.has_screen("codex_browser"):
            return
        try:
            renpy.run(ShowMenu("codex_browser"))
        except Exception:
            # Fallback — raw show, for contexts where ShowMenu can't fire.
            renpy.show_screen("codex_browser")

    def _solveil_open_characters():
        if not _solveil_in_game():
            return
        if not renpy.has_screen("characters_screen"):
            return
        # Characters screen is modal but not menu-tagged (it doesn't use
        # game_menu wrapper), so showing it directly is correct.
        try:
            if renpy.get_screen("characters_screen"):
                renpy.hide_screen("characters_screen")
                return
        except Exception:
            pass
        renpy.show_screen("characters_screen")

init 1 python:
    # Append, don't stomp — other files may have added keys too.
    config.keymap.setdefault("solveil_codex", [])
    config.keymap.setdefault("solveil_characters", [])
    for _k in ("c", "K_c", "K_F2"):
        if _k not in config.keymap["solveil_codex"]:
            config.keymap["solveil_codex"].append(_k)
    for _k in ("v", "K_v", "K_F3"):
        if _k not in config.keymap["solveil_characters"]:
            config.keymap["solveil_characters"].append(_k)

    # renpy.Keymap ties the keycodes above to the helper functions
    # defined at init -1 so they are callable anywhere the scene
    # layer is accepting input (dialogue, choice menus, transitions).
    config.underlay.append(renpy.Keymap(
        solveil_codex=_solveil_open_codex,
        solveil_characters=_solveil_open_characters,
    ))


# ================================================================
# 2) CHARACTERS SCREEN
# ----------------------------------------------------------------
# The Characters screen is now defined in
# game/ui/character_screens.rpy — a full tabbed card grid with
# detail view, codex cross-links, and an Eternum-style replay
# gallery. It reads data from game/data/character_profiles.rpy.
#
# This file keeps the key-binding + main-menu hooks so the C/V
# shortcuts and the pause-menu button land on the new screen.
# ================================================================


# ================================================================
# 3) TRUE PATH INTERSTICE
# ----------------------------------------------------------------
# Non-interactive activation vignette. Call from the scene that
# fires evaluate_true_path() — the Mirror Choice in Act 4/5.
#
# Usage inside a .rpy scene:
#     $ evaluate_true_path()
#     call screen tp_interstice_screen
#
# The screen self-dismisses after ~6 seconds. Audio hooks are
# commented out and safe to enable when files exist.
# ================================================================
transform _tp_fade_in:
    alpha 0.0
    linear 1.2 alpha 1.0

transform _tp_mirror_shimmer:
    alpha 0.0
    linear 2.0 alpha 0.85
    linear 2.0 alpha 0.55
    linear 2.0 alpha 0.85
    repeat

transform _tp_slow_fade_out:
    on replace:
        alpha 1.0
        linear 1.0 alpha 0.0

screen tp_interstice_screen():
    modal True
    zorder 200

    # Hard black base — the scene behind is wiped for the moment.
    add Solid("#000000")

    # A subtle path-tinted veil for EMP warm / OB cold feel.
    add Solid(ui_overlay_color())

    # Core motif line — this is the activation signature.
    # "It's not fate. It's a mirror."
    frame:
        xalign 0.5
        yalign 0.5
        padding (72, 56)
        background None

        vbox:
            spacing 24
            xalign 0.5

            text _("It's not fate."):
                font gui.narration_font
                size 40
                color "#E6ECF2"
                xalign 0.5
                at _tp_fade_in

            text _("It's a mirror."):
                font gui.narration_font
                size 40
                color path_accent()
                xalign 0.5
                at _tp_mirror_shimmer

    # Soft cue text — acknowledges depth without a ranking.
    text _("(something shifts underneath the scene)"):
        xalign 0.5
        yalign 0.88
        font gui.interface_font
        size 16
        color "#8FA6B8"
        at _tp_fade_in

    # Auto-dismiss after ~6 seconds, or on any key/click.
    timer 6.0 action Return()
    key "mouseup_1"  action Return()
    key "K_RETURN"   action Return()
    key "K_SPACE"    action Return()
    key "K_ESCAPE"   action Return()


# ================================================================
# 4) NAVIGATION OVERRIDE — adds Codex + Characters buttons
# ----------------------------------------------------------------
# The default screens.rpy `navigation()` has no codex hook. We
# redefine it here (later init order wins) with the extra buttons,
# gated so Codex only appears once the system has at least one
# unlocked entry.
# ================================================================
init python:
    def _codex_has_any():
        try:
            u = renpy.store.STATE.get("codex", {}).get("unlocked", set())
            return bool(u)
        except Exception:
            return False

screen navigation():

    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start") action Start()
            # From the main menu these are shortcuts to the same screens.
            if _codex_has_any():
                textbutton _("Codex") action ShowMenu("codex_browser")
        else:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")

        if not main_menu:
            # In-game only shortcuts.
            # Codex uses ShowMenu — it flows through the menu stack
            # because codex_browser is wrapped in game_menu.
            if _codex_has_any():
                textbutton _("Codex") action ShowMenu("codex_browser")
            # Characters is a transient overlay, not a menu — Show()
            # leaves the pause menu open underneath.
            textbutton _("Characters") action Show("characters_screen")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=not main_menu)
