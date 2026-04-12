#!/usr/bin/env python3
# =============================================================
# Asset manifest generator for Ashes of Solveil.
#
# Scans the project for every referenced image/audio asset and
# writes a checklist to game/data/asset_manifest.md.
#
# Re-run whenever a new batch of scene files lands:
#     python3 tools/gen_asset_manifest.py
#
# The manifest itself is designed as a handoff sheet for artists
# and sound designers.
# =============================================================
import glob
import os
import re
from collections import defaultdict

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(REPO_ROOT)


def parse_character_profiles():
    """Return (portraits, scenes) extracted from character_profiles.rpy."""
    path = "game/data/character_profiles.rpy"
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    # First, pull out the _CA_* color constants so we can resolve
    # "accent": _CA_LYRA to the actual hex value.
    accent_map = {}
    for m in re.finditer(r"(_CA_\w+)\s*=\s*\"(#[0-9A-Fa-f]+)\"", text):
        accent_map[m.group(1)] = m.group(2)

    portraits = []
    for m in re.finditer(
        r'"(\w+)":\s*\{\s*"display_name":\s*"([^"]+)".*?"accent":\s*(\w+).*?"portrait":\s*"([^"]+)"',
        text,
        re.DOTALL,
    ):
        cid, name, accent_var, p = m.groups()
        accent_hex = accent_map.get(accent_var, accent_var)
        portraits.append((cid, name, p, accent_hex))

    scenes = []
    for m in re.finditer(
        r'"id":\s*"(\w+)",\s*"label":\s*"(\w+)",\s*"title":\s*"([^"]+)",\s*"act":\s*(\d+),\s*"path":\s*"(\w+)"',
        text,
    ):
        sid, label, title, act, p = m.groups()
        scenes.append((sid, title, "Act " + act, p))

    return portraits, scenes


def scan_backgrounds():
    """Return dict: bg_tag -> list of (file, line_num, commented)."""
    refs = defaultdict(list)
    pat = re.compile(r"^(\s*)(#\s*)?scene\s+(bg_[a-z0-9_]+)", re.IGNORECASE)
    for f in sorted(glob.glob("game/act*/*.rpy")):
        if "OLD" in f:
            continue
        with open(f, encoding="utf-8", errors="ignore") as fh:
            for i, line in enumerate(fh, 1):
                m = pat.match(line)
                if m:
                    _, comment, name = m.groups()
                    refs[name].append((f, i, comment is not None))
    return refs


def scan_audio():
    """Return dict: audio_path -> list of (file, line_num, channel, commented)."""
    refs = defaultdict(list)
    pat = re.compile(
        r'^(\s*)(#\s*)?(play|queue)\s+(music|sound|ambient|ambient2|voice)\s+["\']([^"\']+)["\']',
        re.IGNORECASE,
    )
    for f in sorted(glob.glob("game/act*/*.rpy")):
        if "OLD" in f:
            continue
        with open(f, encoding="utf-8", errors="ignore") as fh:
            for i, line in enumerate(fh, 1):
                m = pat.match(line)
                if m:
                    _, comment, _action, chan, path = m.groups()
                    refs[path].append((f, i, chan, comment is not None))
    return refs


def scan_scene_render_budget():
    """For each scene file, return a row describing its render budget.

    Returns list of dicts with:
        scene_id      filename stem
        act           directory-based act key (act1, act2, ...)
        path          absolute path
        beats         count of dialogue/narration lines inside the label
        stubs         count of `# scene <id>_NNN ... @render_stub` lines
        renders       count of .png/.jpg/.webp files in images/bg/<scene_id>/
    """
    say_pat = re.compile(r'^\s*([a-z_][a-z_0-9]*\s+)?"[^"]')
    stub_pat = re.compile(r'^\s*#\s*scene\s+\S+\s+with\s+\w+\s+#\s*@render_stub')
    rows = []
    for f in sorted(glob.glob("game/act*/*.rpy")):
        if "OLD" in f:
            continue
        scene_id = os.path.splitext(os.path.basename(f))[0]
        # Skip diagnostic / scratch files
        if scene_id.startswith("DIAGNOSTIC") or scene_id.startswith("_"):
            continue
        # Skip interludes — short by design, rendered as single-shot stills
        # more often than per-beat sequences.
        if "_int_" in scene_id:
            continue

        # Derive act from the parent directory
        parts = f.replace("\\", "/").split("/")
        act = parts[1] if len(parts) >= 3 else "?"  # game/actN/file.rpy

        beats = 0
        stubs = 0
        in_label = False
        with open(f, encoding="utf-8", errors="ignore") as fh:
            for line in fh:
                if line.lstrip().startswith("label "):
                    in_label = True
                if in_label:
                    if stub_pat.match(line):
                        stubs += 1
                    elif say_pat.match(line):
                        beats += 1

        # Count rendered files in the matching folder
        folder = os.path.join("images", "bg", scene_id)
        renders = 0
        if os.path.isdir(folder):
            for name in os.listdir(folder):
                if name.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                    renders += 1

        rows.append({
            "scene_id": scene_id,
            "act":      act,
            "path":     f,
            "beats":    beats,
            "stubs":    stubs,
            "renders":  renders,
        })
    return rows


