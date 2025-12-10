let luz = 0
let nyan_sonando = false
let alegre_sonando = false
let funebre_sonando = false
let temp = 0
basic.forever(function () {
    luz = input.lightLevel()
    if (luz > 200) {
        if (!(alegre_sonando)) {
            music.stopAllSounds()
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Entertainer), music.PlaybackMode.InBackground)
            alegre_sonando = true
            funebre_sonando = false
            nyan_sonando = false
        }
    } else if (luz < 100) {
        if (!(funebre_sonando)) {
            music.stopAllSounds()
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Funeral), music.PlaybackMode.InBackground)
            funebre_sonando = true
            alegre_sonando = false
            nyan_sonando = false
        }
    } else if (!(nyan_sonando)) {
        music.stopAllSounds()
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Nyan), music.PlaybackMode.InBackground)
        nyan_sonando = true
        alegre_sonando = false
        funebre_sonando = false
    }
})
loops.everyInterval(200, function () {
    temp = input.temperature()
    if (temp > 22) {
        basic.showString("Calor")
    } else {
        basic.showString("Fred")
    }
})
