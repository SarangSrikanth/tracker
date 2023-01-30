def updateScores():
    OLED.clear()
    OLED.write_string_new_line("Player1;" + str(Player1))
    OLED.new_line()
    OLED.write_string_new_line("\"player2\";" + str(player2))
    OLED.new_line()
    OLED.write_string_new_line("\"rounds" + str(rounds))
    OLED.new_line()
    OLED.write_string_new_line("\"ties\"" + str(ties))
Player1 = 0
player2 = 0
rounds = 0
ties = 0
ties = 0
rounds = 0
player2 = 0
Player1 = 0
OLED.init(128, 64)
OLED.write_string_new_line("\"Shall we play a game\"")
basic.pause(2000)
updateScores()