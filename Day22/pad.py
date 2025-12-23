from turtle import Turtle
MOVE_DISTANCE = 20

class Pad(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.up()
        self.color("white")
        self.shapesize(5, 1)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)