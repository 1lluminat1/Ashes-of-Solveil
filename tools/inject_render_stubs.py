#!/usr/bin/env python3
# =============================================================================
# Render stub injector for Ashes of Solveil
# -----------------------------------------------------------------------------
# Walks a single scene .rpy file and inserts commented `# scene <tag>` stubs
# at the start of each "beat cluster" — a run of N consecutive dialogue lines
# that share a single rendered background.
#
# Design assumptions (per workflow discussion 2026-04):
#
#   - One render per cluster of ~3 dialogue beats by default
#   - Renders live in images/bg/<scene_id>/<NNN>.png
#     (auto-registered at init by game/systems/bg_autoregister.rpy)
#   - Scene statements use the `scene` keyword (not `show`)
#   - Default transition is `with dissolve`
#   - Stubs are inserted commented out — uncomment when the render lands
#
# Cluster boundaries:
#   1. Every N beats (configurable via --cluster, default 3)
#   2. Section-header comments (# CAMERA:, # LIGHTING:, # ====, etc.)
#   3. menu:, label :, if / elif / else: blocks
#   4. call / jump statements
#
# Usage:
#   python3 tools/inject_render_stubs.py <scene_id>
#   python3 tools/inject_render_stubs.py <scene_id> --cluster 2
#   python3 tools/inject_render_stubs.py <scene_id> --dry-run
#   python3 tools/inject_render_stubs.py <scene_id> --undo
#   python3 tools/inject_render_stubs.py <scene_id> --force
#
# Examples:
#   python3 tools/inject_render_stubs.py a1_s06_gala
#   python3 tools/inject_render_stubs.py a4_s19_tessa_the_trainee_ob --cluster 2
#
# Arguments:
#   scene_id   Either the Ren'Py label/filename root (e.g. "a1_s06_gala") or
#              a full path (e.g. "game/act1/a1_s06_gala.rpy"). The tool
#              resolves both.
#
# Flags:
#   --cluster N   Beats per cluster before forcing a new stub. Default: 3.
#   --dry-run     Print the patch preview without writing.
#   --undo        Remove all render stubs injected by this tool. Idempotent.
#   --force       Re-inject stubs even if some already exist (runs undo first).
# =============================================================================

import argparse
import glob
import os
import re
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ---- regexes ---------------------------------------------------------------

# Line that introduces a dialogue / narration beat.
# Matches bare narration ("...") and speaker-prefixed ("l ...", "athought ...")
# but NOT comments, python statements, or keywords.
SAY_PAT = re.compile(r'^(\s*)([a-z_][a-z_0-9]*\s+)?"[^"]')

# Lines that should force a cluster reset BEFORE they are written.
RESET_COMMENT_PAT = re.compile(
    r'^\s*#\s*(CAMERA|LIGHTING|VISUAL|SFX|SOUND|FX|COMP|BLOCKING|FACE|PROP|NOTE|STAGE|={2,}|-{2,}|\*{2,})',
    re.IGNORECASE,
)

RESET_CONTROL_PAT = re.compile(
    r'^\s*(menu:|label\s+\w+:|if\s+|elif\s+|else:|jump\s+\w+|call\s+\w+)'
)

# Existing stubs we inject (so --undo can remove them).
# The marker trails the stub so we know it came from this tool.
STUB_MARKER = "# @render_stub"
STUB_PAT = re.compile(r'^\s*#\s*scene\s+\S+\s+with\s+\w+\s+' + re.escape(STUB_MARKER) + r'\s*$')


# ---- helpers ---------------------------------------------------------------

def resolve_scene_path(scene_arg: str) -> str:
    """Return absolute path to the .rpy file for a given scene arg.

    Accepts:
        a1_s06_gala           → search game/act*/a1_s06_gala.rpy
        game/act1/a1_s06_gala.rpy
    """
    if scene_arg.endswith(".rpy") and os.path.exists(scene_arg):
        return os.path.abspath(scene_arg)
    if scene_arg.endswith(".rpy") and os.path.exists(os.path.join(REPO_ROOT, scene_arg)):
        return os.path.abspath(os.path.join(REPO_ROOT, scene_arg))

    # Search all act folders for a matching filename
    candidates = glob.glob(os.path.join(REPO_ROOT, "game", "act*", scene_arg + ".rpy"))
    if candidates:
        return candidates[0]
    candidates = glob.glob(os.path.join(REPO_ROOT, "game", "act*", "*" + scene_arg + "*.rpy"))
    if len(candidates) == 1:
        return candidates[0]
    if len(candidates) > 1:
        sys.exit(
            "Multiple matches for '" + scene_arg + "':\n  "
            + "\n  ".join(candidates)
            + "\nBe more specific."
        )
    sys.exit("No scene file found for '" + scene_arg + "'.")


def scene_id_from_path(path: str) -> str:
    return os.path.splitext(os.path.basename(path))[0]


def is_dialogue_beat(line: str) -> bool:
    return SAY_PAT.match(line) is not None


