import colorsys
from turtle import *
import random

def vshape():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)

def snowflakeArm():
    for x in range(0,4):
        forward(30)
        vshape()
    backward(120)

def snowflake():
    for x in range(0, 18):
        snowflakeArm()
        right(20)

print("Do you like shapes ?")
print("choose 1, 2, 3, 4, 5,or 6")
print("1 is a snowflake")
print("hello")
shape("circle")
color ("dark orchid")
speed(90)
pensize(1)
playerChoice = input()
if playerChoice == "1":
    snowflake()
    hideturtle()


mainloop()
