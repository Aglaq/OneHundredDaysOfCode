from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.high_score = 0
        self.ht()
        self.goto(0, 275)
        self.up()
        self.load_high_score()
        self.update_scoreboard()

    # Loading High Score from external file data.txt
    def load_high_score(self):
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())

    # Updates score after losing or at the start of the game
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    # Adds score after collecting food
    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    # Resets the game after losing and sents High Score to external file data.txt
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # NOT USED ANYMORE
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align = ALIGNMENT, font = FONT)