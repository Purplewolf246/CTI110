#write a program that displays your first and last initials
#CTI-110
#P4LAB1 - Turtle Graphic (P4LABb)
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
#First Inital
alex.left(180)
alex.forward(40)
alex.right(35)
alex.forward(40)
alex.right(35)
alex.forward(40)
alex.right(35)
alex.forward(40)
alex.right(35)
alex.forward(40)
alex.right(35)
alex.forward(40)
#Pen Pick up/Drop + Second Inital
alex.penup()
alex.forward(100)
alex.right(90)
alex.forward(125)
alex.pendown()
alex.right(90)
alex.forward(40)
alex.right(35)
alex.forward(40)
alex.right(35)
alex.forward(40)
alex.right(35)
alex.forward(40)
alex.right(35)
alex.forward(40)
alex.right(35)
alex.forward(40)
