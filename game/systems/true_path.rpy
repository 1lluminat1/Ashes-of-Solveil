# =======================================================
# TRUE PATH SYSTEM — Helper Functions & State
# File: game/systems/true_path.rpy
# =======================================================
# This file implements the True Path hidden overlay system.
# True Path is a mirror that reflects what the player has been
# consistently doing — not a third route, but a recognition
# of integration between EMP and OB impulses.
#
# Core motif: "It's not fate. It's a mirror."
# =======================================================

init -1 python:
    import time as _time

    # ========= TRUE PATH STATE INITIALIZATION =========
    # These are initialized in the main STATE dict elsewhere,
    # but we define defaults here for safety.

    def tp_init():
        """Initialize True Path state variables if not present."""
        if "true_path" not in STATE:
            STATE["true_path"] = False
        if "tp_depth" not in STATE:
            STATE["tp_depth"] = 0

        # Ensure metrics exist
        for key in ["truth_shards", "tp_emergence_count",
                     "tp_integration", "tp_narrator_ack", "consistency"]:
            if key not in STATE.get("metrics", {}):
                if "metrics" not in STATE:
                    STATE["metrics"] = {}
                STATE["metrics"][key] = 0

    # ========= TRUE PATH SEED (Early Game) =========

    def tp_seed(tag, value=1):
        """
        One-time True Path resonance increment. Idempotent.
        Used for early-game micro-moments that signal the player
        is willing to not suppress uncomfortable truths.

        Args:
            tag: Unique string identifier (e.g., "a1.hallway.wrist_show")
            value: Amount to increment truth_shards (default 1)
        """
        tp_init()
        key = "tp_seed_{}".format(tag)
        if not flag(key):
            flag(key, True)
            if "metrics" not in STATE:
                STATE["metrics"] = {}
            STATE["metrics"]["truth_shards"] = STATE["metrics"].get("truth_shards", 0) + value
            log_line("TP_SEED:{}:shards={}".format(tag, STATE["metrics"]["truth_shards"]))

    # ========= EMERGENCE MECHANIC =========

    def tp_emergence_found(scene_id):
        """
        Record that the player found a hidden Emergence option.
        Called when they select a third choice that appeared after
        waiting on a choice menu.

        Args:
            scene_id: The current scene ID string
        """
        tp_init()
        key = "tp_emergence_{}".format(scene_id)
        if not flag(key):
            flag(key, True)
            STATE["metrics"]["tp_emergence_count"] = STATE["metrics"].get("tp_emergence_count", 0) + 1
            STATE["metrics"]["truth_shards"] = STATE["metrics"].get("truth_shards", 0) + 1
            log_line("TP_EMERGENCE:{}:count={}".format(scene_id, STATE["metrics"]["tp_emergence_count"]))

    # ========= NARRATOR AWARENESS =========

    def tp_narrator_acknowledged(scene_id):
        """
        Record that the player acknowledged the narrator's partial truth
        ("Both of those things are true") instead of arguing (EMP)
        or merging (OB).

        Args:
            scene_id: The current scene ID string
        """
        tp_init()
        key = "tp_narrator_{}".format(scene_id)
        if not flag(key):
            flag(key, True)
            STATE["metrics"]["tp_narrator_ack"] = STATE["metrics"].get("tp_narrator_ack", 0) + 1
            STATE["metrics"]["truth_shards"] = STATE["metrics"].get("truth_shards", 0) + 1
            log_line("TP_NARRATOR:{}:ack={}".format(scene_id, STATE["metrics"]["tp_narrator_ack"]))

    # ========= INTEGRATION CHECKPOINTS =========

    def tp_integration_earned(scene_id):
        """
        Record that the player made a contextually justified cross-path
        choice at an Integration Checkpoint — choosing against their
        dominant path when the situation demanded it.

        Args:
            scene_id: The current scene ID string
        """
        tp_init()
        key = "tp_integration_{}".format(scene_id)
        if not flag(key):
            flag(key, True)
            STATE["metrics"]["tp_integration"] = STATE["metrics"].get("tp_integration", 0) + 1
            STATE["metrics"]["truth_shards"] = STATE["metrics"].get("truth_shards", 0) + 1
            log_line("TP_INTEGRATION:{}:count={}".format(scene_id, STATE["metrics"]["tp_integration"]))

    # ========= SILENCE MECHANIC =========

    def tp_silence_used(scene_id):
        """
        Record that the player refused to choose from borrowed voices
        at the council scene — let the timer expire without clicking.

        Args:
            scene_id: The current scene ID string
        """
        tp_init()
        if not flag("tp_silence_used"):
            flag("tp_silence_used", True)
            STATE["metrics"]["truth_shards"] = STATE["metrics"].get("truth_shards", 0) + 1
            log_line("TP_SILENCE:{}:used=True".format(scene_id))

    # ========= NAME MECHANIC =========

    def tp_name_typed(scene_id):
        """
        Record that the player typed "Aeron" into the invisible text field.

        Args:
            scene_id: The current scene ID string
        """
        tp_init()
        if not flag("tp_name_typed"):
            flag("tp_name_typed", True)
            STATE["metrics"]["truth_shards"] = STATE["metrics"].get("truth_shards", 0) + 1
            log_line("TP_NAME:{}:typed=True".format(scene_id))

    # ========= CODEX SEARCH HOOK =========

    def codex_search_hook(search_term, active_menu_id=None):
        """
        Called whenever the player searches the codex.
        Checks if the search term is relevant to a TP-gated menu.

        Args:
            search_term: The string the player searched for
            active_menu_id: The ID of the currently active choice menu, if any
        """
        tp_init()
        if active_menu_id == "harmony_core_decision":
            key_terms = ["verdant concordat", "concordat", "synchronization",
                         "resonance threshold", "viable conductor", "harmonize",
                         "verdant", "protocol verdant"]
            if search_term.lower().strip() in key_terms:
                flag("tp_codex_search_found", True)
                STATE["metrics"]["truth_shards"] = STATE["metrics"].get("truth_shards", 0) + 1
                log_line("TP_CODEX_SEARCH:term={}:found=True".format(search_term))

    # ========= TRUE PATH ACTIVATION =========
    # SHARD ECONOMY (9 moments total):
    #   REQUIRED (3): The Name (Act 3) + Codex Search (Act 4) + Mirror Choice (Act 4/5)
    #   OPTIONAL (6): Emergence x2 (Breaking Point, Depot Guard)
    #                  Silence x1 (Council Debate, Act 3)
    #                  Narrator Awareness x3 (various scenes)
    #   ACTIVATION: 5 of 9 required (3 required + 2 of 6 optional)
    #   DEPTH: 5-9 based on total moments engaged (affects post-activation content richness)

    def mirror_choice_available():
        """
        Check if the Mirror Choice's third option should appear.
        Requires: Name typed + Codex searched + 2 optional mechanics.
        Total: 5 of 9 moments across the game.
        """
        tp_init()
        # Required gates
        if not flag("tp_name_typed"):
            return False
        if not flag("tp_codex_search_found"):
            return False

        # Flexible requirement: at least 2 optional mechanics
        m = STATE["metrics"]
        optional_count = 0
        optional_count += min(2, m.get("tp_emergence_count", 0))  # Max 2 from Emergence
        if flag("tp_silence_used"):
            optional_count += 1                                    # Max 1 from Silence
        optional_count += min(3, m.get("tp_narrator_ack", 0))      # Max 3 from Narrator

        return optional_count >= 2

    def evaluate_true_path():
        """
        Primary activation: Called when the player selects the Mirror Choice.
        This should be called directly from the Mirror Choice label.
        """
        tp_init()
        STATE["true_path"] = True
        evaluate_true_path_depth()
        log_line("TP_ACTIVATED:depth={}".format(STATE["tp_depth"]))

    def evaluate_true_path_depth():
        """
        Calculate TP depth based on how many of the 9 moments
        the player engaged. Minimum is 5 (required to activate).
        """
        tp_init()
        m = STATE["metrics"]
        depth = 3  # Name + Codex + Mirror (always true if we're here)

        # Count optional mechanics engaged
        if m.get("tp_emergence_count", 0) >= 1:
            depth += 1
        if m.get("tp_emergence_count", 0) >= 2:
            depth += 1
        if flag("tp_silence_used"):
            depth += 1
        if m.get("tp_narrator_ack", 0) >= 1:
            depth += 1
        if m.get("tp_narrator_ack", 0) >= 2:
            depth += 1
        if m.get("tp_narrator_ack", 0) >= 3:
            depth += 1

        STATE["tp_depth"] = min(depth, 9)  # Range: 5-9

    # ========= CONSISTENCY TRACKING =========

    def tp_consistency_check(scene_id, choice_alignment):
        """
        Check if a post-doctrine choice aligns with declared doctrine.
        Call this for choices in the consistency window (3-5 major
        decisions after Doctrine Declaration).

        Args:
            scene_id: Current scene ID
            choice_alignment: "EMP" or "OB" — which path this choice aligns with
        """
        tp_init()
        doctrine = STATE.get("doctrine_choice", None)
        if doctrine is None:
            return  # Doctrine not yet declared

        m = STATE["metrics"]
        if doctrine == "OB_DOCTRINE" and choice_alignment == "OB":
            m["consistency"] = min(3, m.get("consistency", 0) + 1)
        elif doctrine == "EMP_DOCTRINE" and choice_alignment == "EMP":
            m["consistency"] = min(3, m.get("consistency", 0) + 1)
        elif doctrine == "OB_DOCTRINE" and choice_alignment == "EMP":
            m["consistency"] = max(-3, m.get("consistency", 0) - 1)
        elif doctrine == "EMP_DOCTRINE" and choice_alignment == "OB":
            m["consistency"] = max(-3, m.get("consistency", 0) - 1)

        log_line("TP_CONSISTENCY:{}:choice={}:doctrine={}:value={}".format(
            scene_id, choice_alignment, doctrine, m["consistency"]))

    # ========= TP-GATED CONTENT HELPERS =========

    def tp_active():
        """Returns True if the True Path is active."""
        tp_init()
        return STATE.get("true_path", False)

    def tp_depth():
        """Returns the current TP depth (0-7)."""
        tp_init()
        return STATE.get("tp_depth", 0)

    def tp_has_emergence():
        """Returns True if the player found any Emergence option."""
        tp_init()
        return STATE["metrics"].get("tp_emergence_count", 0) >= 1

    def tp_has_narrator_ack():
        """Returns True if the player acknowledged the narrator."""
        tp_init()
        return STATE["metrics"].get("tp_narrator_ack", 0) >= 1

    def tp_narrator_available():
        """
        Returns True if Narrator Awareness options should be shown.
        Available if player has demonstrated ANY TP behavior.
        """
        tp_init()
        m = STATE["metrics"]
        return (m.get("tp_emergence_count", 0) >= 1
                or m.get("tp_integration", 0) >= 1
                or m.get("truth_shards", 0) >= 3)
