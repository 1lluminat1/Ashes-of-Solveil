# =======================================================
# ACT 2 - Scene 28: Selene Finale (OB)
# File: a2_s28_selene_finale_ob.rpy
# Act 2 closer. Execution. The point of no return.
# =======================================================

# ========= SCENE START TASKS =========
$ _current_scene_id = "a2_s28_selene_finale_ob"
$ scene_mark(_current_scene_id, "entered")

label a2_s28_selene_finale_ob:

    # ========= STAGE DIRECTIONS (cinema-first) =========
    # CAMERA: 50mm, locked. Same framing as EMP — the contrast is deliberate. Same room. Same table.
    #         Different ending. Push-in on Selene during "I will not follow you."
    #         THE SHOT: Camera on Aeron's hand. Then on Selene's face. Then silence.
    #         After: wide shot. The body. The witnesses. The closed door. Hold for 5 seconds. No cuts.
    # LIGHTING: Morning. But colder than the EMP version — the overhead strips winning over the amber.
    #           After the shot: the light doesn't change. That's the horror. The world doesn't react.
    # SFX: The gunshot. Then tinnitus ring. Then Tessa's sobbing. Then nothing.
    #       The door hiss when Aeron leaves is the last sound.
    # FACE: Selene wounded but hard. Aeron controlled. The team watching something break.
    #        After: Lyra's hand over her mouth. Zira frozen. Noelle staring. Tessa on the floor.

    # ========== THE STRATEGY CHAMBER — MORNING ==========

    "The strategy chamber. Same walls. Same table. Same faces."

    "But something is different today. Not the edge of crisis. Something worse. Something personal."

    # VISUAL: Selene enters last. Wound visible. Tessa moves to help. Selene waves her off — sharper than the EMP version.
    sel "I won't sit this out because I'm bleeding. We don't have that luxury."

    "Every step costs her something. She doesn't let it show."

    athought "Yesterday she threw herself in front of a bullet meant for a private. Someone whose name I didn't know."
    athought "Sentimental. The kind of decision that gets commanders killed."

    "She reaches the table. Braces against it. Looks up."

    sel "I called you all here because something needs to be said."

    # ========== THE ACKNOWLEDGMENT THAT CURDLES ==========

    sel "I've watched you change, Aeron."

    "Her voice is calm. Not warm — certain."

    sel "Yesterday, you made calls that kept the operation intact. You stepped into command when the line wavered."

    athought "I meet her gaze. I don't look away."

    sel "But the way you did it..."

    "Her voice hardens. The acknowledgment curdles."

    sel "You treated them like numbers. Acceptable losses in a calculation."

    a "We can't afford hesitation. Every second of delay costs lives."

    sel "And every life you sacrifice 'efficiently' costs us something we can't get back."

    "She steps forward despite the wound. Hand braced against the table, knuckles white."

    sel "You're starting to sound like them. Like the people we swore to burn."

    # ========== THE ROOM FRACTURES ==========

    l "Selene..."

    "Lyra's voice is soft. Trying to find middle ground."

    l "Aeron has been under enormous pressure. We all have. Maybe this isn't—"

    sel "This is exactly the time, Lyra. Before it goes any further."

    l "He's not... he's still—"

    a "Lyra. Enough."

    "She falls silent."

    z "Okay, can we all take a breath here?"

    "Zira pushes off from the wall."

    z "Selene, you're bleeding. Aeron, you're being a hardass. Both of those things can be true without—"

    sel "This isn't about his tone. It's about his direction."

    z "And what direction is that? Winning?"

    sel "Winning means nothing if we become what we're fighting."

    z "Tell that to the people in Sector 8 who got purged while we were still debating ethics."

    "Selene stares at her. Something flickers — disappointment."

    sel "Then I've already lost more than I knew."

    t "Please. Can this wait? Selene, you nearly died yesterday—"

    sel "No, Tessa. It can't."

    "Her voice softens for a moment when she looks at Tessa. Just a moment."

    sel "If I wait, it will be too late."

    t "Too late for what?"

    sel "To stop him from becoming something we can't come back from."

    "Tessa looks at Aeron. Eyes pleading — for him to say something. To prove Selene wrong."

    athought "I don't."

    n "If the two of you fracture command here, internal collapse probability exceeds sixty percent within thirty days."

    sel "This isn't about tactics, Noelle."

    n "Everything is about tactics. You're both treating this as a moral question when it's structural. The rebellion cannot sustain divided leadership."

    a "Then the division needs to end."

    "Noelle pauses. Looks at him. Something shifts — the first flicker of concern."

    n "...That is not what I meant."

    # ========== THE LINE ==========

    sel "Aeron."

    "She straightens. The pain costs her."

    sel "I've given nineteen years to this rebellion. I've buried friends. I've made choices that still wake me at night."

    sel "I've earned the right to draw a line."

    sel "If you keep down this path, I will not follow you."

    "The room goes cold."

    sel "I won't ask anyone here to follow you."

    "Her eyes move to the others. To Lyra. To Tessa. To Zira."

    sel "I won't watch you drag them into the same pit that made Echelon."

    sel "I will call the council. And I will relieve you of field command."

    athought "I watch the faces around the room."
    athought "Lyra — torn. Zira — calculating. Tessa — afraid. Noelle — frozen."
    athought "Some of them are considering it."
    athought "That is unacceptable."

    a "You would fracture command in the middle of a war."

    sel "I will fracture anything I have to before I watch you rebuild what we swore to burn."

    "She steps toward him. One step. Despite the wound."

    sel "If I have to stand between you and this path, I—"

    # ========== THE SHOT ==========

    # SOUND: Single gunshot. Close. Final.
    # VISUAL: Camera on Aeron's hand. Then on Selene's face — the fraction of a second before.
    # She sees it coming. She doesn't move. She stands her ground.

    "The gun is in his hand."

    athought "I don't remember drawing it."

    "Her eyes meet his in the fraction of a second before the trigger pulls."

    "She sees it coming."

    "She doesn't move."

    "She stands her ground."

    "And then she doesn't stand at all."

    # SOUND: Cut to tinnitus ring. All ambient drops.
    pause 0.3

    "The sound of the shot swallows everything."

    "She falls."

    "Blood on the edge of the table. Her body on the floor. The room frozen."

    # ========== THE SILENCE ==========

    pause 2.0

    "Lyra has her hand over her mouth. Eyes wide. Fixed on the body. She is not breathing."

    "Zira is frozen mid-step. Her eyes are on the gun. She's running scenarios — odds, exits. None of them end with her winning this room."

    "Noelle is staring at the body with an expression she has never worn. Like an equation that doesn't solve."

    "Nobody speaks. Nobody challenges. Nobody moves."

    # ========== TESSA ==========

    "Tessa breaks first."

    "She drops to her knees beside the body. Hands moving automatically — checking pulse, assessing damage. The medic taking over while the woman retreats somewhere safe."

    t "Selene? Selene, stay with me—"

    "Her hands go still."

    "She looks at the wound. At the blood. At the absolute stillness."

    "She knows."

    "Her hands move to Selene's face. Slowly. Gently."

    "She closes Selene's eyes."

    "Then her shoulders begin to shake."

    "The sound that comes out of her is not a scream. Not a word. Something broken — a sob that tears itself out and doesn't stop."

    # ========== AERON ==========

    "He holsters the weapon. Slow. Deliberate."

    "He looks at each of them in turn."

    "Lyra. Zira. Noelle. Tessa, sobbing over the body."

    "They watched. They did not stop him."

    a "We cannot afford doubt in command."

    athought "My voice is steady. Cold."

    a "Selene forgot that."

    "No one answers."

    a "This rebellion stands, or it dies with her."

    "He turns his back on the body. On the blood. On the woman who took a bullet for a nobody yesterday and died for her principles today."

    "His footsteps are the only sound in the room except for Tessa's weeping."

    "At the door, he pauses."

    a "Prepare the body for burial. We'll need a story for the others."

    athought "I don't look back."
    athought "I don't need to."

    athought "Four witnesses. Four people who could expose me, challenge me, end this right now."

    athought "Four people who will not."

    athought "By tomorrow, they will have chosen their reasons. By the funeral, they will believe them."

    athought "That is how it works. That is how it has always worked."

    "The door hisses shut."

    "On the other side, he can still hear Tessa crying."

    "He keeps walking."

    pause 2.0

    # ========== ACT CLOSE ==========

    scene black with fade

    centered "{size=+20}END OF ACT II{/size}"
    pause 1.0
    centered "{size=+10}The Iron Accord{/size}"
    pause 2.0
    scene black with fade

    # ========== STATE UPDATES ==========

    $ canon_set("selene_alive", False)
    $ canon_set("selene_killed_by_aeron", True)
    $ canon_set("shared_command", False)
    $ flag("lis_witnessed_execution", True)
    $ npc_remember("Lyra", "witnessed_selene_execution", tone="horror")
    $ npc_remember("Zira", "witnessed_selene_execution", tone="calculating")
    $ npc_remember("Noelle", "witnessed_selene_execution", tone="unsolvable")
    $ npc_remember("Tessa", "witnessed_selene_execution", tone="broken")
    $ flag("act2_complete", True)
    $ scene_mark(_current_scene_id, "completed")

    return


