# Day 23 - Capstone Project
# Day 23 - The Turtle Crossing

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() == player.finish_line:
        player.restart()
        # scoreboard.level_up()
        # car_manager.level_up()



screen.exitonclick()
