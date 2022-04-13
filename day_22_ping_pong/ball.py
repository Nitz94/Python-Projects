from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def ball_move(self):         # moving the ball across the screen
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):   # changing the y cor to opposite direction after collision. effect takes place on ball_move
        self.y_move *= -1  # in ball_move method y_move becomes -10

    def bounce_x(self):
        self.x_move *= -1  # changing x coordinate of ball_move method if ball collides with paddle
        self.move_speed *= 0.9   # optional speed increase for higher difficulty

    def reset(self):    # resetting the ball to (0,0) and returning the ball to other player
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
