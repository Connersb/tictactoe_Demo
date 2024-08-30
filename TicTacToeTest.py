from ticTacToeEasyAI import easy
from ticTacToeMediumAI import medium
from ticTacToeHardAI import hard
from ticTacToe2Players import twoPlayers
from turtleHelp import *
from turtle import *


# players = input("1 player or 2 player: ")
players = textinput('', '1 player or 2 players?')
if players == '1':
    while True:
        reset()
        drawboard()
        difficultly = textinput('', "Easy, medium, or hard AI? ")
        if difficultly.lower() == 'e':
            easy()
            if textinput('', 'Would you like to play again? (y/n) ') == 'n':
                break
        elif difficultly.lower() == 'm':
            medium()
            if textinput('', 'Would you like to play again? (y/n) ') == 'n':
                break
        elif difficultly.lower() == 'h':
            hard()
            if textinput('', 'Would you like to play again? (y/n) ') == 'n':
                break
        else:
            textinput('', 'Incorrect format of entry. Please type e for easy, m for medium, or h for hard.')
else:
    while True:
        reset()
        drawboard()
        twoPlayers()
        if textinput('', 'Would you like to play again? (y/n) ') == 'n':
            break
textinput('', 'Thanks for playing')