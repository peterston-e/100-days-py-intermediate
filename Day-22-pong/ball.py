from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 1
        self.x_move = 1
        # self.move_speed = 0.1



    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move = round(self.x_move * -1.1, 1)
        if self.y_move < 0:
            self.y_move = round(self.y_move + -0.1, 1)
        else:
            self.y_move = round(self.y_move + 0.1, 1)

    def reset_position(self):
        self.goto(0, 0)
        # self.move_speed = 0.1

    def increase_speed(self):
        pass

    def reset_speed(self):
        pass
