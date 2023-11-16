from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_speed = 3
        self.x_speed = 3
        self.move()


    def move(self):
        new_y = self.ycor() + self.y_speed
        new_x = self.xcor() + self.x_speed
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_speed *= -1
