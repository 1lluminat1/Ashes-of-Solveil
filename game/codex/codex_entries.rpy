# ===================================================
# Solveil Codex Entries — authoring file
# Register here; the system file will ingest on start.
# ===================================================

init 1 python:
    CODEX_ENTRIES = {
        "ghostline": {
            "title": _("Ghostline"),
            "category": _("Systems"),
            "tags": ["mesh","relay","Unders"],
            "body": [
                _("Encrypted relay mesh stitched through forgotten Unders infrastructure."),
                _("Traffic rides on industrial noise bursts ('ghost hops')."),
                _("Access rotates via beacons curated by Zira."),
            ],
        },
        "beacon_chip": {
            "title": _("Beacon Chip"),
            "category": _("Artifacts"),
            "tags": ["token","credential","Zira"],
            # staged example: stage 0 → vague; stage 1 → full
            "stages": [
                { "body": [ _("A sealed credential token. Purpose unclear.") ] },
                { "body": [
                    _("Not storage—credential. Later authenticates Aeron on Ghostline."),
                    _("Contains a signed attest shard related to the purge."),
                ]},
            ],
        },
        "obsidian_bridge": {
            "title": _("Obsidian Bridge"),
            "category": _("Places"),
            "tags": ["Sector 10","carrier hiss","meet site"],
            "body": [
                _("Decommissioned black composite span in Sector 10."),
                _("Wind shear generates a carrier hiss Zira uses to mask comms."),
                _("Path evaluation happens here [r1](criteria withheld)[/r]."),
            ],
        },
        "purge_8_10": {
            "title": _("Purge — Sectors 8–10"),
            "category": _("Events"),
            "tags": ["state action","containment","atrocity"],
            "body": [
                _("Coordinated sweep executed without public pre-notice."),
                _("Aeron and Lyra do not know beforehand; witnessing it reorients their moral axis."),
            ],
        },
        "harmony_cores": {
            "title": _("Harmony Cores"),
            "category": _("Artifacts"),
            "tags": ["resonance","relic","instability"],
            "body": [
                _("Resonance relics of Verdant/Ethereal unity—fossilized coherence, not batteries."),
                _("Instability grows the further use departs from harmony."),
            ],
        },
        "lineages": {
            "title": _("Verdant & Ethereal Lineages"),
            "category": _("Lore"),
            "tags": ["Aeron","Lyra","unity"],
            "body": [
                _("Verdant: attuned to living systems (embodied empathy)."),
                _("Ethereal: attuned to structure/clarity (disciplined purpose)."),
                _("Union theme: harmony as relationship."),
            ],
        },
        "bands": {
            "title": _("Resonance Bands"),
            "category": _("Systems"),
            "tags": ["haptic","intercept","tuning"],
            "body": [
                _("Passive wrist transducers (coil + micro-capacitive array)."),
                _("They intercept lineage resonance and translate it to haptic/thermal feedback (tune/dampen/spike)."),
            ],
        },
        "solveil_tiers": {
            "title": _("Solveil — Aeries / Middle / Unders"),
            "category": _("Places"),
            "tags": ["city-state","strata"],
            "body": [
                _("Aeries (elite terraces above the clouds)."),
                _("Middle (industrial stacks)."),
                _("Unders (derelict strata and ghostlines)."),
            ],
        },
        "glass": {
            "title": _("Glass (Aeron)"),
            "category": _("Motifs"),
            "tags": ["dissociation","shame","mask"],
            "body": [
                _("Aeron’s dissociative shell—transparent, empty, sharp when needed."),
                _("Returns as a faint metallic ping when shame flares."),
            ],
        },
    }

    # Register with the system (also gets picked up via global in bootstrap)
    if "codex_register_entries" in renpy.store.__dict__:
        renpy.store.codex_register_entries(CODEX_ENTRIES)