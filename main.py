def on_button_pressed_a():
    global Player1, rounds
    Player1 += 1
    basic.show_leds("""
        . # # # .
                . # . # .
                . # # # .
                . # . # .
                . # . # .
    """)
    rounds += 1
    updateScores()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global ties, rounds
    ties += 1
    basic.show_leds("""
        # # # # #
                . . # . .
                . . # . .
                . . # . .
                . . # . .
    """)
    rounds += 1
    updateScores()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global player2, rounds
    player2 += 1
    rounds += 1
    basic.show_leds("""
        # # # . .
                # . . # .
                # # # . .
                # . . # .
                # # # . .
    """)
    updateScores()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    reset()
    basic.show_string("\"Shall we play a game\"")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def updateScores():
    OLED.clear()
    OLED.write_string_new_line("Player1;" + ("" + str(Player1)))
    OLED.new_line()
    OLED.write_string_new_line("Player2" + ("" + str(player2)))
    OLED.new_line()
    OLED.write_string_new_line("rounds" + ("" + str(rounds)))
    OLED.new_line()
    OLED.write_string_new_line("ties" + ("" + str(ties)))
def reset():
    global ties, rounds, player2, Player1
    ties = 0
    rounds = 0
    player2 = 0
    Player1 = 0
    OLED.init(128, 64)
    OLED.write_string_new_line("\"Shall we play a game\"")
    basic.pause(2000)
    updateScores()
player2 = 0
ties = 0
rounds = 0
Player1 = 0
reset()