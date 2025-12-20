from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.ht()
        self.goto(0, 275)
        self.up()
        self.add_score()

    def add_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align = ALIGNMENT, font = FONT)