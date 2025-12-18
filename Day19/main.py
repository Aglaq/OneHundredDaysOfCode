# Day 19 - More Turtle Graphics, Event Listeners, State and Multiple Instances
# Day 19 - Etch a Sketch, Racing Turtles
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[index])
    new_turtle.up()
    new_turtle.goto(-230, (-100 + 40 * index))
    all_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

# Etch a Sketch
# def move_forwards():
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def turn_right():
#     tim.right(10)

# def turn_left():
#     tim.left(10)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_right, "d")
# screen.onkey(turn_left, "a")
# screen.onkey(clear, "c")
# screen.exitonclick()
