import datetime as dt
from turtle import Turtle

FONT = ("Calibre", 20, "bold")


class Datetime:
    def __init__(self):
        self.getting_time()
        self.tur = Turtle()
        self.tur.hideturtle()

    def getting_time(self):  # getting current time
        self.sec = dt.datetime.now().second
        self.minute = dt.datetime.now().minute
        self.hr = dt.datetime.now().hour

    def display_time(self):
        self.tur.write(f"{self.hr} : {self.minute} :{self.sec}", align="center", font=FONT)

# this project is been created or completed by Anushka on 11th sept 2023.
