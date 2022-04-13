import turtle
from turtle import Turtle, Screen
import random

amesh = Turtle()
amesh.shapesize(2)
amesh.shape("triangle")
amesh.color("red")
amesh.pensize(10)
screen = Screen()

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

turtle.colormode(255)


def move_forward():
    amesh.pencolor(random.choice(color_list))
    amesh.forward(20)


def move_backwards():
    amesh.pencolor(random.choice(color_list))
    amesh.back(20)


def counter_clock_wise():
    amesh.left(10)


def clock_wise():
    amesh.right(10)


def clear_screen():
    amesh.clear()
    amesh.penup()
    amesh.home()
    amesh.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clock_wise)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
