from turtle import Screen, Turtle
from time_display import Datetime
import time

screen = Screen()
screen.setup(width=500, height=300)
screen.title("DIGITAL CLOCK")
screen.bgcolor("gray")
d_time = Datetime()
time_turtle = Turtle()
time_turtle.penup()
time_turtle.hideturtle()
time_turtle.goto(x=-60, y=50)
time_turtle.write(arg="TIME", font=("Calibre", 35, "bold"))
time_is_on = True
while time_is_on:
    time.sleep(1)
    d_time.tur.clear()
    d_time.getting_time()
    d_time.display_time()

screen.exitonclick()

# I have created a class named Datetime in different file named time_display.
