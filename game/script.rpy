
label start:
    call a1_s00_tutorial

    # ========= ACT 1 =========
    call a1_s00a_intro
    call a1_s01_branding
    call a1_s02_bedroom
    call a1_s03_sector7_mission
    call a1_s04_morning_routine
    call a1_s05_hallway
    call a1_s06_gala
    # a1_s06a_daren_flashback is called conditionally from within a1_s06_gala
    call a1_s07_balcony
    call a1_s08_bedroom
    call a1_s09_inspection_day
    call a1_s10_barracks_morning
    call a1_s11_hill_flashback
    call a1_s13_demonstration_floor
    call a1_s14_brothers_rooftop
    call a1_s15_archive_of_merit
    call a1_s16_debrief_theater
    call a1_s17_breaking_point
    call a1_s18_lyra_visit
    call a1_s19_the_message
    call a1_s20_lower_spans
    call a1_s21_zira_first_contact
    call a1_s22_return_to_aeries
    call a1_s23_the_sweep
    call a1_s24_confession_with_lyra
    call a1_s25_morning_after
    call a1_s26_obsidian_bridge
    call a1_s27_investigation
    call a1_s28_purge
    # ========= END ACT 1 =========

    # ========= ACT 2 =========
    call a2_s01_descent
    call a2_s02_reality_check
    call a2_s03_safe_house_planning
    call a2_s04_first_day_out
    call a2_s05_clinic
    call a2_s06_hand_off_the_wire
    call a2_s07_quiet_night
    call a2_s08_the_analyst
    call a2_s09_armor_down
    call a2_s10_static_faith
    call a2_s11_selenes_judgment
    call a2_s12_proof_of_intent
    call a2_s13_echelon_interlude_1
    call a2_s14_the_intel_den
    call a2_s15_algorithm_of_chaos
    call a2_s16_finding_home
    call a2_s17_building_something
    call a2_s18_the_patient
    call a2_s19_recruitment_wave
    call a2_s20_doctrine_declaration
    call a2_s21_command_temperature
    call a2_s22_massive_recruitment
    call a2_s23_mercy_and_counting
    call a2_s24_echelon_interlude_2
    call a2_s25_echelon_raid_defense
    call a2_s26_carry_scene

    # Zira commitment — path branched
    if pass_ob():
        call a2_s27_zira_commitment_ob
    else:
        call a2_s27_zira_commitment_emp

    # Selene finale — path branched (the act's hard fork;
    # OB kills Selene, EMP keeps her alive)
    if pass_ob():
        call a2_s28_selene_finale_ob
    else:
        call a2_s28_selene_finale_emp
    # ========= END ACT 2 =========

    # ========= ACT 3 =========
    # Hard EMP/OB split. All Act 3 scenes are path-exclusive.
    # EMP is the default; OB requires a committed obedience score.
    if pass_ob():
        # ----- ACT 3 OBSIDIAN PATH -----
        call a3_s01_ashes_in_formation_ob
        call a3_s02_stay_with_me_ob
        call a3_s02a_silent_table_ob
        call a3_s04_who_commands_now_ob
        call a3_s05_echoes_in_rain_ob
        call a3_s06_request_for_alignment_ob
        call a3_s07_terms_of_order_ob
        call a3_s08_perfect_execution_ob
        call a3_s09_echelon_interlude_3_ob
        call a3_s10_tessa_friction_ob
        call a3_s11_counter_strike_ob
        call a3_s12_the_oath_ob
        call a3_s13_proof_of_life_ob
        call a3_s14_noelle_calculus_ob
        call a3_s15_chain_of_two_ob
        call a3_s16_data_and_doubt_ob
        call a3_s17_count_the_cost_ob
        call a3_s18_field_sync_ob
        call a3_s19_the_weight_ob
        call a3_s19a_the_letter_ob
        call a3_s20_you_dont_get_to_break_ob
        call a3_s21_the_story_keeper_ob
        call a3_s22_the_hunt_ob
        call a3_s23_bookend_before_mirror_ob
        call a3_s24_liora_ob
        call a3_s25_aftermath_ob
    else:
        # ----- ACT 3 EMPATHY PATH -----
        call a3_s01_back_from_edge_emp
        call a3_s03_breath_of_faith_emp
        call a3_s04_shared_ground_emp
        call a3_s04a_the_silence_emp
        call a3_s05_two_healers_emp
        call a3_s05a_woman_from_sector_7_emp
        call a3_s06_orders_and_prayers_emp
        call a3_s07_echelon_strikes_back_emp
        call a3_s08_the_unmeasurable_emp
        call a3_s09_echelon_interlude_3_emp
        call a3_s10_field_sync_emp
        call a3_s11_empirical_tenderness_emp
        call a3_s12_corridor_op_emp
        call a3_s13_scar_and_steady_emp
        call a3_s14_cipher_and_skin_emp
        call a3_s15_signal_under_fire_emp
        call a3_s16_command_and_surrender_emp
        call a3_s17_faith_in_flaws_emp
        call a3_s18_the_weight_emp
        call a3_s18a_the_letter_emp
        call a3_s19_noelle_revelation_emp
        call a3_s20_the_story_keeper_emp
        call a3_s21_bookend_before_storm_emp
        call a3_s22_liora_execution_emp
        call a3_s23_aftermath_emp
    # Act 3 interludes (a3_int_*) are called conditionally from
    # within their parent scenes, not from the main flow.
    # ========= END ACT 3 =========

    # ========= ACT 4 =========
    # Hard EMP/OB split continues. Path is locked by end of Act 3.
    if pass_ob():
        # ----- ACT 4 OBSIDIAN PATH — Violence Normalized -----
        call a4_s01_the_cold_room_ob
        call a4_s02_the_new_shape_ob
        call a4_s03_marcus_adapts_ob
        call a4_s04_lyra_prays_alone_ob
        call a4_s05_zira_cannot_leave_ob
        call a4_s06_tessa_at_the_board_ob
        call a4_s07_aeron_and_nyra_cold_ob
        call a4_s08_echelon_interlude_4_ob
        call a4_s09_sector_12_sweep_ob
        call a4_s10_noelle_doctrine_ob
        call a4_s11_nyra_second_oath_ob
        call a4_s12_zira_confrontation_ob
        call a4_s13_zira_deepening_erotic_ob
        call a4_s14_lyra_sanctifying_violence_ob
        call a4_s15_lyra_deepening_erotic_ob
        call a4_s16_tessa_fracture_point_ob
        call a4_s17_tessa_conditional_beat_ob
        call a4_s18_rhea_arrives_ob
        call a4_s19_tessa_the_trainee_ob
        call a4_s20_noelle_deepening_erotic_ob
        call a4_s21_the_letter_ob
        call a4_s22_council_of_attrition_ob
        call a4_s23_aeron_alone_ob
        call a4_s24_nyra_the_mirror_ob
        call a4_s25_lyra_at_the_altar_ob
        call a4_s26_act_four_close_ob
    else:
        # ----- ACT 4 EMPATHY PATH — Shared Authority -----
        call a4_s01_morning_after_broadcast_emp
        call a4_s02_first_cracks_emp
        call a4_s03_marcus_adapts_emp
        call a4_s04_lyra_unbuckled_emp
        call a4_s05_delegation_test_emp
        call a4_s05a_you_are_not_a_machine_emp
        call a4_s06_tessa_counts_different_emp
        call a4_s07_echelon_interlude_4_emp
        call a4_s08_zira_exit_plan_emp
        call a4_s09_noelle_implicated_emp
        call a4_s09a_she_calls_him_out_emp
        call a4_s10_what_selene_meant_emp
        call a4_s11_mercy_call_costs_emp
        call a4_s11a_prayer_after_mercy_emp
        call a4_s11b_the_ones_he_lost_emp
        call a4_s12_held_not_fixed_emp
        call a4_s12a_she_is_not_just_tactical_emp
        call a4_s13_protecting_exhaustion_emp
        call a4_s13a_quiet_after_failure_emp
        call a4_s14_return_to_the_table_emp
        call a4_s15_zira_deepening_erotic_emp
        call a4_s16_rhea_strikes_emp
        call a4_s17_selene_deepening_erotic_emp
        call a4_s18_noelle_deepening_erotic_emp
        call a4_s19_lyra_deepening_erotic_emp
        call a4_s20_tessa_deepening_erotic_emp
        call a4_s21_marcus_second_cut_emp
        call a4_s22_act_four_close_emp
    # ========= END ACT 4 =========

    # ========= ACT 5 =========
    # Act 5 is not yet written. Path-branched entry gates live at
    # flag("act4_emp_complete") / flag("act4_ob_complete") — set by
    # the Act 4 close scenes. When Act 5 is written, the same
    # pass_ob() branching pattern continues here.
    # ========= END ACT 5 =========

    return
