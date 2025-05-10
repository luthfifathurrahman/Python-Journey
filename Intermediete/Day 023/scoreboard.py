from turtle import Turtle

FONT = ("Courier", 15, "bold")
LEVEL_BOARD_POSITION = (-240, 225)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.level_board()

    def level_board(self):
        self.clear()
        self.goto(LEVEL_BOARD_POSITION)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.level +=1
        self.goto(LEVEL_BOARD_POSITION)
        self.write(f"Level: {self.level}", align="left", font=FONT)
