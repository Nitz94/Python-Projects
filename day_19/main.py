from turtle import Turtle, Screen

amesh = Turtle()
screen = Screen()


def move_forward():
    amesh.forward(10)


#  Asks screen to listen for input
screen.listen()
# onkey uses two arguments one is the  key to listen and other a function to do when the key is pressed
screen.onkey(key="space", fun=move_forward)
# when calling a function as an argument inside another function, there is no need for ()
screen.exitonclick()

