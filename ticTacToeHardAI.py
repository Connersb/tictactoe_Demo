import math
import random
from turtle import *
from turtleHelp import *

def hard():
    checker = False
    count = 0
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    while True:
        helpMe = True
        while helpMe:
            try:
                spot = textinput('', 'Enter row and column')
                spot = spot.split()
                if board[int(spot[0])][int(spot[1])] == 0:
                    helpMe = False
                else:
                    textinput('', 'Invalid point. \nHit Enter to try again')
            except:
                textinput('', "Bad entry")
        board[int(spot[0])][int(spot[1])] = 1
        drawMove(int(spot[0]), int(spot[1]), 1)
        if sum(board[0]) == 3 or sum(board[0]) == 12:
            checker = True
        if sum(board[1]) == 3 or sum(board[1]) == 12:
            checker = True
        if sum(board[2]) == 3 or sum(board[2]) == 12:
            checker = True
        if board[0][0] + board[1][0] + board[2][0] == 3 or board[0][0] + board[1][0] + board[2][0] == 12:
            checker = True
        if board[0][1] + board[1][1] + board[2][1] == 3 or board[0][1] + board[1][1] + board[2][1] == 12:
            checker = True
        if board[0][2] + board[1][2] + board[2][2] == 3 or board[0][2] + board[1][2] + board[2][2] == 12:
            checker = True
        if board[0][0] + board[1][1] + board[2][2] == 3 or board[0][0] + board[1][1] + board[2][2] == 12:
            checker = True
        if board[0][2] + board[1][1] + board[2][0] == 3 or board[0][2] + board[1][1] + board[2][0] == 12:
            checker = True
        if checker:
            for i in board:
                print(i)
            textinput('', 'Game over: You Win!!!')
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
        if board[1][1] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        elif board[0][0] + board[0][2] + board[2][0] + board[2][2] == 1:
            if board[0][1] == 1:
                if board[0][0] == 0:
                    board[0][0] = 4
                    drawMove(0, 0, 2)
                elif board[0][2] == 0:
                    board[0][2] = 4
                    drawMove(0, 2, 2)
            elif board[1][0] == 1:
                if board[0][0] == 0:
                    board[0][0] = 4
                    drawMove(0, 0, 2)
                elif board[2][0] == 0:
                    board[2][0] = 4
                    drawMove(2, 0, 2)
            elif board[1][2] == 1:
                if board[0][2] == 0:
                    board[0][2] = 4
                    drawMove(0, 2, 2)
                elif board[2][2] == 0:
                    board[2][2] = 4
                    drawMove(2, 2, 2)
            elif board[2][1] == 1:
                if board[2][0] == 0:
                    board[2][0] = 4
                    drawMove(2, 0, 2)
                elif board[2][2] == 0:
                    board[2][2] = 4
                    drawMove(2, 2, 2)
        # trying to win
        # horizontal
        elif board[0][0] + board[0][1] == 8 and board[0][2] == 0:
            board[0][2] = 4
            drawMove(0, 2, 2)
        elif board[0][1] + board[0][2] == 8 and board[0][0] == 0:
            board[0][0] = 4
            drawMove(0, 0, 2)
        elif board[1][0] + board[1][1] == 8 and board[1][2] == 0:
            board[1][2] = 4
            drawMove(1, 2, 2)
        elif board[1][1] + board[1][2] == 8 and board[1][0] == 0:
            board[1][0] = 4
            drawMove(1, 0, 2)
        elif board[2][0] + board[2][1] == 8 and board[2][2] == 0:
            board[2][2] = 4
            drawMove(2, 2, 2)
        elif board[2][1] + board[2][2] == 8 and board[2][0] == 0:
            board[2][0] = 4
            drawMove(2, 0, 2)
        elif board[0][0] + board[0][2] == 8 and board[0][1] == 0:
            board[0][1] = 4
            drawMove(0, 1, 2)
        elif board[1][0] + board[1][2] == 8 and board[1][1] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        elif board[2][0] + board[2][2] == 8 and board[2][1] == 0:
            board[2][1] = 4
            drawMove(2, 1, 2)
        # vertical
        elif board[0][0] + board[1][0] == 8 and board[2][0] == 0:
            board[2][0] = 4
            drawMove(2, 0, 2)
        elif board[1][0] + board[2][0] == 8 and board[0][0] == 0:
            board[0][0] = 4
            drawMove(0, 0, 2)
        elif board[0][1] + board[1][1] == 8 and board[2][1] == 0:
            board[2][1] = 4
            drawMove(2, 1, 2)
        elif board[1][1] + board[2][1] == 8 and board[0][1] == 0:
            board[0][1] = 4
            drawMove(0, 1, 2)
        elif board[0][2] + board[1][2] == 8 and board[2][2] == 0:
            board[2][2] = 4
            drawMove(2, 2, 2)
        elif board[2][2] + board[1][2] == 8 and board[0][2] == 0:
            board[0][2] = 4
            drawMove(0, 2, 2)
        elif board[0][0] + board[2][0] == 8 and board[1][0] == 0:
            board[1][0] = 4
            drawMove(1, 0, 2)
        elif board[0][1] + board[2][1] == 8 and board[1][1] == 0:
            board[1][1] = 4
            drawMove(1, 2, 2)
        elif board[0][2] + board[2][2] == 8 and board[1][2] == 0:
            board[1][2] = 4
            drawMove(1, 2, 2)
        # corners
        elif board[0][0] + board[1][1] == 8 and board[2][2] == 0:
            board[2][2] = 4
            drawMove(2, 2, 2)
        elif board[1][1] + board[2][2] == 8 and board[0][0] == 0:
            board[0][0] = 4
            drawMove(0, 0, 2)
        elif board[0][2] + board[1][1] == 8 and board[2][0] == 0:
            board[2][0] = 4
            drawMove(2, 0, 2)
        elif board[2][0] + board[1][1] == 8 and board[0][2] == 0:
            board[0][2] = 4
            drawMove(0, 2, 2)
        elif board[0][0] + board[2][2] == 8 and board[1][1] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        elif board[0][2] + board[2][0] == 8 and board[1][1] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        # trying to block
        # horizontal
        elif board[0][0] + board[0][1] == 2 and board[0][2] == 0:
            board[0][2] = 4
            drawMove(0, 2, 2)
        elif board[0][1] + board[0][2] == 2 and board[0][0] == 0:
            board[0][0] = 4
            drawMove(0, 0, 2)
        elif board[1][0] + board[1][1] == 2 and board[1][2] == 0:
            board[1][2] = 4
            drawMove(1, 2, 2)
        elif board[1][1] + board[1][2] == 2 and board[1][0] == 0:
            board[1][0] = 4
            drawMove(1, 0, 2)
        elif board[2][0] + board[2][1] == 2 and board[2][2] == 0:
            board[2][2] = 4
            drawMove(2, 2, 2)
        elif board[2][1] + board[2][2] == 2 and board[2][0] == 0:
            board[2][0] = 4
            drawMove(2, 0, 2)
        elif board[0][0] + board[0][2] == 2 and board[0][1] == 0:
            board[0][1] = 4
            drawMove(0, 1, 2)
        elif board[1][0] + board[1][2] == 2 and board[1][1] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        elif board[2][0] + board[2][2] == 2 and board[2][1] == 0:
            board[2][1] = 4
            drawMove(2, 1, 2)
        # vertical
        elif board[0][0] + board[1][0] == 2 and board[2][0] == 0:
            board[2][0] = 4
            drawMove(2, 0, 2)
        elif board[1][0] + board[2][0] == 2 and board[0][0] == 0:
            board[0][0] = 4
            drawMove(0, 0, 2)
        elif board[0][1] + board[1][1] == 2 and board[2][1] == 0:
            board[2][1] = 4
            drawMove(2, 1, 2)
        elif board[1][1] + board[2][1] == 2 and board[0][1] == 0:
            board[0][1] = 4
            drawMove(0, 1, 2)
        elif board[0][2] + board[1][2] == 2 and board[2][2] == 0:
            board[2][2] = 4
            drawMove(2, 2, 2)
        elif board[2][2] + board[1][2] == 2 and board[0][2] == 0:
            board[0][2] = 4
            drawMove(0, 2, 2)
        elif board[0][0] + board[2][0] == 2 and board[1][0] == 0:
            board[1][0] = 4
            drawMove(1, 0, 2)
        elif board[0][1] + board[2][1] == 2 and board[1][1] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        elif board[0][2] + board[2][2] == 2 and board[1][2] == 0:
            board[1][2] = 4
            drawMove(1, 2, 2)
        # corners
        elif board[0][0] + board[1][1] == 2 and board[2][2] == 0:
            board[2][2] = 4
            drawMove(2, 2, 2)
        elif board[1][1] + board[2][2] == 2 and board[0][0] == 0:
            board[0][0] = 4
            drawMove(0, 0, 2)
        elif board[0][2] + board[1][1] == 2 and board[2][0] == 0:
            board[2][0] = 4
            drawMove(2, 0, 2)
        elif board[2][0] + board[1][1] == 2 and board[0][2] == 0:
            board[0][2] = 4
            drawMove(0, 2, 2)
        elif board[0][0] + board[2][2] == 2 and board[1][1] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        elif board[0][2] + board[2][0] == 2 and board[1][1] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        elif count == 0:
            if board[0][0] == 1 or board[0][2] == 1 or board[2][0] == 1 or board[2][2] == 1:
                while True:
                    rando = random.randint(0, 3)
                    if rando == 0:
                        x = 0
                        y = 1
                    elif rando == 1:
                        x = 1
                        y = 0
                    elif rando == 2:
                        x = 1
                        y = 2
                    else:
                        x = 2
                        y = 1
                    if board[x][y] == 0:
                        board[x][y] = 4
                        drawMove(x, y, 2)
                        break
            else:
                while True:
                    x = 2*random.randint(0, 1)
                    y = 2*random.randint(0, 1)
                    if board[x][y] == 0:
                        board[x][y] = 4
                        drawMove(x, y, 2)
                        count += 1
                        break
            count += 1
        # setting up a win
        # horizontal start
        elif board[0][0] + board[0][1] == 8 and board[2][0] == 0 and board[0][2] == 0 and board[1][0] == 0:
            board[1][0] = 4
            drawMove(1, 0, 2)
        elif board[0][0] + board[0][1] == 8 and board[2][1] == 0 and board[2][2] == 0 and board[1][1] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        elif board[0][1] + board[0][2] == 8 and board[2][1] == 0 and board[2][0] == 0 and board[1][1] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        elif board[0][1] + board[0][2] == 8 and board[0][0] == 0 and board[2][0] == 0 and board[1][2] == 0:
            board[1][2] = 4
            drawMove(1, 2, 2)
        elif board[1][0] + board[1][1] == 8 and board[0][0] == 0 and board[2][0] == 0 and board[2][2] == 0:
            board[0][0] = 4
            drawMove(0, 0, 2)
        elif board[1][0] + board[1][1] == 8 and board[0][0] == 0 and board[2][0] == 0 and board[0][2] == 0:
            board[2][0] = 4
            drawMove(2, 0, 2)
        elif board[1][1] + board[1][2] == 8 and board[0][2] == 0 and board[2][2] == 0 and board[2][0] == 0:
            board[0][2] = 4
            drawMove(0, 2, 2)
        elif board[1][1] + board[1][2] == 8 and board[0][2] == 0 and board[2][2] == 0 and board[0][0] == 0:
            board[2][2] = 4
            drawMove(2, 2, 2)
        elif board[2][0] + board[2][1] == 8 and board[1][0] == 0 and board[0][0] == 0 and board[2][2] == 0:
            board[1][0] = 4
            drawMove(1, 0, 2)
        elif board[2][0] + board[2][1] == 8 and board[1][1] == 0 and board[0][2] == 0 and board[0][1] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        elif board[2][1] + board[2][2] == 8 and board[1][2] == 0 and board[2][0] == 0 and board[0][0] == 0:
            board[1][2] = 4
            drawMove(1, 2, 2)
        elif board[2][1] + board[2][2] == 8 and board[1][1] == 0 and board[0][0] == 0 and board[0][1] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        # vertical
        elif board[0][0] + board[1][0] == 8 and board[0][1] == 0 and board[2][0] == 0 and board[0][2] == 0:
            board[0][1] = 4
            drawMove(0, 1, 2)
        elif board[0][0] + board[1][0] == 8 and board[1][1] == 0 and board[1][2] == 0 and board[2][2] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        elif board[1][0] + board[2][0] == 8 and board[2][1] == 0 and board[0][0] == 0 and board[2][2] == 0:
            board[2][1] = 4
            drawMove(2, 1, 2)
        elif board[1][0] + board[2][0] == 8 and board[1][1] == 0 and board[0][2] == 0 and board[1][2] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        elif board[0][1] + board[1][1] == 8 and board[0][0] == 0 and board[0][2] == 0 and board[2][2] == 0:
            board[0][0] = 4
            drawMove(0, 0, 2)
        elif board[0][1] + board[1][1] == 8 and board[0][0] == 0 and board[0][2] == 0 and board[2][0] == 0:
            board[0][2] = 4
            drawMove(0, 2, 2)
        elif board[1][1] + board[2][1] == 8 and board[2][0] == 0 and board[2][2] == 0 and board[0][0] == 0:
            board[2][2] = 4
            drawMove(2, 2, 2)
        elif board[1][1] + board[2][1] == 8 and board[2][0] == 0 and board[2][2] == 0 and board[0][2] == 0:
            board[2][0] = 4
            drawMove(2, 0, 2)
        elif board[0][2] + board[1][2] == 8 and board[0][1] == 0 and board[0][0] == 0 and board[2][2] == 0:
            board[0][1] = 4
            drawMove(0, 1, 2)
        elif board[0][2] + board[1][2] == 8 and board[1][1] == 0 and board[2][0] == 0 and board[1][0] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        elif board[1][2] + board[2][2] == 8 and board[2][1] == 0 and board[2][0] == 0 and board[0][2] == 0:
            board[2][1] = 4
            drawMove(2, 1, 2)
        elif board[1][2] + board[2][2] == 8 and board[1][1] == 0 and board[0][0] == 0 and board[1][0] == 0:
            board[1][1] = 4
            drawMove(1, 1, 2)
        # corners
        elif board[0][0] + board[0][2] == 8 and board[1][1] == 0 and board[1][0] == 0 and board[2][0] == 0:
            board[2][0] = 4
            drawMove(2, 0, 2)
        elif board[0][0] + board[0][2] == 8 and board[1][1] == 0 and board[1][2] == 0 and board[2][2] == 0:
            board[2][2] = 4
            drawMove(2, 2, 2)
        elif board[2][0] + board[2][2] == 8 and board[1][1] == 0 and board[0][0] == 0 and board[1][0] == 0:
            board[0][0] = 4
            drawMove(0, 0, 2)
        elif board[2][0] + board[2][2] == 8 and board[1][1] == 0 and board[0][2] == 0 and board[1][2] == 0:
            board[0][2] = 4
            drawMove(0, 2, 2)
        elif board[0][0] + board[2][0] == 8 and board[1][1] == 0 and board[0][2] == 0 and board[0][1] == 0:
            board[0][2] = 4
            drawMove(0, 2, 2)
        elif board[0][0] + board[2][0] == 8 and board[1][1] == 0 and board[2][2] == 0 and board[2][1] == 0:
            board[2][2] = 4
            drawMove(2, 2, 2)
        elif board[0][2] + board[2][2] == 8 and board[1][1] == 0 and board[0][0] == 0 and board[0][1] == 0:
            board[0][0] = 4
            drawMove(0, 0, 2)
        elif board[0][2] + board[2][2] == 8 and board[1][1] == 0 and board[2][0] == 0 and board[2][1] == 0:
            board[2][0] = 4
            drawMove(2, 0, 2)
        elif board[0][0] + board[2][2] == 8 and board[2][0] == 0 and board[1][0] == 0 and board[2][1] == 0:
            board[2][0] = 4
            drawMove(2, 0, 2)
        elif board[0][0] + board[2][2] == 8 and board[0][2] == 0 and board[0][1] == 0 and board[1][2] == 0:
            board[0][2] = 4
            drawMove(0, 2, 2)
        elif board[0][2] + board[2][0] == 8 and board[0][0] == 0 and board[0][1] == 0 and board[1][0] == 0:
            board[0][0] = 4
            drawMove(0, 0, 2)
        elif board[0][2] + board[2][0] == 8 and board[2][2] == 0 and board[1][2] == 0 and board[2][1] == 0:
            board[2][2] = 4
            drawMove(2, 2, 2)
        elif board[0][0] + board[0][2] + board[2][0] + board[2][2] == 5:
            if board[0][0] == 0:
                board[0][0] = 4
                drawMove(0, 0, 2)
            elif board[0][2] == 0:
                board[0][2] = 4
                drawMove(0, 2, 2)
            elif board[2][0] == 0:
                board[2][0] = 4
                drawMove(2, 0, 2)
            elif board[2][2] == 0:
                drawMove(2, 2, 2)
                board[2][2] = 4
        else:
            while True:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                if board[x][y] == 0:
                    board[x][y] = 4
                    drawMove(x, y, 2)
                    break
        for i in board:
            print(i)
        if sum(board[0]) == 3 or sum(board[0]) == 12:
            checker = True
        if sum(board[1]) == 3 or sum(board[1]) == 12:
            checker = True
        if sum(board[2]) == 3 or sum(board[2]) == 12:
            checker = True
        if board[0][0] + board[1][0] + board[2][0] == 3 or board[0][0] + board[1][0] + board[2][0] == 12:
            checker = True
        if board[0][1] + board[1][1] + board[2][1] == 3 or board[0][1] + board[1][1] + board[2][1] == 12:
            checker = True
        if board[0][2] + board[1][2] + board[2][2] == 3 or board[0][2] + board[1][2] + board[2][2] == 12:
            checker = True
        if board[0][0] + board[1][1] + board[2][2] == 3 or board[0][0] + board[1][1] + board[2][2] == 12:
            checker = True
        if board[0][2] + board[1][1] + board[2][0] == 3 or board[0][2] + board[1][1] + board[2][0] == 12:
            checker = True
        if checker:
            textinput('', 'Game over: You Lose :(')
            break
