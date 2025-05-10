from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(90)
        self.color("white")
        self.shapesize(stretch_len=5)
        self.goto(position, 0)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)
