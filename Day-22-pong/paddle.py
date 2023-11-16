from turtle import Turtle

class Paddle:

    def __init__(self):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.shapesize(stretch_len=1, stretch_wid=3)

class