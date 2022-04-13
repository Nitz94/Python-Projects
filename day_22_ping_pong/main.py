# STEP 1 : CREATE THE SCREEN

# STEP 2 : CREATE AND MOVE A PADDLE

# STEP 3 : CREATE ANOTHER PADDLE

# STEP 4 : CREATE THE BALL AND MAKE IT MOVE

# STEP 5 : DETECT COLLISION WITH WALL AND BOUNCE

# STEP 6 : DETECT COLLISION WITH PADDLE

# STEP 7 : DETECT WHEN PADDLE MISSES

# STEP 8 : KEEP SCORE

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# creating screen with suitable size and background color
screen = Screen()
screen.setup(width=800, height=600)   # setting screen width and height
screen.bgcolor("black")
screen.title(" PING-PONG ")
screen.tracer(0)    # turning off the animation

r_paddle = Paddle((350, 0))   # providing position as tuple
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()     # listening to key presses  Using the go up and down methods with paddle objects
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # when the while loop is on time is delayed to slow down the ball to a reasonable speed
    screen.update()   # refreshing screen when necessary
    ball.ball_move()  # ball moves at every refresh of the screen

    # detect collision with top and bottom walls and make the ball bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle and bounce ball
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:  # if right paddle misses
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < - 380:  # if left paddle misses
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
