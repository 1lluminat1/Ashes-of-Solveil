# ===================================================
# Solveil Codex System — API/UI (STATE + dev tools compatible)
# Content lives in codex_entries.rpy
# ===================================================

init 2 python:
    import re

    # ---------------- STATE ROOT ----------------
    def _codex_root():
        st = renpy.store.__dict__.get("STATE", None)
        if st is None:
            renpy.store.STATE = {}
            st = renpy.store.STATE
        st.setdefault("codex", {})
        c = st["codex"]
        c.setdefault("entries", {})        # id -> dict meta (author data)
        c.setdefault("unlocked", set())    # set[str]
        c.setdefault("recent", [])         # list[str], last 3
        c.setdefault("seen_toasts", set()) # set[str]
        c.setdefault("progress", {})       # entry_id -> int stage (0-based)
        return c

    # ---------------- MIGRATIONS ----------------
    def _ensure_codex_schema():
        c = _codex_root()

        # must-have containers
        c.setdefault("entries", {})
        c.setdefault("unlocked", set(c.get("unlocked", set())))
        c.setdefault("seen_toasts", set(c.get("seen_toasts", set())))
        c.setdefault("progress", {})
        # clamp recent and coerce if needed
        r = c.get("recent", [])
        if not isinstance(r, list): r = list(r)
        c["recent"] = r[:3]

        # normalize progress integers; drop junk
        for k in list(c["progress"].keys()):
            try:
                c["progress"][k] = max(0, int(c["progress"][k]))
            except Exception:
                del c["progress"][k]

        # seed entries if codex entries are loaded late (bootstrap also runs on start)
        src = _gather_codex_sources()
        for k, v in src.items():
            c["entries"].setdefault(k, v.copy())

        # prune progress for removed entries
        for k in list(c["progress"].keys()):
            if k not in c["entries"]:
                del c["progress"][k]

    if not hasattr(config, "after_load_callbacks"):
        config.after_load_callbacks = []
    if _ensure_codex_schema not in config.after_load_callbacks:
        config.after_load_callbacks.append(_ensure_codex_schema)

    # ---------------- DEV GATING ----------------
    def _dev_enabled():
        try:
            if not getattr(config, "developer", False):
                return False
            sys = renpy.store.STATE.get("sys", {})
            return bool(sys.get("telemetry_on", True))
        except Exception:
            return False

    def _dev_event(name: str, **payload):
        if not _dev_enabled():
            return
        fn = renpy.store.__dict__.get("dev_event", None)
        if fn:
            try:
                fn(name, **payload)
            except Exception:
                pass

    # ---------------- CONTENT REGISTRATION ----------------
    # external files can register additional dicts here
    CODEX_SEEDERS = []

    def codex_register_entries(d: dict):
        """Register a dict of codex entries. Safe to call multiple times."""
        if isinstance(d, dict):
            CODEX_SEEDERS.append(d)

    def _gather_codex_sources():
        # merge in this order: global CODEX_ENTRIES (if any) then registered dicts
        merged = {}
        g = renpy.store.__dict__.get("CODEX_ENTRIES", None)
        if isinstance(g, dict):
            merged.update(g)
        for d in CODEX_SEEDERS:
            if isinstance(d, dict):
                merged.update(d)
        return merged

    def codex_bootstrap():
        c = _codex_root()
        src = _gather_codex_sources()
        for k, v in src.items():
            c["entries"].setdefault(k, v.copy())

    if codex_bootstrap not in config.start_callbacks:
        config.start_callbacks.append(codex_bootstrap)

    # ---------------- PATH FLAVOR CUE ----------------
    def codex_open_cue():
        try:
            ps = renpy.store.STATE.get("canon", {}).get("path_state", None)
            if not ps and "empathy_band" in renpy.store.__dict__:
                band = renpy.store.empathy_band()
                ps = "EMP" if band == "empathy" else ("OB" if band == "obedience" else None)
            if ps == "EMP":
                renpy.play("sfx/ui_pulse_soft.ogg")
            elif ps == "OB":
                renpy.play("sfx/ui_silence_tick.ogg")
        except Exception:
            pass

    # ---------------- STAGE + REDACTION ----------------
    _r_tag = re.compile(r"\[r(\d+)\](.*?)\[/r\]", re.DOTALL)

    def _mask_text(s: str) -> str:
        return "".join(("█" if ch.isalnum() else ch) for ch in s)

    def _apply_redactions(text: str, stage: int) -> str:
        def sub(m):
            threshold = int(m.group(1))
            inner = m.group(2)
            return inner if stage >= threshold else _mask_text(inner)
        return _r_tag.sub(sub, text)

    def codex_current_stage(entry_id) -> int:
        c = _codex_root()
        return int(c["progress"].get(entry_id, 0))

    def codex_set_stage(entry_id, stage: int, source=None, toast=True):
        c = _codex_root()
        if entry_id not in c["entries"]:
            return False
        prev = codex_current_stage(entry_id)
        new  = max(int(prev), int(stage))
        c["unlocked"].add(entry_id)
        c["progress"][entry_id] = new
        if toast:
            renpy.show_screen("codex_toast", entry_id, mode=("expand" if new > prev else "unlock"))
        _dev_event("codex_reveal", entry=entry_id, stage=new, prev=prev,
                scene_id=renpy.game.context()._label or "", source=source or "")
        if "log_line" in renpy.store.__dict__ and new > prev:
            renpy.store.log_line(f"codex:expanded:{entry_id}→{new}")
        return True

    def codex_reveal(entry_id, to_stage=None, add=1, source=None, toast=True):
        if to_stage is None:
            to_stage = codex_current_stage(entry_id) + int(add)
        return codex_set_stage(entry_id, to_stage, source=source, toast=toast)

    def codex_render(entry_id):
        """Return a list of paragraphs for the player’s current knowledge."""
        c = _codex_root()
        meta = c["entries"].get(entry_id, {})
        stage = codex_current_stage(entry_id)
        if "stages" in meta and meta["stages"]:
            idx = min(stage, len(meta["stages"]) - 1)
            body = list(meta["stages"][idx].get("body", []))
        else:
            body = list(meta.get("body", []))
        return [_apply_redactions(p, stage) for p in body]

    # ---------------- PUBLIC API ----------------
    def codex_unlock(entry_id, source=None):
        c = _codex_root()
        if entry_id not in c["entries"]:
            return False
        just_now = entry_id not in c["unlocked"]
        c["unlocked"].add(entry_id)
        c["progress"].setdefault(entry_id, 0)
        if entry_id not in c["seen_toasts"]:
            c["seen_toasts"].add(entry_id)
            renpy.show_screen("codex_toast", entry_id, mode="unlock")
        _dev_event("codex_unlock", entry=entry_id, source=source or "",
                scene_id=renpy.game.context()._label or "")
        if "log_line" in renpy.store.__dict__ and just_now:
            renpy.store.log_line(f"codex:unlocked:{entry_id}")
        return True

    def codex_push_recent(entry_id):
        c = _codex_root()
        r = c["recent"]
        if entry_id in r:
            r.remove(entry_id)
        r.insert(0, entry_id)
        del r[3:]

    def codex_open(entry_id=None, source=None):
        codex_bootstrap()
        if entry_id:
            codex_unlock(entry_id, source=source)
            codex_push_recent(entry_id)
            _dev_event("codex_open", entry=entry_id, scene_id=renpy.game.context()._label or "")
            renpy.call_screen("codex_entry_modal", entry_id)
        else:
            _dev_event("codex_browser_open", scene_id=renpy.game.context()._label or "")
            renpy.call_screen("codex_browser")

    def codex_mention(entry_id, source=None):
        """Unlock silently without opening (for off-screen first mentions)."""
        codex_unlock(entry_id, source=source)

    # Search/filter (index only rendered text so we don’t leak spoilers)
    def codex_list(category=None, unlocked_only=True, query=u""):
        c = _codex_root()
        items = []
        q = (query or u"").strip().lower()
        for k, meta in c["entries"].items():
            is_unlocked = (k in c["unlocked"])
            if unlocked_only and not is_unlocked:
                continue
            if category and meta.get("category") != category:
                continue
            rendered = " ".join(codex_render(k)).lower()
            title = meta.get("title", u"")
            tags  = " ".join(meta.get("tags", []))
            hay = " ".join([title, tags, rendered]).lower()
            if q and q not in hay:
                continue
            items.append((k, meta, is_unlocked))
        items.sort(key=lambda t: renpy.translation.translate_string(t[1].get("title", u""), None).lower())
        return items

    # Inline hyperlinks: {a=codex:<id>}…{/a}
    def _codex_hyperlink(target):
        codex_open(target, source="inline")
    config.hyperlink_handlers["codex"] = _codex_hyperlink


