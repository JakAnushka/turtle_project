import turtle
from turtle import Turtle,Screen
import random
from random import choice

tim=Turtle()
tim.shape("classic")

# drawing simple turtle
# for i in range(0,4):
#     tim.forward(100)
#     tim.right(90)
#     i=i+1


# for printing dashed line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)

# for printing shapes overlapping each other
# list=["red","blue","magenta","green","black","LightSkyBlue"]
#
# n=3
#
# while n<9:
#
#     for i in range(n):
#
#         tim.forward(100)
#         tim.right(360/n)
#     n=n+1
#     co = choice(list)
#     tim.color(co)

# printing turtle to move random
# Moves=[0,90,180,270]
# tim.pensize(10)
# turtle.colormode(255)
#
# def ran_color():#trying to change color of pen by pencolor method in turtle method....first turtle.colomode()need to be done
#     r=random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     t=(r,g,b)
#     return t
#
# # list=["red","blue","magenta","green","black","LightSkyBlue"]
#
# for i in range(0,100):
#     # co = choice(list)
#     # tim.color(co)
#     co=ran_color()
#     tim.pencolor(co)
#     random_move = choice(Moves)
#     tim.forward(10)
#     tim.setheading(random_move)
#     tim.forward(10)

# spirograph
tim.speed(20)
turtle.colormode(255)
def ran_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t=(r,g,b)
    return t


for i in range(0,80):
    tim.pencolor(ran_color())
    tim.circle(100)
    tim.left(5)



screen= Screen()
screen.exitonclick()
