# ACT V — NIECE MEETING SCENE (design outline, NOT a finished script)

Reference design document for the scene where Aeron meets Soren, his niece,
for the first time. Two variants — EMP and OB — with a shared gate structure.

**Read this alongside** `game/canon_notes_kael.md`. If anything in this
outline contradicts canon notes, canon notes win.

Last updated: 2026-04-14.

---

## 0. PURPOSE AND CONSTRAINTS

- This scene is the terminal payoff for the Kael storyline. It must
  carry the weight of: Kael's survival, Kael's death, Rava's death
  at Aeron's own hand, and the nine-year compartment Selene has been
  carrying.
- The scene is NOT a reconciliation. It is a test. Soren is eleven
  years old in 390 AC. She does not owe Aeron anything. She has one
  question for him, and the question is the whole scene.
- The scene must be **memory-gated.** The reveal completes only if
  Aeron both (a) chose correctly in `a1_s20_lower_spans` and (b)
  remembers the choice when Soren tests him. Memory is the test.
- If Aeron fails either half of the gate, the scene still happens —
  it just ends as a partial meeting, not a reveal. The player does
  not get told they failed. The scene simply ends where it ends.

## 1. THE TWO VARIANTS — SAME GATE, DIFFERENT HANDS

### 1a. EMP variant — Selene delivers

- Selene takes Aeron to the meeting. Liora is dead on this path; her
  final courier message (delivered in `a4_s10a`) is the chain that
  made this meeting possible.
- Selene has been the compartment-keeper for nine years. The scene
  opens with her handing the compartment over. She is not the one
  who speaks to Soren. She is the one who opens the door.
- Scene location: a small Outlands safe house (to be designed).
  Liora's courier network protected Soren there after Operation 391.
- Selene's role in the scene: she enters with Aeron, introduces him
  by name ("This is Aeron. You have heard the name before."), and
  then steps back to the wall. She does not participate in the test.
  She is present as witness only.

### 1b. OB variant — Liora grants

- Liora is alive on this path. She has been holding Soren since the
  Sector 10 sweep. She has never told Selene where Soren is. She has
  never told anyone.
- The OB gate for the meeting is different from EMP. On OB, the gate
  is "Liora has decided Aeron is worth the meeting." That decision is
  informed by Aeron's Act 4 treatment of her — specifically the `a4`
  beats where Liora appears. TODO: identify the 2–3 OB scenes that
  should feed into Liora's trust decision.
- Liora does the introduction herself. Her register is NOT Selene's.
  She is colder, more transactional. She tells Aeron in the first
  line that this meeting is a favor she is doing against her better
  judgment, and that the favor is not renewable.
- Liora stays in the room the whole scene. She is not witness — she
  is chaperone.

## 2. THE SHARED GATE — THE TEST

The gate has TWO halves. Both must be true for the full reveal.

### Gate half A — the a1_s20 choice

- `a1_s20_lower_spans` has a choice_and_dev factor=1 branch where
  Aeron either `reassured_child` or `ignored_child` the small girl
  between the pipes.
- Gate condition: `scene_has("a1_s20_lower_spans", "reassured_child")`
- If the player chose `ignored_child`, Gate A fails and the scene
  ends on a partial-meeting branch. No reveal.

### Gate half B — the memory

- Soren does not know her own story all the way to the bottom. She
  knows her father's name (Kael), she knows her mother's name (Rava),
  she knows Aeron is her uncle, she knows Aeron led the sweep that
  killed her mother. She has been told all of this by the people
  who raised her.
- What she does not know: whether Aeron was the kind of soldier who
  would have stopped for her in the Lower Spans when she was four.
- Her test is a single question: *"Do you remember me?"*
- The question has to be asked cold. She does not prime it. She does
  not say "from the Lower Spans" or "from Sector 10" or "when I was
  four." She just asks.
- Gate B succeeds if Aeron's response includes an unprompted
  recollection of the Lower Spans child-between-pipes encounter.
  The player triggers this by selecting a dialogue option that
  reads "The Lower Spans. A child between two pipes. I stopped."
- Gate B fails if the player selects any other option — including
  options that sound sympathetic but do not recall the specific
  encounter.

### What happens on partial failure

- If Gate A is false: Soren does not ask the question. The scene
  ends on a brief, cold exchange — she looks at him, she says
  something about the shape of his face, she leaves. No reveal.
- If Gate A is true but Gate B fails: Soren asks the question, Aeron
  answers generically, Soren accepts the answer the way a child
  accepts an adult's inability to see them. The scene ends with
  Soren saying "okay" in the exact tone a child uses when she has
  just learned that the adult in front of her is not going to be
  the adult she needed. No reveal.
