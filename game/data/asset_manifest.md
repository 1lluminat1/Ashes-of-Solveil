# Ashes of Solveil — Asset Manifest

Generated checklist of every image and audio asset referenced in the project. Use as a handoff sheet when briefing artists and sound designers.

## Status conventions

- ⬜ Referenced but file not present
- ✅ File present at expected path
- 💤 Commented-out reference (will be uncommented when asset lands)

---

## 1. Character Portraits

One portrait per character (10 total). Rendered as a 420x520 card on the Characters detail screen and 150x220 on the grid card. Drop PNGs at the listed paths and `profile_portrait()` in `game/data/character_profiles.rpy` picks them up automatically. Until present, each slot renders as an accent-tinted Solid.

| Character | Path | Accent |
|---|---|---|
| ⬜ Lyra Vashar | `images/ui/portraits/lyra.png` | #C8A2FF |
| ⬜ Zira | `images/ui/portraits/zira.png` | #5FE3FF |
| ⬜ Tessa | `images/ui/portraits/tessa.png` | #80C37A |
| ⬜ Noelle Korr | `images/ui/portraits/noelle.png` | #9C87C9 |
| ⬜ Selene Valen | `images/ui/portraits/selene.png` | #C1B8A8 |
| ⬜ Nyra | `images/ui/portraits/nyra.png` | #7A9EC0 |
| ⬜ General Marcus Rylan | `images/ui/portraits/marcus.png` | #7A3B3F |
| ⬜ Kael Rylan | `images/ui/portraits/kael.png` | #A48E8A |
| ⬜ Liora Rylan | `images/ui/portraits/liora.png` | #B8A8D4 |
| ⬜ Commander Rhea Vestin | `images/ui/portraits/rhea.png` | #8A95A4 |

## 2. Scene Gallery Thumbnails

One 160x160 thumbnail per replay scene. Drop PNGs at `images/ui/gallery/<scene_id>.png`. The gallery fallback is a tinted Solid keyed off the character accent.

| Scene ID | Title | Act | Path | Expected Path |
|---|---|---|---|---|
| ⬜ `a3_s03_breath_of_faith_emp` | Breath of Faith | Act 3 | EMP | `images/ui/gallery/a3_s03_breath_of_faith_emp.png` |
| ⬜ `a3_s13_proof_of_life_ob` | Proof of Life | Act 3 | OB | `images/ui/gallery/a3_s13_proof_of_life_ob.png` |
| ⬜ `a3_s17_faith_in_flaws_emp` | Faith in Flaws | Act 3 | EMP | `images/ui/gallery/a3_s17_faith_in_flaws_emp.png` |
| ⬜ `a4_s19_lyra_deepening_erotic_emp` | Anayet | Act 4 | EMP | `images/ui/gallery/a4_s19_lyra_deepening_erotic_emp.png` |
| ⬜ `a4_s15_lyra_deepening_erotic_ob` | Recognize Me | Act 4 | OB | `images/ui/gallery/a4_s15_lyra_deepening_erotic_ob.png` |
| ⬜ `a3_s15_signal_under_fire_emp` | Signal Under Fire | Act 3 | EMP | `images/ui/gallery/a3_s15_signal_under_fire_emp.png` |
| ⬜ `a3_s15_chain_of_two_ob` | Chain of Two | Act 3 | OB | `images/ui/gallery/a3_s15_chain_of_two_ob.png` |
| ⬜ `a4_s15_zira_deepening_erotic_emp` | The Clock Runs Back | Act 4 | EMP | `images/ui/gallery/a4_s15_zira_deepening_erotic_emp.png` |
| ⬜ `a4_s13_zira_deepening_erotic_ob` | Something From Before | Act 4 | OB | `images/ui/gallery/a4_s13_zira_deepening_erotic_ob.png` |
| ⬜ `a3_s13_scar_and_steady_emp` | Scar and Steady | Act 3 | EMP | `images/ui/gallery/a3_s13_scar_and_steady_emp.png` |
| ⬜ `a3_s17_count_the_cost_ob` | Count the Cost | Act 3 | OB | `images/ui/gallery/a3_s17_count_the_cost_ob.png` |
| ⬜ `a4_s20_tessa_deepening_erotic_emp` | Not a Medic Tonight | Act 4 | EMP | `images/ui/gallery/a4_s20_tessa_deepening_erotic_emp.png` |
| ⬜ `a4_s17_tessa_conditional_beat_ob` | Remember Who I Am Writing It For | Act 4 | OB | `images/ui/gallery/a4_s17_tessa_conditional_beat_ob.png` |
| ⬜ `a3_s11_empirical_tenderness_emp` | Empirical Tenderness | Act 3 | EMP | `images/ui/gallery/a3_s11_empirical_tenderness_emp.png` |
| ⬜ `a3_s16_data_and_doubt_ob` | Data and Doubt | Act 3 | OB | `images/ui/gallery/a3_s16_data_and_doubt_ob.png` |
| ⬜ `a4_s18_noelle_deepening_erotic_emp` | As a Sentence Now | Act 4 | EMP | `images/ui/gallery/a4_s18_noelle_deepening_erotic_emp.png` |
| ⬜ `a4_s20_noelle_deepening_erotic_ob` | A Hand I Cannot Predict | Act 4 | OB | `images/ui/gallery/a4_s20_noelle_deepening_erotic_ob.png` |
| ⬜ `a3_s16_command_and_surrender_emp` | Command and Surrender | Act 3 | EMP | `images/ui/gallery/a3_s16_command_and_surrender_emp.png` |
| ⬜ `a4_s17_selene_deepening_erotic_emp` | Held as Woman | Act 4 | EMP | `images/ui/gallery/a4_s17_selene_deepening_erotic_emp.png` |
| ⬜ `a3_s12_the_oath_ob` | The Oath | Act 3 | OB | `images/ui/gallery/a3_s12_the_oath_ob.png` |
| ⬜ `a4_s11_nyra_second_oath_ob` | The Second Oath | Act 4 | OB | `images/ui/gallery/a4_s11_nyra_second_oath_ob.png` |

## 3. Scene Backgrounds

