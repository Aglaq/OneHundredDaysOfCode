from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.ht()
        self.add_score()

    def add_score(self):
        self.clear()
        self.up()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", True, align = "center", font = ("Arial", 16, "normal"))
        self.score += 1
