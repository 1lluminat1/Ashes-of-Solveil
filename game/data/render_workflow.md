# Render Workflow Guide

How to scaffold, render, and wire visual backgrounds for *Ashes of Solveil*
scene by scene. This is the guide — the live numbers and per-scene checklist
live in [`asset_manifest.md`](asset_manifest.md) next to this file
(regenerated on demand via `python3 tools/gen_asset_manifest.py`).

---

## 1. The workflow this guide assumes

*Ashes of Solveil* uses a **pre-baked scene** approach:

- **No character sprites.** The game never calls `show lyra happy` or similar.
- **Each render is a full composition.** Background + any characters are
  already posed and staged at render time.
- **One scene file → one folder of renders.** Every scene has its own
  `images/bg/<scene_id>/` folder.
- **Cluster-based rendering.** One render covers a cluster of roughly
  2–3 dialogue beats. The same render holds while a character monologues
  for a few lines; the next cluster gets a fresh render with slightly
  different pose / eyes / hands so the scene feels animated without
  requiring a unique frame per line.
- **The `scene` keyword.** Backgrounds switch via `scene <tag> with dissolve`,
  not `show`.
- **Auto-registration.** Dropping a file into the right folder is all
  it takes to make it renderable — no manual `image` definitions.

---

## 2. Current render budget (baseline)

At `--cluster 3` (default), the estimated render count across all Acts 1–4:

| Act  | Scenes | Dialogue beats | Est. renders |
|------|--------|----------------|--------------|
| act1 | 30     | 2,463          | ~821         |
| act2 | 30     | 4,232          | ~1,410       |
| act3 | 51     | 6,337          | ~2,112       |
| act4 | 54     | 10,291         | ~3,430       |
| **Total** | **165** | **23,323** | **~7,770** |

This is the upper bound if every scene gets fully scaffolded and every
stub gets a unique frame. In practice the real number comes in lower
because many beats reuse earlier backgrounds — a character can talk for
five lines on one render if the pose doesn't need to change. **Expect
the realised count to drop 20–40% below the baseline as you render.**

### Tuning the baseline

Run the injector with a different cluster size per scene:

- `--cluster 2` → denser, ~50% more renders, use for high-action or
  physicality-heavy scenes where pose changes rapidly
- `--cluster 3` → default, matches the "2-3 dialogue lines per pose" rule
- `--cluster 5` → sparser, ~40% fewer renders, use for static interiors
  or long dialogue passages with a fixed tableau

Regenerate the manifest (`python3 tools/gen_asset_manifest.py`) after
any bulk change to see the new budget.

---

## 3. Folder convention

```
images/
└── bg/
    ├── a1_s01_branding/
    │   ├── 001.png
    │   ├── 002.png
    │   └── ...
    ├── a1_s02_bedroom/
    │   └── ...
    └── ...
```

- One folder per scene, named exactly after the scene file's stem
  (the `.rpy` filename without extension).
- Numbered PNG files, zero-padded to three digits: `001.png`, `002.png`,
  up to however many renders the scene needs. (`.jpg`, `.jpeg`, and
  `.webp` are also accepted.)
- `game/systems/bg_autoregister.rpy` walks this tree at init time and
  registers every file as a Ren'Py image named `<scene_id>_<beat>` —
  for example, `a1_s06_gala/047.png` becomes the tag `a1_s06_gala_047`.

### Why folder-per-scene

- Renders stay physically grouped during production
- Easy to back up, share, or re-render one scene without touching others
- Matches the `scene_id` key everywhere else in the project
  (codex entries, character profiles, gallery data, script flow)

---

## 4. The injector tool

**Location:** `tools/inject_render_stubs.py`

**Purpose:** Insert commented `# scene <scene_id>_NNN with dissolve`
placeholders at each cluster boundary inside a scene file, so you can
uncomment them one by one as matching renders land.

### Basic usage

```bash
python3 tools/inject_render_stubs.py <scene_id>
```

Where `<scene_id>` is the filename stem (e.g. `a1_s06_gala`) or a full
path (e.g. `game/act1/a1_s06_gala.rpy`). The tool searches all act
directories for a match.

### Flags

| Flag | Default | Effect |
|---|---|---|
| `--cluster N` | 3 | Beats per cluster before forcing a new stub |
| `--transition X` | dissolve | Transition keyword appended to each stub |
| `--dry-run` | off | Print the preview, don't write anything |
| `--undo` | off | Remove every stub previously injected by this tool |
| `--force` | off | Wipe existing stubs and re-inject from scratch |

### Examples

