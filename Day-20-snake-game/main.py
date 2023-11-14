from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# SIZE = 40
# snake_length = 3

# color = ["red", "white", "blue"]
# new_col = 0
# starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# segments = []

# for position in starting_positions:
#     new_segment = Turtle(shape="square")
#     new_segment.penup()
#     new_segment.color(color[new_col])
#     new_segment.goto(position)
#     segments.append(new_segment)
#     new_col += 1 % 3

snake = Snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # for seg_num in range(len(segments) - 1, 0, -1):  # start, stop, step
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)

screen.exitonclick()
