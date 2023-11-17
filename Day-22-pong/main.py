from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


left_paddle = Paddle((-360, 0))
right_paddle = Paddle((360, 0))
ball = Ball()



screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True
while game_on:
    screen.update()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()

    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()


screen.exitonclick()
