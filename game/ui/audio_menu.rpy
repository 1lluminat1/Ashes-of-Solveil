init python:
    # dedicate an ambience channel so it can sit under 'music'
    if "ambient" not in renpy.audio.audio.get_all_channel_names():
        renpy.music.register_channel("ambient", mixer="sfx", loop=True, stop_on_mute=True)
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

    config.enter_main_menu_callbacks.append(enter_main_menu_audio)
    config.exit_main_menu_callbacks.append(exit_main_menu_audio)
