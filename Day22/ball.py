from turtle import Turtle
from random import randint
STARTING_POSITION = (0, 0)
SPEED = 20
move_angle = randint(0, 360)
# move_angle = 80

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color("white")
        self.goto(STARTING_POSITION)
        self.setheading(move_angle)
        self.move_angle = move_angle
        
    def move(self):
        self.forward(SPEED)

    def change_direction_wall(self):
        new_angle = 360 - self.move_angle
        self.setheading(new_angle)
        self.move_angle = new_angle

    def change_direction_pad(self):
        new_angle = 180 - self.move_angle
        self.setheading(new_angle)
        self.move_angle = new_angle