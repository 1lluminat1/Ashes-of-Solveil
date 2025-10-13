# act1_21_purge.rpy


# =======================================================
# ACT 1 - Scene 21: The Rooftop → The Purge (Act I Finale)
# =======================================================

label act1_purge:
    # VISUAL: Rooftop — night sky above Solveil; high balcony rail; glass parapets.
    # LIGHTING: Cold blue ambient; faint neon bounce from below.
    # SOUND: Low wind; distant engine thrum; far airship beacon.

    "{i}The rooftop is quiet. Just wind and distant engines. The city doesn't sleep... but tonight, he needs silence.{/i}"

    a "{i}I used to think the stars looked brighter from up here.{/i}"
    a "{i}Maybe that was only when we stood here together...{/i}"

    # SOUND: Door servo whisper.
    # VISUAL: Lyra's silhouette in doorway; corridor neon frames her.
    l "(softly) Do you think the city ever grows tired of listening to us?"
    a "(without turning) I thought you left hours ago."
    l "(approaches slowly) I did. Then I came back."
    a "Why?"
    l "(shrugs) Something told me you would be up here."

    # BLOCKING: She joins him at the rail; both looking outward, shoulder-width apart.
    l "We used to come up here, remember?"
    a "I remember everything."
    l "Even the good parts?"
    a "(quietly) Especially the good parts."
    l "(barely audible) Then perhaps they are not gone."

    # VISUAL: Silence settles between them—not awkward, just... present.
    "{i}They stand in silence. Not the heavy kind. The kind that doesn't need filling.{/i}"

    # VISUAL: Lyra's hand rests on the rail, inches from Aeron's.
    # LIGHTING: Neon light traces the edge of her fingers; close but not touching.
    "{i}Her hand rests near his. Close. Not touching. Almost.{/i}"

    l "(quietly) I lied earlier."
    a "(glances at her) About what?"
    l "When I said I came back because something told me you would be here."
    a "Then why?"
    l "(pause) Because I could not stop thinking about you standing at the edge."

    # VISUAL: Aeron's breath catches; doesn't respond immediately.
    "{i}The words land heavier than they should.{/i}"

    a "(carefully) I wasn't going to jump."
    l "Were you not?"
    a "...I don't know."
    l "(turns to face him) That frightens me more than if you had said yes."

    # VISUAL: Their eyes meet—longer than usual; something unspoken passing between them.
    "{i}Her eyes catch the city lights. Violet and amber. Human.{/i}"
    a "{i}When did I forget how to look at her without the weight of everything else?{/i}"

    l "You asked me once what I see when I look at this city."
    a "You said a room drunk on power."
    l "I did. But that is not all I see."
    a "What else?"
    l "(softly) You. Still here. Still breathing. Still fighting even when you pretend you are not."

    # VISUAL: Her hand shifts—just slightly—closer to his.
    "{i}Her fingers move. Barely. The distance between them shrinks.{/i}"

    a "(voice low) You give me too much credit."
    l "Perhaps. Or perhaps you do not give yourself enough."

    # VISUAL: The wind picks up; her hair moves across her face; she doesn't brush it away.
    "{i}Wind stirs her hair. She doesn't move. Neither does he.{/i}"

    a "Lyra—"
    l "Yes?"

    # VISUAL: He almost speaks—words forming, dying, forming again.
    "{i}The words are there. Right there. All he has to do is say them.{/i}"

    # ACTION: Player choice—reach for her hand or stay still.
    menu:
        "The space between their hands feels infinite and nonexistent at once."
        "Reach for her hand.":
            $ aeron_reached_for_lyra = True
            # VISUAL: His hand moves—slow, deliberate—covers hers on the rail.
            "{i}His hand moves. Covers hers. Warm against the cold metal.{/i}"
            # VISUAL: She doesn't pull away; her fingers curl slightly, accepting.
            "{i}She doesn't pull away. Her fingers shift. Not rejection. Acceptance.{/i}"
            l "(barely a whisper) Aeron..."
            a "I'm still here."
            l "I know."
            "{i}For a moment, the city disappears. Just two people. Just this.{/i}"

        "Stay still.":
            $ aeron_reached_for_lyra = False
            "{i}He doesn't move. The moment stretches. Fragile.{/i}"
            a "(quietly) Thank you. For coming back."
            l "(nods) Always."
            "{i}The words are enough. Almost.{/i}"

    # VISUAL: Lyra looks out over the city; profile lit by distant towers.
    l "When this is over... when the gala ends and the orders stop..."
    a "What then?"
    l "(pause) I do not know. But I think... I would like to find out."

    # VISUAL: Aeron's expression softens—just slightly; hope, fragile and new.
    a "{i}Maybe there's still something worth staying for.{/i}"
    a "(softly) Yeah. Me too."

    # VISUAL: They stand together—closer than before; city sprawling below.
    "{i}For a breath, the city feels smaller. Just two people on a roof.{/i}"

    # --- EXTENDED BREATH BEFORE THE PURGE ---
    # SOUND: A deep mechanical undertone joins — sub-bass grid resonance, almost rhythmic.
    "{i}A low hum threads through the air — not weather, not traffic. The kind of sound the city makes when it's holding its breath.{/i}"
    l "(soft) Do you hear that?"
    a "Power reroutes. Central grid recalibration, maybe."
    l "No. This tone is older. It precedes resets... or strikes."
    a "You sound like my father."
    l "(faint smile) Then perhaps he is right about one thing. The city breathes before it kills."

    # VISUAL: Far towers blink in sequence: red → white → red. Visible static on glass edges.
    a "{i}The towers blink — a pattern. Almost deliberate.{/i}"
    a "You ever wonder if it dreams?"
    l "Solveil?"
    a "The city. All this light and sound... it feels alive sometimes."
    l "(quietly) Maybe it dreams of silence."
    a "Then we're its nightmare."

    # CAMERA: Hold on their hands at the railing; subtle vibration.
    "{i}A soft tremor crawls through the steel beneath their fingers.{/i}"
    l "(uneasy) That is new."

    # --- THE PURGE ERUPTS (NO TRANSITION) ---
    # LIGHTING FX: Horizon flash — cold white bloom → hard red wash; sequence travels spire to spire.
    "{i}A flash blooms on the horizon — white, then red. Another follows. Then the sky itself shifts.{/i}"
    a "(tense) That's no storm."
    # SOUND: Deep mechanical roar rolls across the skyline; distant pressure wave.
    "{i}A pulse races down the spires, each tower answering in turn like a lit fuse.{/i}"
    l "(staring) Grid surge across every line... what are they—?"

    # VFX: Low cloud deck ignites from below; under-cloud glow floods upward.
    "{i}The Unders ignite. Light punches through the clouds — for one instant, the world below glows like a furnace.{/i}"
    a "(hoarse) They're purging the lower sectors."

    # CITY BROADCAST: Marcus over wideband; processed, ceremonial.
    # SOUND: Civic siren motif underneath; authoritative reverb.
    m "By order of the Council of Echelon, Sectors Eight through Ten are under immediate quarantine."
    m "All unregistered citizens will be purged to preserve city integrity."
    m "Order above all. Unity before self."

    # LIGHTING: Firelight climbs the glass; ash starts to fall.
    l "(shaken) No... that cannot be—"
    a "That's his voice."
    l "They said it was a containment sweep—"
    a "Containment doesn't scream."

    # CAMERA: Slow orbit around them; balcony bathed in orange; reflected flame cascades.
    "{i}Below, structures convulse and fold. Fire crawls upward like breath exhaled from hell.{/i}"
    a "{i}Order above all...{/i}"
    a "Is that what peace looks like, Father? Burning the world to keep it obedient?"
    a "{i}The chip burns cold in my pocket. She said it was the truth.{/i}"
    a "{i}Maybe it's time I find out what kind of truth leaves this much ash behind.{/i}"

    # PROP FX: Ash flecks on coat shoulders; stray ember drifts past.
    l "(broken) Aeron— look away."
    a "I won't."

    # SOUND: Sirens layer and rise; distant detonations; wind hardens.
    "{i}A thousand mechanical voices coil through the skyline. The light devours everything beneath the clouds.{/i}"

    a "(low) You see it now. This is what obedience becomes."
    l "(trembling) And if we speak out—?"
    a "Then we burn with them."

    # CAMERA: Tight on Aeron's eyes — fire mirrored; resolve forms.
    "{i}The fires mirror in his eyes. Not fear — awakening.{/i}"

    a "{i}From above, it almost looks clean.{/i}"
    a "{i}But it's only clean because it burns everything beneath it.{/i}"
    a "{i}And I'm done pretending not to see.{/i}"

    # FINAL IMAGE: Extreme wide — two silhouettes against the inferno; banners ripple; towers thrum.
    # SOUND: Low, endless city hum under the roar, like a machine satisfied.
    "{i}The city burns. The towers hum. And in the glow of a dying night, something inside him finally breaks free.{/i}"

    a "{i}I know what I have to do now.{/i}"

    # FADE OUT — END OF ACT I

    return