# Day 20 - Build the Snake Game Part 1: Animation and Coordinates
# Day 20 - Project: Snake Game
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")

for i in range(3):
    new_snake_part = Turtle("square")
    new_snake_part.up()
    new_snake_part.color("white")
    new_snake_part.goto((0 + (-20) * i), 0)



screen.exitonclick()