# -------------------- SCREENS --------------------
screen codex_toast(entry_id, mode="unlock"):
    modal False
    zorder 150
    frame at truecenter:
        padding (16, 12)
        background Solid("#111a")
        $ title = STATE["codex"]["entries"][entry_id]["title"]
        if mode == "expand":
            text _("Codex expanded: [title]") size 22
        else:
            text _("Codex updated: [title]") size 22
    timer 1.5 action Hide("codex_toast")

screen codex_entry_modal(entry_id):
    style_prefix "codex"
    modal True
    zorder 120
    on "show" action Function(codex_open_cue)
    key "mouseup_3" action Return()
    key "K_KP_ENTER" action Return()
    frame:
        style_prefix "codex"
        vbox:
            hbox:
                xfill True
                spacing 12

                $ _meta = STATE["codex"]["entries"][entry_id]
                $ _prog = STATE["codex"]["progress"].get(entry_id, 0)
                $ _maxs = max(0, len(_meta.get("stages", [])) - 1)

                text _meta["title"] size 36

                if _maxs >= 1 and _prog < _maxs:
                    null width 8
                    text _("(partial)") size 16 color "#9aa"

                # flex spacer (replaces 'spacer')
                null xfill True

                if entry_id in STATE["codex"]["recent"]:
                    text _("recent") size 14 color "#888"
                    null width 12

                textbutton _("Full Codex") action ShowMenu("codex_browser")
                textbutton _("Back") action Return()

    null height 8
    vpgrid:
        cols 1
        mousewheel True
        draggable True
        for para in codex_render(entry_id):
            text para size 26
            null height 8
    null height 12
    $ recent = [i for i in STATE["codex"]["recent"] if i != entry_id]
    if recent:
        hbox:
            text _("Recent:") size 18
            for rid in recent:
                textbutton STATE["codex"]["entries"][rid]["title"] action [Function(codex_push_recent, rid), Hide("codex_entry_modal"), Function(codex_open, rid)]

