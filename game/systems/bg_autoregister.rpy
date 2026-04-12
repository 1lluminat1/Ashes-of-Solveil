# =============================================================
# BACKGROUND AUTO-REGISTRATION
# File: game/systems/bg_autoregister.rpy
# -------------------------------------------------------------
# Scans images/bg/<scene_id>/ at init time and registers every
# PNG under it as a Ren'Py image with a tag derived from the
# folder + filename.
#
# Convention (matches tools/inject_render_stubs.py):
#
#   images/bg/a1_s06_gala/001.png
#           → image a1_s06_gala_001 = "images/bg/a1_s06_gala/001.png"
#
# After auto-registration, scene statements like
#   scene a1_s06_gala_047 with dissolve
# just work. No manual `image` definitions required.
#
# Accepted extensions: .png, .jpg, .jpeg, .webp (the three Ren'Py
# reliably blits without extra config).
# =============================================================

init -2 python:

    def _auto_register_bg_folders():
        try:
            all_files = renpy.list_files()
        except Exception:
            return

        _registered = 0
        _exts = (".png", ".jpg", ".jpeg", ".webp")

        for f in all_files:
            # Only look under images/bg/ (use both / and \ separators)
            _norm = f.replace("\\", "/")
            if not _norm.startswith("images/bg/"):
                continue
            if not _norm.lower().endswith(_exts):
                continue

            parts = _norm.split("/")
            # Expect: images/bg/<scene_id>/<beat>.<ext>
            if len(parts) < 4:
                # Flat image right under images/bg/ — register as-is with
                # the filename (minus extension) as the tag.
                fname = parts[-1]
                tag = fname.rsplit(".", 1)[0]
                try:
                    renpy.image(tag, _norm)
                    _registered += 1
                except Exception:
                    pass
                continue

            scene_id = parts[2]
            fname = parts[-1]
            beat = fname.rsplit(".", 1)[0]

            # Tag: "<scene_id>_<beat>" — matches the stub injector.
            # Zero-padded beat numbers sort correctly out of the box.
            tag = scene_id + "_" + beat
            try:
                renpy.image(tag, _norm)
                _registered += 1
            except Exception:
                pass

        # Stash the count on the store so the debug overlay can read it.
        try:
            renpy.store._bg_auto_registered = _registered
        except Exception:
            pass

    _auto_register_bg_folders()