Every `scene bg_xxx` reference across the script, commented or active. When a real plate arrives:

1. Drop the PNG in `images/bg/` (or your asset path)
2. Register it via `image bg_xxx = "images/bg/xxx.png"`
3. Uncomment the `scene bg_xxx` line in each referencing file

Stub placeholders exist for bg tags that lint would otherwise flag in `game/ui/stub_defs.rpy` (cold-color Solid blocks).

| Background tag | References | Status |
|---|---|---|
| `bg_aeries_command_spire_dusk` | 1 | 1 commented |
| `bg_aeries_spire_dusk` | 1 | 1 commented |
| `bg_aeron_apartment` | 1 | 1 active |
| `bg_aeron_quarters_day_empty` | 1 | 1 commented |
| `bg_aeron_quarters_late_day` | 1 | 1 commented |
| `bg_aeron_quarters_ob_latenight` | 1 | 1 commented |
| `bg_aeron_quarters_ob_night` | 7 | 7 commented |
| `bg_aeron_quarters_ob_night_after` | 1 | 1 commented |
| `bg_aeron_room_night` | 1 | 1 active |
| `bg_altar_alcove_ob_predawn` | 1 | 1 commented |
| `bg_analysis_alcove_emp` | 1 | 1 commented |
| `bg_analysis_station_night_ob` | 1 | 1 commented |
| `bg_apartment_afternoon` | 1 | 1 commented |
| `bg_apartment_morning` | 1 | 1 commented |
| `bg_apartment_morning_investigation` | 1 | 1 commented |
| `bg_archive_annex_emp` | 1 | 1 commented |
| `bg_archive_corridor` | 1 | 1 commented |
| `bg_archive_plaque_bridge` | 1 | 1 commented |
| `bg_archive_plaque_maxims` | 1 | 1 commented |
| `bg_audit_room_idle` | 1 | 1 commented |
| `bg_balcony_night_emp` | 1 | 1 commented |
| `bg_barracks_corridor_morning` | 1 | 1 commented |
| `bg_base_approach_predawn` | 1 | 1 commented |
| `bg_base_edge_dusk_ob` | 1 | 1 commented |
| `bg_base_interior_damaged` | 1 | 1 commented |
| `bg_bedroom_night` | 1 | 1 commented |
| `bg_bedroom_night_lyra` | 1 | 1 commented |
| `bg_bedroom_night_terminal` | 1 | 1 commented |
| `bg_bedroom_panright` | 1 | 1 commented |
| `bg_branding_chamber_closeup` | 1 | 1 commented |
| `bg_cipher_alcove_emp` | 1 | 1 commented |
| `bg_cipher_alcove_night_late_emp` | 1 | 1 commented |
| `bg_command_center_emp` | 1 | 1 commented |
| `bg_command_post_noelle_board_emp` | 1 | 1 commented |
| `bg_common_area_emp` | 1 | 1 commented |
| `bg_common_area_evening_emp` | 1 | 1 commented |
| `bg_common_area_evening_ob` | 1 | 1 commented |
| `bg_corridor_night_emp` | 1 | 1 commented |
| `bg_corridor_ops_overnight_emp` | 1 | 1 commented |
| `bg_council_room_emptying_late_morning` | 1 | 1 commented |
| `bg_council_room_secondary_base_morning` | 1 | 1 commented |
| `bg_data_alcove_drafting` | 1 | 1 commented |
| `bg_data_alcove_evening` | 2 | 2 commented |
| `bg_data_alcove_model_failure` | 1 | 1 commented |
| `bg_data_alcove_night` | 1 | 1 commented |
| `bg_debrief_theater` | 1 | 1 commented |
| `bg_demo_floor_idle` | 1 | 1 commented |
| `bg_echelon_war_room_amber` | 1 | 1 commented |
| `bg_elevator_ascending` | 1 | 1 commented |
| `bg_extraction_exit_dawn` | 1 | 1 commented |
| `bg_industrial_corridor_night` | 2 | 2 commented |
| `bg_lower_spans_grid62` | 1 | 1 commented |
| `bg_lower_spans_night` | 1 | 1 commented |
| `bg_lyra_private_altar_emp` | 2 | 2 commented |
| `bg_lyra_private_altar_emp_night` | 1 | 1 commented |
| `bg_lyra_quarters_late_emp` | 1 | 1 commented |
| `bg_lyra_quarters_predawn_ob` | 1 | 1 commented |
| `bg_mapping_station_night_emp` | 1 | 1 commented |
| `bg_mapping_station_night_late_emp` | 1 | 1 commented |
| `bg_marcus_grey_room_morning` | 1 | 1 commented |
| `bg_medbay_corridor_night` | 1 | 1 active |
| `bg_medbay_emp` | 1 | 1 commented |
| `bg_medbay_emp_night` | 1 | 1 commented |
| `bg_medbay_main_aftercare_low` | 1 | 1 commented |
| `bg_medbay_main_hold_wide` | 1 | 1 commented |
| `bg_medbay_main_nightlow_emp` | 1 | 1 commented |
| `bg_medbay_night_emp` | 1 | 1 commented |
| `bg_medbay_night_low_light` | 1 | 1 commented |
| `bg_medbay_ob` | 1 | 1 commented |
| `bg_medbay_overnight_lamp_emp` | 1 | 1 commented |
| `bg_medbay_supply_room_night` | 1 | 1 commented |
| `bg_medical_main_night` | 1 | 1 commented |
| `bg_medical_wing_night` | 1 | 1 commented |
| `bg_memorial_chamber_day` | 1 | 1 commented |
| `bg_mess_hall_emp` | 1 | 1 commented |
| `bg_mess_hall_night` | 1 | 1 commented |
| `bg_mess_hall_third_shift_emp` | 1 | 1 commented |
| `bg_mess_morning_ob` | 1 | 1 commented |
| `bg_muster_bay_ob_morning` | 1 | 1 commented |
| `bg_new_medwing_ob` | 1 | 1 commented |
| `bg_noelle_workspace_data_crystal` | 1 | 1 commented |
| `bg_noelle_workspace_night` | 1 | 1 commented |
| `bg_noelle_workspace_overhead_full_emp` | 1 | 1 commented |
| `bg_nyra_quarters_interior_ob` | 1 | 1 commented |
| `bg_nyra_quarters_night_ob` | 1 | 1 commented |
| `bg_nyra_quarters_ob_night` | 1 | 1 commented |
| `bg_nyra_quarters_window_alone_ob` | 1 | 1 commented |
| `bg_observation_deck_night_emp` | 1 | 1 commented |
| `bg_obsidian_bridge_night` | 1 | 1 commented |
| `bg_officers_corridor_ob_night` | 1 | 1 commented |
| `bg_ops_corridor_morning_ob` | 1 | 1 commented |
| `bg_ops_corridor_night_ob` | 1 | 1 commented |
| `bg_ops_room_night_emp` | 1 | 1 commented |
| `bg_ops_room_ob` | 2 | 2 commented |
| `bg_ops_room_ob_late_night` | 1 | 1 commented |
| `bg_ops_room_ob_night` | 1 | 1 commented |
| `bg_ops_room_ob_predawn` | 1 | 1 commented |
| `bg_ops_room_predawn` | 1 | 1 commented |
| `bg_ops_wing_corridor_day` | 3 | 3 commented |
| `bg_ops_wing_table_day` | 2 | 2 commented |
| `bg_ops_wing_table_predawn` | 1 | 1 commented |
| `bg_outlander_safe_house` | 1 | 1 commented |
| `bg_phoenix_corridor_dawn` | 1 | 1 commented |
| `bg_phoenix_ops_room_ob_predawn` | 1 | 1 commented |
| `bg_phoenix_war_room_ob_morning` | 1 | 1 commented |
| `bg_quarters_corridor_ob_night` | 1 | 1 commented |
| `bg_rally_point_morning` | 1 | 1 commented |
| `bg_relay_station_night_emp` | 1 | 1 commented |
| `bg_rooftop_brothers_flashback` | 1 | 1 commented |
| `bg_rooftop_evening` | 1 | 1 commented |
| `bg_ruined_sector_rain` | 1 | 1 commented |
| `bg_safehouse_sector11_morning` | 1 | 1 commented |
| `bg_secondary_base_corridor_night` | 1 | 1 commented |
| `bg_secondary_base_corridor_night_low` | 2 | 2 commented |
| `bg_secondary_base_corridor_predawn` | 1 | 1 commented |
| `bg_secondary_base_edge_morning_rise` | 1 | 1 commented |
| `bg_secondary_base_outer_corridor_night_emp` | 1 | 1 commented |
| `bg_sector10_approach` | 1 | 1 commented |
| `bg_sector11_checkpoint_morning` | 1 | 1 commented |
| `bg_sector3_corridor_dawn` | 1 | 1 commented |
| `bg_sector3_corridor_night` | 1 | 1 commented |
| `bg_sector4_depot_dawn` | 1 | 1 commented |
| `bg_sector4_depot_night` | 1 | 1 commented |
| `bg_sector4_fog` | 1 | 1 commented |
| `bg_sector7_corridor` | 1 | 1 commented |
| `bg_sector_12_ravine_predawn_emp` | 1 | 1 commented |
| `bg_selene_quarters_lamp_only` | 1 | 1 commented |
| `bg_selene_quarters_night` | 2 | 1 active, 1 commented |
| `bg_selene_quarters_two_lamps_emp` | 1 | 1 commented |
| `bg_service_tunnel_dark` | 1 | 1 commented |
| `bg_shrine_alcove_ob_morning` | 1 | 1 commented |
| `bg_signal_bay_ob` | 3 | 3 commented |
| `bg_strategic_room_ob_dawn` | 1 | 1 commented |
| `bg_strategic_room_ob_interior` | 1 | 1 commented |
| `bg_tactical_room_ob` | 1 | 1 commented |
| `bg_tunnel_sector6_night` | 1 | 1 commented |
| `bg_war_room_emp` | 8 | 8 commented |
| `bg_war_room_night_emp` | 2 | 2 commented |
| `bg_war_room_night_ob` | 2 | 2 commented |
| `bg_war_room_ob` | 6 | 6 commented |
| `bg_war_room_ob_0900` | 1 | 1 commented |
| `bg_war_room_ob_tactical` | 1 | 1 commented |
| `bg_war_room_operational_morning` | 1 | 1 commented |
| `bg_warroom_ob` | 1 | 1 commented |
| `bg_workshop_alone_ob` | 1 | 1 commented |
| `bg_workshop_night_ob` | 1 | 1 commented |
| `bg_zira_alcove_after` | 2 | 2 active |
| `bg_zira_alcove_night` | 4 | 4 active |
| `bg_zira_station_evening_emp` | 1 | 1 commented |
| `bg_zira_station_evening_ob` | 1 | 1 commented |
| `bg_zira_station_night_emp` | 1 | 1 commented |
| `bg_zira_station_night_ob` | 1 | 1 commented |
| `bg_zira_workshop_night` | 1 | 1 commented |
| `bg_zira_workshop_night_late` | 1 | 1 commented |
| `bg_zira_workshop_night_ob` | 1 | 1 commented |
| `bg_zira_workshop_ob_night` | 1 | 1 commented |

