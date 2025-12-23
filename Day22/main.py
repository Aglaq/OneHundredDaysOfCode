import time
from turtle import Screen
from ball import Ball
from pad import Pad

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

game_is_on = True
ball = Ball()
pad_1 = Pad((-350, 0))
pad_2 = Pad((350, 0))

screen.listen()
screen.onkey(pad_1.move_up, "w")
screen.onkey(pad_1.move_down, "s")
screen.onkey(pad_2.move_up, "Up")
screen.onkey(pad_2.move_down, "Down")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()


screen.exitonclick()