# ========= CANONICAL NOTES =========
# cann.scene_id: a2_s28_selene_finale_ob
# cann.chapter: Act II, Chapter IV — The Cost
# cann.chapter_start: False
# cann.when_in_timeline:
#   - Morning after the raid and Zira commitment (OB) scene. Act 2 finale.
#   - OB path. Selene alive but wounded. She confronts Aeron. He kills her.
# cann.what_happened:
#   - Selene confronts Aeron about treating people as numbers. "You're starting to sound like them."
#   - Each team member reacts: Lyra defends, Zira argues pragmatism, Tessa pleads, Noelle warns of structural collapse.
#   - Selene draws the line: "I will relieve you of field command."
#   - Aeron shoots her. She sees it coming. She doesn't move.
#   - Tessa closes Selene's eyes. Breaks completely.
#   - Aeron walks out: "We cannot afford doubt in command."
#   - Four witnesses. None stop him. None challenge him.
#   - Subtitle: "The Iron Accord."
# cann.aeron_state:
#   - The OB journey culminates: from Glass to something worse than Marcus.
#   - "I don't remember drawing it." — the violence is reflexive, not calculated. That's scarier.
#   - "By tomorrow, they will have chosen their reasons." — he understands complicity perfectly.
#   - No remorse. No hesitation. The doctrine ate the man.
# cann.path_tracking:
#   - No player choice — this is the consequence of the OB path.
#   - canon_set("selene_alive", False), canon_set("selene_killed_by_aeron", True).
#   - All four LIs remember witnessing the execution with distinct emotional tones.
#   - flag("lis_witnessed_execution") gates all Act 3 OB dynamics.
#   - flag("act2_complete").
# cann.thematic_flags:
#   - "She stands her ground. And then she doesn't stand at all." — the scene's hinge.
#   - "I don't remember drawing it." — OB Aeron has become the machine. Violence as reflex.
#   - "Four witnesses. Four people who will not." — complicity as the OB thesis.
#   - "By tomorrow, they will have chosen their reasons." — how systems perpetuate themselves.
#   - Zira's silence: she chose him last night (commitment scene). She stays because she already chose.
#   - Tessa closing Selene's eyes: the healer performing the last act of care on someone she can't save.
#   - "On the other side, he can still hear Tessa crying. He keeps walking." — Act 2's final image.
# cann.character_moments:
#   - Selene: Stands her ground. Sees the gun. Doesn't move. Dies for her principles.
#     The woman who took a bullet for a nobody yesterday. Killed by the man she was trying to save.
#   - Tessa: Drops to her knees. Medic instinct takes over. Then she knows. Closes Selene's eyes.
#     The sob that "tears itself out" — same sound as the mercy death, but worse. No consent here.
#   - Lyra: Frozen. Hand over mouth. "Looking at me like she has never seen me before."
#   - Zira: Running scenarios. Doesn't draw. She chose him last night. That choice binds her now.
#   - Noelle: "Like an equation that doesn't solve." — her framework can't process this.
#   - Each witness's silence is a different kind of complicity. Each will justify it differently.
# cann.block_status:
#   - VARIANT (OB only). Act 2 finale. Point of no return.
# cann.requires_followup:
#   - Selene's death defines Act 3 OB. Every character processes the execution differently.
#   - Nyra arrives in Act 3 to fill the command vacuum. She validates what Aeron became.
#   - Tessa's board: Selene's name goes on the dead side. The name that breaks the system.
#   - Zira's commitment night becomes tragic context: "Don't make me regret it."
#   - Lyra's horror here is the seed of either her breaking or her resistance in Act 3.
#   - Noelle's "unsolvable equation" — she will try to rationalize it. She might not succeed.
#   - "We'll need a story for the others." — the cover-up itself becomes an Act 3 plot thread.