## 4. Audio

Every `play music/sound/ambient` reference across the script, commented or active. Channels in use: `music`, `sound`, `ambient`, `ambient2`, `voice`. Channel registration lives in `game/ui/audio_menu.rpy`.

| File | Channel | References | Status |
|---|---|---|---|
| ⬜ `audio/amb/base_low_deep.ogg` | ambient | 1 | 1 commented |
| ⬜ `audio/amb/base_predawn.ogg` | ambient | 1 | 1 commented |
| ⬜ `audio/amb/base_quiet.ogg` | ambient | 2 | 2 commented |
| ⬜ `audio/amb/dawn_quiet.ogg` | ambient | 1 | 1 commented |
| ⬜ `audio/amb/ductwork_distant.ogg` | ambient | 1 | 1 commented |
| ⬜ `audio/amb/echelon_lab_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `audio/amb/ghostline_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `audio/amb/lab_crystal_pulse.ogg` | ambient | 1 | 1 commented |
| ⬜ `audio/amb/lab_low_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `audio/amb/lamp_stillness.ogg` | ambient | 1 | 1 commented |
| ⬜ `audio/amb/medbay_low_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `audio/amb/morning_clean.ogg` | ambient | 1 | 1 commented |
| ⬜ `audio/amb/phoenix_base_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `audio/amb/washroom_tap.ogg` | ambient | 1 | 1 commented |
| ⬜ `audio/amb/workshop_low.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/aeries_broadcast_feed.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/aeries_spire_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/alcove_quiet_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/alcove_three_candles.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/analysis_station_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/balcony_wind_warm.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/base_activity_warm.ogg` | ambient | 2 | 2 commented |
| ⬜ `sfx/ambient/base_aftermath_quiet.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/base_corridor_low.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/base_damaged_drip.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/base_deep_night.ogg` | ambient | 2 | 2 commented |
| ⬜ `sfx/ambient/base_evening_domestic.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/base_evening_operational.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/base_hum_cold.ogg` | ambient | 5 | 1 active, 4 commented |
| ⬜ `sfx/ambient/base_hum_coldest.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/base_hum_tense.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/base_loadout_distant.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/base_night_corridor.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/base_night_deep.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/base_night_late_mapping.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/base_night_quiet.ogg` | ambient | 3 | 3 commented |
| ⬜ `sfx/ambient/base_pre_shift.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/base_predawn_generator.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/base_quiet_post_op.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/city_predawn_fog.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/command_wing_night_late.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/convoy_road_morning.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/corridor_dawn_cold.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/corridor_deep_night_distant_wind.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/corridor_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/corridor_morning_ops.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/corridor_night_low.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/corridor_overnight_low.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/council_room_after_low.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/council_room_morning_low.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/crystal_hum_low.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/data_alcove_drafting.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/data_alcove_full_load.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/data_alcove_hum.ogg` | ambient | 3 | 3 commented |
| ⬜ `sfx/ambient/dawn_wind_crowd.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/deep_base_hum_distant.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/echelon_war_room_warm.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/ghostline_static.ogg` | ambient | 2 | 2 commented |
| ⬜ `sfx/ambient/grey_room_silence.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/industrial_corridor_combat.ogg` | ambient | 2 | 2 commented |
| ⬜ `sfx/ambient/mapping_station_hum.ogg` | ambient | 7 | 7 commented |
| ⬜ `sfx/ambient/medbay_hold_low.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/medbay_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/medbay_night_low.ogg` | ambient | 2 | 2 commented |
| ⬜ `sfx/ambient/medbay_night_quiet.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/medbay_nightlow_vigil.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/medbay_quiet_night.ogg` | ambient | 2 | 2 commented |
| ⬜ `sfx/ambient/medbay_quiet_postcount.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/medbay_warm.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/medical_wing_night.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/medwing_hvac.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/mess_hall_night.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/mess_hall_warm.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/mess_night_low.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/morning_wind_warm.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/muster_bay_loadout.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/observation_wind_warm.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/ops_room_analytical.ogg` | ambient | 2 | 2 commented |
| ⬜ `sfx/ambient/ops_room_deep_night.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/ops_room_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/ops_room_hvac.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/ops_room_low.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/ops_room_predawn.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/ops_room_standby.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/ops_wing_fourth_shift.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/ops_wing_full.ogg` | ambient | 2 | 2 commented |
| ⬜ `sfx/ambient/predawn_ravine_cold.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/quarters_cold_hum.ogg` | ambient | 5 | 5 commented |
| ⬜ `sfx/ambient/quarters_deep_night.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/quarters_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/quarters_latenight.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/quarters_minimal.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/quarters_night_cycle.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/quarters_night_datapad.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/quarters_old_building.ogg` | ambient | 2 | 2 commented |
| ⬜ `sfx/ambient/quarters_quiet_low.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/quarters_quiet_warm.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/rain_heavy_urban.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/relay_station_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/room_quiet_cold.ogg` | ambient | 1 | 1 active |
| ⬜ `sfx/ambient/room_quiet_warm.ogg` | ambient | 2 | 2 active |
| ⬜ `sfx/ambient/safe_house_neutral.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/safehouse_kitchen_morning.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/sector11_street_morning.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/spire_wind_low.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/tech_hum_cold.ogg` | ambient | 2 | 2 active |
| ⬜ `sfx/ambient/tech_hum_warm.ogg` | ambient | 2 | 2 active |
| ⬜ `sfx/ambient/tunnel_deep_drip.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/tunnel_operation.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/urban_night_industrial.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/urban_night_tense.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/war_room_active.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/war_room_cold.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/war_room_council.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/war_room_full.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/war_room_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/war_room_operational.ogg` | ambient | 2 | 2 commented |
| ⬜ `sfx/ambient/war_room_ops.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/war_room_planning.ogg` | ambient | 3 | 3 commented |
| ⬜ `sfx/ambient/war_room_post_op.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/war_room_quiet.ogg` | ambient | 2 | 2 commented |
| ⬜ `sfx/ambient/warroom_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/wind_tunnel_empty.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/wind_urban_quiet.ogg` | ambient | 2 | 2 commented |
| ⬜ `sfx/ambient/workshop_forge_banked.ogg` | ambient | 2 | 2 commented |
| ⬜ `sfx/ambient/workshop_generator_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/workshop_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/workshop_standby_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `sfx/ambient/workspace_hum.ogg` | ambient | 2 | 2 commented |
| ⬜ `sfx/ambient/workspace_overhead_hum.ogg` | ambient | 1 | 1 commented |
| ⬜ `amb/tower_hum.ogg` | music | 1 | 1 commented |
| ⬜ `music/home_theme_quiet.ogg` | music | 1 | 1 commented |
| ⬜ `music/intimacy_lyra_tender.ogg` | music | 1 | 1 commented |
| ⬜ `music/lyra_theme_intimate.ogg` | music | 1 | 1 commented |
| ⬜ `music/lyra_theme_soft.ogg` | music | 1 | 1 commented |
| ⬜ `music/ob_funeral_drone.ogg` | music | 1 | 1 commented |
| ⬜ `music/score/act4_close_long_low_string.ogg` | music | 1 | 1 commented |
| ⬜ `sfx/alcove_door_approach.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/alcove_door_close_slow.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/alcove_door_measured.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/boots_on_concrete_fast.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/boots_on_grating_distant.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/boots_running_grating.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/brand_connect.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/breach_charge.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/breach_charge_distant.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/cauterize_hiss.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/combat/band_hum_low.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/combat/band_hum_low_stutter.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/combat/weapons_exchange_suppressed.ogg` | sound | 2 | 2 commented |
| ⬜ `sfx/comm_ground_team_check_in.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/comm_ping.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/comms_intercept_click.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/comms_intercept_end.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/comms_playback_start.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/crossfire_burst.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/desk_lamp_click_on.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/door_bolt_interior_slow.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/door_breach_clean.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/door_hiss.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/door_hiss_soft.ogg` | sound | 3 | 3 commented |
| ⬜ `sfx/door_knock_precise.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/door_knock_single.ogg` | sound | 2 | 2 commented |
| ⬜ `sfx/door_reseal_soft.ogg` | sound | 2 | 2 commented |
| ⬜ `sfx/door_unseal_quarters.ogg` | sound | 7 | 7 commented |
| ⬜ `sfx/ghostline_voice_crackle.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/gunfire_burst_distant.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/heartbeat_low.ogg` | sound | 2 | 2 commented |
| ⬜ `sfx/holo_table_boot.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/hud_confirm.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/lights_flicker.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/low_pulse.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/marker_cap.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/marker_stroke_name.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/marker_stroke_sentence.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/marker_uncap.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/mess_doors_close.ogg` | sound | 2 | 2 commented |
| ⬜ `sfx/mess_doors_open.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/one_shot/bolt_cutter_soft.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/one_shot/boots_plant_two.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/one_shot/breath_deep_soft.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/one_shot/crystal_chime_soft.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/one_shot/datapad_wall_impact.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/one_shot/execution_silence.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/one_shot/holo_activate.ogg` | sound | 2 | 2 commented |
| ⬜ `sfx/one_shot/lacquer_box_open.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/one_shot/mortar_grind_soft.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/one_shot/radio_click.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/one_shot/thermite_sequence.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/one_shot/tunnel_door_seal.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/one_shot/workshop_door_seal_soft.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/ops_priority_ping.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/overwatch_engagement_low.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/relay_connection_tone.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/spire_door_slide.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/stylus_set_down_ritual.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/stylus_signature_single.ogg` | sound | 3 | 3 commented |
| ⬜ `sfx/stylus_single_mark.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/suppressed_fire_burst.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/suppressed_gunfire_burst.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/sync_pulse.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/sync_pulse_climb.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/sync_reject.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/tactical/comms_chatter_controlled.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/vent_cycle_off.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/whiteboard_marker_writing.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/wind_exterior_high.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx/wing_doors_close.ogg` | sound | 2 | 2 commented |
| ⬜ `sfx/wing_doors_open.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx_wardrobe_creak.ogg` | sound | 1 | 1 commented |
| ⬜ `sfx_wind_low.ogg` | sound | 1 | 1 commented |

