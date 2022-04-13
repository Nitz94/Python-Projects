from turtle import Turtle, Screen
import random

is_race_on = False

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_position = [-200, -140, -80, -20, 40, 100, 160]
screen = Screen()
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make Your Bet.", prompt=" Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

all_turtle = []
for color_index in range(0, 7):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    # new_turtle.shapesize(2)
    new_turtle.color(colors[color_index])
    new_turtle.goto(x=-470, y=y_position[color_index])
    all_turtle.append(new_turtle)

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 470:  # Turtle shape size is 40x40 so subtract 20 from the racetrack end to find the winner
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!!! The winning color is {winning_color}")
            else:
                print(f"You've lost!!! The winning color is {winning_color}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
