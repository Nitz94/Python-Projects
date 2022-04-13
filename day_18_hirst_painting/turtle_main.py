import turtle
from turtle import Turtle, Screen
import random

# from colors import colors
turtle.colormode(255)
amesh = Turtle()
amesh.shape("classic")
amesh.color("green4", "black")
amesh.shapesize(2)
amesh.pensize(2)
amesh.speed("fastest")
# Draw a square
# for _ in range(4):
#     amesh.forward(100)
#     amesh.left(90)


# Draw a dashed line
# for _ in range(15):
#     amesh.forward(10)
#     amesh.penup()
#     amesh.forward(10)
#     amesh.pendown()

# Drawing different shapes
# amesh.color(random.choice(colors))
# for _ in range(3):
#     amesh.forward(100)
#     amesh.right(360/3)
# amesh.color(random.choice(colors))
# for _ in range(4):
#     amesh.forward(100)
#     amesh.right(360/4)
# amesh.color(random.choice(colors))
# for _ in range(5):
#     amesh.forward(100)
#     amesh.right(360 / 5)
#
# amesh.color(random.choice(colors))
# for _ in range(6):
#     amesh.forward(100)
#     amesh.right(360 / 6)
#
# amesh.color(random.choice(colors))
# for _ in range(7):
#     amesh.forward(100)
#     amesh.right(360 / 7)
# amesh.color(random.choice(colors))
# for _ in range(8):
#     amesh.forward(100)
#     amesh.right(360 / 8)
# amesh.color(random.choice(colors))
# for _ in range(9):
#     amesh.forward(100)
#     amesh.right(360 / 9)
# amesh.color(random.choice(colors))
# for _ in range(10):
#     amesh.forward(100)
#     amesh.right(360 / 10)

# **********simpler solution********
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         amesh.forward(100)
#         amesh.right(angle)
#
#
# for shape_side_n in range(3, 10):
#     amesh.color(random.choice(colors))
#     draw_shape(shape_side_n)


# Draw a random walk also generate random rgb colors
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# direction = [0, 90, 180, 270]
# for _ in range(200):
#     amesh.pencolor(random_color())
#     amesh.forward(35)
#     amesh.setheading(random.choice(direction))


# Draw a spirograph

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        amesh.color(random_color())
        amesh.circle(150)
        # current_heading = amesh.heading()
        amesh.setheading(amesh.heading() + size_of_gap)  # (old)amesh.setheading(amesh.heading()+10)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()
