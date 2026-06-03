from turtle import Turtle

class Write(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.ht()
        self.up()

    def update_screen(self, name, x, y):
        self.goto(x, y)
        self.write(name, align="center", font=("Arial", 8, "normal"))