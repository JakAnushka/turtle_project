# this game is made with help of python turtle module

import turtle
from turtle import Turtle, Screen
tur=Turtle()
tur.shape("arrow")
def fd_movement():
    tur.forward(100)

def bd_movement():
    tur.backward(200)
def counter_clockwise():
    n_h=tur.heading()+10
    tur.setheading(n_h)
def clockwise():
    n_h = tur.heading() - 10
    tur.setheading(n_h)

def up_down():
    tur.circle(120,180)

def clear():
    # turtle.resetscreen()
    tur.clear()
    tur.penup()
    tur.home()
    tur.pendown()
screen= Screen()
screen.listen()
screen.onkey(key="W",fun=fd_movement)
screen.onkey(key="S",fun=bd_movement)
screen.onkey(key="A",fun=counter_clockwise)
screen.onkey(key="D",fun=clockwise)
screen.onkey(key="Up",fun=up_down)
screen.onkey(key="Down",fun=up_down)
screen.onkey(key="C",fun=clear)
screen.exitonclick()