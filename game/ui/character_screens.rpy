# ================================================================
# CHARACTER SCREENS — grid + detail + gallery
# File: game/ui/character_screens.rpy
# ----------------------------------------------------------------
# Replaces the earlier trust/affection-bars screen with a full
# Eternum-style character browser:
#
#   characters_screen           — tabbed grid of character cards
#   ├─ Love Interests tab       — 6 LI cards
#   └─ Supporting tab           — family + antagonists
#
#   character_detail_screen     — full view of one character
#   ├─ Portrait + basic info    — left column
#   ├─ Codex Entries panel      — unlocked entries with "Open in Codex"
#   └─ Scene Gallery panel      — Eternum-style replay tiles
#
# Depends on:
#   game/data/character_profiles.rpy   (CHARACTER_PROFILES + helpers)
#   game/systems/scene_gallery.rpy     (gallery_unlock / gallery_play)
#   game/codex/codex_system.rpy        (codex_open for "Open in Codex")
#   game/ui/ui_solveil.rpy             (palette + path_accent)
# ================================================================


# ----------------------------------------------------------------
# 1) CHARACTERS SCREEN — tabbed card grid
# ----------------------------------------------------------------
# Opened via V/F3 or the pause-menu "Characters" button.
# Screen-local state:
#   active_tab   "love_interests" | "supporting"
#   detail_id    None → show grid; char_id → show detail view
# ----------------------------------------------------------------

screen characters_screen():
    modal True
    zorder 130

    default active_tab = "love_interests"
    default detail_id  = None

    $ pal = ui_current()

    add Solid(pal["bg"])
    add Solid("#00000066")
    add Solid(ui_overlay_color())

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1600
        ysize 900
        padding (32, 28)
        background Solid(pal["box_bg"])

        has vbox
        spacing 14

        # ---------- HEADER ----------
        hbox:
            xfill True
            yminimum 56

            if detail_id is None:
                text _("Characters"):
                    font gui.name_font
                    size 40
                    color pal["name"]
            else:
                textbutton _("← Back"):
                    action SetScreenVariable("detail_id", None)
                    text_size 22
                null width 24
                $ _prof_header = profile_get(detail_id)
                if _prof_header:
                    text _prof_header["display_name"]:
                        font gui.name_font
                        size 36
                        color _prof_header.get("accent", pal["name"])

            null xfill True

            textbutton _("Close"):
                action Hide("characters_screen")
                text_size 22

        # ---------- DIVIDER ----------
        frame:
            xfill True
            ysize 1
            background Solid(pal["accent"])
            padding (0, 0)

        # ---------- BODY ----------
        if detail_id is None:
            use characters_grid(active_tab, SetScreenVariable("active_tab", None), pal) id "grid"
        else:
            use character_detail_body(detail_id, pal) id "detail"

    key "K_ESCAPE" action If(
        detail_id is not None,
        true=SetScreenVariable("detail_id", None),
        false=Hide("characters_screen"),
    )
    key "mouseup_3" action If(
        detail_id is not None,
        true=SetScreenVariable("detail_id", None),
        false=Hide("characters_screen"),
    )


# ----------------------------------------------------------------
# 2) GRID BODY — tab row + card grid
# ----------------------------------------------------------------

screen characters_grid(active_tab, tab_action, pal):

    vbox:
        spacing 18
        xfill True

        # Tab row
        hbox:
            spacing 12
            textbutton _("Love Interests"):
                action SetScreenVariable("active_tab", "love_interests")
                text_size 24
                text_color (path_accent() if active_tab == "love_interests" else pal["text_dim"] if "text_dim" in pal else pal["highlight"])
                text_hover_color pal["text"]
            textbutton _("Supporting"):
                action SetScreenVariable("active_tab", "supporting")
                text_size 24
                text_color (path_accent() if active_tab == "supporting" else pal["highlight"])
                text_hover_color pal["text"]

            null xfill True

            $ _emp_count = sum(1 for _k, _p in CHARACTER_PROFILES.items() if _p.get("tab") == "love_interests")
            $ _sup_count = sum(1 for _k, _p in CHARACTER_PROFILES.items() if _p.get("tab") == "supporting")
            if active_tab == "love_interests":
                text _("[_emp_count] characters"):
                    size 16
                    color pal["highlight"]
            else:
                text _("[_sup_count] characters"):
                    size 16
                    color pal["highlight"]

        # Card grid — viewport for overflow on small windows
        viewport:
            xfill True
            yfill True
            mousewheel True
            draggable True
            scrollbars "vertical"

            $ _profiles = profiles_in_tab(active_tab)

            grid 3 2:
                xfill True
                yfill False
                spacing 20

                for _cid, _prof in _profiles:
                    use character_card(_cid, _prof, pal)

                # Pad remaining slots so the grid doesn't collapse
                $ _pad = max(0, 6 - len(_profiles))
                for _i in range(_pad):
                    null