def is_cluster_reset(line: str) -> bool:
    return bool(RESET_COMMENT_PAT.match(line) or RESET_CONTROL_PAT.match(line))


def is_existing_stub(line: str) -> bool:
    return bool(STUB_PAT.match(line))


def get_indent(line: str) -> str:
    m = re.match(r"^(\s*)", line)
    return m.group(1) if m else ""


# ---- core ------------------------------------------------------------------

def inject(scene_path: str, cluster_size: int = 3, dry_run: bool = False,
           transition: str = "dissolve") -> int:
    """Inject render stubs into the given scene file.

    Returns the number of stubs inserted.
    """
    scene_id = scene_id_from_path(scene_path)
    with open(scene_path, encoding="utf-8") as fh:
        lines = fh.readlines()

    out = []
    beat_num = 0
    cluster_count = 0
    in_label = False
    inserted = 0

    for line in lines:
        stripped = line.lstrip()

        if stripped.startswith("label "):
            in_label = True
            out.append(line)
            continue

        if not in_label:
            out.append(line)
            continue

        # Cluster reset triggers (before writing the line)
        if is_cluster_reset(line):
            cluster_count = 0
            out.append(line)
            continue

        # Dialogue beat → maybe inject stub before it
        if is_dialogue_beat(line):
            if cluster_count == 0:
                beat_num += 1
                indent = get_indent(line)
                tag = scene_id + "_" + str(beat_num).zfill(3)
                stub = (
                    indent
                    + "# scene " + tag
                    + " with " + transition
                    + " " + STUB_MARKER + "\n"
                )
                out.append(stub)
                inserted += 1

            cluster_count += 1
            if cluster_count >= cluster_size:
                cluster_count = 0

            out.append(line)
            continue

        # Otherwise just pass through
        out.append(line)

    if dry_run:
        # Show a diff-style preview
        sys.stdout.write("--- " + scene_path + "\n")
        sys.stdout.write("+++ (with stubs, cluster=" + str(cluster_size) + ")\n")
        for i, new_line in enumerate(out):
            if STUB_MARKER in new_line:
                sys.stdout.write("+ " + new_line)
        sys.stdout.write("\nWould insert " + str(inserted) + " stubs.\n")
        return inserted

    with open(scene_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.writelines(out)
    return inserted


def undo(scene_path: str, dry_run: bool = False) -> int:
    """Remove all render stubs that this tool previously injected."""
    with open(scene_path, encoding="utf-8") as fh:
        lines = fh.readlines()

    out = [ln for ln in lines if not is_existing_stub(ln)]
    removed = len(lines) - len(out)

    if dry_run:
        sys.stdout.write("Would remove " + str(removed) + " stubs from " + scene_path + "\n")
        return removed

    with open(scene_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.writelines(out)
    return removed


def existing_stub_count(scene_path: str) -> int:
    with open(scene_path, encoding="utf-8") as fh:
        return sum(1 for ln in fh if is_existing_stub(ln))


# ---- cli -------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Inject or remove render stubs in an Ashes of Solveil scene file."
    )
    ap.add_argument("scene", help="Scene ID (a1_s06_gala) or path (game/act1/a1_s06_gala.rpy)")
    ap.add_argument("--cluster", type=int, default=3,
                    help="Beats per cluster before forcing a new stub. Default 3.")
    ap.add_argument("--transition", default="dissolve",
                    help="Transition suffix for each stub. Default: dissolve")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print the patch preview without writing to the file.")
    ap.add_argument("--undo", action="store_true",
                    help="Remove all render stubs injected by this tool.")
    ap.add_argument("--force", action="store_true",
                    help="Re-inject stubs, removing any existing ones first.")
    args = ap.parse_args()

    scene_path = resolve_scene_path(args.scene)
    scene_id = scene_id_from_path(scene_path)

    if args.undo:
        n = undo(scene_path, dry_run=args.dry_run)
        if not args.dry_run:
            print("Removed " + str(n) + " stubs from " + scene_id)
        return

    existing = existing_stub_count(scene_path)
    if existing and not args.force:
        print(
            "Scene '" + scene_id + "' already has " + str(existing)
            + " render stubs. Use --force to re-inject or --undo to remove."
        )
        return

    if args.force and existing:
        removed = undo(scene_path, dry_run=args.dry_run)
        if not args.dry_run:
            print("Removed " + str(removed) + " existing stubs from " + scene_id)

    inserted = inject(
        scene_path,
        cluster_size=args.cluster,
        dry_run=args.dry_run,
        transition=args.transition,
    )
    if not args.dry_run:
        print(
            "Injected " + str(inserted) + " render stubs into " + scene_id
            + " (cluster=" + str(args.cluster) + ", transition=" + args.transition + ")"
        )
        print("Renders expected at images/bg/" + scene_id + "/001.png through "
              + str(inserted).zfill(3) + ".png")


if __name__ == "__main__":
    main()
