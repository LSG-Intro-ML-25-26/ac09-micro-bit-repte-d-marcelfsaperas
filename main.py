temp = 0

alegre_sonando = False
funebre_sonando = False
nyan_sonando = False

def on_forever():
    global alegre_sonando, funebre_sonando, nyan_sonando
    luz = input.light_level()

    if luz > 200:
        if not alegre_sonando:
            music.stop_all_sounds()
            music._play_default_background(
                music.built_in_playable_melody(Melodies.ENTERTAINER),
                music.PlaybackMode.IN_BACKGROUND
            )
            alegre_sonando = True
            funebre_sonando = False
            nyan_sonando = False

    elif luz < 100:
        if not funebre_sonando:
            music.stop_all_sounds()
            music._play_default_background(
                music.built_in_playable_melody(Melodies.FUNERAL),
                music.PlaybackMode.IN_BACKGROUND
            )
            funebre_sonando = True
            alegre_sonando = False
            nyan_sonando = False

    else:
        if not nyan_sonando:
            music.stop_all_sounds()
            music._play_default_background(
                music.built_in_playable_melody(Melodies.NYAN),
                music.PlaybackMode.IN_BACKGROUND
            )
            nyan_sonando = True
            alegre_sonando = False
            funebre_sonando = False

basic.forever(on_forever)



def on_every_interval():
    global temp
    temp = input.temperature()
    if temp > 22:
        basic.show_string("Calor")
    else:
        basic.show_string("Fred")
loops.every_interval(200, on_every_interval)
