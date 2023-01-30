function updateScores () {
    OLED.clear()
    OLED.writeStringNewLine("Player1;" + Player1)
    OLED.newLine()
    OLED.writeStringNewLine("\"player2\";" + player2)
    OLED.newLine()
    OLED.writeStringNewLine("\"rounds" + rounds)
    OLED.newLine()
    OLED.writeStringNewLine("\"ties\"" + ties)
}
let Player1 = 0
let player2 = 0
let rounds = 0
let ties = 0
ties = 0
rounds = 0
player2 = 0
Player1 = 0
OLED.init(128, 64)
OLED.writeStringNewLine("\"Shall we play a game\"")
basic.pause(2000)
updateScores()