## 5. Per-Scene Render Budget

Workflow: each scene lives in its own folder under `images/bg/<scene_id>/` and is rendered as a numbered sequence `001.png`, `002.png`, etc. One render typically covers 2-3 dialogue beats — a character talks for a few lines on one pose, then the next render handles the next 2-3 beats.

**To scaffold a scene before you render it:**

```
python3 tools/inject_render_stubs.py <scene_id>
```

That inserts commented `# scene <scene_id>_NNN with dissolve` stubs at each cluster boundary. Uncomment each as the matching render lands in `images/bg/<scene_id>/NNN.png`. Auto-registration lives in `game/systems/bg_autoregister.rpy` — just drop files in the folder and Ren'Py picks them up without manual `image` definitions.

**Columns:**

- **Beats** — dialogue/narration lines inside the scene's label
- **Stubs** — commented `# scene ... @render_stub` lines (0 = not scaffolded yet)
- **Renders** — PNG/JPG/WEBP files present in the scene's folder
- **%** — renders / stubs, or renders / (beats/3) as an estimate if unscaffolded

| Scene | Beats | Stubs | Renders | % | Status |
|---|---|---|---|---|---|
| `a1_s00_tutorial` | 0 | 0 | 0 | 0% | ⬜ not started |
| `a1_s00a_intro` | 10 | 0 | 0 | 0% | ⬜ not started |
| `a1_s01_branding` | 71 | 0 | 0 | 0% | ⬜ not started |
| `a1_s02_bedroom` | 28 | 0 | 0 | 0% | ⬜ not started |
| `a1_s03_sector7_mission` | 57 | 0 | 0 | 0% | ⬜ not started |
| `a1_s04_morning_routine` | 27 | 0 | 0 | 0% | ⬜ not started |
| `a1_s05_hallway` | 48 | 0 | 0 | 0% | ⬜ not started |
| `a1_s06_gala` | 126 | 0 | 0 | 0% | ⬜ not started |
| `a1_s06a_daren_flashback` | 13 | 0 | 0 | 0% | ⬜ not started |
| `a1_s07_balcony` | 129 | 0 | 0 | 0% | ⬜ not started |
| `a1_s08_bedroom` | 45 | 0 | 0 | 0% | ⬜ not started |
| `a1_s09_inspection_day` | 59 | 0 | 0 | 0% | ⬜ not started |
| `a1_s10_barracks_morning` | 42 | 0 | 0 | 0% | ⬜ not started |
| `a1_s11_hill_flashback` | 94 | 0 | 0 | 0% | ⬜ not started |
| `a1_s13_demonstration_floor` | 49 | 0 | 0 | 0% | ⬜ not started |
| `a1_s14_brothers_rooftop` | 81 | 0 | 0 | 0% | ⬜ not started |
| `a1_s15_archive_of_merit` | 31 | 0 | 0 | 0% | ⬜ not started |
| `a1_s16_debrief_theater` | 24 | 0 | 0 | 0% | ⬜ not started |
| `a1_s17_breaking_point` | 78 | 0 | 0 | 0% | ⬜ not started |
| `a1_s18_lyra_visit` | 130 | 0 | 0 | 0% | ⬜ not started |
| `a1_s19_the_message` | 90 | 0 | 0 | 0% | ⬜ not started |
| `a1_s20_lower_spans` | 84 | 0 | 0 | 0% | ⬜ not started |
| `a1_s21_zira_first_contact` | 101 | 0 | 0 | 0% | ⬜ not started |
| `a1_s22_return_to_aeries` | 80 | 0 | 0 | 0% | ⬜ not started |
| `a1_s23_the_sweep` | 155 | 0 | 0 | 0% | ⬜ not started |
| `a1_s24_confession_with_lyra` | 118 | 0 | 0 | 0% | ⬜ not started |
| `a1_s25_morning_after` | 184 | 0 | 0 | 0% | ⬜ not started |
| `a1_s26_obsidian_bridge` | 136 | 0 | 0 | 0% | ⬜ not started |
| `a1_s27_investigation` | 143 | 0 | 0 | 0% | ⬜ not started |
| `a1_s28_purge` | 232 | 0 | 0 | 0% | ⬜ not started |
| `a2_s01_descent` | 181 | 0 | 0 | 0% | ⬜ not started |
| `a2_s02_reality_check` | 192 | 0 | 0 | 0% | ⬜ not started |
| `a2_s03_safe_house_planning` | 87 | 0 | 0 | 0% | ⬜ not started |
| `a2_s04_first_day_out` | 202 | 0 | 0 | 0% | ⬜ not started |
| `a2_s05_clinic` | 270 | 0 | 0 | 0% | ⬜ not started |
| `a2_s06_hand_off_the_wire` | 235 | 0 | 0 | 0% | ⬜ not started |
| `a2_s07_quiet_night` | 199 | 0 | 0 | 0% | ⬜ not started |
| `a2_s08_the_analyst` | 179 | 0 | 0 | 0% | ⬜ not started |
| `a2_s09_armor_down` | 189 | 0 | 0 | 0% | ⬜ not started |
| `a2_s10_static_faith` | 132 | 0 | 0 | 0% | ⬜ not started |
| `a2_s11_selenes_judgment` | 150 | 0 | 0 | 0% | ⬜ not started |
| `a2_s12_proof_of_intent` | 180 | 0 | 0 | 0% | ⬜ not started |
| `a2_s13_echelon_interlude_1` | 39 | 0 | 0 | 0% | ⬜ not started |
| `a2_s14_the_intel_den` | 138 | 0 | 0 | 0% | ⬜ not started |
| `a2_s15_algorithm_of_chaos` | 122 | 0 | 0 | 0% | ⬜ not started |
| `a2_s16_finding_home` | 151 | 0 | 0 | 0% | ⬜ not started |
| `a2_s17_building_something` | 144 | 0 | 0 | 0% | ⬜ not started |
| `a2_s18_the_patient` | 103 | 0 | 0 | 0% | ⬜ not started |
| `a2_s19_recruitment_wave` | 181 | 0 | 0 | 0% | ⬜ not started |
| `a2_s20_doctrine_declaration` | 87 | 0 | 0 | 0% | ⬜ not started |
| `a2_s21_command_temperature` | 109 | 0 | 0 | 0% | ⬜ not started |
| `a2_s22_massive_recruitment` | 64 | 0 | 0 | 0% | ⬜ not started |
| `a2_s23_mercy_and_counting` | 112 | 0 | 0 | 0% | ⬜ not started |
| `a2_s24_echelon_interlude_2` | 21 | 0 | 0 | 0% | ⬜ not started |
| `a2_s25_echelon_raid_defense` | 95 | 0 | 0 | 0% | ⬜ not started |
| `a2_s26_carry_scene` | 128 | 0 | 0 | 0% | ⬜ not started |
| `a2_s27_zira_commitment_emp` | 166 | 0 | 0 | 0% | ⬜ not started |
| `a2_s27_zira_commitment_ob` | 206 | 0 | 0 | 0% | ⬜ not started |
| `a2_s28_selene_finale_emp` | 57 | 0 | 0 | 0% | ⬜ not started |
| `a2_s28_selene_finale_ob` | 115 | 0 | 0 | 0% | ⬜ not started |
| `a3_s01_ashes_in_formation_ob` | 104 | 0 | 0 | 0% | ⬜ not started |
| `a3_s01_back_from_edge_emp` | 101 | 0 | 0 | 0% | ⬜ not started |
| `a3_s02_stay_with_me_ob` | 179 | 0 | 0 | 0% | ⬜ not started |
| `a3_s02a_silent_table_ob` | 146 | 0 | 0 | 0% | ⬜ not started |
| `a3_s03_breath_of_faith_emp` | 126 | 0 | 0 | 0% | ⬜ not started |
| `a3_s04_shared_ground_emp` | 132 | 0 | 0 | 0% | ⬜ not started |
| `a3_s04_who_commands_now_ob` | 132 | 0 | 0 | 0% | ⬜ not started |
| `a3_s04a_the_silence_emp` | 113 | 0 | 0 | 0% | ⬜ not started |
| `a3_s05_echoes_in_rain_ob` | 168 | 0 | 0 | 0% | ⬜ not started |
| `a3_s05_two_healers_emp` | 110 | 0 | 0 | 0% | ⬜ not started |
| `a3_s05a_woman_from_sector_7_emp` | 162 | 0 | 0 | 0% | ⬜ not started |
| `a3_s06_orders_and_prayers_emp` | 114 | 0 | 0 | 0% | ⬜ not started |
| `a3_s06_request_for_alignment_ob` | 198 | 0 | 0 | 0% | ⬜ not started |
| `a3_s07_echelon_strikes_back_emp` | 282 | 0 | 0 | 0% | ⬜ not started |
| `a3_s07_terms_of_order_ob` | 157 | 0 | 0 | 0% | ⬜ not started |
| `a3_s08_perfect_execution_ob` | 111 | 0 | 0 | 0% | ⬜ not started |
| `a3_s08_the_unmeasurable_emp` | 130 | 0 | 0 | 0% | ⬜ not started |
| `a3_s09_echelon_interlude_3_emp` | 45 | 0 | 0 | 0% | ⬜ not started |
| `a3_s09_echelon_interlude_3_ob` | 59 | 0 | 0 | 0% | ⬜ not started |
| `a3_s10_field_sync_emp` | 79 | 0 | 0 | 0% | ⬜ not started |
| `a3_s10_tessa_friction_ob` | 115 | 0 | 0 | 0% | ⬜ not started |
| `a3_s11_counter_strike_ob` | 139 | 0 | 0 | 0% | ⬜ not started |
| `a3_s11_empirical_tenderness_emp` | 172 | 0 | 0 | 0% | ⬜ not started |
| `a3_s12_corridor_op_emp` | 157 | 0 | 0 | 0% | ⬜ not started |
| `a3_s12_the_oath_ob` | 159 | 0 | 0 | 0% | ⬜ not started |
| `a3_s13_proof_of_life_ob` | 148 | 0 | 0 | 0% | ⬜ not started |
| `a3_s13_scar_and_steady_emp` | 187 | 0 | 0 | 0% | ⬜ not started |
| `a3_s14_cipher_and_skin_emp` | 144 | 0 | 0 | 0% | ⬜ not started |
| `a3_s14_noelle_calculus_ob` | 102 | 0 | 0 | 0% | ⬜ not started |
| `a3_s15_chain_of_two_ob` | 128 | 0 | 0 | 0% | ⬜ not started |
| `a3_s15_signal_under_fire_emp` | 162 | 0 | 0 | 0% | ⬜ not started |
| `a3_s16_command_and_surrender_emp` | 133 | 0 | 0 | 0% | ⬜ not started |
| `a3_s16_data_and_doubt_ob` | 152 | 0 | 0 | 0% | ⬜ not started |
| `a3_s17_count_the_cost_ob` | 123 | 0 | 0 | 0% | ⬜ not started |
| `a3_s17_faith_in_flaws_emp` | 120 | 0 | 0 | 0% | ⬜ not started |
| `a3_s18_field_sync_ob` | 85 | 0 | 0 | 0% | ⬜ not started |
| `a3_s18_the_weight_emp` | 93 | 0 | 0 | 0% | ⬜ not started |
| `a3_s18a_the_letter_emp` | 72 | 0 | 0 | 0% | ⬜ not started |
| `a3_s18b_zira_the_relay_emp` | 39 | 0 | 0 | 0% | ⬜ not started |
| `a3_s19_noelle_revelation_emp` | 103 | 0 | 0 | 0% | ⬜ not started |
| `a3_s19_the_weight_ob` | 94 | 0 | 0 | 0% | ⬜ not started |
| `a3_s19a_the_letter_ob` | 86 | 0 | 0 | 0% | ⬜ not started |
| `a3_s19b_zira_before_the_weight_ob` | 30 | 0 | 0 | 0% | ⬜ not started |
| `a3_s20_the_story_keeper_emp` | 81 | 0 | 0 | 0% | ⬜ not started |
| `a3_s20_you_dont_get_to_break_ob` | 77 | 0 | 0 | 0% | ⬜ not started |
| `a3_s20a_lyra_archive_emp` | 62 | 0 | 0 | 0% | ⬜ not started |
| `a3_s20a_lyra_prays_for_the_hunt_ob` | 35 | 0 | 0 | 0% | ⬜ not started |
| `a3_s21_bookend_before_storm_emp` | 84 | 0 | 0 | 0% | ⬜ not started |
| `a3_s21_the_story_keeper_ob` | 81 | 0 | 0 | 0% | ⬜ not started |
| `a3_s22_liora_execution_emp` | 204 | 0 | 0 | 0% | ⬜ not started |
| `a3_s22_the_hunt_ob` | 108 | 0 | 0 | 0% | ⬜ not started |
| `a3_s22a_nyra_before_the_mirror_ob` | 54 | 0 | 0 | 0% | ⬜ not started |
| `a3_s22a_tessa_after_liora_emp` | 55 | 0 | 0 | 0% | ⬜ not started |
| `a3_s23_aftermath_emp` | 44 | 0 | 0 | 0% | ⬜ not started |
| `a3_s23_bookend_before_mirror_ob` | 94 | 0 | 0 | 0% | ⬜ not started |
| `a3_s23a_noelle_before_liora_ob` | 64 | 0 | 0 | 0% | ⬜ not started |
| `a3_s24_liora_ob` | 185 | 0 | 0 | 0% | ⬜ not started |
| `a3_s25_aftermath_ob` | 61 | 0 | 0 | 0% | ⬜ not started |
| `a4_s01_morning_after_broadcast_emp` | 113 | 0 | 0 | 0% | ⬜ not started |
| `a4_s01_the_cold_room_ob` | 171 | 0 | 0 | 0% | ⬜ not started |
| `a4_s02_first_cracks_emp` | 149 | 0 | 0 | 0% | ⬜ not started |
| `a4_s02_the_new_shape_ob` | 197 | 0 | 0 | 0% | ⬜ not started |
| `a4_s03_marcus_adapts_emp` | 125 | 0 | 0 | 0% | ⬜ not started |
| `a4_s03_marcus_adapts_ob` | 176 | 0 | 0 | 0% | ⬜ not started |
| `a4_s04_lyra_prays_alone_ob` | 153 | 0 | 0 | 0% | ⬜ not started |
| `a4_s04_lyra_unbuckled_emp` | 149 | 0 | 0 | 0% | ⬜ not started |
| `a4_s05_delegation_test_emp` | 203 | 0 | 0 | 0% | ⬜ not started |
| `a4_s05_zira_cannot_leave_ob` | 163 | 0 | 0 | 0% | ⬜ not started |
| `a4_s05a_you_are_not_a_machine_emp` | 167 | 0 | 0 | 0% | ⬜ not started |
| `a4_s06_tessa_at_the_board_ob` | 143 | 0 | 0 | 0% | ⬜ not started |
| `a4_s06_tessa_counts_different_emp` | 134 | 0 | 0 | 0% | ⬜ not started |
| `a4_s07_aeron_and_nyra_cold_ob` | 136 | 0 | 0 | 0% | ⬜ not started |
| `a4_s07_echelon_interlude_4_emp` | 117 | 0 | 0 | 0% | ⬜ not started |
| `a4_s08_echelon_interlude_4_ob` | 175 | 0 | 0 | 0% | ⬜ not started |
| `a4_s08_zira_exit_plan_emp` | 198 | 0 | 0 | 0% | ⬜ not started |
| `a4_s09_noelle_implicated_emp` | 184 | 0 | 0 | 0% | ⬜ not started |
| `a4_s09_sector_12_sweep_ob` | 232 | 0 | 0 | 0% | ⬜ not started |
| `a4_s09a_she_calls_him_out_emp` | 174 | 0 | 0 | 0% | ⬜ not started |
| `a4_s10_noelle_doctrine_ob` | 240 | 0 | 0 | 0% | ⬜ not started |
| `a4_s10_what_selene_meant_emp` | 192 | 0 | 0 | 0% | ⬜ not started |
| `a4_s11_mercy_call_costs_emp` | 197 | 0 | 0 | 0% | ⬜ not started |
| `a4_s11_nyra_second_oath_ob` | 267 | 0 | 0 | 0% | ⬜ not started |
| `a4_s11a_prayer_after_mercy_emp` | 159 | 0 | 0 | 0% | ⬜ not started |
| `a4_s11b_the_ones_he_lost_emp` | 175 | 0 | 0 | 0% | ⬜ not started |
| `a4_s12_held_not_fixed_emp` | 168 | 0 | 0 | 0% | ⬜ not started |
| `a4_s12_zira_confrontation_ob` | 123 | 0 | 0 | 0% | ⬜ not started |
| `a4_s12a_she_is_not_just_tactical_emp` | 229 | 0 | 0 | 0% | ⬜ not started |
| `a4_s13_protecting_exhaustion_emp` | 246 | 0 | 0 | 0% | ⬜ not started |
| `a4_s13_zira_deepening_erotic_ob` | 191 | 0 | 0 | 0% | ⬜ not started |
| `a4_s13a_quiet_after_failure_emp` | 209 | 0 | 0 | 0% | ⬜ not started |
| `a4_s14_lyra_sanctifying_violence_ob` | 168 | 0 | 0 | 0% | ⬜ not started |
| `a4_s14_return_to_the_table_emp` | 157 | 0 | 0 | 0% | ⬜ not started |
| `a4_s14a_familiar_ground_emp` | 286 | 0 | 0 | 0% | ⬜ not started |
| `a4_s14a_oath_and_flower_ob` | 234 | 0 | 0 | 0% | ⬜ not started |
| `a4_s15_lyra_deepening_erotic_ob` | 210 | 0 | 0 | 0% | ⬜ not started |
| `a4_s15_zira_deepening_erotic_emp` | 262 | 0 | 0 | 0% | ⬜ not started |
| `a4_s16_rhea_strikes_emp` | 198 | 0 | 0 | 0% | ⬜ not started |
| `a4_s16_tessa_fracture_point_ob` | 186 | 0 | 0 | 0% | ⬜ not started |
| `a4_s16a_door_and_data_emp` | 292 | 0 | 0 | 0% | ⬜ not started |
| `a4_s17_selene_deepening_erotic_emp` | 329 | 0 | 0 | 0% | ⬜ not started |
| `a4_s17_tessa_conditional_beat_ob` | 156 | 0 | 0 | 0% | ⬜ not started |
| `a4_s18_noelle_deepening_erotic_emp` | 278 | 0 | 0 | 0% | ⬜ not started |
| `a4_s18_rhea_arrives_ob` | 240 | 0 | 0 | 0% | ⬜ not started |
| `a4_s19_lyra_deepening_erotic_emp` | 277 | 0 | 0 | 0% | ⬜ not started |
| `a4_s19_tessa_the_trainee_ob` | 357 | 0 | 0 | 0% | ⬜ not started |
| `a4_s20_noelle_deepening_erotic_ob` | 313 | 0 | 0 | 0% | ⬜ not started |
| `a4_s20_tessa_deepening_erotic_emp` | 237 | 0 | 0 | 0% | ⬜ not started |
| `a4_s20a_command_and_the_door_emp` | 301 | 0 | 0 | 0% | ⬜ not started |
| `a4_s20a_doctrine_and_weapon_ob` | 265 | 0 | 0 | 0% | ⬜ not started |
| `a4_s21_marcus_second_cut_emp` | 225 | 0 | 0 | 0% | ⬜ not started |
| `a4_s21_the_letter_ob` | 164 | 0 | 0 | 0% | ⬜ not started |
| `a4_s22_act_four_close_emp` | 146 | 0 | 0 | 0% | ⬜ not started |
| `a4_s22_council_of_attrition_ob` | 153 | 0 | 0 | 0% | ⬜ not started |
| `a4_s23_aeron_alone_ob` | 144 | 0 | 0 | 0% | ⬜ not started |
| `a4_s24_nyra_the_mirror_ob` | 164 | 0 | 0 | 0% | ⬜ not started |
| `a4_s25_lyra_at_the_altar_ob` | 172 | 0 | 0 | 0% | ⬜ not started |
| `a4_s26_act_four_close_ob` | 108 | 0 | 0 | 0% | ⬜ not started |

### Per-Act Render Totals

| Act | Scenes | Beats | Stubs | Renders | Est. Target |
|---|---|---|---|---|---|
| act1 | 30 | 2465 | 0 | 0 | ~821 |
| act2 | 30 | 4234 | 0 | 0 | ~1411 |
| act3 | 58 | 6680 | 0 | 0 | ~2226 |
| act4 | 59 | 11677 | 0 | 0 | ~3892 |

## Summary

| Category | Total | Present | Missing |
|---|---|---|---|
| Character portraits | 10 | 0 | 10 |
| Gallery thumbnails | 21 | 0 | 21 |
| Scene backgrounds | 156 | — | — |
| Audio files | 211 | 0 | 211 |

---

_Regenerate with `python3 tools/gen_asset_manifest.py`_
