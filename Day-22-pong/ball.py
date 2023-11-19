from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 2
        self.x_move = 2
        # self.move_speed = 0.1



    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed()

    def reset_position(self):
        self.goto(0, 0)


    def increase_speed(self):
        if self.y_move < 0 and self.x_move < 0:
            self.y_move += -0.1
            self.x_move += -0.1
        elif self.y_move > 0 and self.x_move > 0:
            self.y_move += 0.1
            self.x_move += 0.1
        elif self.y_move > 0 and self.x_move < 0:
            self.y_move += 0.1
            self.x_move += -0.1
        elif self.y_move < 0 and self.x_move > 0:
            self.y_move += -0.1
            self.x_move += 0.1

    def reset_speed(self):
        if self.y_move < 0 and self.x_move < 0:
            self.y_move = -2
            self.x_move = -2
        elif self.y_move > 0 and self.x_move > 0:
            self.y_move = 2
            self.x_move = 2
        elif self.y_move > 0 and self.x_move < 0:
            self.y_move = 2
            self.x_move = -2
        elif self.y_move < 0 and self.x_move > 0:
            self.y_move = -2
            self.x_move = 2
