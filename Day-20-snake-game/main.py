from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

SIZE = 40
snake_length = 3
y_position = 0.0


for square in range(0, snake_length):
    new_turtle = Turtle(shape="square")
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.goto(square * -20.0, 0)













screen.exitonclick()