# # object oriented programming
# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle") # change shape
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name", ["John", "Anna", "Peter"])
table.add_column("Age", [28, 22, 34])
# make all column align left
table.align = "l"
print(table)