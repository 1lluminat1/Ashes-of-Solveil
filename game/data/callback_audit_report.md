# Callback Audit Report — Ashes of Solveil

Generated 2026-04-12. Covers Acts 1–4, both EMP and OB paths.

**Status after fix pass:** All 5 HIGH-priority gaps and 7 MEDIUM-priority gaps
have been addressed in commit `d2e6fea`. The fixes are noted inline below.

---

## 1. Confirmed Working Callbacks

### 1.1 Tessa's Rule of Three
- **Origin**: `a2_int_tessa_torins_name.rpy` L43-57 — "say it three times, sweet thing, and you are still here"
- **Callback A (teaching)**: `a4_s05a_you_are_not_a_machine_emp.rpy` L363-411 — Tessa silently applies the rule to Aeron's sleeping body
- **Callback B (application)**: `a4_s11b_the_ones_he_lost_emp.rpy` L82-230 — Aeron runs the full rule on the gala dead, then the rule breaks on Liora's name
- **Callback C (evolution)**: `a4_s06_tessa_counts_different_emp.rpy` L139, L203, L215, L383 — Tessa's rule goes silent
- **Status**: ✅ FULLY WIRED. Most powerful arc in Act 4. All four reference points confirmed.

### 1.2 Liora on Tessa's Board (EMP)
- **Origin**: `a3_int_tessa_the_board_emp.rpy` — Liora placed on both LIVING and DEAD columns
- **Callback**: `a4_s06_tessa_counts_different_emp.rpy` L107-113 — "LIORA RYLAN is on both columns"
- **Status**: ✅ CONSISTENT. Board entry correctly reflects death.

### 1.3 Selene's Kael Story
- **Origin**: `a3_int_selene_kael_emp.rpy` (flashback)
- **Setup**: `a4_s05_delegation_test_emp.rpy` — "we'll finish it later"
- **Callback (completion)**: `a4_s10_what_selene_meant_emp.rpy` L102-232 — full story delivered, thesis line "delegate the question"
- **Status**: ✅ FULLY WIRED. Explicit meta-acknowledgement at L238.

### 1.4 Anayet / Seren (Old Tongue)
- **Origin A (Anayet)**: `a4_s04_lyra_unbuckled_emp.rpy` L172, L194
- **Origin B (Seren)**: `a4_s11a_prayer_after_mercy_emp.rpy` L149-209
- **Callbacks**: 5 confirmed echo points across a4_s11a, a4_s11b, a4_s19, a4_s22, a4_s25
- **Status**: ✅ FULLY WIRED, triple-callback structure, cross-path preservation.

### 1.5 Zira's "Door"
- **Origin**: `a4_s08_zira_exit_plan_emp.rpy` L305, L347, L387-463
- **Callbacks**: 48 occurrences in s13, 32 in s15, 2 in s22
- **Status**: ✅ WIRED. Densely echoed in Phase II/III.

### 1.6 The Pressed Flower
- **Origin**: `a4_s05_zira_cannot_leave_ob.rpy` L290-300
- **Callback A**: `a4_s13_zira_deepening_erotic_ob.rpy` L504-582
- **Callback B**: `a4_s12_zira_confrontation_ob.rpy` L364
- **Callback C (cross-path echo)**: `a4_s21_the_letter_ob.rpy` L326
- **Status**: ✅ WIRED. Three-beat OB progression plus one cross-path echo.

### 1.7 Marcus's Empty Chair
- **Origin**: `a4_s08_echelon_interlude_4_ob.rpy` L150, L355-451
- **EMP twin**: `a4_s07_echelon_interlude_4_emp.rpy` L119, L265, L315
- **Callbacks**: 6+ confirmed echo points across a4_s13, s14, s21, s22, s24 (both paths)
- **Status**: ✅ EXTREMELY WELL WIRED. Second most densely echoed motif in the project.

### 1.8 Noelle "Variable to Sentence"
- **Origin (variable)**: `a4_s13a_quiet_after_failure_emp.rpy` L218-276
- **Callback (sentence)**: `a4_s18_noelle_deepening_erotic_emp.rpy` L654-680
- **Deep lineage**: `a2_int_noelle_variable_name.rpy` L51-53 — original framework from Act 2
- **Status**: ✅ FULLY WIRED with three-scene lineage.

### 1.9 Liora's Letter (Cross-Path)
- **EMP foreshadow**: `a3_s22_liora_execution_emp.rpy` L109, L279
- **EMP delivery**: `a3_s18a_the_letter_emp.rpy`
- **OB mirror**: `a4_s21_the_letter_ob.rpy`
- **OB Act 3 pair**: `a3_s19a_the_letter_ob.rpy`
- **Status**: ✅ WIRED. Execution scene correctly foreshadows the letter.

### 1.10 Tessa's Board Overwrite (OB)
- **Origin**: `a4_s06_tessa_at_the_board_ob.rpy` L120-130
- **Callback A**: `a4_s16_tessa_fracture_point_ob.rpy` L19, L40-44
- **Callback B**: `a4_s19_tessa_the_trainee_ob.rpy` L56
- **Status**: ✅ FULLY WIRED. Three-scene arc with physical object continuity.

### 1.11 Kesa Marin / Joren Hale (Named Dead)
- **Origin**: `a4_s05_delegation_test_emp.rpy` L304-306
- **Callback A**: `a4_s06_tessa_counts_different_emp.rpy` L173 — names on dead column
- **Callback B**: `a4_s11b_the_ones_he_lost_emp.rpy` L218-230 — rule of three
- **Status**: ✅ FULLY WIRED. Named, witnessed on board, ritually kept.

