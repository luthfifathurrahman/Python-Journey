from turtle import Screen
from player import Player
from car_manager import CarManager
import time
from scoreboard import Scoreboard

# create screen
screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=500, height=500)
screen.tracer(0)

# create turtle
player = Player()

car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "w")
screen.onkeypress(player.go_down, "s")
screen.onkeypress(player.go_right, "d")
screen.onkeypress(player.go_left, "a")

game_is_on = True
move_speed = 0.1
while game_is_on:
    time.sleep(move_speed)
    screen.update()

    # create car
    car_manager.create_car()

    # move car
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        if player.ycor() >= 250:
            move_speed *= 0.9
            player.level_up()
            scoreboard.level_up()





screen.exitonclick()