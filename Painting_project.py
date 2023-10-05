# import colorgram
# rgb_color=[]
# colors=colorgram.extract("d1.jpg",30)
# for color in colors:
#     r=color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     list=(r,g,b)
#     rgb_color.append(list)
# print(rgb_color)

import turtle
from turtle import Turtle,Screen
import random
tur=Turtle()
turtle.colormode(255)
tur.penup()
tur.hideturtle()
tur.setheading(225)
tur.forward(300)
tur.setheading(0)

colour_list= [(208, 162, 101), (152, 75, 42), (240, 245, 241), (235, 238, 243), (223, 200, 135), (49, 92, 127), (176, 149, 36), (140, 38, 20), (130, 161, 186), (201, 94, 70), (57, 44, 38), (50, 120, 94), (11, 95, 69), (146, 174, 146), (31, 47, 55), (39, 35, 38), (160, 145, 159), (15, 81, 91), (234, 176, 161), (105, 77, 79), (45, 65, 85), (182, 202, 172), (23, 48, 40), (99, 141, 131), (108, 127, 153), (176, 191, 210), (69, 63, 57), (213, 179, 184)]


def move_turtle():
    co = random.choice(colour_list)
    tur.pencolor(co)
    tur.dot(20)
    tur.penup()
    tur.forward(50)


def moving_forward():
    tur.setheading(90)
    tur.forward(50)
    tur.setheading(180)
    tur.forward(500)
    tur.setheading(0)
    for k in range(10):
        move_turtle()


for i in range(10):
    move_turtle()
for j in range(9):
    moving_forward()


screen = Screen()

screen.exitonclick()