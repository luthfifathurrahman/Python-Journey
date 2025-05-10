from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,255)
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} | High Score = {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.scoreboard()

    def add_score(self):
        self.score += 1
        self.scoreboard()