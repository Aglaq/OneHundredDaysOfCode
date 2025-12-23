from turtle import Turtle
from random import randint
STARTING_POSITION = (0, 0)
move_angle = randint(0, 360)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color("white")
        self.goto(STARTING_POSITION)
        self.setheading(move_angle)
        
    def move(self):
        self.forward(20)
