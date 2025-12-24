from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNEMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.up()
        self.ht()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 260)
        self.write(f"Level: {self.level}", align=ALIGNEMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNEMENT, font=FONT)