- If both gates succeed: the full reveal happens. Soren tells Aeron
  her mother's last instruction — *"Some soldiers still got hearts.
  If one stops and looks you in the face, you remember his face."*
  She tells him she has been remembering his face for seven years.
  She tells him her mother had seen him before. She tells him her
  mother recognized his jaw as Kael's jaw. She gives him his
  brother's family back in a sentence no scene has prepared him
  to hear.

## 3. SCENE BEATS — HIGH LEVEL

1. **Threshold.** Aeron is brought to the door. Whoever brought him
   (Selene EMP / Liora OB) opens it. He does not cross. The camera
   holds on the doorway.
2. **Soren seen.** First visual: an eleven-year-old girl sitting at a
   small table. She has Kael's hairline. She has Rava's shoulders.
   She does not stand. She does not look up. She knows he is there.
3. **Introduction.** The bringer introduces him. One line. No
   elaboration. Then the bringer steps back — EMP Selene to the wall,
   OB Liora to the corner.
4. **The stillness.** Aeron's entry. He does not sit unless invited.
   She does not invite him. He stands.
5. **The question.** Soren looks up. She asks: *"Do you remember me?"*
6. **The gate resolves.** Player-facing dialogue options surface here.
   See §2 for the gate branching.
7. **On full reveal:** Soren delivers Rava's instruction and the
   family-resemblance recognition. Aeron carries the weight of the
   sweep. The scene does not offer him absolution. It offers him the
   truth.
8. **On partial:** Scene ends. Soren says "okay." Aeron is walked
   out by the bringer. The scene is over.
9. **Departure.** Regardless of branch, the bringer walks Aeron out.
   EMP Selene does not speak on the way out until they are outside
   the building. OB Liora speaks only to say "that was the favor."

## 4. BLOCKING AND TONE NOTES

- **Soren is eleven. Not a miniature adult.** She speaks the way a
  child speaks when a child has had to carry too much. Short
  sentences. Small gestures. She does not perform.
- Aeron should NOT cry on-camera in this scene regardless of branch.
  Whatever he is feeling, the scene's discipline is that he holds it.
  The scene is about Soren's test, not Aeron's catharsis.
- The bringer (Selene or Liora) should NOT speak during the test.
  Their silence is load-bearing. If either of them speaks during the
  test the scene collapses into an adult scene, not a child's scene.
- Lighting: low, warm, not candlelight. Practical room light. The
  scene is not sacred — it is ordinary, and the ordinariness is the
  point. A kitchen table. A cup. A window with an Outlands view.

## 5. AFTERMATH HOOKS

- On full reveal: a follow-up scene is needed where Aeron processes
  with whichever LI is strongest at the moment. The canonical default
  is Selene (she was the bringer on EMP and she has been holding the
  compartment the longest). On OB, the processing scene should be
  with whichever of Aeron's OB-aligned LIs is trust-highest at the
  moment.
- On partial: no follow-up processing scene. The partial is its own
  punishment. The player earned it.
- The Lower Spans encounter becomes retroactively the most important
  choice in the game. A future pass may want to add a faint
  acknowledgment of this — maybe a line in the final Act V epilogue
  that references the Lower Spans in passing — but this outline does
  not prescribe it.

## 6. OPEN QUESTIONS FOR LATER

- Who physically lives with Soren in the Outlands safe house? Is it a
  single guardian, a small family, a communal arrangement? The
  answer shapes how the threshold beat is staged.
- Does Soren know Kael's survival story (the fall, the maintenance
  tunnel, the nine years)? Probably yes — Liora knew and would have
  told her. But the scene does not require her to bring it up.
- Is there a version of this scene where Soren is hostile rather than
  still? The current design bets on stillness. A hostile variant
  would change the whole tone. Decision deferred until the scene is
  actually written.
- What does Soren call Aeron? "Aeron" (by name), "sir" (protective),
  "uncle" (after the reveal)? Default assumption: she calls him
  nothing until after the gate resolves, and then — only on full
  reveal — she calls him by his first name once.

## 7. DO-NOT-DO LIST

- Do not have Aeron recognize Soren on sight. He has no reason to.
- Do not have Soren forgive Aeron. She is eleven. Forgiveness is not
  hers to give and the scene should not ask her to give it.
- Do not put Selene and Liora in the same room for this scene. They
  do not need to meet here. The bringer is one OR the other, not both.
- Do not reveal the fall (Kael's miles-long rooftop survival) for the
  first time in this scene. That reveal has already happened in
  `a4_s10` EMP. On OB, Liora will have handled that separately.
- Do not use Old Tongue vocabulary in the test. Soren was raised in
  the Outlands, not the Cathedral. She does not speak Lyra's register.
