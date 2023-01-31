input.onButtonPressed(Button.A, function () {
    Player1 += 1
    basic.showLeds(`
        . # # # .
        . # . # .
        . # # # .
        . # . # .
        . # . # .
        `)
    rounds += 1
    updateScores()
})
input.onButtonPressed(Button.AB, function () {
    ties += 1
    basic.showLeds(`
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        `)
    rounds += 1
    updateScores()
})
input.onButtonPressed(Button.B, function () {
    player2 += 1
    rounds += 1
    basic.showLeds(`
        # # # . .
        # . . # .
        # # # . .
        # . . # .
        # # # . .
        `)
    updateScores()
})
input.onGesture(Gesture.Shake, function () {
    reset()
    basic.showString("\"Shall we play a game\"")
})
function updateScores () {
    OLED.clear()
    OLED.writeStringNewLine("Player1;" + ("" + Player1))
    OLED.newLine()
    OLED.writeStringNewLine("Player2" + ("" + player2))
    OLED.newLine()
    OLED.writeStringNewLine("rounds" + ("" + rounds))
    OLED.newLine()
    OLED.writeStringNewLine("ties" + ("" + ties))
}
function reset () {
    ties = 0
    rounds = 0
    player2 = 0
    Player1 = 0
    OLED.init(128, 64)
    OLED.writeStringNewLine("\"Shall we play a game\"")
    basic.pause(2000)
    updateScores()
}
let player2 = 0
let ties = 0
let rounds = 0
let Player1 = 0
reset()