# ----------------------------------------------------------------
# 3) CARD — one character tile on the grid
# ----------------------------------------------------------------

screen character_card(char_id, prof, pal):
    $ _unlocked_scenes, _total_scenes = gallery_unlocked_count_for(char_id)

    button:
        xsize 480
        ysize 280
        padding (16, 14)
        background Solid(pal["choice_idle"])
        hover_background Solid(pal["choice_hover"])
        action SetScreenVariable("detail_id", char_id)

        has hbox
        spacing 18

        # LEFT: portrait
        frame:
            xsize 150
            ysize 220
            padding (0, 0)
            background Solid(prof.get("accent", "#444") + "22")
            add profile_portrait(char_id):
                xsize 150
                ysize 220
                fit "cover"

        # RIGHT: name + info + scene counter
        vbox:
            xfill True
            yfill True
            spacing 4

            text prof["display_name"]:
                font gui.name_font
                size 24
                color prof.get("accent", pal["name"])

            text prof.get("tagline", ""):
                size 14
                color pal["highlight"]
                line_spacing 2

            null height 6

            # Top 3 info rows on the card (compact view)
            for _label, _val in prof.get("basic_info", [])[:3]:
                hbox:
                    spacing 6
                    text _label:
                        xsize 80
                        size 13
                        color pal["highlight"]
                    text _val:
                        size 13
                        color pal["text"]

            null height 4
            null yfill True

            # Scene counter pill (hidden for characters with no scenes)
            if _total_scenes > 0:
                hbox:
                    spacing 6
                    yalign 1.0
                    text "◆":
                        size 14
                        color prof.get("accent", pal["highlight"])
                    text _("[_unlocked_scenes] / [_total_scenes] scenes"):
                        size 13
                        color pal["highlight"]


# ----------------------------------------------------------------
# 4) DETAIL BODY — single character full view
# ----------------------------------------------------------------

screen character_detail_body(char_id, pal):
    $ _prof = profile_get(char_id)
    if _prof is None:
        text _("(character profile missing)"):
            color "#ff6666"
    else:
        default detail_tab = "codex"

        hbox:
            spacing 28
            xfill True
            yfill True

            # ========== LEFT COLUMN — portrait + info ==========
            vbox:
                xsize 420
                spacing 14

                frame:
                    xsize 420
                    ysize 520
                    padding (0, 0)
                    background Solid(_prof.get("accent", "#444") + "22")
                    add profile_portrait(char_id):
                        xsize 420
                        ysize 520
                        fit "cover"

                # Tagline
                text _prof.get("tagline", ""):
                    size 16
                    color pal["highlight"]
                    line_spacing 4

                null height 6

                # Basic info table
                vbox:
                    spacing 4
                    for _label, _val in _prof.get("basic_info", []):
                        hbox:
                            spacing 10
                            text _label:
                                xsize 110
                                size 15
                                color pal["highlight"]
                            text _val:
                                size 15
                                color pal["text"]

            # ========== RIGHT COLUMN — tabs + panels ==========
            vbox:
                xfill True
                yfill True
                spacing 12

                # Inner tabs
                hbox:
                    spacing 14
                    $ _codex_count = len(profile_unlocked_codex_ids(char_id))
                    $ _codex_total = len(profile_codex_ids(char_id))
                    $ _sc_unlocked, _sc_total = gallery_unlocked_count_for(char_id)

                    textbutton _("Codex  ([_codex_count]/[_codex_total])"):
                        action SetScreenVariable("detail_tab", "codex")
                        text_size 22
                        text_color (_prof.get("accent", pal["name"]) if detail_tab == "codex" else pal["highlight"])
                        text_hover_color pal["text"]

                    if _sc_total > 0:
                        textbutton _("Scenes ([_sc_unlocked]/[_sc_total])"):
                            action SetScreenVariable("detail_tab", "scenes")
                            text_size 22
                            text_color (_prof.get("accent", pal["name"]) if detail_tab == "scenes" else pal["highlight"])
                            text_hover_color pal["text"]

                # Divider under tabs
                frame:
                    xfill True
                    ysize 1
                    background Solid(pal["accent"])
                    padding (0, 0)

                # Panel area (one of two)
                if detail_tab == "codex":
                    use character_detail_codex(char_id, _prof, pal)
                else:
                    use character_detail_scenes(char_id, _prof, pal)


# ----------------------------------------------------------------
# 5) DETAIL — codex panel
# ----------------------------------------------------------------

