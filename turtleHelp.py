from turtle import *
speed(1000000)
def drawMove(col,row,player):
   penup()
   xCord = -125+(100*(row))
   yCord = 80-100*(col)
   goto(xCord,yCord)
   pendown()
   if(player == 1):
       color('Orange')
       write('O', move=False, align='center', font=('Ariel', 60, 'normal'))
       penup()
   if(player == 2 or player == 4):
       color('Maroon')
       write('X', move=False, align='center', font=('Ariel', 60, 'normal'))
       penup()



def drawboard():
   speed(1000000)
   penup()
   goto(-75, 180)
   pendown()
   right(90)
   forward(302)
   penup()
   goto(25, 180)
   pendown()
   forward(302)
   penup()

   left(90)
   penup()
   goto(-175, 79)
   pendown()
   forward(302)

   penup()
   goto(-175, -21)
   pendown()
   forward(302)
   penup()

   goto(-175, 180)
   pendown()
   forward(302)
   right(90)
   forward(300)
   right(90)
   forward(302)
   right(90)
   forward(300)
   penup()

   penup()
   goto(-20, 200)
   color('black')
   write('Welcome to Tic-Tac-Toe!', move=True, align='center', font=('Arial', 20, 'normal'))
   penup()
