# Day 18 - Turtle Graphics, Tuples and Importing Modules
# Day 18 - Project: The Hirst Painting

# Code to extract colors from image (Used once to get the list of colors)
# import colorgram

# colors = colorgram.extract('image.jpg', 30)

# def basic_colors(col):
#     rgb = col.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     return r, g, b

# colors_list = []
# for color in colors:
#     colors_list.append(basic_colors(color))

from random import choice
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("turtle")
tim.color(("SpringGreen"))
tim.speed(0)
tim.hideturtle()

# List of Colours (some close to white has been removed)
list_of_colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.up()
tim.setposition(-300, -300)
for j in range(10):
    tim.setposition(-300, (-300 + j * 70))
    for i in range(10):
        tim.dot(20, choice(list_of_colors))
        tim.forward(70)

screen.exitonclick()



# from turtle import Turtle, Screen
# from random import randint

# tim = Turtle()
# screen = Screen()
# screen.colormode(255)
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
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     r_color = (r, g, b)
#     return r_color

# for i in range(3, 11):
#     tim.pencolor((random_color()))
#     for j in range(i):
#         tim.forward(100)
#         tim.right(360 / i)

# Challange 4
# tim.speed(0)
# tim.width(5)
# for i in range(200):
#     tim.pencolor((random_color()))
#     angle = randint(1, 4)
#     tim.right(90 * angle)
#     tim.forward(30)
#     tim.width(5 + i * 0.1)

# Challange 5
# tim.speed(0)
# number_of_circles = 40
# for i in range(number_of_circles):
#     tim.pencolor((random_color()))
#     tim.left(360 / number_of_circles)
#     tim.circle(100)

# screen.exitonclick()

# print("Hello from Day 18!")
