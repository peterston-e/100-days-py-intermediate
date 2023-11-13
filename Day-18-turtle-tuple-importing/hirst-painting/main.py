import colorgram
import turtle
from turtle import Turtle, Screen
from random import choice

CANVAS = 660
PADDING = 40
screen = Screen()
screen.setup(width=CANVAS + PADDING, height=CANVAS + PADDING, )

turtle.colormode(255)
tim = Turtle()
tim.shape("arrow")
tim.speed(9)

color_thing = colorgram.extract('colorful.jpeg', 50)


def random_color():
    color_obj = choice(color_thing)
    c_rgb = color_obj.rgb
    color = (c_rgb.r, c_rgb.g, c_rgb.b)
    return color


def draw_dot_matrix(dots_per_row, dots_per_col, dot_size):
    """takes three arguments: number of dots per row and number of
    dots per column and dot size"""
    spacing_x = (CANVAS / dots_per_row)
    spacing_y = (CANVAS / dots_per_col)

    for _ in range(dots_per_col):
        for _ in range(dots_per_row):
            tim.dot(dot_size, random_color())
            tim.penup()
            x = tim.position()[0]  # x coordinate
            y = tim.position()[1]  # y coordinate
            tim.setposition(x + spacing_x, y)
            tim.pendown()

        tim.penup()
        y = tim.position()[1]  # y coordinate
        tim.setposition(-315, y - spacing_y)
        tim.pendown()


# set location top left
tim.hideturtle()
tim.penup()
tim.setposition(-315, 315)
tim.pendown()
draw_dot_matrix(10, 10, 25)

screen.exitonclick()
