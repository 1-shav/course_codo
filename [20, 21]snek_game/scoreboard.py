from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("Courier", 15, "normal")
GAME_OVER_FONT = ("SubwayTicker", 50, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_rn = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score_rn}  Highest score: {self.highscore}", align=ALIGNMENT, font=SCORE_FONT)

    def reset(self):
        if self.score_rn > self.highscore:
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score_rn}")
        self.score_rn = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)


    def increase_score(self):
        self.score_rn += 1
        self.update_score()