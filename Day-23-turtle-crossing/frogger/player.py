from turtle import Turtle
STARTING_POSITION = (0, -300)
MOVE_DISTANCE = 50

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("DarkGreen")
        self.penup()
        self.goto(STARTING_POSITION)
        self.seth(90)

    def t_up(self):
        self.seth(90)
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def t_right(self):
        self.seth(0)
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def t_down(self):
        self.seth(270)
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)

    def t_left(self):
        self.seth(180)
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())
