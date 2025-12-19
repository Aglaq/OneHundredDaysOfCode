# Day 20 - Build the Snake Game Part 1: Animation and Coordinates
# Day 20 - Project: Snake Game
import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True
snake = Snake()
screen.update()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()