screen codex_browser():
    style_prefix "codex"
    tag menu
    use game_menu(_("Codex"), scroll="viewport"):
        default _query = ""
        default _category = None
        default _show_locked = False
        vbox:
            hbox:
                xfill True
                spacing 12

                text _("Search: ") size 22
                input value VariableInputValue("_query") length 30 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -'"
                null width 24

                text _("Category: ") size 22
                $ cats = sorted(set([m["category"] for m in STATE["codex"]["entries"].values()]))
                textbutton _("All") action SetVariable("_category", None)
                for cat in cats:
                    textbutton cat action SetVariable("_category", cat)

                # flex spacer (replaces 'spacer')
                null xfill True

                textbutton _("Show Locked") action SetVariable("_show_locked", True)
                textbutton _("Hide Locked") action SetVariable("_show_locked", False)

        null height 12
        $ items = codex_list(category=_category, unlocked_only=(not _show_locked), query=_query)
        if not items:
            text _("No entries yet.") size 24
        else:
            for k, meta, is_unlocked in items:
                frame:
                    has hbox
                    vbox:
                        hbox:
                            text meta["title"] size 30
                            $ prog = STATE["codex"]["progress"].get(k, 0)
                            $ max_stage = max(0, len(meta.get("stages", [])) - 1)
                            if max_stage >= 1 and prog < max_stage:
                                null width 8
                                text _("(partial)") size 14 color "#9aa"
                        text meta["category"] size 16 color "#888"
                        text ", ".join(meta.get("tags", [])) size 16 color "#aaa"
                    null xfill True
                    if is_unlocked:
                        textbutton _("Open") action [Function(codex_push_recent, k), Function(codex_open, k)]
                    else:
                        text _("Locked") size 20 color "#777"

# -------------------- STYLE --------------------
init 2:
    # Inheritance
    style codex_vbox is vbox
    style codex_label is default
    style codex_text  is default
    style codex_frame is frame

    # Properties
    style codex_label:
        size 22
        color "#C0C5CE"

    style codex_text:
        size 20
        color "#dddddd"
        kerning 0.2

    # Rounded background for frames (use Solid or a 9-slice PNG)
    # If you have a 9-slice asset, use: Frame("gui/dialog_box_12.png", 12, 12)
    style codex_frame:
        background Frame(Solid("#0a0a0cff"), 12, 12)