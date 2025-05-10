from turtle import Turtle

STARTING_POSITION = (0, -230)
MOVING_DISTANCE = 40
FINISH_LINE = 230

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVING_DISTANCE)

    def go_down(self):
        self.backward(MOVING_DISTANCE)

    def go_right(self):
        new_x = self.xcor() + MOVING_DISTANCE
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - MOVING_DISTANCE
        self.goto(new_x, self.ycor())

    def level_up(self):
        self.goto(STARTING_POSITION)


