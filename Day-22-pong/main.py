from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
# import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-360, 0))
right_paddle = Paddle((360, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True
while game_on:
    # time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
        ball.increase_speed()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        ball.increase_speed()

    # right side missed.
    if ball.xcor() > 380:
        scoreboard.increase_l_score()
        ball.reset_position()
        ball.bounce_x()
        # reset speed

    # left side missed
    if ball.xcor() < -380:
        scoreboard.increase_r_score()
        ball.reset_position()
        ball.bounce_x()
        # reset speed

screen.exitonclick()
