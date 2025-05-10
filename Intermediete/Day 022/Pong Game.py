from turtle import Screen
from field import Field
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


R_PADDLE = 460
L_PADDLE = -460

# create screen
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create field
field = Field()

# create paddle
r_paddle = Paddle(R_PADDLE)
l_paddle = Paddle(L_PADDLE)

# move paddle
screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

# create ball
ball = Ball()

# create scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()

    #move the ball
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 430) or (ball.distance(l_paddle) < 50 and ball.xcor() < -430):
        ball.bounce_x()

    # detect r_paddle misses
    if ball.xcor() > 480:
        scoreboard.l_point()
        ball.reset_position()

    # detect l_paddle misses
    if ball.xcor() < -480:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()