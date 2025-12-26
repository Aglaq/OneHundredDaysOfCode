from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.up()
        self.color(choice(COLORS))
        self.shapesize(1, 2)
        self.setheading(180)
        self.goto(position)