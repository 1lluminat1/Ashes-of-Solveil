# ================================================================
# SCENE GALLERY — state, unlock helpers, replay mechanism
# File: game/systems/scene_gallery.rpy
# ----------------------------------------------------------------
# The gallery is the Eternum-style replay grid that lives inside
# the character detail screen. Scenes unlock when the player plays
# them through normally (via gallery_unlock()) and can then be
# replayed via gallery_play(), which uses Ren'Py's call_replay()
# context so the replay does not mutate the main run state.
#
# Scene metadata (titles, descriptions, paths, thumbnails) lives
# in game/data/character_profiles.rpy under each character's
# "scenes" list. This file owns the unlock state and replay API.
# ================================================================

init -1 python:

    def _gallery_init():
        """Ensure STATE['gallery'] exists with the schema we expect."""
        g = STATE.setdefault("gallery", {})
        if "unlocked" not in g:
            g["unlocked"] = set()
        elif not isinstance(g["unlocked"], set):
            # migrate from list (older save) → set
            g["unlocked"] = set(g["unlocked"])
        g.setdefault("last_played", None)
        g.setdefault("replay_count", 0)

    # ------------------------------------------------------------
    # UNLOCK HELPERS
    # ------------------------------------------------------------

    def gallery_unlock(scene_id):
        """Mark a scene as unlocked in the gallery. Idempotent.

        Call this once inside every intimate scene label so the
        scene surfaces in the player's gallery after the first
        natural playthrough. Typical placement: right after the
        scene's opening tasks, or immediately after the aftercare
        block so the unlock only lands if the player saw the
        meaningful part of the scene."""
        _gallery_init()
        STATE["gallery"]["unlocked"].add(scene_id)

    def gallery_lock(scene_id):
        """Remove a scene from the unlocked set. Rarely needed,
        but useful for debug menus and NG+ resets."""
        _gallery_init()
        STATE["gallery"]["unlocked"].discard(scene_id)

    def gallery_is_unlocked(scene_id):
        _gallery_init()
        return scene_id in STATE["gallery"]["unlocked"]

    def gallery_unlocked_count():
        _gallery_init()
        return len(STATE["gallery"]["unlocked"])

    def gallery_unlocked_count_for(char_id):
        """Return (unlocked, total) scene counts for one character.
        Reads the character's scene list from CHARACTER_PROFILES."""
        _gallery_init()
        prof = renpy.store.__dict__.get("CHARACTER_PROFILES", {}).get(char_id)
        if not prof:
            return (0, 0)
        scenes = prof.get("scenes", [])
        unlocked = STATE["gallery"]["unlocked"]
        hit = sum(1 for s in scenes if s.get("id") in unlocked)
        return (hit, len(scenes))

    # ------------------------------------------------------------
    # REPLAY
    # ------------------------------------------------------------
    # Ren'Py's call_replay() enters a special replay context where
    # the label runs to completion but state mutations don't
    # persist to the main run. Choices still work during replay
    # (consent gates still gate content). When the label returns,
    # we're back in the character screen.

    def gallery_play(scene_label):
        """Replay the given scene label via Ren'Py's replay system.
        The caller should be a screen action — Ren'Py will close
        the calling menu before entering replay mode, and return
        here after the replay ends."""
        _gallery_init()
        STATE["gallery"]["last_played"] = scene_label
        STATE["gallery"]["replay_count"] = STATE["gallery"].get("replay_count", 0) + 1
        try:
            renpy.call_replay(scene_label, scope={})
        except Exception as _e:
            # If replay fails (e.g., label missing), log it and
            # silently return rather than crashing the screen.
            try:
                log_line("gallery: replay of " + str(scene_label) + " failed: " + str(_e))
            except Exception:
                pass

    # ------------------------------------------------------------
    # After-load migration
    # ------------------------------------------------------------
    if not hasattr(config, "after_load_callbacks"):
        config.after_load_callbacks = []
    if _gallery_init not in config.after_load_callbacks:
        config.after_load_callbacks.append(_gallery_init)
