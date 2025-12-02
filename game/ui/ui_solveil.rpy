# === ASHES OF SOLVEIL — UI THEME + FONTS + CHARACTERS + ACT HELPERS ===
# Single source of truth for:
# - Font registrations
# - Text styles (narration, centered, thoughts, choice text, system text)
# - Character colors (early/late) + Character objects
# - Act management helpers (set_act, late color update, color lookup)
# - Solveil palette helpers (used by the custom screens)

# -------------------------------
# FONT FILE DEFINITIONS
# -------------------------------
define gui.text_font = "fonts/Exo2-Regular.ttf"            # 400
define gui.name_font = "fonts/Exo2-Medium.ttf"             # 500
define gui.interface_font = "fonts/Exo2-Regular.ttf"       # 400
define gui.choice_button_text_font = "fonts/Exo2-SemiBold.ttf"  # 600
define gui.thin_font = "fonts/Exo2-Light.ttf"              # 200

define gui.narration_font = "fonts/SourceSerif4-Light.ttf"
define gui.narration_italic_font = "fonts/SourceSerif4-LightItalic.ttf"

define gui.system_font = "fonts/ShareTechMono-Regular.ttf"

# -------------------------------
# FONT SIZE DEFINITIONS
# -------------------------------
define gui.text_size = 24
define gui.name_text_size = 28
define gui.interface_text_size = 22
define gui.label_text_size = 32
define gui.notify_text_size = 20
define gui.title_text_size = 72

# -------------------------------
# TEXT STYLES
# -------------------------------

## NARRATION (Third-person, regular - NOT italic)
style narrator:
    font "fonts/SourceSerif4-Light.ttf"
    size 22
    color "#D4D9E0"
    line_spacing 10

## INTERNAL VO TEXT STYLES (inherit positioning from say_dialogue)
style athought_text is say_dialogue:
    font "fonts/Exo2-Italic.ttf"

style lthought_text is say_dialogue:
    font "fonts/Exo2-Italic.ttf"

style zthought_text is say_dialogue:
    font "fonts/Exo2-Italic.ttf"

style tthought_text is say_dialogue:
    font "fonts/Exo2-Italic.ttf"

style selenethought_text is say_dialogue:
    font "fonts/Exo2-Italic.ttf"

style nthought_text is say_dialogue:
    font "fonts/Exo2-Italic.ttf"

style mthought_text is say_dialogue:
    font "fonts/Exo2-Italic.ttf"

style yathought_text is say_dialogue:
    font "fonts/Exo2-Italic.ttf"

style ylthought_text is say_dialogue:
    font "fonts/Exo2-Italic.ttf"

style kthought_text is say_dialogue:
    font "fonts/Exo2-Italic.ttf"

## CENTERED TEXT
style centered:
    font "fonts/SourceSerif4-LightItalic.ttf"
    size 22
    color "#D4D9E0"
    line_spacing 10
    italic True
    text_align 0.5
    xalign 0.5

## CHOICE BUTTON TEXT
style choice_button_text:
    font "fonts/Exo2-SemiBold.ttf"
    size 22
    color "#C0C5CE"
    hover_color "#EDF1F5"

## SYSTEM TEXT
style system_text:
    font "fonts/ShareTechMono-Regular.ttf"
    size 18
    color "#5A7A99"

# -------------------------------
# CHARACTER COLORS
# -------------------------------

## MAIN CHARACTERS - Early Game Colors
define color_aeron_early = "#B8B8A8"
define color_lyra_early = "#C8A2FF"
define color_zira = "#5FE3FF"
define color_tessa_early = "#80C37A"
define color_selene = "#C1B8A8"
define color_noelle = "#9C87C9"

## SUPPORTING CHARACTERS
define color_marcus = "#7A3B3F"
define color_young_aeron = "#A2C5da"
define color_young_lyra = "#D5C8CD"
define color_kael = "#A48E8A"

## MAIN CHARACTERS - Late Game Colors (Acts IV-V)
define color_aeron_late = "#D4C8A8"
define color_lyra_late = "#E8D8FF"
define color_tessa_late = "#A8D89C"

# -------------------------------
# CHARACTER OBJECTS
# -------------------------------

## Main Cast
define a = Character("Aeron", color=color_aeron_early)
define l = Character("Lyra", color=color_lyra_early)
define z = Character("Zira", color=color_zira)
define t = Character("Tessa", color=color_tessa_early)
define selene = Character("Selene", color=color_selene)
define n = Character("Noelle", color=color_noelle)

