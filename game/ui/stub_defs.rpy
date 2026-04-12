# ================================================================
# STUB DEFINITIONS — character aliases + placeholder images
# File: game/ui/stub_defs.rpy
# ----------------------------------------------------------------
# Quality-of-life shims so the project compiles cleanly under
# Ren'Py lint while the authoring layer catches up:
#
#   1) Character aliases — scenes were written using long-form
#      speaker names (`marcus`, `cade`, `mira`, `recruit`, etc.)
#      that were never defined centrally. We map them here to
#      existing Character objects or build new ones.
#
#   2) Stub background images — scenes reference bg_* tags that
#      don't have real plates yet. We register color-block
#      placeholders so `scene bg_foo_bar` doesn't fail lint.
#
# Delete any line in here once the real asset / definition lands.
# ================================================================


# ----------------------------------------------------------------
# Character aliases
# ----------------------------------------------------------------
# `marcus` is the long-form speaker name used by some scenes for
# readability. Hardcoded color hex here to sidestep init ordering
# against ui_solveil.rpy — stub_defs loads first alphabetically.
# Value matches color_marcus in ui_solveil.rpy; keep them in sync.
define marcus = Character("General Marcus Rylan", color="#7A3B3F")

# One-off speakers used in Act 1-3 NPC beats. These were inlined
# by writers without a central define; gather them here so every
# scene resolves without scattering per-file defines.
define cade       = Character("Cade", color="#9FB6C5")
define mira       = Character("Mira", color="#C6AD85")
define recruit    = Character("Recruit", color="#A8B6C2")
define officer    = Character("Officer", color="#B07070")
define guard      = Character("Guard", color="#7A8C9E")
define worker     = Character("Worker", color="#A8A070")
define qm         = Character("Quartermaster", color="#8E9DB0")
define jr         = Character("Junior Recruit", color="#A0B0C0")
define li         = Character("Lieutenant", color="#9A8FB5")
define o          = Character("Operator", color="#8BA2B8")
define unknown          = Character("???", color="#909090")
define unknown_female   = Character("???", color="#A89090")

# Recruit-internal thought (matches the l/z/t/n *thought convention).
define rthought   = Character("Recruit",
    color="#A8B6C2",
    what_style="athought_text")


# ----------------------------------------------------------------
# Stub background images
# ----------------------------------------------------------------
# Until plate renders land, register a cold gray/black Solid for
# each missing bg_ tag the lint flagged. `scene bg_foo` will then
# render a placeholder instead of erroring out.
#
# NOTE: Real plates should replace these by dropping PNG/WebP files
# into images/bg/ and removing the matching stub image line.
# ----------------------------------------------------------------

image bg_aeron_room_night       = Solid("#0B0F16")
image bg_aeron_apartment        = Solid("#12171F")
image bg_medbay_corridor_night  = Solid("#0C1218")
image bg_selene_quarters_night  = Solid("#111821")
image bg_zira_alcove_night      = Solid("#0E1218")
image bg_zira_alcove_after      = Solid("#161C24")
