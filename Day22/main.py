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

    # Detect collision with top and bottom wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_direction_wall()

    # Detect collision with right paddle.
    if ball.distance(pad_1) < 50 and ball.xcor() < -320 or ball.distance(pad_2) < 50 and ball.xcor() > 320:
        ball.change_direction_pad()

    # Detect when paddle misses.
    if ball.xcor() < -380:
        print("Point for right")
        ball.reset_position()
        # game_is_on = False
    if ball.xcor() > 380:
        print("Point for left")
        ball.reset_position()
        # game_is_on = False

screen.exitonclick()
