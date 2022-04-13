# Using colorgram to extract colors from a jpg image
# converting it to tuples of rgb vales and putting them in a list
# import colorgram
# colors = colorgram.extract("sample.jpg", 30)
# rgb_color = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)
import turtle
from turtle import Turtle, Screen
import random

amesh = Turtle()

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

turtle.colormode(255)
# Hiding the line
amesh.penup()
amesh.hideturtle()
# turning turtle to a suitable position to fit the screen
amesh.setheading(225)
# moving to that position
amesh.forward(300)
amesh.setheading(0)
number_of_dots = 100
# drawing the dots. when dot count reaches 10 moving the turtle to start of the next line until 100dots
for dot_count in range(1, number_of_dots+1):
    amesh.dot(25, random.choice(color_list))
    amesh.forward(50)
    if dot_count % 10 == 0:
        amesh.setheading(90)
        amesh.forward(50)
        amesh.setheading(180)
        amesh.forward(500)
        amesh.setheading(0)


screen = Screen()
screen.exitonclick()
