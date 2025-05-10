import random
from turtle import Turtle

Y_POSITION = [- 190, -110, -30, 50, 130, 210]
MOVING_DISTANCE = 5

class CarManager():
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.goto(250, random.choice(Y_POSITION))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(MOVING_DISTANCE)