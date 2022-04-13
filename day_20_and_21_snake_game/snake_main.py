# STEP 1 CREATE A SNAKE BODY (WITH 3 20X20 PIXELS SQUARES)

# STEP 2 MOVE THE SNAKE

# STEP 3 CONTROL THE SNAKE

# STEP 4 DETECT COLLISION WITH FOOD

# STEP 5 CREATE A SCOREBOARD

# STEP 6 DETECT COLLISION WITH WALL

# STEP 7 DETECT COLLISION WITH TAIL


from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNEK")
# turning off the animation using tracer it will only refresh or show the coding in screen when update is used
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
# listening to key stokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:

    screen.update()  # Sleep for 0.1 seconds and update only when all segments have moved
    time.sleep(0.1)
    snake.move()
    # Detects collision with food
    if snake.head.distance(food) < 15:  # compares the position of one turtle with another. here snake vs food
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall # x and y cor are adjustable to fit the desired visual experience
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:    # checking if snake.head is the first segment

        if snake.head.distance(segment[1:]) < 10:   # checking if the distance from head and another segment
            scoreboard.game_over()


screen.exitonclick()
