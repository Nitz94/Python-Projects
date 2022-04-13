from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()        # clears the score to prevent over writing
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 50, "bold"))

    def l_point(self):   # increasing scores
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
