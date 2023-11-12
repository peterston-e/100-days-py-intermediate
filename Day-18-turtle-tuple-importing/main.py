import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()
tim.shape("arrow")
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.seth(tim.heading() + gap_size)

draw_spirograph(3)
# ************* RANDOM WALK *****************
# tim.pensize(10)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# angle = 90
# def random_angle(n_angle):
#     n_angle *= random.randint(1, 4)
#     return n_angle
#
#
# for _ in range(200):
#     tim.forward(20)
#     tim.seth(random_angle(angle))
#     tim.color(random_color())



# ******** SHAPES **********
# color_list = ["cyan", "blue", "green", "red", "yellow", "magenta", "purple"]
# sides = 3
# angle = 120
# tim.pu()
# tim.setposition(-50, 200)
# tim.pd()
#
# for _ in range(10):
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)
#     sides += 1
#     angle = 360 / sides
#     tim.color(choice(color_list))



# for _ in range(36):
#     for _ in range(4):
#         for _ in range(5):
#             tim.forward(10)
#             tim.pu()
#             tim.forward(10)
#             tim.pd()
#         tim.right(90)
#     tim.right(10)













screen = Screen()
screen.exitonclick()
