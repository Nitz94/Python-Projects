from turtle import Turtle,Screen
import time
from TC_car_manager import CarManager
from TC_scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.title("THE TURTLE CROSSING")
screen.tracer(0)


player = Turtle("turtle")

# creating function instead of class here because at the time of writing turtle module was not functioning


def player_properties():
    player.color("coral")
    player.penup()
    player.goto(0, -280)
    player.setheading(90)


def go_up():
    new_y = player.ycor() + 10
    player.goto(player.xcor(), new_y)


player_properties()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)   # refreshing screen every 0.1sec
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # detecting collision between car and player
    for cars in car_manager.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detecting if the player reaches finishline
    if player.ycor() > FINISH_LINE_Y:
        player.goto(STARTING_POSITION)
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()