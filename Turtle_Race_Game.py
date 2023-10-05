import random
import turtle
from turtle import Turtle,Screen
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Bet",prompt="Who do you think will win in this game?")
game_on=False
colour=["red","yellow","green","purple","blue","orange"]
turtles=[]
y_position=[70,40,10,-20,-50,-80]
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour[i])
    new_turtle.fillcolor ("black")
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position[i])
    turtles.append(new_turtle)
if user_bet:
    game_on=True

while game_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            winning_turtle=turtle.pencolor()
            game_on=False
            if winning_turtle==user_bet.lower():
                print(f"You have won the bet!!! The {winning_turtle} has won the game.")
            else:
                print(f"You have lost the bet!!! The {winning_turtle} has won the game.")
        Distance=random.randint(0,10)
        turtle.forward(Distance)

screen.exitonclick()