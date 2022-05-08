from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:    # reading from data.txt to get 0 as initial value
            self.high_score = int(data.read())    # initializing high score to 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):   # instead of game over method reset method is used
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:  # writing the new high score to data.txt that value will be shown
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
