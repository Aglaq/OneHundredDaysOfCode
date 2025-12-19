from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.setup()

    def setup(self):
        for i in range(3):
            new_snake_part = Turtle("square")
            new_snake_part.up()
            new_snake_part.color("white")
            new_snake_part.goto((0 + (-20) * i), 0)
            self.segments.append(new_snake_part)
    def move(self):
        seg = self.segments
        for seg_num in range(len(seg) - 1, 0, -1):
            new_x = seg[seg_num - 1].xcor()
            new_y = seg[seg_num - 1].ycor()
            seg[seg_num].goto(new_x, new_y)
        seg[0].forward(20)