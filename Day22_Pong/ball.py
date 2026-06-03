from turtle import Turtle
from random import randint
STARTING_POSITION = (0, 0)
STARTING_SPEED = 20
INCREASE_IN_SPEED = 2
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
        self.move_speed = STARTING_SPEED
    
    def random_angle(self):
        self.move_angle = randint(0, 360)
        self.setheading(self.move_angle)

    def move(self):
        self.forward(self.move_speed)

    def change_direction_wall(self):
        new_angle = 360 - self.move_angle
        self.setheading(new_angle)
        self.move_angle = new_angle

    def change_direction_pad(self):
        new_angle = 180 - self.move_angle
        self.setheading(new_angle)
        self.move_angle = new_angle
        self.move_speed += INCREASE_IN_SPEED

    def reset_position(self):
        self.home()
        self.random_angle()
        self.move_speed = STARTING_SPEED
        