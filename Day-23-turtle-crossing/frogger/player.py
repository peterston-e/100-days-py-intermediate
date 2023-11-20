from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.seth(90)
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)