# Day 18 - Turtle Graphics, Tuples and Importing Modules
# Day 18 - Project: The Hirst Painting
from turtle import Turtle, Screen
from random import randint

tim = Turtle()
screen = Screen()
# tim.shape("turtle")
# tim.color(("SpringGreen"))
# tim.forward(100)


# Challange 1
# for i in range(4):
#     tim.forward(100)    
#     tim.right(90)

# Challange 2
# for i in range(50):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

# Challange 3
# screen.colormode(255)
# for i in range(3, 11):
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     tim.pencolor((r, g, b))
#     for j in range(i):
#         tim.forward(100)
#         tim.right(360 / i)

# Challange 4
screen.colormode(255)
tim.speed(10)
for i in range(50):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tim.pencolor((r, g, b))
    angle = randint(1, 4)
    tim.right(90 * angle)
    tim.forward(30)
    tim.width(5 + i * 0.1)

screen.exitonclick()

# print("Hello from Day 18!")
