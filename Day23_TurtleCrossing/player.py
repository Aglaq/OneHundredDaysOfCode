from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
DIRECTION = 90

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.finish_line = FINISH_LINE_Y
        self.restart()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.goto(STARTING_POSITION)
        self.setheading(DIRECTION)
        