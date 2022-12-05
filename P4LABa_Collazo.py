#Whole or for loop, write program that draws both Square & Triangle (Can Overlap/visable)
#CTI-110
#P4LAB1 - Turtle Graphic (P4LABa)
#Crystal Collazo
#12/4/2022
#

import turtle
turtle.shape("turtle")
wn = turtle.Screen()
wn.title("Turtle Graphic")
alex = turtle.Turtle()
alex.color("Blue")
alex.pensize(3)
#Turtle Movements(Square)
alex.forward(100)
alex.right(90)
alex.forward(100)
alex.right(90)
alex.forward(100)
alex.right(90)
alex.forward(100)
#Turtle Movements(Triangle)
alex.left(90)
alex.forward(20)
alex.right(130)
alex.forward(120)
alex.right(110)
alex.forward(110)
alex.right(120)
alex.forward(20)
