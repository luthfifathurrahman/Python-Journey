from turtle import Turtle, Screen

FONT = ("Courier", 8, "normal")
FONT_GAME_OVER = ("Courier", 40, "bold")

class UserGuess():
    def __init__(self):
        self.screen = Screen()
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.correct = 0

    def ask_user(self):
        self.user_answer = self.screen.textinput(title=f"{self.correct}/50 States Correct", prompt="Guess the state's name:")
        return self.user_answer

    def correct_answer(self, answer_state, x, y):
        self.correct += 1
        self.turtle.goto(x, y)
        self.turtle.write(f"{answer_state}", align ="center", font=FONT)

    def game_over(self):
        self.turtle.goto(0, 0)
        self.turtle.write(f"YOU WON!!", align ="center", font=FONT_GAME_OVER)