def ref_status(refs_for_one):
    total = len(refs_for_one)
    commented_n = sum(1 for r in refs_for_one if (r[-1] if len(r) == 4 else r[2]))
    active_n = total - commented_n
    if commented_n > 0 and active_n > 0:
        return str(active_n) + " active, " + str(commented_n) + " commented"
    if commented_n == total:
        return str(total) + " commented"
    return str(total) + " active"


def write_manifest():
    portraits, scenes = parse_character_profiles()
    bg_refs = scan_backgrounds()
    audio_refs = scan_audio()
    render_rows = scan_scene_render_budget()

    out = []
    out.append("# Ashes of Solveil — Asset Manifest")
    out.append("")
    out.append(
        "Generated checklist of every image and audio asset referenced "
        "in the project. Use as a handoff sheet when briefing artists "
        "and sound designers."
    )
    out.append("")
    out.append("## Status conventions")
    out.append("")
    out.append("- ⬜ Referenced but file not present")
    out.append("- ✅ File present at expected path")
    out.append("- 💤 Commented-out reference (will be uncommented when asset lands)")
    out.append("")
    out.append("---")
    out.append("")

    # Portraits
    out.append("## 1. Character Portraits")
    out.append("")
    out.append(
        "One portrait per character (10 total). Rendered as a 420x520 card "
        "on the Characters detail screen and 150x220 on the grid card. "
        "Drop PNGs at the listed paths and `profile_portrait()` in "
        "`game/data/character_profiles.rpy` picks them up automatically. "
        "Until present, each slot renders as an accent-tinted Solid."
    )
    out.append("")
    out.append("| Character | Path | Accent |")
    out.append("|---|---|---|")
    for cid, name, p, accent in portraits:
        mark = "✅" if os.path.exists(p) else "⬜"
        out.append("| " + mark + " " + name + " | `" + p + "` | " + accent + " |")
    out.append("")

    # Gallery thumbnails
    out.append("## 2. Scene Gallery Thumbnails")
    out.append("")
    out.append(
        "One 160x160 thumbnail per replay scene. Drop PNGs at "
        "`images/ui/gallery/<scene_id>.png`. The gallery fallback is a "
        "tinted Solid keyed off the character accent."
    )
    out.append("")
    out.append("| Scene ID | Title | Act | Path | Expected Path |")
    out.append("|---|---|---|---|---|")
    for sid, title, act, p in scenes:
        thumb_path = "images/ui/gallery/" + sid + ".png"
        mark = "✅" if os.path.exists(thumb_path) else "⬜"
        out.append(
            "| " + mark + " `" + sid + "` | " + title + " | " + act + " | " + p + " | `" + thumb_path + "` |"
        )
    out.append("")

    # Backgrounds
    out.append("## 3. Scene Backgrounds")
    out.append("")
    out.append(
        "Every `scene bg_xxx` reference across the script, commented or "
        "active. When a real plate arrives:"
    )
    out.append("")
    out.append("1. Drop the PNG in `images/bg/` (or your asset path)")
    out.append("2. Register it via `image bg_xxx = \"images/bg/xxx.png\"`")
    out.append("3. Uncomment the `scene bg_xxx` line in each referencing file")
    out.append("")
    out.append(
        "Stub placeholders exist for bg tags that lint would otherwise flag "
        "in `game/ui/stub_defs.rpy` (cold-color Solid blocks)."
    )
    out.append("")
    out.append("| Background tag | References | Status |")
    out.append("|---|---|---|")
    for name in sorted(bg_refs.keys()):
        refs = bg_refs[name]
        out.append("| `" + name + "` | " + str(len(refs)) + " | " + ref_status(refs) + " |")
    out.append("")

    # Audio
    out.append("## 4. Audio")
    out.append("")
    out.append(
        "Every `play music/sound/ambient` reference across the script, "
        "commented or active. Channels in use: `music`, `sound`, "
        "`ambient`, `ambient2`, `voice`. Channel registration lives in "
        "`game/ui/audio_menu.rpy`."
    )
    out.append("")
    out.append("| File | Channel | References | Status |")
    out.append("|---|---|---|---|")
    by_chan = defaultdict(list)
    for path, refs in audio_refs.items():
        chan = refs[0][2]
        by_chan[chan].append((path, refs))
    for chan in sorted(by_chan.keys()):
        for path, refs in sorted(by_chan[chan]):
            mark = "✅" if os.path.exists(path) else "⬜"
            # Adapt ref_status to audio ref tuple shape
            total = len(refs)
            commented_n = sum(1 for r in refs if r[3])
            active_n = total - commented_n
            if commented_n > 0 and active_n > 0:
                status = str(active_n) + " active, " + str(commented_n) + " commented"
            elif commented_n == total:
                status = str(total) + " commented"
            else:
                status = str(total) + " active"
            out.append(
                "| " + mark + " `" + path + "` | " + chan + " | " + str(total) + " | " + status + " |"
            )
    out.append("")

    # Per-Scene Render Budget
    out.append("## 5. Per-Scene Render Budget")
    out.append("")
    out.append(
        "Workflow: each scene lives in its own folder under "
        "`images/bg/<scene_id>/` and is rendered as a numbered sequence "
        "`001.png`, `002.png`, etc. One render typically covers 2-3 "
        "dialogue beats — a character talks for a few lines on one pose, "
        "then the next render handles the next 2-3 beats."
    )
    out.append("")
    out.append("**To scaffold a scene before you render it:**")
    out.append("")
    out.append("```")
    out.append("python3 tools/inject_render_stubs.py <scene_id>")
    out.append("```")
    out.append("")
    out.append(
        "That inserts commented `# scene <scene_id>_NNN with dissolve` stubs "
        "at each cluster boundary. Uncomment each as the matching render lands "
        "in `images/bg/<scene_id>/NNN.png`. Auto-registration lives in "
        "`game/systems/bg_autoregister.rpy` — just drop files in the folder "
        "and Ren'Py picks them up without manual `image` definitions."
    )
    out.append("")
    out.append("**Columns:**")
    out.append("")
    out.append("- **Beats** — dialogue/narration lines inside the scene's label")
    out.append("- **Stubs** — commented `# scene ... @render_stub` lines (0 = not scaffolded yet)")
    out.append("- **Renders** — PNG/JPG/WEBP files present in the scene's folder")
    out.append("- **%** — renders / stubs, or renders / (beats/3) as an estimate if unscaffolded")
    out.append("")
    out.append("| Scene | Beats | Stubs | Renders | % | Status |")
    out.append("|---|---|---|---|---|---|")

    def _pct(rendered, target):
        if target <= 0:
            return 0
        return int(100 * rendered / target)

    act_totals = defaultdict(lambda: {"beats": 0, "stubs": 0, "renders": 0, "scenes": 0})
    for row in render_rows:
        sid = row["scene_id"]
        act_key = row.get("act", "?")
        act_totals[act_key]["beats"] += row["beats"]
        act_totals[act_key]["stubs"] += row["stubs"]
        act_totals[act_key]["renders"] += row["renders"]
        act_totals[act_key]["scenes"] += 1

        # Target = stubs if scaffolded, else estimate (beats / 3)
        target = row["stubs"] if row["stubs"] > 0 else max(1, row["beats"] // 3)
        pct = _pct(row["renders"], target)

        if row["renders"] == 0 and row["stubs"] == 0:
            status = "⬜ not started"
        elif row["renders"] == 0 and row["stubs"] > 0:
            status = "📋 scaffolded"
        elif row["renders"] < target:
            status = "🔄 in progress"
        else:
            status = "✅ complete"

        out.append(
            "| `" + sid + "` | " + str(row["beats"]) + " | "
            + str(row["stubs"]) + " | " + str(row["renders"]) + " | "
            + str(pct) + "% | " + status + " |"
        )
    out.append("")

    # Per-act totals
    out.append("### Per-Act Render Totals")
    out.append("")
    out.append("| Act | Scenes | Beats | Stubs | Renders | Est. Target |")
    out.append("|---|---|---|---|---|---|")
    for act_key in sorted(act_totals.keys()):
        t = act_totals[act_key]
        est_target = t["stubs"] if t["stubs"] > 0 else t["beats"] // 3
        out.append(
            "| " + act_key + " | " + str(t["scenes"]) + " | "
            + str(t["beats"]) + " | " + str(t["stubs"]) + " | "
            + str(t["renders"]) + " | ~" + str(est_target) + " |"
        )
    out.append("")

    # Summary
    out.append("## Summary")
    out.append("")
    out.append("| Category | Total | Present | Missing |")
    out.append("|---|---|---|---|")
    p_total = len(portraits)
    p_present = sum(1 for _, _, p, _ in portraits if os.path.exists(p))
    out.append("| Character portraits | " + str(p_total) + " | " + str(p_present) + " | " + str(p_total - p_present) + " |")
    t_total = len(scenes)
    t_present = sum(
        1 for sid, _, _, _ in scenes if os.path.exists("images/ui/gallery/" + sid + ".png")
    )
    out.append("| Gallery thumbnails | " + str(t_total) + " | " + str(t_present) + " | " + str(t_total - t_present) + " |")
    out.append("| Scene backgrounds | " + str(len(bg_refs)) + " | — | — |")
    a_total = len(audio_refs)
    a_present = sum(1 for p in audio_refs if os.path.exists(p))
    out.append("| Audio files | " + str(a_total) + " | " + str(a_present) + " | " + str(a_total - a_present) + " |")
    out.append("")
    out.append("---")
    out.append("")
    out.append("_Regenerate with `python3 tools/gen_asset_manifest.py`_")

    manifest_path = "game/data/asset_manifest.md"
    os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
    with open(manifest_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(out) + "\n")

    print("Wrote " + manifest_path)
    print(
        "Portraits: "
        + str(p_total)
        + ", Thumbnails: "
        + str(t_total)
        + ", Backgrounds: "
        + str(len(bg_refs))
        + ", Audio: "
        + str(a_total)
    )


if __name__ == "__main__":
    write_manifest()
