from turtle import Turtle


ALIGNMENT = "center"
FONT = "courier"
FONT_SIZE = 12
FONT_TYPE = "bold"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def game_over(self):
        self.goto(0, 0)
        self.write(" GAME OVER", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

