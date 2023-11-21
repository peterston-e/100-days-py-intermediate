import time
from turtle import Screen
from player import Player
from car_manager import CarManager
# from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=700)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.t_up, "Up")
screen.onkey(player.t_right, "Right")
screen.onkey(player.t_down, "Down")
screen.onkey(player.t_left, "Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car(lane="lane_1")
    car_manager.move_lane_1()

    car_manager.create_car(lane="lane_2")
    car_manager.move_lane_2()

    car_manager.create_car(lane="lane_3")
    car_manager.move_lane_3()

    car_manager.create_car(lane="lane_4")
    car_manager.move_lane_4()

    car_manager.create_car(lane="lane_5")
    car_manager.move_lane_5()

screen.exitonclick()
