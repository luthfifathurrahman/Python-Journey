from turtle import Turtle, Screen, colormode
import colorgram
import random

rgb_color = []
colors = colorgram.extract("D:/PycharmProjects/UdemyPython/Intermediete/Day 18/image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_color.append(rgb)

colormode(255)

def dot_stamp():
    tim.color(random.choice(rgb_color))
    tim.dot(40)
    tim.forward(80)

def hirst_painting(h, w):
    x_coordinate = -452
    y_coordinate = -350
    for height in range(h):
        tim.goto(x_coordinate, y_coordinate)
        for width in range(w):
            dot_stamp()
        y_coordinate = y_coordinate + 80

tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

hirst_painting(10, 10)

screen = Screen()
screen.exitonclick()