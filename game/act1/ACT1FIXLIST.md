The "Compliance Loop" (Skinner Box)
This is how Echelon controls Aeron (and the player).

Plaintext

1. AUDIT (Scene 06a)
   "Promise us you are loyal."
         |
         v
2. ACTION (Scene 09b/17)
   "Prove it by killing."
         |
         v
3. REWARD (Scene 10c)
   "Good job. Here are your metrics."
         |
         v
4. REINFORCEMENT
   "Do it again to keep your score."
         |
   (Repeat)
Why it works: It makes the player complicit. You want the high score (99.7%), even if it feels bad.

The Master Fix List (Step-by-Step)
Here is the executable checklist to polish Act 1. I have sorted these by File Name so you can open one file, fix it, close it, and move to the next.

1. act1_02_bedroom.rpy
Fix Audio Ambiguity: Clarify if the pulse sound is the tower or his heart.

Change: athought "Wind sweeps the glass..." → athought "Is that the tower humming? Or my own blood?"

2. act1_02b_sector7_mission.rpy
Fix "Mercy" Logic: He recites "Precision is Mercy" then asks "Who taught me that word?" It’s contradictory.

Change: athought "...Mercy. Who taught me that word?" → athought "...Mercy. The definition is slipping."

Fix Engagement Logic: The jump to shooting the family is too fast.

Add: Before the shooting SFX, add athought "Protocol 5. No witnesses."

3. act1_03_morning_routing.rpy
Fix Timeline Clarity: Clarify he hasn't slept much.

Add: athought "Four hours of sleep. Not enough to wash the 99.7% out of my head."

4. act1_04_hallway.rpy
Prune "Glass" (End of scene):

Change: athought "Glass doesn't retreat." → athought "There is no retreat. Only forward."

5. act1_05_gala.rpy
Fix "Young Elite" Dialogue: Make it less poetic, more nasty.

Change: ye3 "Father tried to make him a believer. Made Glass instead." → ye3 "They say Rylan stripped the belief right out of him. Now there's nothing left but the glass."

Fix "On Time" Line: Clarify Lyra's meaning.

Change: l "You are on time." → l "Precise. I calculated you would approach within three minutes."

6. act1_06_balcony.rpy
Prune "Glass":

Change: l "I call it glass. Transparent..." → l "I call it being a window. People look right through you to see the power behind."

Fix OB Logic on Ash:

Change: athought "Let it fall. Out of sight..." → athought "Disposal complete. Gravity handles the cleanup. Efficient."

7. act1_07_bedroom.rpy
Prune "Glass":

Change: athought "Glass confirms. Glass complies..." → athought "Confirm. Comply. Continue. The machine doesn't blink."

Fix "Open Now" Thought:

Change: athought "Glass doesn't hesitate." → athought "Muscle memory takes over. My hands know the ritual better than I do."

8. act1_08_hill_flashback.rpy
Fix Young Lyra's Metaphor: 10-year-olds shouldn't invent the game's main theme perfectly.

Change: yl "Glass tower." → yl "Crystal tower. Pretty, but cold." (Let Adult Aeron think: She meant Glass.)

9. act1_09_ritual_flashback.rpy
Add "Taboo" Detail: Emphasize the shame of the bare wrist.

Add: c3 "(stepping back) Impossible..." -> "Cleric 3's hand flies to his own wrist, covering the silver. A reflex."

10. act1_09b_demonstration_floor.rpy
Fix Filename: Rename act1_09b_demonstration_floot.rpy to act1_09b_demonstration_floor.rpy.

11. act1_10_brothers_rooftop.rpy
Fix Nickname: "Little Professor" feels off.

Change: k "Listen to you, little professor." → k "Always calculating the drop. You never just look at the view, do you?"

Fix Location: Ensure the transition text matches the start of Scene 11 (Apartment vs Rooftop).

12. act1_10c_debrief_theater.rpy
CRITICAL FIX: The Flag Check Mismatch.

Find: if check_scene_flag("act1_barracks_morning", ...)

Replace with: if check_scene_flag("act1_07b_barracks_morning", ...)

13. act1_11_breaking_point.rpy
Fix Cigarette Logic: Explain why he smokes.

Add: athought "Kael's brand. Stolen from his stash. Ten years stale, but I need the burn."

14. act1_12_lyra_visit.rpy
CRITICAL FIX: Dialogue Duplication:

You have a loop where Lyra says "Glass recognizes Glass" three times.

Action: Cut the middle block of dialogue (lines ~150-170) where they re-discuss being "Glass." Keep the "Sector 7" story and the ending.

15. act1_13_the_message.rpy
Fix "Wait" Choice: Give it a reward so it's not a fake choice.

Add: $ add_item("intel_cache", "encrypted_sig", 1) to the "Wait" branch.

Prune "Glass":

Change: athought "Tonight, Glass decides..." → athought "Tonight, the weapon turns to look at the target."

16. act1_14_lower_spans.rpy
Prune "Glass" (Heavy Pruning Needed):

Change: athought "Glass executes orders." → athought "I execute orders."

Change: athought "Glass obeys." → athought "The uniform obeys."

17. act1_15_zira_first_contact.rpy
Fix "Honesty Trade": Give a specific reward for being honest.

Add: $ add_intel("Sector 10", "Vent Access Route") if he stops her.

Fix Drone Pacing:

Add: BLOCKING: They duck behind a rusted pylon. The light passes. (Before continuing the long conversation).

18. act1_16_return_to_aeries.rpy
Fix "Minimal Prep" Thought:

Change: athought "Maybe imperfection is the crack..." → athought "If I'm not ready, maybe I'll hesitate when it matters. Good."

19. act1_17_the_sweep.rpy
Fix "KIA" Logic: Why does the squad lie for him?

Add: a "(cold) Did I stutter? Mark him." / unit3 "(swallows) ...Target marked."

20. act1_19_obsidian_bridge.rpy
Fix "Device Withheld":

Action: Ensure the next scene (act1_20) has a check for device_withheld.

(Self-Correction: You actually handled this well in act1_20 with the if has_device or em >= 1 check. Just make sure device_withheld doesn't accidentally trigger the "has_device" logic.)

21. act1_20_investigation.rpy
Fix "Keep Digging" Choice:

Add: If they keep digging, give them the file name ORBITAL_ALIGNMENT_SEQ_ALPHA as a reward for persistence.