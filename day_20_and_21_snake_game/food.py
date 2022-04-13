from turtle import Turtle

import random


class Food(Turtle):
    # generating food by inheriting Turtle class and using it in Food class
    def __init__(self):
        super().__init__()
        self.shape("circle")       # all the features of Food is inherited from Turtle
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # decreasing shape size
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)   # random x and y position for food for initial position and after
        random_y = random.randint(-280, 280)   # being collided with snake head
        self.goto(random_x, random_y)