screen character_detail_codex(char_id, prof, pal):
    $ _all_ids      = profile_codex_ids(char_id)
    $ _unlocked_ids = profile_unlocked_codex_ids(char_id)

    viewport:
        xfill True
        yfill True
        mousewheel True
        draggable True
        scrollbars "vertical"

        vbox:
            spacing 10

            if not _all_ids:
                text _("(No codex entries linked to this character yet.)"):
                    size 16
                    color pal["highlight"]

            for _cid in _all_ids:
                $ _is_unlocked = _cid in _unlocked_ids
                $ _meta = STATE["codex"]["entries"].get(_cid, None) if _is_unlocked else None

                frame:
                    xfill True
                    padding (18, 14)
                    background Solid(pal["choice_idle"])

                    has hbox
                    spacing 14

                    # LEFT: title + stage indicator
                    vbox:
                        xfill True
                        spacing 4

                        if _is_unlocked and _meta:
                            text _meta.get("title", _cid):
                                size 22
                                color pal["text"]
                            $ _stage = STATE["codex"]["progress"].get(_cid, 0)
                            $ _max_stage = max(0, len(_meta.get("stages", [])) - 1)
                            if _max_stage >= 1:
                                text _("Stage [_stage]/[_max_stage]"):
                                    size 14
                                    color pal["highlight"]
                            else:
                                text _meta.get("category", ""):
                                    size 14
                                    color pal["highlight"]
                        else:
                            text _("???"):
                                size 22
                                color pal["highlight"]
                            text _("Entry locked"):
                                size 14
                                color pal["highlight"]

                    # RIGHT: Open in Codex button
                    if _is_unlocked:
                        textbutton _("Open in Codex"):
                            action [
                                Hide("characters_screen"),
                                Function(codex_open, _cid, source="character_screen"),
                            ]
                            text_size 16
                            yalign 0.5


# ----------------------------------------------------------------
# 6) DETAIL — scene gallery panel
# ----------------------------------------------------------------

screen character_detail_scenes(char_id, prof, pal):
    $ _scenes = prof.get("scenes", [])

    viewport:
        xfill True
        yfill True
        mousewheel True
        draggable True
        scrollbars "vertical"

        vbox:
            spacing 14

            if not _scenes:
                text _("(No replay scenes for this character.)"):
                    size 16
                    color pal["highlight"]

            # 2-column scene tile layout — use vbox + paired hboxes so
            # the row count isn't a hard-coded grid expression.
            $ _scene_pairs = [ _scenes[i:i+2] for i in range(0, len(_scenes), 2) ]
            vbox:
                spacing 14
                for _row in _scene_pairs:
                    hbox:
                        spacing 14
                        for _scene in _row:
                            use character_scene_tile(char_id, _scene, prof, pal)


# ----------------------------------------------------------------
# 7) SCENE TILE — one gallery entry
# ----------------------------------------------------------------

screen character_scene_tile(char_id, scene, prof, pal):
    $ _sid = scene.get("id", "")
    $ _unlocked = gallery_is_unlocked(_sid)
    $ _label    = scene.get("label", _sid)
    $ _title    = scene.get("title", _sid)
    $ _act      = scene.get("act", "?")
    $ _path     = scene.get("path", "")
    $ _desc     = scene.get("description", "")

    # Compute hover background once so the expression isn't evaluated
    # inline on a screen statement child (which Ren'Py rejects).
    $ _hover_bg = Solid(pal["choice_hover"]) if _unlocked else Solid(pal["choice_idle"])

    button:
        xsize 480
        ysize 190
        padding (14, 12)
        background Solid(pal["choice_idle"])
        hover_background _hover_bg
        sensitive _unlocked
        action Function(gallery_play, _label)

        has hbox
        spacing 14

        # LEFT: thumbnail
        frame:
            xsize 160
            ysize 160
            padding (0, 0)
            background Solid(prof.get("accent", "#444") + "18")
            if _unlocked:
                add profile_scene_thumbnail(char_id, _sid):
                    xsize 160
                    ysize 160
                    fit "cover"
            else:
                # Locked silhouette — a soft tinted square with a lock glyph
                add Solid(prof.get("accent", "#444") + "0C"):
                    xsize 160
                    ysize 160
                text "🔒":
                    xalign 0.5
                    yalign 0.5
                    size 36
                    color pal["highlight"]

        # RIGHT: title + meta
        vbox:
            xfill True
            yfill True
            spacing 4

            if _unlocked:
                text _title:
                    size 20
                    color pal["text"]
                hbox:
                    spacing 6
                    text _("Act [_act]"):
                        size 13
                        color pal["highlight"]
                    text "·":
                        size 13
                        color pal["highlight"]
                    text _path:
                        size 13
                        color (path_accent() if _path in ("EMP","OB") else pal["highlight"])
                null height 6
                text _desc:
                    size 14
                    color pal["highlight"]
                    line_spacing 2

                null yfill True

                text _("▶ Replay"):
                    yalign 1.0
                    size 14
                    color prof.get("accent", pal["highlight"])
            else:
                text _("??? ???"):
                    size 20
                    color pal["highlight"]
                text _("Act [_act] · [_path]"):
                    size 13
                    color pal["highlight"]
                null height 6
                text _("Play through the story to unlock."):
                    size 13
                    color pal["highlight"]
                    italic True