```bash
# Preview what would happen without touching the file
python3 tools/inject_render_stubs.py a1_s06_gala --dry-run

# Scaffold the gala scene with default cluster=3
python3 tools/inject_render_stubs.py a1_s06_gala

# Re-scaffold with tighter clusters
python3 tools/inject_render_stubs.py a1_s06_gala --force --cluster 2

# Remove all stubs from the breaking point scene
python3 tools/inject_render_stubs.py a1_s17_breaking_point --undo
```

### Cluster reset rules

The injector starts a new stub at the first of these triggers:

1. **N consecutive dialogue beats** have been recorded (default N=3)
2. A **section-header comment** is encountered:
   `# CAMERA:`, `# LIGHTING:`, `# VISUAL:`, `# SFX:`, `# SOUND:`,
   `# FX:`, `# COMP:`, `# BLOCKING:`, `# FACE:`, `# PROP:`, `# NOTE:`,
   `# STAGE`, `# ====`, `# ----`, `# ****`
3. A **control-flow statement** starts a new branch:
   `menu:`, `label:`, `if`, `elif`, `else:`, `jump`, `call`

So if a scene has a four-line monologue followed by a `# LIGHTING:`
comment and another four lines, you get two stubs — one per
visually-distinct section — even though each section is under the
cluster cap.

### The `@render_stub` sentinel

Every injected line has a trailing `# @render_stub` marker, e.g.:

```
# scene a1_s06_gala_047 with dissolve # @render_stub
```

`--undo` uses this sentinel to find and remove only the lines the tool
injected. Hand-written `# scene` lines stay safe.

When you uncomment a stub to wire a real render, feel free to strip
the `# @render_stub` tag too — the tool won't try to `--undo` it
afterward, but it's cleaner:

```
scene a1_s06_gala_047 with dissolve
```

---

## 5. The asset manifest

**Location:** `game/data/asset_manifest.md` — regeneratable anytime via:

```bash
python3 tools/gen_asset_manifest.py
```

The manifest has five sections:

1. **Character Portraits** — 10 portrait slots (6 LIs + 4 supporting)
2. **Scene Gallery Thumbnails** — 21 replay gallery thumbs
3. **Scene Backgrounds** — every `bg_*` tag currently referenced in script
4. **Audio** — every `play music/sound/ambient` reference
5. **Per-Scene Render Budget** — the main production tracker (see below)

### Reading the Per-Scene Render Budget table

```
| Scene         | Beats | Stubs | Renders | % | Status      |
|---------------|-------|-------|---------|---|-------------|
| a1_s06_gala   | 126   | 0     | 0       | 0%  | ⬜ not started |
| a1_s07_balcony| 129   | 43    | 12      | 28% | 🔄 in progress |
| a1_s26_bridge | 157   | 52    | 52      | 100%| ✅ complete    |
```

Columns:

- **Beats** — dialogue / narration lines inside the scene's label
- **Stubs** — how many `@render_stub` lines the injector has inserted
- **Renders** — how many real image files are in `images/bg/<scene_id>/`
- **%** — `renders / stubs` if scaffolded, else `renders / (beats/3)`
  as an estimate
- **Status** — automatically derived:
  - ⬜ **not started** — no stubs, no renders
  - 📋 **scaffolded** — stubs exist but no renders yet
  - 🔄 **in progress** — some renders landed, still less than target
  - ✅ **complete** — renders match or exceed target

Per-act totals at the bottom of the section show aggregate progress
across all scenes in each act.

### Regenerate after every batch

Every time you:

- Run the injector on a new scene
- Drop new renders into an `images/bg/<scene_id>/` folder
- Write or edit scene dialogue

…re-run `python3 tools/gen_asset_manifest.py` and the status markers
flip automatically.

---

## 6. Step-by-step per-scene workflow

Typical production loop for one scene:

### Step 1 — Scaffold the scene

```bash
python3 tools/inject_render_stubs.py a1_s06_gala
```

Console output tells you how many stubs were inserted and where the
renders are expected to live.

### Step 2 — Open the scene file

`game/act1/a1_s06_gala.rpy` now has commented `# scene` lines at
each cluster boundary. Read through it once, noting where each stub
lands relative to the dialogue. If a cluster boundary feels wrong
(too tight / too sparse), run `--undo` and re-inject at a different
cluster size.

### Step 3 — Render the first beat

Set up your render tool (HS2, DAZ, Koikatsu, whatever). Stage the scene
as it's described in the file's stage directions (CAMERA / LIGHTING /
BLOCKING comments). Render the first frame and save it as:

```
images/bg/a1_s06_gala/001.png
```

### Step 4 — Uncomment the first stub

Open `a1_s06_gala.rpy`, find the first `# scene a1_s06_gala_001` line,
and uncomment it:

```
scene a1_s06_gala_001 with dissolve
```

Optional: strip the `# @render_stub` tail for cleanliness.

### Step 5 — Verify in-engine