## Supporting Characters
define m = Character("General Marcus Rylan", color=color_marcus)
define ya = Character("Young Aeron", color=color_young_aeron)
define yl = Character("Young Lyra", color=color_young_lyra)
define k = Character("Kael", color=color_kael)

# -------------------------------
# INTERNAL VO CHARACTERS (thoughts)
# -------------------------------
define athought = Character("Aeron",
    color=color_aeron_early,
    what_style="athought_text")

define lthought = Character("Lyra",
    color=color_lyra_early,
    what_style="lthought_text")

define zthought = Character("Zira",
    color=color_zira,
    what_style="zthought_text")

define tthought = Character("Tessa",
    color=color_tessa_early,
    what_style="tthought_text")

define selenethought = Character("Selene",
    color=color_selene,
    what_style="selenethought_text")

define nthought = Character("Noelle",
    color=color_noelle,
    what_style="nthought_text")

define mthought = Character("General Marcus Rylan",
    color=color_marcus,
    what_style="mthought_text")

define yathought = Character("Young Aeron",
    color=color_young_aeron,
    what_style="yathought_text")

define ylthought = Character("Young Lyra",
    color=color_young_lyra,
    what_style="ylthought_text")

define kthought = Character("Kael",
    color=color_kael,
    what_style="kthought_text")

# -------------------------------
# ACT MANAGEMENT + COLOR UPDATES
# -------------------------------
init python:
    # Track current act & path (if not already defined elsewhere)
    if "current_act" not in globals():
        current_act = 1
    if "path_state" not in globals():
        path_state = "DT"  # "OB" | "EMP" | "DT"

    def set_act(act_num):
        """Change to a new act."""
        global current_act
        current_act = int(act_num)

    def update_character_colors_late_game():
        """Call this when transitioning to Acts IV-V to warm key colors."""
        a.color = color_aeron_late
        l.color = color_lyra_late
        t.color = color_tessa_late
        athought.color = color_aeron_late
        lthought.color = color_lyra_late
        tthought.color = color_tessa_late

    def get_character_color(char_name):
        """Helper function to get character color by name."""
        color_map = {
            "Aeron": a.color,
            "Lyra": l.color,
            "Zira": z.color,
            "Tessa": t.color,
            "Selene": selene.color,
            "Noelle": n.color,
            "General Marcus Rylan": m.color,
            "Young Aeron": ya.color,
            "Young Lyra": yl.color,
            "Kael": k.color,
        }
        return color_map.get(char_name, "#C0C5CE")

# -------------------------------
# SOLVEIL PALETTE (for screens)
# -------------------------------
init python:
    UI_PALETTE = {
        1: dict(
            bg="#0A0E14", text="#C0C5CE", accent="#3D4C5F", highlight="#5A7A99",
            name="#8FA6B8", box_bg="#0F1419", box_border="#3D4C5F",
            choice_idle="#1A2332", choice_hover="#3D4C5F",
            radius=0, padding=40
        ),
        2: dict(
            bg="#0D1117", text="#C8CDD3", accent="#4A5A6F", highlight="#6B8CAF",
            name="#C8CDD3", box_bg="#121820", box_border="#4A5A6F",
            choice_idle="#1C2330", choice_hover="#4A5A6F",
            radius=1, padding=42
        ),
        3: dict(
            bg="#111822", text="#D4D9E0", accent="#5A6B7F", highlight="#7FA3C9",
            name="#D4D9E0", box_bg="#111822", box_border="#5A6B7F",
            choice_idle="#1E2632", choice_hover="#5A6B7F",
            radius=4, padding=44
        ),
        4: dict(
            bg="#151D28", text="#E0E4EA", accent="#6B7D92", highlight="#94B8D6",
            name="#E0E4EA", box_bg="#151D28", box_border="#6B7D92",
            choice_idle="#202834", choice_hover="#6B7D92",
            radius=8, padding=46
        ),
        5: dict(
            bg="#1A2530", text="#EDF1F5", accent="#7A8FA5", highlight="#B0CFE8",
            name="#EDF1F5", box_bg="#1A2530", box_border="#7A8FA5",
            choice_idle="#22303C", choice_hover="#7A8FA5",
            radius=12, padding=48
        ),
    }

    def ui_current():
        """Act palette with subtle path deltas."""
        pal = UI_PALETTE.get(current_act, UI_PALETTE[1]).copy()
        if path_state == "OB":
            pal["radius"] = max(0, pal["radius"] - 2)
        elif path_state == "EMP":
            pal["radius"] = min(12, pal["radius"] + 2)
        return pal
