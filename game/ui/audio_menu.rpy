init python:
    # dedicate ambience channels so they can sit under 'music'.
    # The channels dict check is the public Ren'Py 8.x way to detect
    # whether a channel is already registered — older get_all_channel_names()
    # helper was removed somewhere between 7.x and 8.4.
    _registered_channels = getattr(renpy.audio.audio, "channels", {})
    if "ambient" not in _registered_channels:
        renpy.music.register_channel("ambient",  mixer="sfx", loop=True, stop_on_mute=True)
    if "ambient2" not in _registered_channels:
        renpy.music.register_channel("ambient2", mixer="sfx", loop=True, stop_on_mute=True)

    # sensible default levels
    renpy.music.set_volume(0.70, channel="music")     # menu pad
    renpy.music.set_volume(0.35, channel="ambient")   # rain
    renpy.music.set_volume(0.25, channel="ambient2")  # city hum

    def _menu_track_for_act(act):
        return {
            1: "audio/music/menu_act1.ogg",
            2: "audio/music/menu_act2.ogg",
            3: "audio/music/menu_act3.ogg",
            4: "audio/music/menu_act4.ogg",
            5: "audio/music/menu_act5.ogg",
        }.get(act, "audio/music/menu_act1.ogg")

    def enter_main_menu_audio():
        # pick track by your global current_act
        track = _menu_track_for_act(globals().get("current_act", 1))
        renpy.music.play(track, channel="music", loop=True, fadein=1.5)
        renpy.music.play("audio/ambience/rain_loop.ogg", channel="ambient", loop=True, fadein=1.5)
        renpy.music.play("audio/ambience/city_hum.ogg", channel="ambient2", loop=True, fadein=1.5)

    def exit_main_menu_audio():
        renpy.music.stop(channel="ambient", fadeout=0.8)
        renpy.music.stop(channel="ambient2", fadeout=0.8)
        # let music crossfade into in-game if you start; otherwise stop as needed later

    # `config.enter_main_menu_callbacks` was removed somewhere before
    # Ren'Py 8.4. We stash the helpers on the store and call them
    # manually from the main_menu screen and from a screen-hide hook
    # if/when audio assets are actually present. No error-throwing
    # registration at init time.
    renpy.store.enter_main_menu_audio = enter_main_menu_audio
    renpy.store.exit_main_menu_audio  = exit_main_menu_audio
