from turtle import *
from turtleHelp import *


def twoPlayers():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    count = 0
    checker1 = False
    checker2 = False
    for i in board:
        print(i)
    while True:
        if count % 2 == 0:
            helpMe = True
            while helpMe:
                try:
                    spot = textinput('Player 1', "Enter row and column")
                    spot = spot.split()
                    if board[int(spot[0])][int(spot[1])] == 0:
                        helpMe = False
                    else:
                        textinput('Player 1', 'Invalid point. \nHit Enter to try again')
                except:
                    textinput('Player 1', "Bad entry")
            board[int(spot[0])][int(spot[1])] = 1
            drawMove(int(spot[0]), int(spot[1]), 1)
        else:
            helpMe = True
            while helpMe:
                try:
                    spot = textinput('Player 2', "Enter row and column")
                    spot = spot.split()
                    if board[int(spot[0])][int(spot[1])] == 0:
                        helpMe = False
                    else:
                        textinput('Player 2', 'Invalid point. \nHit Enter to try again')
                except:
                    textinput('Player 2', "Bad entry")
            board[int(spot[0])][int(spot[1])] = 2
            drawMove(int(spot[0]), int(spot[1]), 2)
        if board[0][0] * board[0][1] * board[0][2] == 1:
            checker1 = True
        elif board[1][0] * board[1][1] * board[1][2] == 1:
            checker1 = True
        elif board[2][0] * board[2][1] * board[2][2] == 1:
            checker1 = True
        elif board[0][0] * board[1][0] * board[2][0] == 1:
            checker1 = True
        elif board[0][1] * board[1][1] * board[2][1] == 1:
            checker1 = True
        elif board[0][2] * board[1][2] * board[2][2] == 1:
            checker1 = True
        elif board[0][0] * board[1][1] * board[2][2] == 1:
            checker1 = True
        elif board[0][2] * board[1][1] * board[2][0] == 1:
            checker1 = True
        if sum(board[0]) == 6:
            checker2 = True
        elif sum(board[1]) == 6:
            checker2 = True
        elif sum(board[2]) == 6:
            checker2 = True
        elif board[0][0] + board[1][0] + board[2][0] == 6:
            checker2 = True
        elif board[0][1] + board[1][1] + board[2][1] == 6:
            checker2 = True
        elif board[0][2] + board[1][2] + board[2][2] == 6:
            checker2 = True
        elif board[0][0] + board[1][1] + board[2][2] == 6:
            checker2 = True
        elif board[0][2] + board[1][1] + board[2][0] == 6:
            checker2 = True
        for i in board:
            print(i)
        if checker1:
            textinput('', 'Player 1 wins')
            break
        elif checker2:
            textinput("", 'Player 2 wins')
            break
        number = 0
        for i in board:
            if 0 not in i:
                number += 1
        if number == 3:
            for i in board:
                print(i)
            textinput('', 'Game over: Tie')
            break
        else:
            count += 1