Launch Ren'Py and play up to this scene. The `bg_autoregister.rpy`
helper picks up your new file automatically — no `image` definition
needed. The scene should render your image behind the dialogue.

If Ren'Py says "image not found":

- Double-check the filename matches (zero-padding matters: `001`, not `1`)
- Make sure the folder name exactly matches the scene's `scene_id`
- Verify the file is under `images/bg/` (not `images/`)

### Step 6 — Repeat through the scene

Stub by stub, render → drop in folder → uncomment. You can do them
out of order — a scene with stubs 001–043 can have 007, 012, 019
rendered first if those are the easiest shots.

### Step 7 — Track progress

After each batch:

```bash
python3 tools/gen_asset_manifest.py
```

Open `game/data/asset_manifest.md` and check the "Per-Scene Render
Budget" section. The scene's status should flip from 📋 to 🔄 as
renders accumulate, and 🔄 to ✅ when it's done.

---

## 7. Reuse strategy

**The 8k total is the ceiling, not the floor.** In practice:

- **Same pose, multiple lines.** A character holds a pose for 3–5 lines
  → one render, multiple stubs uncommented to the same filename.
  That's not a bug; stubs can share a filename if the pose is held.
- **Micro-variants.** Render one "base" pose, then two variants with
  slight mouth / eye / arm changes. Use them in rotation through a
  long dialogue block so the scene feels animated without rendering
  per line.
- **Scene-level backgrounds.** A conversation in the cathedral
  might use 15 different character poses but reuse the same two
  cathedral wides between them. You can register those wides once
  and leave character-pose renders to handle the action beats.
- **Mirror-the-cluster reuse.** If two scenes happen in the same
  location, copy the relevant base renders between `images/bg/<a>/`
  and `images/bg/<b>/` — each scene stays self-contained but the
  renders themselves are reused.

A realistic final render count is probably **4,500–6,000** once you
apply aggressive reuse. That's a lot of renders but it's the right
order of magnitude for a ~23,000-word VN.

---

## 8. Naming conventions reference

| Thing | Pattern | Example |
|---|---|---|
| Scene file | `a<act>_s<num>[a-z]_<slug>[_<path>].rpy` | `a4_s19_tessa_the_trainee_ob.rpy` |
| Scene ID | same as file stem | `a4_s19_tessa_the_trainee_ob` |
| Render folder | `images/bg/<scene_id>/` | `images/bg/a4_s19_tessa_the_trainee_ob/` |
| Render file | `<NNN>.<ext>` | `047.png` |
| Auto-generated image tag | `<scene_id>_<NNN>` | `a4_s19_tessa_the_trainee_ob_047` |
| Injector stub | `# scene <tag> with dissolve # @render_stub` | — |
| Uncommented stub | `scene <tag> with dissolve` | — |

---

## 9. Troubleshooting

**The injector says "Scene already has N stubs".**
You've already run the tool on this scene. Use `--force` to wipe and
re-inject, or `--undo` to start over clean.

**Ren'Py says "not an image" when I uncomment a stub.**
The render file isn't in the expected folder, or the filename doesn't
match. Double-check the `images/bg/<scene_id>/NNN.png` path and that
the file actually exists. `bg_autoregister.rpy` runs at init so you
need to reload the game after adding new files.

**The stub indent looks wrong.**
The injector copies indent from the dialogue beat it's precede. If
a scene uses unusual indentation (e.g., nested inside `with` blocks),
the stub will match. If it's genuinely wrong, use `--undo` and edit
the file by hand — the stubs are just comments, so hand-placing them
works fine.

**I want stubs in a commented-out control-flow branch that the injector skipped.**
The injector only processes lines inside the `label:` body. Nested
`if` branches still get stubs (one per branch's first beat). If you
have a truly dead code path that the injector skipped, add stubs
manually — they're just comment lines.

**I want to share base renders across scenes.**
Either copy the file between `images/bg/<a>/` and `images/bg/<b>/`
(simplest), or register a shared image by hand in a small `.rpy`
file and use that tag directly in the `scene` statement instead of
the auto-generated per-scene tag. The manifest won't track the
manual reference but the scene will work.

---

## 10. Ship checklist

When every scene you care about hits ✅ complete in the manifest:

1. `python3 tools/gen_asset_manifest.py` one more time to lock in
   the numbers
2. Confirm the Per-Act Render Totals table shows the renders-present
   count matching the stubs-injected count for every act
3. `renpy.exe . lint` — clean lint pass
4. Sanity-playtest at least one scene per act and verify backgrounds
   actually switch on beat

At that point the scripts are fully wired to their art and the build
is one Ren'Py export away from a playable release.

---

_Regenerate this guide's numbers section by running the manifest
generator. This file itself is hand-maintained — edit it when the
workflow evolves._
