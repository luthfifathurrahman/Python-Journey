from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-250, 250)
        self.pendown()
        for i in range(4):
            self.forward(500)
            self.right(90)