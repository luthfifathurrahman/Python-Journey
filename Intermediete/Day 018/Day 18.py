import random
from turtle import Turtle, Screen

turtle_colors = [
    "red", "green", "blue", "yellow", "orange",
    "purple", "pink", "brown", "black", "white",
    "gray", "cyan", "magenta", "violet", "indigo",
    "gold", "silver", "maroon", "lime", "olive",
    "navy", "teal", "aqua", "coral", "salmon",
    "turquoise", "khaki", "plum", "orchid", "tan",
    "azure", "beige", "bisque", "chocolate", "crimson",
    "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen",
    "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid",
    "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray",
    "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray",
    "dodgerblue", "firebrick", "forestgreen", "gainsboro", "ghostwhite",
    "goldenrod", "greenyellow", "honeydew", "hotpink", "indianred",
    "ivory", "lavender", "lavenderblush", "lawngreen", "lemonchiffon",
    "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray",
    "lightgreen", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue",
    "lightslategray", "lightsteelblue", "lightyellow", "limegreen", "linen",
    "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen",
    "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue",
    "mintcream", "mistyrose", "moccasin", "navajowhite", "oldlace",
    "olivedrab", "orangered", "palegoldenrod", "palegreen", "paleturquoise"
]

timmy = Turtle()
timmy.shape("turtle") # change shape
timmy.color("red") # change color
# # draw a square
# for _ in range(4):
#     timmy.forward(100) # move forward
#     timmy.right(90) # turn right

# # draw dashed line
# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# # draw multiple shape
# for i in range(3, 11):
#     timmy.color(random.choice(turtle_colors))
#     for _ in range(i):
#         timmy.speed(10)
#         timmy.pensize(10)
#         timmy.forward(100)
#         timmy.right(360/i)

# # draw random walk
# def random_color_rgb():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     color = (r, g, b)
#     return color
#
# angle = [0, 90, 180, 270]
# for _ in range(200):
#     timmy.speed(10)
#     timmy.color(random_color_rgb())
#     timmy.pensize(10)
#     timmy.forward(30)
#     timmy.setheading(random.choice(angle))

# draw spirograph
def spirograph(angle):
    for _ in range(int(360 / angle)):
        timmy.speed("fastest")
        timmy.color(random.choice(turtle_colors))
        timmy.circle(100)
        timmy.setheading(timmy.heading() + angle)

spirograph(5)

screen = Screen()
screen.exitonclick()