### 1.12 Operation 391 / Sector 10 Sweep
- **Origin**: `a1_s08_bedroom.rpy` L98, L132; `a1_s23_the_sweep.rpy`
- **Callbacks A-D**: a2_s01, a2_s02, a2_s08, a2_s06
- **Status**: ✅ WIRED in Acts 1-2. **(FIXED)** Now also echoes in a4_s11b (Op 391 number callback).

### 1.13 Glass (Aeron's Street Name)
- **Origin**: `a1_s26_obsidian_bridge.rpy` L64, L338
- **Callback**: `a2_s08_the_analyst.rpy` L108 — "textbook Glass"
- **Status**: ✅ PARTIALLY WIRED. **(FIXED)** Aeron now references "Glass" internally in `a4_s23_aeron_alone_ob.rpy`.

### 1.14 "I Will Meet You Anywhere" (Aeron to Lyra)
- **Reference**: `a4_s19_lyra_deepening_erotic_emp.rpy` L349-678
- **Status**: **(FIXED)** Seed now exists in `a1_s24_confession_with_lyra.rpy` — Lyra: "Wherever you end up... I'll find you."

---

## 2. Missed Callback Opportunities

### HIGH priority (all FIXED in commit d2e6fea)

1. ~~**Balcony near-jump (a1_s17) has no Act 3/4 direct echo from Aeron himself.**~~
   **FIXED** in `a3_s21_bookend_before_storm_emp.rpy`: "I remember the rail. How far down it felt."

2. ~~**"Tier Hall. Age twelve." disappears after Act 1.**~~
   **FIXED** in `a3_s21_bookend_before_storm_emp.rpy`: "I was twelve in the Tier Hall when the Band rejected me."

3. ~~**Kael's rail = Aeron's rail never spoken.**~~
   **FIXED** in `a3_s21_bookend_before_storm_emp.rpy`: "Kael's rail. My rail. Fifteen years apart."

4. ~~**"I will meet you anywhere" has no earlier seed.**~~
   **FIXED** in `a1_s24_confession_with_lyra.rpy`: Lyra's closing beat.

5. ~~**"Mercy is a decision made today" only exists in Act 4.**~~
   **FIXED** in `a2_s23_mercy_and_counting.rpy`: Aeron's post-mercy-death internal.

### MEDIUM priority (all FIXED in commit d2e6fea)

6. ~~**Operation 391 number doesn't recur in Act 3/4.**~~
   **FIXED** in `a4_s11b_the_ones_he_lost_emp.rpy`.

7. ~~**"Glass" as internal Aeron self-label is missing.**~~
   **FIXED** in `a4_s23_aeron_alone_ob.rpy`.

8. ~~**Liora's 6000-names network never gets explicit inheritance beat.**~~
   **FIXED** in `a4_s21_the_letter_ob.rpy`: "Six thousand names. The Ghostline is her ghost."

9. ~~**a3_s24_liora_ob does not reference the OB letter.**~~
   **FIXED** in `a3_s24_liora_ob.rpy`: "The letter is still in my jacket."

10. ~~**Backward-running clock is single-scene reference.**~~
    **FIXED** in `a4_s22_act_four_close_emp.rpy`: Aeron internalizes the clock as metaphor.

11. ~~**Joran Tev only surfaces twice.**~~
    **FIXED** in `a4_s14_return_to_the_table_emp.rpy`: Joran walking the corridor, alive.

12. ~~**"Person first, not a tool" echo missing.**~~
    **FIXED** in `a4_s14_return_to_the_table_emp.rpy`: Aeron recalls Kael's words.

### LOW priority (not yet addressed — optional polish)

- **Fractured Echelon crest** (a4_s11_nyra_second_oath_ob L44) — should appear in another OB scene as a recurring object. Currently single-scene.
- **Tessa's lamp** — functions as character-defining object in a4_s06_ob but not recurring as a physical callback. Consider a4_s17 or s19 OB reference.
- **Vigil blessing / Lyra's Band** — referenced in multiple Lyra scenes but the specific "blessing" motif from Act 1-2 doesn't carry a fixed phrase.
- **Ghostline chip** as a physical object appears many times but is used for plot; it's not treated as a callback object with its own motif weight.
- **Noelle's "TK" placeholder filename** (Tessa's initial used as variable name in her unmodeled log) — quiet homo-coded beat that never gets a callback. Would be devastating if acknowledged in a4_s18.

---

## 3. Broken / Inconsistent Callbacks

### FIXED

- ~~**Board strip medium mismatch**: a4_s06 described the overwrite as "handwriting in a different marker"; a4_s16 described it as "adhesive plastic strip that peels."~~
  **FIXED** in `a4_s06_tessa_at_the_board_ob.rpy`: aligned to "adhesive plastic strip" consistently.

### Remaining (minor, non-blocking)

- **a4_s19 "I will meet you anywhere" meta-narration**: The scene has narrator text that reads "spoken fully for the first time in the run" — this narrator claim is now technically false since the SEED exists in a1_s24. The narrator text should be updated to "spoken back to her for the first time" or similar. Very minor.

---

## Summary

The callback engine is strong. Rule of Three, Kael story, Marcus empty chair,
Board overwrite, Anayet/Seren, and the pressed flower are exceptionally
well-structured (3+ reference points each, meta-narrative acknowledgement,
structural payoffs). The variable-to-sentence Noelle arc quietly reaches back
into Act 2, which is gorgeous.

All 12 HIGH+MEDIUM gaps have been addressed. The remaining LOW-priority items
are optional polish that can be swept up in a future pass or left as-is without
narrative damage.
