from turtle import Turtle

class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 310)
        self.setheading(270)
        self.pendown()
        self.color("white")
        self.forward(620)
